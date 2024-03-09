"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._978 import KlingelnbergCycloPalloidHypoidGearDesign
    from ._979 import KlingelnbergCycloPalloidHypoidGearMeshDesign
    from ._980 import KlingelnbergCycloPalloidHypoidGearSetDesign
    from ._981 import KlingelnbergCycloPalloidHypoidMeshedGearDesign
else:
    import_structure = {
        "_978": ["KlingelnbergCycloPalloidHypoidGearDesign"],
        "_979": ["KlingelnbergCycloPalloidHypoidGearMeshDesign"],
        "_980": ["KlingelnbergCycloPalloidHypoidGearSetDesign"],
        "_981": ["KlingelnbergCycloPalloidHypoidMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KlingelnbergCycloPalloidHypoidGearDesign",
    "KlingelnbergCycloPalloidHypoidGearMeshDesign",
    "KlingelnbergCycloPalloidHypoidGearSetDesign",
    "KlingelnbergCycloPalloidHypoidMeshedGearDesign",
)
