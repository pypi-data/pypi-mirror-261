"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._974 import KlingelnbergCycloPalloidSpiralBevelGearDesign
    from ._975 import KlingelnbergCycloPalloidSpiralBevelGearMeshDesign
    from ._976 import KlingelnbergCycloPalloidSpiralBevelGearSetDesign
    from ._977 import KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign
else:
    import_structure = {
        "_974": ["KlingelnbergCycloPalloidSpiralBevelGearDesign"],
        "_975": ["KlingelnbergCycloPalloidSpiralBevelGearMeshDesign"],
        "_976": ["KlingelnbergCycloPalloidSpiralBevelGearSetDesign"],
        "_977": ["KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KlingelnbergCycloPalloidSpiralBevelGearDesign",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshDesign",
    "KlingelnbergCycloPalloidSpiralBevelGearSetDesign",
    "KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign",
)
