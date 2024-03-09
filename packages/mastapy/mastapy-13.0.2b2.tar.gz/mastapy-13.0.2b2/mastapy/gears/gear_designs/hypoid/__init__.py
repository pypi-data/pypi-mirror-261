"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._986 import HypoidGearDesign
    from ._987 import HypoidGearMeshDesign
    from ._988 import HypoidGearSetDesign
    from ._989 import HypoidMeshedGearDesign
else:
    import_structure = {
        "_986": ["HypoidGearDesign"],
        "_987": ["HypoidGearMeshDesign"],
        "_988": ["HypoidGearSetDesign"],
        "_989": ["HypoidMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "HypoidGearDesign",
    "HypoidGearMeshDesign",
    "HypoidGearSetDesign",
    "HypoidMeshedGearDesign",
)
