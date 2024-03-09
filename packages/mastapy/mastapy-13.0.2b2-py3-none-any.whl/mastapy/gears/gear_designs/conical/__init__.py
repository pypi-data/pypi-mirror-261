"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1151 import ActiveConicalFlank
    from ._1152 import BacklashDistributionRule
    from ._1153 import ConicalFlanks
    from ._1154 import ConicalGearCutter
    from ._1155 import ConicalGearDesign
    from ._1156 import ConicalGearMeshDesign
    from ._1157 import ConicalGearSetDesign
    from ._1158 import ConicalMachineSettingCalculationMethods
    from ._1159 import ConicalManufactureMethods
    from ._1160 import ConicalMeshedGearDesign
    from ._1161 import ConicalMeshMisalignments
    from ._1162 import CutterBladeType
    from ._1163 import CutterGaugeLengths
    from ._1164 import DummyConicalGearCutter
    from ._1165 import FrontEndTypes
    from ._1166 import GleasonSafetyRequirements
    from ._1167 import KIMoSBevelHypoidSingleLoadCaseResultsData
    from ._1168 import KIMoSBevelHypoidSingleRotationAngleResult
    from ._1169 import KlingelnbergFinishingMethods
    from ._1170 import LoadDistributionFactorMethods
    from ._1171 import TopremEntryType
    from ._1172 import TopremLetter
else:
    import_structure = {
        "_1151": ["ActiveConicalFlank"],
        "_1152": ["BacklashDistributionRule"],
        "_1153": ["ConicalFlanks"],
        "_1154": ["ConicalGearCutter"],
        "_1155": ["ConicalGearDesign"],
        "_1156": ["ConicalGearMeshDesign"],
        "_1157": ["ConicalGearSetDesign"],
        "_1158": ["ConicalMachineSettingCalculationMethods"],
        "_1159": ["ConicalManufactureMethods"],
        "_1160": ["ConicalMeshedGearDesign"],
        "_1161": ["ConicalMeshMisalignments"],
        "_1162": ["CutterBladeType"],
        "_1163": ["CutterGaugeLengths"],
        "_1164": ["DummyConicalGearCutter"],
        "_1165": ["FrontEndTypes"],
        "_1166": ["GleasonSafetyRequirements"],
        "_1167": ["KIMoSBevelHypoidSingleLoadCaseResultsData"],
        "_1168": ["KIMoSBevelHypoidSingleRotationAngleResult"],
        "_1169": ["KlingelnbergFinishingMethods"],
        "_1170": ["LoadDistributionFactorMethods"],
        "_1171": ["TopremEntryType"],
        "_1172": ["TopremLetter"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ActiveConicalFlank",
    "BacklashDistributionRule",
    "ConicalFlanks",
    "ConicalGearCutter",
    "ConicalGearDesign",
    "ConicalGearMeshDesign",
    "ConicalGearSetDesign",
    "ConicalMachineSettingCalculationMethods",
    "ConicalManufactureMethods",
    "ConicalMeshedGearDesign",
    "ConicalMeshMisalignments",
    "CutterBladeType",
    "CutterGaugeLengths",
    "DummyConicalGearCutter",
    "FrontEndTypes",
    "GleasonSafetyRequirements",
    "KIMoSBevelHypoidSingleLoadCaseResultsData",
    "KIMoSBevelHypoidSingleRotationAngleResult",
    "KlingelnbergFinishingMethods",
    "LoadDistributionFactorMethods",
    "TopremEntryType",
    "TopremLetter",
)
