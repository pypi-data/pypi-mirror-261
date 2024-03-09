"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._962 import StraightBevelGearDesign
    from ._963 import StraightBevelGearMeshDesign
    from ._964 import StraightBevelGearSetDesign
    from ._965 import StraightBevelMeshedGearDesign
else:
    import_structure = {
        "_962": ["StraightBevelGearDesign"],
        "_963": ["StraightBevelGearMeshDesign"],
        "_964": ["StraightBevelGearSetDesign"],
        "_965": ["StraightBevelMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "StraightBevelGearDesign",
    "StraightBevelGearMeshDesign",
    "StraightBevelGearSetDesign",
    "StraightBevelMeshedGearDesign",
)
