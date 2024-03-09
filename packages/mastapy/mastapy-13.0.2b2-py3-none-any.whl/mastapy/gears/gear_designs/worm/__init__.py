"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._957 import WormDesign
    from ._958 import WormGearDesign
    from ._959 import WormGearMeshDesign
    from ._960 import WormGearSetDesign
    from ._961 import WormWheelDesign
else:
    import_structure = {
        "_957": ["WormDesign"],
        "_958": ["WormGearDesign"],
        "_959": ["WormGearMeshDesign"],
        "_960": ["WormGearSetDesign"],
        "_961": ["WormWheelDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "WormDesign",
    "WormGearDesign",
    "WormGearMeshDesign",
    "WormGearSetDesign",
    "WormWheelDesign",
)
