"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1453 import ContactSpecification
    from ._1454 import CrowningSpecificationMethod
    from ._1455 import CycloidalAssemblyDesign
    from ._1456 import CycloidalDiscDesign
    from ._1457 import CycloidalDiscDesignExporter
    from ._1458 import CycloidalDiscMaterial
    from ._1459 import CycloidalDiscMaterialDatabase
    from ._1460 import CycloidalDiscModificationsSpecification
    from ._1461 import DirectionOfMeasuredModifications
    from ._1462 import GeometryToExport
    from ._1463 import NamedDiscPhase
    from ._1464 import RingPinsDesign
    from ._1465 import RingPinsMaterial
    from ._1466 import RingPinsMaterialDatabase
else:
    import_structure = {
        "_1453": ["ContactSpecification"],
        "_1454": ["CrowningSpecificationMethod"],
        "_1455": ["CycloidalAssemblyDesign"],
        "_1456": ["CycloidalDiscDesign"],
        "_1457": ["CycloidalDiscDesignExporter"],
        "_1458": ["CycloidalDiscMaterial"],
        "_1459": ["CycloidalDiscMaterialDatabase"],
        "_1460": ["CycloidalDiscModificationsSpecification"],
        "_1461": ["DirectionOfMeasuredModifications"],
        "_1462": ["GeometryToExport"],
        "_1463": ["NamedDiscPhase"],
        "_1464": ["RingPinsDesign"],
        "_1465": ["RingPinsMaterial"],
        "_1466": ["RingPinsMaterialDatabase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ContactSpecification",
    "CrowningSpecificationMethod",
    "CycloidalAssemblyDesign",
    "CycloidalDiscDesign",
    "CycloidalDiscDesignExporter",
    "CycloidalDiscMaterial",
    "CycloidalDiscMaterialDatabase",
    "CycloidalDiscModificationsSpecification",
    "DirectionOfMeasuredModifications",
    "GeometryToExport",
    "NamedDiscPhase",
    "RingPinsDesign",
    "RingPinsMaterial",
    "RingPinsMaterialDatabase",
)
