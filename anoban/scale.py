# impementing a utility module for feature scaling
# implementing following the sklearn scalers

import numpy as np
from numpy.typing import NDArray
from typing import override


class MaxDivideScaler(object):
    """ """

    def __init__(
        self, copy: bool = True, feature_range: tuple[float, float] = (0.00, 1.000)
    ) -> None:
        self.copy: bool = copy
        self.feature_range: tuple[float, float] = feature_range

    @override
    def __repr__(self) -> str:
        pass

    def fit(self, data: NDArray[np.floating | np.integer] | pd.DataFrame) -> None:
        """ """
        pass

    def fit_transform(self) -> NDArray[np.floating | np.integer]:
        """ """
        pass

    def transform(self) -> NDArray[np.floating | np.integer]:
        """ """
        pass


class MeanNormalizationScaler(object):
    pass


class ZScoreScaler(object):
    pass
