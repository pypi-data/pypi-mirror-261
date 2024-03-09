"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1443 import KeywayHalfRating
    from ._1444 import KeywayRating
else:
    import_structure = {
        "_1443": ["KeywayHalfRating"],
        "_1444": ["KeywayRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KeywayHalfRating",
    "KeywayRating",
)
