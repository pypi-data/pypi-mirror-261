"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1380 import ElectricMachineHarmonicLoadDataBase
    from ._1381 import ForceDisplayOption
    from ._1382 import HarmonicLoadDataBase
    from ._1383 import HarmonicLoadDataControlExcitationOptionBase
    from ._1384 import HarmonicLoadDataType
    from ._1385 import SpeedDependentHarmonicLoadData
    from ._1386 import StatorToothInterpolator
    from ._1387 import StatorToothLoadInterpolator
    from ._1388 import StatorToothMomentInterpolator
else:
    import_structure = {
        "_1380": ["ElectricMachineHarmonicLoadDataBase"],
        "_1381": ["ForceDisplayOption"],
        "_1382": ["HarmonicLoadDataBase"],
        "_1383": ["HarmonicLoadDataControlExcitationOptionBase"],
        "_1384": ["HarmonicLoadDataType"],
        "_1385": ["SpeedDependentHarmonicLoadData"],
        "_1386": ["StatorToothInterpolator"],
        "_1387": ["StatorToothLoadInterpolator"],
        "_1388": ["StatorToothMomentInterpolator"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ElectricMachineHarmonicLoadDataBase",
    "ForceDisplayOption",
    "HarmonicLoadDataBase",
    "HarmonicLoadDataControlExcitationOptionBase",
    "HarmonicLoadDataType",
    "SpeedDependentHarmonicLoadData",
    "StatorToothInterpolator",
    "StatorToothLoadInterpolator",
    "StatorToothMomentInterpolator",
)
