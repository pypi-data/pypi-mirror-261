"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1445 import AssemblyMethods
    from ._1446 import CalculationMethods
    from ._1447 import InterferenceFitDesign
    from ._1448 import InterferenceFitHalfDesign
    from ._1449 import StressRegions
    from ._1450 import Table4JointInterfaceTypes
else:
    import_structure = {
        "_1445": ["AssemblyMethods"],
        "_1446": ["CalculationMethods"],
        "_1447": ["InterferenceFitDesign"],
        "_1448": ["InterferenceFitHalfDesign"],
        "_1449": ["StressRegions"],
        "_1450": ["Table4JointInterfaceTypes"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AssemblyMethods",
    "CalculationMethods",
    "InterferenceFitDesign",
    "InterferenceFitHalfDesign",
    "StressRegions",
    "Table4JointInterfaceTypes",
)
