"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1439 import KeyedJointDesign
    from ._1440 import KeyTypes
    from ._1441 import KeywayJointHalfDesign
    from ._1442 import NumberOfKeys
else:
    import_structure = {
        "_1439": ["KeyedJointDesign"],
        "_1440": ["KeyTypes"],
        "_1441": ["KeywayJointHalfDesign"],
        "_1442": ["NumberOfKeys"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KeyedJointDesign",
    "KeyTypes",
    "KeywayJointHalfDesign",
    "NumberOfKeys",
)
