"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._982 import KlingelnbergConicalGearDesign
    from ._983 import KlingelnbergConicalGearMeshDesign
    from ._984 import KlingelnbergConicalGearSetDesign
    from ._985 import KlingelnbergConicalMeshedGearDesign
else:
    import_structure = {
        "_982": ["KlingelnbergConicalGearDesign"],
        "_983": ["KlingelnbergConicalGearMeshDesign"],
        "_984": ["KlingelnbergConicalGearSetDesign"],
        "_985": ["KlingelnbergConicalMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KlingelnbergConicalGearDesign",
    "KlingelnbergConicalGearMeshDesign",
    "KlingelnbergConicalGearSetDesign",
    "KlingelnbergConicalMeshedGearDesign",
)
