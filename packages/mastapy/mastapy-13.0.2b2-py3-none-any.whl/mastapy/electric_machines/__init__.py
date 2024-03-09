"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1244 import AbstractStator
    from ._1245 import AbstractToothAndSlot
    from ._1246 import AirGapPartition
    from ._1247 import CADConductor
    from ._1248 import CADElectricMachineDetail
    from ._1249 import CADMagnetDetails
    from ._1250 import CADMagnetsForLayer
    from ._1251 import CADRotor
    from ._1252 import CADStator
    from ._1253 import CADToothAndSlot
    from ._1254 import Coil
    from ._1255 import CoilPositionInSlot
    from ._1256 import CoolingDuctLayerSpecification
    from ._1257 import CoolingDuctShape
    from ._1258 import CoreLossBuildFactorSpecificationMethod
    from ._1259 import CoreLossCoefficients
    from ._1260 import DoubleLayerWindingSlotPositions
    from ._1261 import DQAxisConvention
    from ._1262 import Eccentricity
    from ._1263 import ElectricMachineDetail
    from ._1264 import ElectricMachineDetailInitialInformation
    from ._1265 import ElectricMachineMechanicalAnalysisMeshingOptions
    from ._1266 import ElectricMachineMeshingOptions
    from ._1267 import ElectricMachineMeshingOptionsBase
    from ._1268 import ElectricMachineSetup
    from ._1269 import ElectricMachineType
    from ._1270 import FillFactorSpecificationMethod
    from ._1271 import FluxBarrierOrWeb
    from ._1272 import FluxBarrierStyle
    from ._1273 import HairpinConductor
    from ._1274 import HarmonicLoadDataControlExcitationOptionForElectricMachineMode
    from ._1275 import IndividualConductorSpecificationSource
    from ._1276 import InteriorPermanentMagnetAndSynchronousReluctanceRotor
    from ._1277 import InteriorPermanentMagnetMachine
    from ._1278 import IronLossCoefficientSpecificationMethod
    from ._1279 import MagnetClearance
    from ._1280 import MagnetConfiguration
    from ._1281 import MagnetData
    from ._1282 import MagnetDesign
    from ._1283 import MagnetForLayer
    from ._1284 import MagnetisationDirection
    from ._1285 import MagnetMaterial
    from ._1286 import MagnetMaterialDatabase
    from ._1287 import MotorRotorSideFaceDetail
    from ._1288 import NonCADElectricMachineDetail
    from ._1289 import NotchShape
    from ._1290 import NotchSpecification
    from ._1291 import PermanentMagnetAssistedSynchronousReluctanceMachine
    from ._1292 import PermanentMagnetRotor
    from ._1293 import Phase
    from ._1294 import RegionID
    from ._1295 import Rotor
    from ._1296 import RotorInternalLayerSpecification
    from ._1297 import RotorSkewSlice
    from ._1298 import RotorType
    from ._1299 import SingleOrDoubleLayerWindings
    from ._1300 import SlotSectionDetail
    from ._1301 import Stator
    from ._1302 import StatorCutOutSpecification
    from ._1303 import StatorRotorMaterial
    from ._1304 import StatorRotorMaterialDatabase
    from ._1305 import SurfacePermanentMagnetMachine
    from ._1306 import SurfacePermanentMagnetRotor
    from ._1307 import SynchronousReluctanceMachine
    from ._1308 import ToothAndSlot
    from ._1309 import ToothSlotStyle
    from ._1310 import ToothTaperSpecification
    from ._1311 import TwoDimensionalFEModelForAnalysis
    from ._1312 import UShapedLayerSpecification
    from ._1313 import VShapedMagnetLayerSpecification
    from ._1314 import WindingConductor
    from ._1315 import WindingConnection
    from ._1316 import WindingMaterial
    from ._1317 import WindingMaterialDatabase
    from ._1318 import Windings
    from ._1319 import WindingsViewer
    from ._1320 import WindingType
    from ._1321 import WireSizeSpecificationMethod
    from ._1322 import WoundFieldSynchronousMachine
