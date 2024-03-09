"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1435 import AGMA6123SplineJointDutyCycleRating
    from ._1436 import GBT17855SplineJointDutyCycleRating
    from ._1437 import SAESplineJointDutyCycleRating
else:
    import_structure = {
        "_1435": ["AGMA6123SplineJointDutyCycleRating"],
        "_1436": ["GBT17855SplineJointDutyCycleRating"],
        "_1437": ["SAESplineJointDutyCycleRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMA6123SplineJointDutyCycleRating",
    "GBT17855SplineJointDutyCycleRating",
    "SAESplineJointDutyCycleRating",
)
