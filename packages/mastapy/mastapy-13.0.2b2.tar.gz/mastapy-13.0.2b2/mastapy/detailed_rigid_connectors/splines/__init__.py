"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1391 import CustomSplineHalfDesign
    from ._1392 import CustomSplineJointDesign
    from ._1393 import DetailedSplineJointSettings
    from ._1394 import DIN5480SplineHalfDesign
    from ._1395 import DIN5480SplineJointDesign
    from ._1396 import DudleyEffectiveLengthApproximationOption
    from ._1397 import FitTypes
    from ._1398 import GBT3478SplineHalfDesign
    from ._1399 import GBT3478SplineJointDesign
    from ._1400 import HeatTreatmentTypes
    from ._1401 import ISO4156SplineHalfDesign
    from ._1402 import ISO4156SplineJointDesign
    from ._1403 import JISB1603SplineJointDesign
    from ._1404 import ManufacturingTypes
    from ._1405 import Modules
    from ._1406 import PressureAngleTypes
    from ._1407 import RootTypes
    from ._1408 import SAEFatigueLifeFactorTypes
    from ._1409 import SAESplineHalfDesign
    from ._1410 import SAESplineJointDesign
    from ._1411 import SAETorqueCycles
    from ._1412 import SplineDesignTypes
    from ._1413 import FinishingMethods
    from ._1414 import SplineFitClassType
    from ._1415 import SplineFixtureTypes
    from ._1416 import SplineHalfDesign
    from ._1417 import SplineJointDesign
    from ._1418 import SplineMaterial
    from ._1419 import SplineRatingTypes
    from ._1420 import SplineToleranceClassTypes
    from ._1421 import StandardSplineHalfDesign
    from ._1422 import StandardSplineJointDesign
else:
    import_structure = {
        "_1391": ["CustomSplineHalfDesign"],
        "_1392": ["CustomSplineJointDesign"],
        "_1393": ["DetailedSplineJointSettings"],
        "_1394": ["DIN5480SplineHalfDesign"],
        "_1395": ["DIN5480SplineJointDesign"],
        "_1396": ["DudleyEffectiveLengthApproximationOption"],
        "_1397": ["FitTypes"],
        "_1398": ["GBT3478SplineHalfDesign"],
        "_1399": ["GBT3478SplineJointDesign"],
        "_1400": ["HeatTreatmentTypes"],
        "_1401": ["ISO4156SplineHalfDesign"],
        "_1402": ["ISO4156SplineJointDesign"],
        "_1403": ["JISB1603SplineJointDesign"],
        "_1404": ["ManufacturingTypes"],
        "_1405": ["Modules"],
        "_1406": ["PressureAngleTypes"],
        "_1407": ["RootTypes"],
        "_1408": ["SAEFatigueLifeFactorTypes"],
        "_1409": ["SAESplineHalfDesign"],
        "_1410": ["SAESplineJointDesign"],
        "_1411": ["SAETorqueCycles"],
        "_1412": ["SplineDesignTypes"],
        "_1413": ["FinishingMethods"],
        "_1414": ["SplineFitClassType"],
        "_1415": ["SplineFixtureTypes"],
        "_1416": ["SplineHalfDesign"],
        "_1417": ["SplineJointDesign"],
        "_1418": ["SplineMaterial"],
        "_1419": ["SplineRatingTypes"],
        "_1420": ["SplineToleranceClassTypes"],
        "_1421": ["StandardSplineHalfDesign"],
        "_1422": ["StandardSplineJointDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CustomSplineHalfDesign",
    "CustomSplineJointDesign",
    "DetailedSplineJointSettings",
    "DIN5480SplineHalfDesign",
    "DIN5480SplineJointDesign",
    "DudleyEffectiveLengthApproximationOption",
    "FitTypes",
    "GBT3478SplineHalfDesign",
    "GBT3478SplineJointDesign",
    "HeatTreatmentTypes",
    "ISO4156SplineHalfDesign",
    "ISO4156SplineJointDesign",
    "JISB1603SplineJointDesign",
    "ManufacturingTypes",
    "Modules",
    "PressureAngleTypes",
    "RootTypes",
    "SAEFatigueLifeFactorTypes",
    "SAESplineHalfDesign",
    "SAESplineJointDesign",
    "SAETorqueCycles",
    "SplineDesignTypes",
    "FinishingMethods",
    "SplineFitClassType",
    "SplineFixtureTypes",
    "SplineHalfDesign",
    "SplineJointDesign",
    "SplineMaterial",
    "SplineRatingTypes",
    "SplineToleranceClassTypes",
    "StandardSplineHalfDesign",
    "StandardSplineJointDesign",
)
