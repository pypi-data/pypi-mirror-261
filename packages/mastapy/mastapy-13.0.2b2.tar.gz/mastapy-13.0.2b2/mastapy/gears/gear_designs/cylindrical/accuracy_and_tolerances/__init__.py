"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1133 import AGMA2000A88AccuracyGrader
    from ._1134 import AGMA20151A01AccuracyGrader
    from ._1135 import AGMA20151AccuracyGrades
    from ._1136 import AGMAISO13281B14AccuracyGrader
    from ._1137 import CylindricalAccuracyGrader
    from ._1138 import CylindricalAccuracyGraderWithProfileFormAndSlope
    from ._1139 import CylindricalAccuracyGrades
    from ._1140 import CylindricalGearAccuracyTolerances
    from ._1141 import DIN3967SystemOfGearFits
    from ._1142 import ISO132811995AccuracyGrader
    from ._1143 import ISO132812013AccuracyGrader
    from ._1144 import ISO1328AccuracyGraderCommon
    from ._1145 import ISO1328AccuracyGrades
    from ._1146 import OverridableTolerance
else:
    import_structure = {
        "_1133": ["AGMA2000A88AccuracyGrader"],
        "_1134": ["AGMA20151A01AccuracyGrader"],
        "_1135": ["AGMA20151AccuracyGrades"],
        "_1136": ["AGMAISO13281B14AccuracyGrader"],
        "_1137": ["CylindricalAccuracyGrader"],
        "_1138": ["CylindricalAccuracyGraderWithProfileFormAndSlope"],
        "_1139": ["CylindricalAccuracyGrades"],
        "_1140": ["CylindricalGearAccuracyTolerances"],
        "_1141": ["DIN3967SystemOfGearFits"],
        "_1142": ["ISO132811995AccuracyGrader"],
        "_1143": ["ISO132812013AccuracyGrader"],
        "_1144": ["ISO1328AccuracyGraderCommon"],
        "_1145": ["ISO1328AccuracyGrades"],
        "_1146": ["OverridableTolerance"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMA2000A88AccuracyGrader",
    "AGMA20151A01AccuracyGrader",
    "AGMA20151AccuracyGrades",
    "AGMAISO13281B14AccuracyGrader",
    "CylindricalAccuracyGrader",
    "CylindricalAccuracyGraderWithProfileFormAndSlope",
    "CylindricalAccuracyGrades",
    "CylindricalGearAccuracyTolerances",
    "DIN3967SystemOfGearFits",
    "ISO132811995AccuracyGrader",
    "ISO132812013AccuracyGrader",
    "ISO1328AccuracyGraderCommon",
    "ISO1328AccuracyGrades",
    "OverridableTolerance",
)
