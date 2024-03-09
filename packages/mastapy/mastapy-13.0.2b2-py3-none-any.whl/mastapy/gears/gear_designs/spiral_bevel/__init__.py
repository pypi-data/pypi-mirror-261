"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._970 import SpiralBevelGearDesign
    from ._971 import SpiralBevelGearMeshDesign
    from ._972 import SpiralBevelGearSetDesign
    from ._973 import SpiralBevelMeshedGearDesign
else:
    import_structure = {
        "_970": ["SpiralBevelGearDesign"],
        "_971": ["SpiralBevelGearMeshDesign"],
        "_972": ["SpiralBevelGearSetDesign"],
        "_973": ["SpiralBevelMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "SpiralBevelGearDesign",
    "SpiralBevelGearMeshDesign",
    "SpiralBevelGearSetDesign",
    "SpiralBevelMeshedGearDesign",
)
