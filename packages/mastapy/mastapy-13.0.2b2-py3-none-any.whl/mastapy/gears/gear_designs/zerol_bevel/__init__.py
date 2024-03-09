"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._953 import ZerolBevelGearDesign
    from ._954 import ZerolBevelGearMeshDesign
    from ._955 import ZerolBevelGearSetDesign
    from ._956 import ZerolBevelMeshedGearDesign
else:
    import_structure = {
        "_953": ["ZerolBevelGearDesign"],
        "_954": ["ZerolBevelGearMeshDesign"],
        "_955": ["ZerolBevelGearSetDesign"],
        "_956": ["ZerolBevelMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ZerolBevelGearDesign",
    "ZerolBevelGearMeshDesign",
    "ZerolBevelGearSetDesign",
    "ZerolBevelMeshedGearDesign",
)
