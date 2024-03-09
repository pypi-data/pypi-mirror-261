"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1323 import DynamicForceResults
    from ._1324 import EfficiencyResults
    from ._1325 import ElectricMachineDQModel
    from ._1326 import ElectricMachineMechanicalResults
    from ._1327 import ElectricMachineMechanicalResultsViewable
    from ._1328 import ElectricMachineResults
    from ._1329 import ElectricMachineResultsForConductorTurn
    from ._1330 import ElectricMachineResultsForConductorTurnAtTimeStep
    from ._1331 import ElectricMachineResultsForLineToLine
    from ._1332 import ElectricMachineResultsForOpenCircuitAndOnLoad
    from ._1333 import ElectricMachineResultsForPhase
    from ._1334 import ElectricMachineResultsForPhaseAtTimeStep
    from ._1335 import ElectricMachineResultsForStatorToothAtTimeStep
    from ._1336 import ElectricMachineResultsLineToLineAtTimeStep
    from ._1337 import ElectricMachineResultsTimeStep
    from ._1338 import ElectricMachineResultsTimeStepAtLocation
    from ._1339 import ElectricMachineResultsViewable
    from ._1340 import ElectricMachineForceViewOptions
    from ._1342 import LinearDQModel
    from ._1343 import MaximumTorqueResultsPoints
    from ._1344 import NonLinearDQModel
    from ._1345 import NonLinearDQModelGeneratorSettings
    from ._1346 import OnLoadElectricMachineResults
    from ._1347 import OpenCircuitElectricMachineResults
else:
    import_structure = {
        "_1323": ["DynamicForceResults"],
        "_1324": ["EfficiencyResults"],
        "_1325": ["ElectricMachineDQModel"],
        "_1326": ["ElectricMachineMechanicalResults"],
        "_1327": ["ElectricMachineMechanicalResultsViewable"],
        "_1328": ["ElectricMachineResults"],
        "_1329": ["ElectricMachineResultsForConductorTurn"],
        "_1330": ["ElectricMachineResultsForConductorTurnAtTimeStep"],
        "_1331": ["ElectricMachineResultsForLineToLine"],
        "_1332": ["ElectricMachineResultsForOpenCircuitAndOnLoad"],
        "_1333": ["ElectricMachineResultsForPhase"],
        "_1334": ["ElectricMachineResultsForPhaseAtTimeStep"],
        "_1335": ["ElectricMachineResultsForStatorToothAtTimeStep"],
        "_1336": ["ElectricMachineResultsLineToLineAtTimeStep"],
        "_1337": ["ElectricMachineResultsTimeStep"],
        "_1338": ["ElectricMachineResultsTimeStepAtLocation"],
        "_1339": ["ElectricMachineResultsViewable"],
        "_1340": ["ElectricMachineForceViewOptions"],
        "_1342": ["LinearDQModel"],
        "_1343": ["MaximumTorqueResultsPoints"],
        "_1344": ["NonLinearDQModel"],
        "_1345": ["NonLinearDQModelGeneratorSettings"],
        "_1346": ["OnLoadElectricMachineResults"],
        "_1347": ["OpenCircuitElectricMachineResults"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DynamicForceResults",
    "EfficiencyResults",
    "ElectricMachineDQModel",
    "ElectricMachineMechanicalResults",
    "ElectricMachineMechanicalResultsViewable",
    "ElectricMachineResults",
    "ElectricMachineResultsForConductorTurn",
    "ElectricMachineResultsForConductorTurnAtTimeStep",
    "ElectricMachineResultsForLineToLine",
    "ElectricMachineResultsForOpenCircuitAndOnLoad",
    "ElectricMachineResultsForPhase",
    "ElectricMachineResultsForPhaseAtTimeStep",
    "ElectricMachineResultsForStatorToothAtTimeStep",
    "ElectricMachineResultsLineToLineAtTimeStep",
    "ElectricMachineResultsTimeStep",
    "ElectricMachineResultsTimeStepAtLocation",
    "ElectricMachineResultsViewable",
    "ElectricMachineForceViewOptions",
    "LinearDQModel",
    "MaximumTorqueResultsPoints",
    "NonLinearDQModel",
    "NonLinearDQModelGeneratorSettings",
    "OnLoadElectricMachineResults",
    "OpenCircuitElectricMachineResults",
)
