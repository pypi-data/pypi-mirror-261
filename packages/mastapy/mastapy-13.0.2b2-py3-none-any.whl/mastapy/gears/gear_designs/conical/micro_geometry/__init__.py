"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1173 import ConicalGearBiasModification
    from ._1174 import ConicalGearFlankMicroGeometry
    from ._1175 import ConicalGearLeadModification
    from ._1176 import ConicalGearProfileModification
else:
    import_structure = {
        "_1173": ["ConicalGearBiasModification"],
        "_1174": ["ConicalGearFlankMicroGeometry"],
        "_1175": ["ConicalGearLeadModification"],
        "_1176": ["ConicalGearProfileModification"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearBiasModification",
    "ConicalGearFlankMicroGeometry",
    "ConicalGearLeadModification",
    "ConicalGearProfileModification",
)
