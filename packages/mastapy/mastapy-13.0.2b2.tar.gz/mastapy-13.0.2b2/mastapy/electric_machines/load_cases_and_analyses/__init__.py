"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1348 import BasicDynamicForceLoadCase
    from ._1349 import DynamicForceAnalysis
    from ._1350 import DynamicForceLoadCase
    from ._1351 import DynamicForcesOperatingPoint
    from ._1352 import EfficiencyMapAnalysis
    from ._1353 import EfficiencyMapLoadCase
    from ._1354 import ElectricMachineAnalysis
    from ._1355 import ElectricMachineBasicMechanicalLossSettings
    from ._1356 import ElectricMachineControlStrategy
    from ._1357 import ElectricMachineEfficiencyMapSettings
    from ._1358 import ElectricMachineFEAnalysis
    from ._1359 import ElectricMachineFEMechanicalAnalysis
    from ._1360 import ElectricMachineLoadCase
    from ._1361 import ElectricMachineLoadCaseBase
    from ._1362 import ElectricMachineLoadCaseGroup
    from ._1363 import ElectricMachineMechanicalLoadCase
    from ._1364 import EndWindingInductanceMethod
    from ._1365 import LeadingOrLagging
    from ._1366 import LoadCaseType
    from ._1367 import LoadCaseTypeSelector
    from ._1368 import MotoringOrGenerating
    from ._1369 import NonLinearDQModelMultipleOperatingPointsLoadCase
    from ._1370 import NumberOfStepsPerOperatingPointSpecificationMethod
    from ._1371 import OperatingPointsSpecificationMethod
    from ._1372 import SingleOperatingPointAnalysis
    from ._1373 import SlotDetailForAnalysis
    from ._1374 import SpecifyTorqueOrCurrent
    from ._1375 import SpeedPointsDistribution
    from ._1376 import SpeedTorqueCurveAnalysis
    from ._1377 import SpeedTorqueCurveLoadCase
    from ._1378 import SpeedTorqueLoadCase
    from ._1379 import Temperatures
else:
    import_structure = {
        "_1348": ["BasicDynamicForceLoadCase"],
        "_1349": ["DynamicForceAnalysis"],
        "_1350": ["DynamicForceLoadCase"],
        "_1351": ["DynamicForcesOperatingPoint"],
        "_1352": ["EfficiencyMapAnalysis"],
        "_1353": ["EfficiencyMapLoadCase"],
        "_1354": ["ElectricMachineAnalysis"],
        "_1355": ["ElectricMachineBasicMechanicalLossSettings"],
        "_1356": ["ElectricMachineControlStrategy"],
        "_1357": ["ElectricMachineEfficiencyMapSettings"],
        "_1358": ["ElectricMachineFEAnalysis"],
        "_1359": ["ElectricMachineFEMechanicalAnalysis"],
        "_1360": ["ElectricMachineLoadCase"],
        "_1361": ["ElectricMachineLoadCaseBase"],
        "_1362": ["ElectricMachineLoadCaseGroup"],
        "_1363": ["ElectricMachineMechanicalLoadCase"],
        "_1364": ["EndWindingInductanceMethod"],
        "_1365": ["LeadingOrLagging"],
        "_1366": ["LoadCaseType"],
        "_1367": ["LoadCaseTypeSelector"],
        "_1368": ["MotoringOrGenerating"],
        "_1369": ["NonLinearDQModelMultipleOperatingPointsLoadCase"],
        "_1370": ["NumberOfStepsPerOperatingPointSpecificationMethod"],
        "_1371": ["OperatingPointsSpecificationMethod"],
        "_1372": ["SingleOperatingPointAnalysis"],
        "_1373": ["SlotDetailForAnalysis"],
        "_1374": ["SpecifyTorqueOrCurrent"],
        "_1375": ["SpeedPointsDistribution"],
        "_1376": ["SpeedTorqueCurveAnalysis"],
        "_1377": ["SpeedTorqueCurveLoadCase"],
        "_1378": ["SpeedTorqueLoadCase"],
        "_1379": ["Temperatures"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BasicDynamicForceLoadCase",
    "DynamicForceAnalysis",
    "DynamicForceLoadCase",
    "DynamicForcesOperatingPoint",
    "EfficiencyMapAnalysis",
    "EfficiencyMapLoadCase",
    "ElectricMachineAnalysis",
    "ElectricMachineBasicMechanicalLossSettings",
    "ElectricMachineControlStrategy",
    "ElectricMachineEfficiencyMapSettings",
    "ElectricMachineFEAnalysis",
    "ElectricMachineFEMechanicalAnalysis",
    "ElectricMachineLoadCase",
    "ElectricMachineLoadCaseBase",
    "ElectricMachineLoadCaseGroup",
    "ElectricMachineMechanicalLoadCase",
    "EndWindingInductanceMethod",
    "LeadingOrLagging",
    "LoadCaseType",
    "LoadCaseTypeSelector",
    "MotoringOrGenerating",
    "NonLinearDQModelMultipleOperatingPointsLoadCase",
    "NumberOfStepsPerOperatingPointSpecificationMethod",
    "OperatingPointsSpecificationMethod",
    "SingleOperatingPointAnalysis",
    "SlotDetailForAnalysis",
    "SpecifyTorqueOrCurrent",
    "SpeedPointsDistribution",
    "SpeedTorqueCurveAnalysis",
    "SpeedTorqueCurveLoadCase",
    "SpeedTorqueLoadCase",
    "Temperatures",
)
