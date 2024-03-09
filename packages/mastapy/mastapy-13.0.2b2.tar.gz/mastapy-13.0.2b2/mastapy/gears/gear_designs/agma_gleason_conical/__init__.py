"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1193 import AGMAGleasonConicalAccuracyGrades
    from ._1194 import AGMAGleasonConicalGearDesign
    from ._1195 import AGMAGleasonConicalGearMeshDesign
    from ._1196 import AGMAGleasonConicalGearSetDesign
    from ._1197 import AGMAGleasonConicalMeshedGearDesign
else:
    import_structure = {
        "_1193": ["AGMAGleasonConicalAccuracyGrades"],
        "_1194": ["AGMAGleasonConicalGearDesign"],
        "_1195": ["AGMAGleasonConicalGearMeshDesign"],
        "_1196": ["AGMAGleasonConicalGearSetDesign"],
        "_1197": ["AGMAGleasonConicalMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMAGleasonConicalAccuracyGrades",
    "AGMAGleasonConicalGearDesign",
    "AGMAGleasonConicalGearMeshDesign",
    "AGMAGleasonConicalGearSetDesign",
    "AGMAGleasonConicalMeshedGearDesign",
)
