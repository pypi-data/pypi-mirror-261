"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1235 import BeamSectionType
    from ._1236 import ContactPairConstrainedSurfaceType
    from ._1237 import ContactPairReferenceSurfaceType
    from ._1238 import ElementPropertiesShellWallType
else:
    import_structure = {
        "_1235": ["BeamSectionType"],
        "_1236": ["ContactPairConstrainedSurfaceType"],
        "_1237": ["ContactPairReferenceSurfaceType"],
        "_1238": ["ElementPropertiesShellWallType"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BeamSectionType",
    "ContactPairConstrainedSurfaceType",
    "ContactPairReferenceSurfaceType",
    "ElementPropertiesShellWallType",
)
