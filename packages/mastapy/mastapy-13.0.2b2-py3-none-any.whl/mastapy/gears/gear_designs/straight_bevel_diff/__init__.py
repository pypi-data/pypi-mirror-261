"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._966 import StraightBevelDiffGearDesign
    from ._967 import StraightBevelDiffGearMeshDesign
    from ._968 import StraightBevelDiffGearSetDesign
    from ._969 import StraightBevelDiffMeshedGearDesign
else:
    import_structure = {
        "_966": ["StraightBevelDiffGearDesign"],
        "_967": ["StraightBevelDiffGearMeshDesign"],
        "_968": ["StraightBevelDiffGearSetDesign"],
        "_969": ["StraightBevelDiffMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "StraightBevelDiffGearDesign",
    "StraightBevelDiffGearMeshDesign",
    "StraightBevelDiffGearSetDesign",
    "StraightBevelDiffMeshedGearDesign",
)
