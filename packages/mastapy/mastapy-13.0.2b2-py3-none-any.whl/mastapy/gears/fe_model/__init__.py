"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1198 import GearFEModel
    from ._1199 import GearMeshFEModel
    from ._1200 import GearMeshingElementOptions
    from ._1201 import GearSetFEModel
else:
    import_structure = {
        "_1198": ["GearFEModel"],
        "_1199": ["GearMeshFEModel"],
        "_1200": ["GearMeshingElementOptions"],
        "_1201": ["GearSetFEModel"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "GearFEModel",
    "GearMeshFEModel",
    "GearMeshingElementOptions",
    "GearSetFEModel",
)
