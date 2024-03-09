"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1202 import CylindricalGearFEModel
    from ._1203 import CylindricalGearMeshFEModel
    from ._1204 import CylindricalGearSetFEModel
else:
    import_structure = {
        "_1202": ["CylindricalGearFEModel"],
        "_1203": ["CylindricalGearMeshFEModel"],
        "_1204": ["CylindricalGearSetFEModel"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearFEModel",
    "CylindricalGearMeshFEModel",
    "CylindricalGearSetFEModel",
)
