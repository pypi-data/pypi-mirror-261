"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1205 import ConicalGearFEModel
    from ._1206 import ConicalMeshFEModel
    from ._1207 import ConicalSetFEModel
    from ._1208 import FlankDataSource
else:
    import_structure = {
        "_1205": ["ConicalGearFEModel"],
        "_1206": ["ConicalMeshFEModel"],
        "_1207": ["ConicalSetFEModel"],
        "_1208": ["FlankDataSource"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearFEModel",
    "ConicalMeshFEModel",
    "ConicalSetFEModel",
    "FlankDataSource",
)
