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
    :param n_jobs: Number of processess in parallel
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
    >>> np.mean(cross_val_score(alg, X, y, cv=StratifiedKFold(n_splits=2)))  # doctest:+ELLIPSIS +NORMALIZE_WHITESPACE
    0.7...
    >>> alg = alg.fit(X[:80])
    >>> alg.predict(X[:2])
    array([1, 0])
    >>> alg.best_score  # doctest:+ELLIPSIS +NORMALIZE_WHITESPACE
    0.6...
    >>> alg.best_params  # doctest:+ELLIPSIS +NORMALIZE_WHITESPACE
    {'criterion': 'gini', 'max_depth': 9, 'max_leaf_nodes': 22, 'min_impurity_decrease': 0.008..., 'min_samples_leaf': 30, 'min_samples_split': 20}
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

        sampler = ParameterSampler(self.search_space, self.n_iter, random_state=self.seed)
        skf = StratifiedKFold(n_splits=self.k, random_state=self.seed, shuffle=True)
        lst = []
        for params, (train_index, test_index) in zip(sampler, skf.split(Xw, y)):
            # prepare data sets
            Xwtr = Xw[train_index]
            Xwts = pair_rows(Xw[test_index], reflexive=True)
            yts = (Xwts[:-1:2, -1] > Xwts[1::2, -1]).astype(int)

            # train with sampled arguments
            super().fit_(Xwtr, extra_kwargs=params)
            zts = super().predict(Xwts, paired_rows=True)[::2]
            lst.append((balanced_accuracy_score(yts, zts), list(params.items())))
        heapify(lst)
        self.best_score, tups = heappop(lst)
        self.best_params = dict(tups)
        super().fit_(Xw, extra_kwargs=self.best_params)  # `_estimator` will contain the best_estimator
        return self
