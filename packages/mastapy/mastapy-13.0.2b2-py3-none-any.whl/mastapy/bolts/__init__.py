"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1467 import AxialLoadType
    from ._1468 import BoltedJointMaterial
    from ._1469 import BoltedJointMaterialDatabase
    from ._1470 import BoltGeometry
    from ._1471 import BoltGeometryDatabase
    from ._1472 import BoltMaterial
    from ._1473 import BoltMaterialDatabase
    from ._1474 import BoltSection
    from ._1475 import BoltShankType
    from ._1476 import BoltTypes
    from ._1477 import ClampedSection
    from ._1478 import ClampedSectionMaterialDatabase
    from ._1479 import DetailedBoltDesign
    from ._1480 import DetailedBoltedJointDesign
    from ._1481 import HeadCapTypes
    from ._1482 import JointGeometries
    from ._1483 import JointTypes
    from ._1484 import LoadedBolt
    from ._1485 import RolledBeforeOrAfterHeatTreatment
    from ._1486 import StandardSizes
    from ._1487 import StrengthGrades
    from ._1488 import ThreadTypes
    from ._1489 import TighteningTechniques
else:
    import_structure = {
        "_1467": ["AxialLoadType"],
        "_1468": ["BoltedJointMaterial"],
        "_1469": ["BoltedJointMaterialDatabase"],
        "_1470": ["BoltGeometry"],
        "_1471": ["BoltGeometryDatabase"],
        "_1472": ["BoltMaterial"],
        "_1473": ["BoltMaterialDatabase"],
        "_1474": ["BoltSection"],
        "_1475": ["BoltShankType"],
        "_1476": ["BoltTypes"],
        "_1477": ["ClampedSection"],
        "_1478": ["ClampedSectionMaterialDatabase"],
        "_1479": ["DetailedBoltDesign"],
        "_1480": ["DetailedBoltedJointDesign"],
        "_1481": ["HeadCapTypes"],
        "_1482": ["JointGeometries"],
        "_1483": ["JointTypes"],
        "_1484": ["LoadedBolt"],
        "_1485": ["RolledBeforeOrAfterHeatTreatment"],
        "_1486": ["StandardSizes"],
        "_1487": ["StrengthGrades"],
        "_1488": ["ThreadTypes"],
        "_1489": ["TighteningTechniques"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AxialLoadType",
    "BoltedJointMaterial",
    "BoltedJointMaterialDatabase",
    "BoltGeometry",
    "BoltGeometryDatabase",
    "BoltMaterial",
    "BoltMaterialDatabase",
    "BoltSection",
    "BoltShankType",
    "BoltTypes",
    "ClampedSection",
    "ClampedSectionMaterialDatabase",
    "DetailedBoltDesign",
    "DetailedBoltedJointDesign",
    "HeadCapTypes",
    "JointGeometries",
    "JointTypes",
    "LoadedBolt",
    "RolledBeforeOrAfterHeatTreatment",
    "StandardSizes",
    "StrengthGrades",
    "ThreadTypes",
    "TighteningTechniques",
)
