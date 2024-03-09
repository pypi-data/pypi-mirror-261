"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1209 import CylindricalGearLTCAContactChartDataAsTextFile
    from ._1210 import CylindricalGearLTCAContactCharts
    from ._1211 import CylindricalGearWorstLTCAContactChartDataAsTextFile
    from ._1212 import CylindricalGearWorstLTCAContactCharts
    from ._1213 import GearLTCAContactChartDataAsTextFile
    from ._1214 import GearLTCAContactCharts
    from ._1215 import PointsWithWorstResults
else:
    import_structure = {
        "_1209": ["CylindricalGearLTCAContactChartDataAsTextFile"],
        "_1210": ["CylindricalGearLTCAContactCharts"],
        "_1211": ["CylindricalGearWorstLTCAContactChartDataAsTextFile"],
        "_1212": ["CylindricalGearWorstLTCAContactCharts"],
        "_1213": ["GearLTCAContactChartDataAsTextFile"],
        "_1214": ["GearLTCAContactCharts"],
        "_1215": ["PointsWithWorstResults"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearLTCAContactChartDataAsTextFile",
    "CylindricalGearLTCAContactCharts",
    "CylindricalGearWorstLTCAContactChartDataAsTextFile",
    "CylindricalGearWorstLTCAContactCharts",
    "GearLTCAContactChartDataAsTextFile",
    "GearLTCAContactCharts",
    "PointsWithWorstResults",
)
