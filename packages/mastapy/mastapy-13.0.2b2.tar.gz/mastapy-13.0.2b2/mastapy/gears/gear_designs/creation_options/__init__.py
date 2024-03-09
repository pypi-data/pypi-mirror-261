"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1147 import CylindricalGearPairCreationOptions
    from ._1148 import GearSetCreationOptions
    from ._1149 import HypoidGearSetCreationOptions
    from ._1150 import SpiralBevelGearSetCreationOptions
else:
    import_structure = {
        "_1147": ["CylindricalGearPairCreationOptions"],
        "_1148": ["GearSetCreationOptions"],
        "_1149": ["HypoidGearSetCreationOptions"],
        "_1150": ["SpiralBevelGearSetCreationOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearPairCreationOptions",
    "GearSetCreationOptions",
    "HypoidGearSetCreationOptions",
    "SpiralBevelGearSetCreationOptions",
)
