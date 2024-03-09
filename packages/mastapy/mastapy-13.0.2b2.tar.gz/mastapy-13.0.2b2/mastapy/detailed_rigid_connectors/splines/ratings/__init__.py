"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1425 import AGMA6123SplineHalfRating
    from ._1426 import AGMA6123SplineJointRating
    from ._1427 import DIN5466SplineHalfRating
    from ._1428 import DIN5466SplineRating
    from ._1429 import GBT17855SplineHalfRating
    from ._1430 import GBT17855SplineJointRating
    from ._1431 import SAESplineHalfRating
    from ._1432 import SAESplineJointRating
    from ._1433 import SplineHalfRating
    from ._1434 import SplineJointRating
else:
    import_structure = {
        "_1425": ["AGMA6123SplineHalfRating"],
        "_1426": ["AGMA6123SplineJointRating"],
        "_1427": ["DIN5466SplineHalfRating"],
        "_1428": ["DIN5466SplineRating"],
        "_1429": ["GBT17855SplineHalfRating"],
        "_1430": ["GBT17855SplineJointRating"],
        "_1431": ["SAESplineHalfRating"],
        "_1432": ["SAESplineJointRating"],
        "_1433": ["SplineHalfRating"],
        "_1434": ["SplineJointRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMA6123SplineHalfRating",
    "AGMA6123SplineJointRating",
    "DIN5466SplineHalfRating",
    "DIN5466SplineRating",
    "GBT17855SplineHalfRating",
    "GBT17855SplineJointRating",
    "SAESplineHalfRating",
    "SAESplineJointRating",
    "SplineHalfRating",
    "SplineJointRating",
)
