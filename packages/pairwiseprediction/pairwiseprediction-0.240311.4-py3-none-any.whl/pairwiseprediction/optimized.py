from heapq import heapify, heappop

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import balanced_accuracy_score
from sklearn.model_selection import StratifiedKFold, cross_val_score, ParameterSampler

from pairwiseprediction.classifier import PairwiseClassifier
from pairwiseprediction.combination import pair_rows


# TODO: tune rejection band during optimization ("class unknown")
class OptimizedPairwiseClassifier(PairwiseClassifier):
    r"""
    Optimized classifier through cross-validation suitable for pairwise prediction

    Pairwise prediction is a specific setting that does not fit well within scikit framework.
    RandomizedSearchCV can be used, but each pair leaks information, resulting in a too optimistic nested cross-validation.

    :param search_space: dict like `{"param1": [val1, val2, val3], "param2": [val1, val2]}`.
    :param k: number of k-folds CV.
    :param algorithm: Class of algorithm to predict pairs internally.
    :param pairwise: Type of combination: "difference" or "concatenation".
    :param threshold: How much difference between target values should be considered as relevant within a pair?
    :param proportion: Is the threshold an absolute value (difference) or relative value (proportion)?
    :param center: Default value is the mean of the training sample.
    :param only_relevant_pairs_on_prediction: Whether to keep only relevant differences during interpolation.
    :param kwargs: Arguments for user-provided `algorithm`.

    >>> import numpy as np
    >>> from sklearn.datasets import load_diabetes
    >>> from sklearn.ensemble import RandomForestClassifier
    >>> a, b = load_diabetes(return_X_y=True)
    >>> me = np.mean(b)
    >>> # noinspection PyUnresolvedReferences
    >>> y = (b > me).astype(int)
    >>> alg = RandomForestClassifier(n_estimators=3, random_state=0, n_jobs=-1)
    >>> np.mean(cross_val_score(alg, a, y, cv=StratifiedKFold(n_splits=2)))  # doctest:+ELLIPSIS +NORMALIZE_WHITESPACE
    0.6...
    >>> c = b.reshape(len(b), 1)
    >>> X = np.hstack([a, c])
    >>> from scipy.stats import poisson, uniform
    >>> spc = {
    ...    'criterion': ['gini', 'entropy'],
    ...    'max_depth': poisson(mu=5, loc=2),
    ...    'min_impurity_decrease': uniform(0, 0.01),
    ...    'max_leaf_nodes': poisson(mu=20, loc=5),
    ...    'min_samples_split': [20, 30, 40],
    ...    'min_samples_leaf': [10, 20, 30]
    ... }
    >>> alg = OptimizedPairwiseClassifier(spc, 2, n_estimators=3, threshold=20, only_relevant_pairs_on_prediction=False, random_state=0, n_jobs=-1)
    >>> round(np.mean(cross_val_score(alg, X[:50], y[:50], cv=StratifiedKFold(n_splits=2))), 2)
    0.64
    >>> alg = alg.fit(X[:80])
    >>> alg.predict(X[:2])
    array([1, 0])
    >>> alg.best_score  # doctest:+ELLIPSIS +NORMALIZE_WHITESPACE
    0.6...
    >>> alg.best_params  # doctest:+ELLIPSIS +NORMALIZE_WHITESPACE
    {'criterion': 'entropy', 'max_depth': 4, 'max_leaf_nodes': 24, 'min_impurity_decrease': 0.001..., 'min_samples_leaf': 10, 'min_samples_split': 30}
    >>> alg.opt_results  # doctest:+ELLIPSIS +NORMALIZE_WHITESPACE
    [(0.61..., {'criterion': 'gini', 'max_depth': 9, 'max_leaf_nodes': 22, 'min_impurity_decrease': 0.008..., 'min_samples_leaf': 30, 'min_samples_split': 20}), (0.6023275581889547, {'criterion': 'entropy', 'max_depth': 4, 'max_leaf_nodes': 24, 'min_impurity_decrease': 0.0011827442586893322, 'min_samples_leaf': 10, 'min_samples_split': 30})]

    """

    def __init__(
        self,
        search_space,
        n_iter,
        k=5,
        seed=0,
        algorithm=RandomForestClassifier,
        pairwise="concatenation",
        threshold=0,
        proportion=False,
        center=None,
        only_relevant_pairs_on_prediction=False,
        **kwargs
    ):
        super().__init__(algorithm, pairwise, threshold, proportion, center, only_relevant_pairs_on_prediction, **kwargs)
        self.search_space = search_space
        self.n_iter = n_iter
        self.k = k
        self.seed = seed
        # self.njobs = njobs

    def fit(self, X, y=None):
        """
        :param X:   Last column is the continuous target.
        :param y:   Ignored.

        :return:
        """
        Xw = X if isinstance(X, np.ndarray) else np.array(X)
        X = y = None
        if self.center is None:
            self.center = np.mean(Xw[:, -1])
        w = Xw[:, -1]
        # noinspection PyUnresolvedReferences
        y = (w >= self.center).astype(int)
        skf = StratifiedKFold(n_splits=self.k, random_state=self.seed, shuffle=True)
        sampler = ParameterSampler(self.search_space, self.n_iter, random_state=self.seed)
        lst = []
        best_score = -1
        for params in sampler:
            ytss, ztss = [], []
            for train_index, test_index in skf.split(Xw, y):
                # prepare data sets
                Xwtr = Xw[train_index]
                Xwts = pair_rows(Xw[test_index], reflexive=True)
                yts = (Xwts[:-1:2, -1] > Xwts[1::2, -1]).astype(int)
                ytss.extend(yts)

                # train with sampled arguments
                super().fit_(Xwtr, extra_kwargs=params)
                zts = super().predict(Xwts, paired_rows=True)[::2]
                ztss.extend(zts)
            score = balanced_accuracy_score(ytss, ztss)
            lst.append((score, params))
            if score > best_score:
                self.best_score = score
                self.best_params = params.copy()
        self.opt_results = lst.copy()
        super().fit_(Xw, extra_kwargs=self.best_params)  # `_estimator` will contain the best_estimator
        return self

    def __sklearn_clone__(self):
        return OptimizedPairwiseClassifier(
            self.search_space, self.n_iter, self.k, self.seed, self.algorithm, self.pairwise, self.threshold, self.proportion, self.center, self.only_relevant_pairs_on_prediction, **self.kwargs
        )
