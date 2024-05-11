# impementing a utility module for feature scaling
# implementing following the sklearn scalers

import numpy as np
import pandas as pd
from numpy.typing import NDArray
from typing import override


class MaxDivideScaler(object):
    """ """

    def __init__(
        self, copy: bool = True, range_max: float = 1.000
    ) -> None:
        self.copy: bool = copy
        self.range_max: float = range_max
        self.is_fitted: bool = False

    @override
    def __repr__(self) -> str:
        pass

    def fit(self, data: NDArray[np.floating | np.integer] | pd.DataFrame) -> None:
        """ """
        self.is_fitted = True
        self.cols_max = data.max(axis = 0)
        pass

    def fit_transform(self, data: NDArray[np.floating | np.integer] | pd.DataFrame) -> NDArray[np.floating | np.integer]:
        """ """
        self.is_fitted = True
        pass

    def transform(self) -> NDArray[np.floating | np.integer]:
        """ """
        pass


class MeanNormalizationScaler(object):
    """ """

    def __init__(
        self, copy: bool = True, range_max: float = 1.000
    ) -> None:
        self.copy: bool = copy
        self.is_fitted: bool = False

    @override
    def __repr__(self) -> str:
        pass

    def fit(self, data: NDArray[np.floating | np.integer] | pd.DataFrame) -> None:
        """ """
        self.is_fitted = True
        self.cols_mean = data.mean(axis = 0)
        self.cols_min = data.min(axis = 0)
        self.cols_max = data.max(axis = 0)


    def fit_transform(self, data: NDArray[np.floating | np.integer] | pd.DataFrame) -> NDArray[np.floating | np.integer]:
        """ """
        self.is_fitted = True
        pass

    def transform(self) -> NDArray[np.floating | np.integer]:
        """ """
        if not is_fitted:
            except In
        pass


class ZScoreScaler(object):
    pass
