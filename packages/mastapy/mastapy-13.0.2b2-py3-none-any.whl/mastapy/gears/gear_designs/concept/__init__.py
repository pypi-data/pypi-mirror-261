"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1177 import ConceptGearDesign
    from ._1178 import ConceptGearMeshDesign
    from ._1179 import ConceptGearSetDesign
else:
    import_structure = {
        "_1177": ["ConceptGearDesign"],
        "_1178": ["ConceptGearMeshDesign"],
        "_1179": ["ConceptGearSetDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConceptGearDesign",
    "ConceptGearMeshDesign",
    "ConceptGearSetDesign",
)
