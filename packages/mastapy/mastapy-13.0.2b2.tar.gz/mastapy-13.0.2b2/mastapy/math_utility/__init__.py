"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1491 import Range
    from ._1492 import AcousticWeighting
    from ._1493 import AlignmentAxis
    from ._1494 import Axis
    from ._1495 import CirclesOnAxis
    from ._1496 import ComplexMatrix
    from ._1497 import ComplexPartDisplayOption
    from ._1498 import ComplexVector
    from ._1499 import ComplexVector3D
    from ._1500 import ComplexVector6D
    from ._1501 import CoordinateSystem3D
    from ._1502 import CoordinateSystemEditor
    from ._1503 import CoordinateSystemForRotation
    from ._1504 import CoordinateSystemForRotationOrigin
    from ._1505 import DataPrecision
    from ._1506 import DegreeOfFreedom
    from ._1507 import DynamicsResponseScalarResult
    from ._1508 import DynamicsResponseScaling
    from ._1509 import Eigenmode
    from ._1510 import Eigenmodes
    from ._1511 import EulerParameters
    from ._1512 import ExtrapolationOptions
    from ._1513 import FacetedBody
    from ._1514 import FacetedSurface
    from ._1515 import FourierSeries
    from ._1516 import GenericMatrix
    from ._1517 import GriddedSurface
    from ._1518 import HarmonicValue
    from ._1519 import InertiaTensor
    from ._1520 import MassProperties
    from ._1521 import MaxMinMean
    from ._1522 import ComplexMagnitudeMethod
    from ._1523 import MultipleFourierSeriesInterpolator
    from ._1524 import Named2DLocation
    from ._1525 import PIDControlUpdateMethod
    from ._1526 import Quaternion
    from ._1527 import RealMatrix
    from ._1528 import RealVector
    from ._1529 import ResultOptionsFor3DVector
    from ._1530 import RotationAxis
    from ._1531 import RoundedOrder
    from ._1532 import SinCurve
    from ._1533 import SquareMatrix
    from ._1534 import StressPoint
    from ._1535 import TransformMatrix3D
    from ._1536 import TranslationRotation
    from ._1537 import Vector2DListAccessor
    from ._1538 import Vector6D
else:
    import_structure = {
        "_1491": ["Range"],
        "_1492": ["AcousticWeighting"],
        "_1493": ["AlignmentAxis"],
        "_1494": ["Axis"],
        "_1495": ["CirclesOnAxis"],
        "_1496": ["ComplexMatrix"],
        "_1497": ["ComplexPartDisplayOption"],
        "_1498": ["ComplexVector"],
        "_1499": ["ComplexVector3D"],
        "_1500": ["ComplexVector6D"],
        "_1501": ["CoordinateSystem3D"],
        "_1502": ["CoordinateSystemEditor"],
        "_1503": ["CoordinateSystemForRotation"],
        "_1504": ["CoordinateSystemForRotationOrigin"],
        "_1505": ["DataPrecision"],
        "_1506": ["DegreeOfFreedom"],
        "_1507": ["DynamicsResponseScalarResult"],
        "_1508": ["DynamicsResponseScaling"],
        "_1509": ["Eigenmode"],
        "_1510": ["Eigenmodes"],
        "_1511": ["EulerParameters"],
        "_1512": ["ExtrapolationOptions"],
        "_1513": ["FacetedBody"],
        "_1514": ["FacetedSurface"],
        "_1515": ["FourierSeries"],
        "_1516": ["GenericMatrix"],
        "_1517": ["GriddedSurface"],
        "_1518": ["HarmonicValue"],
        "_1519": ["InertiaTensor"],
        "_1520": ["MassProperties"],
        "_1521": ["MaxMinMean"],
        "_1522": ["ComplexMagnitudeMethod"],
        "_1523": ["MultipleFourierSeriesInterpolator"],
        "_1524": ["Named2DLocation"],
        "_1525": ["PIDControlUpdateMethod"],
        "_1526": ["Quaternion"],
        "_1527": ["RealMatrix"],
        "_1528": ["RealVector"],
        "_1529": ["ResultOptionsFor3DVector"],
        "_1530": ["RotationAxis"],
        "_1531": ["RoundedOrder"],
        "_1532": ["SinCurve"],
        "_1533": ["SquareMatrix"],
        "_1534": ["StressPoint"],
        "_1535": ["TransformMatrix3D"],
        "_1536": ["TranslationRotation"],
        "_1537": ["Vector2DListAccessor"],
        "_1538": ["Vector6D"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Range",
    "AcousticWeighting",
    "AlignmentAxis",
    "Axis",
    "CirclesOnAxis",
    "ComplexMatrix",
    "ComplexPartDisplayOption",
    "ComplexVector",
    "ComplexVector3D",
    "ComplexVector6D",
    "CoordinateSystem3D",
    "CoordinateSystemEditor",
    "CoordinateSystemForRotation",
    "CoordinateSystemForRotationOrigin",
    "DataPrecision",
    "DegreeOfFreedom",
    "DynamicsResponseScalarResult",
    "DynamicsResponseScaling",
    "Eigenmode",
    "Eigenmodes",
    "EulerParameters",
    "ExtrapolationOptions",
    "FacetedBody",
    "FacetedSurface",
    "FourierSeries",
    "GenericMatrix",
    "GriddedSurface",
    "HarmonicValue",
    "InertiaTensor",
    "MassProperties",
    "MaxMinMean",
    "ComplexMagnitudeMethod",
    "MultipleFourierSeriesInterpolator",
    "Named2DLocation",
    "PIDControlUpdateMethod",
    "Quaternion",
    "RealMatrix",
    "RealVector",
    "ResultOptionsFor3DVector",
    "RotationAxis",
    "RoundedOrder",
    "SinCurve",
    "SquareMatrix",
    "StressPoint",
    "TransformMatrix3D",
    "TranslationRotation",
    "Vector2DListAccessor",
    "Vector6D",
)