else:
    import_structure = {
        "_1244": ["AbstractStator"],
        "_1245": ["AbstractToothAndSlot"],
        "_1246": ["AirGapPartition"],
        "_1247": ["CADConductor"],
        "_1248": ["CADElectricMachineDetail"],
        "_1249": ["CADMagnetDetails"],
        "_1250": ["CADMagnetsForLayer"],
        "_1251": ["CADRotor"],
        "_1252": ["CADStator"],
        "_1253": ["CADToothAndSlot"],
        "_1254": ["Coil"],
        "_1255": ["CoilPositionInSlot"],
        "_1256": ["CoolingDuctLayerSpecification"],
        "_1257": ["CoolingDuctShape"],
        "_1258": ["CoreLossBuildFactorSpecificationMethod"],
        "_1259": ["CoreLossCoefficients"],
        "_1260": ["DoubleLayerWindingSlotPositions"],
        "_1261": ["DQAxisConvention"],
        "_1262": ["Eccentricity"],
        "_1263": ["ElectricMachineDetail"],
        "_1264": ["ElectricMachineDetailInitialInformation"],
        "_1265": ["ElectricMachineMechanicalAnalysisMeshingOptions"],
        "_1266": ["ElectricMachineMeshingOptions"],
        "_1267": ["ElectricMachineMeshingOptionsBase"],
        "_1268": ["ElectricMachineSetup"],
        "_1269": ["ElectricMachineType"],
        "_1270": ["FillFactorSpecificationMethod"],
        "_1271": ["FluxBarrierOrWeb"],
        "_1272": ["FluxBarrierStyle"],
        "_1273": ["HairpinConductor"],
        "_1274": ["HarmonicLoadDataControlExcitationOptionForElectricMachineMode"],
        "_1275": ["IndividualConductorSpecificationSource"],
        "_1276": ["InteriorPermanentMagnetAndSynchronousReluctanceRotor"],
        "_1277": ["InteriorPermanentMagnetMachine"],
        "_1278": ["IronLossCoefficientSpecificationMethod"],
        "_1279": ["MagnetClearance"],
        "_1280": ["MagnetConfiguration"],
        "_1281": ["MagnetData"],
        "_1282": ["MagnetDesign"],
        "_1283": ["MagnetForLayer"],
        "_1284": ["MagnetisationDirection"],
        "_1285": ["MagnetMaterial"],
        "_1286": ["MagnetMaterialDatabase"],
        "_1287": ["MotorRotorSideFaceDetail"],
        "_1288": ["NonCADElectricMachineDetail"],
        "_1289": ["NotchShape"],
        "_1290": ["NotchSpecification"],
        "_1291": ["PermanentMagnetAssistedSynchronousReluctanceMachine"],
        "_1292": ["PermanentMagnetRotor"],
        "_1293": ["Phase"],
        "_1294": ["RegionID"],
        "_1295": ["Rotor"],
        "_1296": ["RotorInternalLayerSpecification"],
        "_1297": ["RotorSkewSlice"],
        "_1298": ["RotorType"],
        "_1299": ["SingleOrDoubleLayerWindings"],
        "_1300": ["SlotSectionDetail"],
        "_1301": ["Stator"],
        "_1302": ["StatorCutOutSpecification"],
        "_1303": ["StatorRotorMaterial"],
        "_1304": ["StatorRotorMaterialDatabase"],
        "_1305": ["SurfacePermanentMagnetMachine"],
        "_1306": ["SurfacePermanentMagnetRotor"],
        "_1307": ["SynchronousReluctanceMachine"],
        "_1308": ["ToothAndSlot"],
        "_1309": ["ToothSlotStyle"],
        "_1310": ["ToothTaperSpecification"],
        "_1311": ["TwoDimensionalFEModelForAnalysis"],
        "_1312": ["UShapedLayerSpecification"],
        "_1313": ["VShapedMagnetLayerSpecification"],
        "_1314": ["WindingConductor"],
        "_1315": ["WindingConnection"],
        "_1316": ["WindingMaterial"],
        "_1317": ["WindingMaterialDatabase"],
        "_1318": ["Windings"],
        "_1319": ["WindingsViewer"],
        "_1320": ["WindingType"],
        "_1321": ["WireSizeSpecificationMethod"],
        "_1322": ["WoundFieldSynchronousMachine"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractStator",
    "AbstractToothAndSlot",
    "AirGapPartition",
    "CADConductor",
    "CADElectricMachineDetail",
    "CADMagnetDetails",
    "CADMagnetsForLayer",
    "CADRotor",
    "CADStator",
    "CADToothAndSlot",
    "Coil",
    "CoilPositionInSlot",
    "CoolingDuctLayerSpecification",
    "CoolingDuctShape",
    "CoreLossBuildFactorSpecificationMethod",
    "CoreLossCoefficients",
    "DoubleLayerWindingSlotPositions",
    "DQAxisConvention",
    "Eccentricity",
    "ElectricMachineDetail",
    "ElectricMachineDetailInitialInformation",
    "ElectricMachineMechanicalAnalysisMeshingOptions",
    "ElectricMachineMeshingOptions",
    "ElectricMachineMeshingOptionsBase",
    "ElectricMachineSetup",
    "ElectricMachineType",
    "FillFactorSpecificationMethod",
    "FluxBarrierOrWeb",
    "FluxBarrierStyle",
    "HairpinConductor",
    "HarmonicLoadDataControlExcitationOptionForElectricMachineMode",
    "IndividualConductorSpecificationSource",
    "InteriorPermanentMagnetAndSynchronousReluctanceRotor",
    "InteriorPermanentMagnetMachine",
    "IronLossCoefficientSpecificationMethod",
    "MagnetClearance",
    "MagnetConfiguration",
    "MagnetData",
    "MagnetDesign",
    "MagnetForLayer",
    "MagnetisationDirection",
    "MagnetMaterial",
    "MagnetMaterialDatabase",
    "MotorRotorSideFaceDetail",
    "NonCADElectricMachineDetail",
    "NotchShape",
    "NotchSpecification",
    "PermanentMagnetAssistedSynchronousReluctanceMachine",
    "PermanentMagnetRotor",
    "Phase",
    "RegionID",
    "Rotor",
    "RotorInternalLayerSpecification",
    "RotorSkewSlice",
    "RotorType",
    "SingleOrDoubleLayerWindings",
    "SlotSectionDetail",
    "Stator",
    "StatorCutOutSpecification",
    "StatorRotorMaterial",
    "StatorRotorMaterialDatabase",
    "SurfacePermanentMagnetMachine",
    "SurfacePermanentMagnetRotor",
    "SynchronousReluctanceMachine",
    "ToothAndSlot",
    "ToothSlotStyle",
    "ToothTaperSpecification",
    "TwoDimensionalFEModelForAnalysis",
    "UShapedLayerSpecification",
    "VShapedMagnetLayerSpecification",
    "WindingConductor",
    "WindingConnection",
    "WindingMaterial",
    "WindingMaterialDatabase",
    "Windings",
    "WindingsViewer",
    "WindingType",
    "WireSizeSpecificationMethod",
    "WoundFieldSynchronousMachine",
)
