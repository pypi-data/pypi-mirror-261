"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1180 import AGMAGleasonConicalGearGeometryMethods
    from ._1181 import BevelGearDesign
    from ._1182 import BevelGearMeshDesign
    from ._1183 import BevelGearSetDesign
    from ._1184 import BevelMeshedGearDesign
    from ._1185 import DrivenMachineCharacteristicGleason
    from ._1186 import EdgeRadiusType
    from ._1187 import FinishingMethods
    from ._1188 import MachineCharacteristicAGMAKlingelnberg
    from ._1189 import PrimeMoverCharacteristicGleason
    from ._1190 import ToothProportionsInputMethod
    from ._1191 import ToothThicknessSpecificationMethod
    from ._1192 import WheelFinishCutterPointWidthRestrictionMethod
else:
    import_structure = {
        "_1180": ["AGMAGleasonConicalGearGeometryMethods"],
        "_1181": ["BevelGearDesign"],
        "_1182": ["BevelGearMeshDesign"],
        "_1183": ["BevelGearSetDesign"],
        "_1184": ["BevelMeshedGearDesign"],
        "_1185": ["DrivenMachineCharacteristicGleason"],
        "_1186": ["EdgeRadiusType"],
        "_1187": ["FinishingMethods"],
        "_1188": ["MachineCharacteristicAGMAKlingelnberg"],
        "_1189": ["PrimeMoverCharacteristicGleason"],
        "_1190": ["ToothProportionsInputMethod"],
        "_1191": ["ToothThicknessSpecificationMethod"],
        "_1192": ["WheelFinishCutterPointWidthRestrictionMethod"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMAGleasonConicalGearGeometryMethods",
    "BevelGearDesign",
    "BevelGearMeshDesign",
    "BevelGearSetDesign",
    "BevelMeshedGearDesign",
    "DrivenMachineCharacteristicGleason",
    "EdgeRadiusType",
    "FinishingMethods",
    "MachineCharacteristicAGMAKlingelnberg",
    "PrimeMoverCharacteristicGleason",
    "ToothProportionsInputMethod",
    "ToothThicknessSpecificationMethod",
    "WheelFinishCutterPointWidthRestrictionMethod",
)
