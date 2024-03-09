"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._999 import AddendumModificationDistributionRule
    from ._1000 import BacklashSpecification
    from ._1001 import BasicRackProfiles
    from ._1002 import CaseHardeningProperties
    from ._1003 import CreateNewSuitableCutterOption
    from ._1004 import CrossedAxisCylindricalGearPair
    from ._1005 import CrossedAxisCylindricalGearPairLineContact
    from ._1006 import CrossedAxisCylindricalGearPairPointContact
    from ._1007 import CylindricalGearAbstractRack
    from ._1008 import CylindricalGearAbstractRackFlank
    from ._1009 import CylindricalGearBasicRack
    from ._1010 import CylindricalGearBasicRackFlank
    from ._1011 import CylindricalGearCuttingOptions
    from ._1012 import CylindricalGearDefaults
    from ._1013 import CylindricalGearDesign
    from ._1014 import CylindricalGearDesignConstraint
    from ._1015 import CylindricalGearDesignConstraints
    from ._1016 import CylindricalGearDesignConstraintsDatabase
    from ._1017 import CylindricalGearDesignConstraintSettings
    from ._1018 import CylindricalGearFlankDesign
    from ._1019 import CylindricalGearMeshDesign
    from ._1020 import CylindricalGearMeshFlankDesign
    from ._1021 import CylindricalGearMicroGeometrySettings
    from ._1022 import CylindricalGearMicroGeometrySettingsDatabase
    from ._1023 import CylindricalGearMicroGeometrySettingsItem
    from ._1024 import CylindricalGearPinionTypeCutter
    from ._1025 import CylindricalGearPinionTypeCutterFlank
    from ._1026 import CylindricalGearProfileMeasurement
    from ._1027 import CylindricalGearProfileMeasurementType
    from ._1028 import CylindricalGearProfileModifications
    from ._1029 import CylindricalGearSetDesign
    from ._1030 import CylindricalGearSetFlankDesign
    from ._1031 import CylindricalGearSetMacroGeometryOptimiser
    from ._1032 import CylindricalGearSetManufacturingConfigurationSelection
    from ._1033 import CylindricalGearSetMicroGeometrySettings
    from ._1034 import CylindricalGearSetOptimisationWrapper
    from ._1035 import CylindricalGearTableMGItemDetail
    from ._1036 import CylindricalGearTableWithMGCharts
    from ._1037 import CylindricalGearToothThicknessSpecification
    from ._1038 import CylindricalMeshAngularBacklash
    from ._1039 import CylindricalMeshedGear
    from ._1040 import CylindricalMeshedGearFlank
    from ._1041 import CylindricalMeshLinearBacklashSpecification
    from ._1042 import CylindricalPlanetaryGearSetDesign
    from ._1043 import CylindricalPlanetGearDesign
    from ._1044 import DIN3967AllowanceSeries
    from ._1045 import DIN3967ToleranceSeries
    from ._1046 import DoubleAxisScaleAndRange
    from ._1047 import FinishToothThicknessDesignSpecification
    from ._1048 import GearFitSystems
    from ._1049 import GearManufacturingConfigSetupViewModel
    from ._1050 import GearSetManufacturingConfigurationSetup
    from ._1051 import GeometrySpecificationType
    from ._1052 import HardenedMaterialProperties
    from ._1053 import HardnessProfileCalculationMethod
    from ._1054 import HeatTreatmentType
    from ._1055 import ISO6336Geometry
    from ._1056 import ISO6336GeometryBase
    from ._1057 import ISO6336GeometryForShapedGears
    from ._1058 import ISO6336GeometryManufactured
    from ._1059 import LinearBacklashSpecification
    from ._1060 import LTCALoadCaseModifiableSettings
    from ._1061 import LTCASettings
    from ._1062 import MicroGeometryConvention
    from ._1063 import MicroGeometryProfileConvention
    from ._1064 import Micropitting
    from ._1065 import NamedPlanetAssemblyIndex
    from ._1066 import NamedPlanetSideBandAmplitudeFactor
    from ._1067 import ReadonlyToothThicknessSpecification
    from ._1068 import RelativeMeasurementViewModel
    from ._1069 import RelativeValuesSpecification
    from ._1070 import RootStressSurfaceChartOption
    from ._1071 import Scuffing
    from ._1072 import ScuffingCoefficientOfFrictionMethods
    from ._1073 import ScuffingTemperatureMethodsAGMA
    from ._1074 import ScuffingTemperatureMethodsISO
    from ._1075 import ShaperEdgeTypes
    from ._1076 import SpurGearLoadSharingCodes
    from ._1077 import StandardRack
    from ._1078 import StandardRackFlank
    from ._1079 import SurfaceRoughness
    from ._1080 import ThicknessType
    from ._1081 import TiffAnalysisSettings
    from ._1082 import TipAlterationCoefficientMethod
    from ._1083 import TolerancedMetalMeasurements
    from ._1084 import TolerancedValueSpecification
    from ._1085 import ToothFlankFractureAnalysisSettings
    from ._1086 import ToothThicknessSpecification
    from ._1087 import ToothThicknessSpecificationBase
    from ._1088 import TypeOfMechanismHousing
    from ._1089 import Usage
else:
    import_structure = {
        "_999": ["AddendumModificationDistributionRule"],
        "_1000": ["BacklashSpecification"],
        "_1001": ["BasicRackProfiles"],
        "_1002": ["CaseHardeningProperties"],
        "_1003": ["CreateNewSuitableCutterOption"],
        "_1004": ["CrossedAxisCylindricalGearPair"],
        "_1005": ["CrossedAxisCylindricalGearPairLineContact"],
        "_1006": ["CrossedAxisCylindricalGearPairPointContact"],
        "_1007": ["CylindricalGearAbstractRack"],
        "_1008": ["CylindricalGearAbstractRackFlank"],
        "_1009": ["CylindricalGearBasicRack"],
        "_1010": ["CylindricalGearBasicRackFlank"],
        "_1011": ["CylindricalGearCuttingOptions"],
        "_1012": ["CylindricalGearDefaults"],
        "_1013": ["CylindricalGearDesign"],
        "_1014": ["CylindricalGearDesignConstraint"],
        "_1015": ["CylindricalGearDesignConstraints"],
        "_1016": ["CylindricalGearDesignConstraintsDatabase"],
        "_1017": ["CylindricalGearDesignConstraintSettings"],
        "_1018": ["CylindricalGearFlankDesign"],
        "_1019": ["CylindricalGearMeshDesign"],
        "_1020": ["CylindricalGearMeshFlankDesign"],
        "_1021": ["CylindricalGearMicroGeometrySettings"],
        "_1022": ["CylindricalGearMicroGeometrySettingsDatabase"],
        "_1023": ["CylindricalGearMicroGeometrySettingsItem"],
        "_1024": ["CylindricalGearPinionTypeCutter"],
        "_1025": ["CylindricalGearPinionTypeCutterFlank"],
        "_1026": ["CylindricalGearProfileMeasurement"],
        "_1027": ["CylindricalGearProfileMeasurementType"],
        "_1028": ["CylindricalGearProfileModifications"],
        "_1029": ["CylindricalGearSetDesign"],
        "_1030": ["CylindricalGearSetFlankDesign"],
        "_1031": ["CylindricalGearSetMacroGeometryOptimiser"],
        "_1032": ["CylindricalGearSetManufacturingConfigurationSelection"],
        "_1033": ["CylindricalGearSetMicroGeometrySettings"],
        "_1034": ["CylindricalGearSetOptimisationWrapper"],
        "_1035": ["CylindricalGearTableMGItemDetail"],
        "_1036": ["CylindricalGearTableWithMGCharts"],
        "_1037": ["CylindricalGearToothThicknessSpecification"],
        "_1038": ["CylindricalMeshAngularBacklash"],
        "_1039": ["CylindricalMeshedGear"],
        "_1040": ["CylindricalMeshedGearFlank"],
        "_1041": ["CylindricalMeshLinearBacklashSpecification"],
        "_1042": ["CylindricalPlanetaryGearSetDesign"],
        "_1043": ["CylindricalPlanetGearDesign"],
        "_1044": ["DIN3967AllowanceSeries"],
        "_1045": ["DIN3967ToleranceSeries"],
        "_1046": ["DoubleAxisScaleAndRange"],
        "_1047": ["FinishToothThicknessDesignSpecification"],
        "_1048": ["GearFitSystems"],
        "_1049": ["GearManufacturingConfigSetupViewModel"],
        "_1050": ["GearSetManufacturingConfigurationSetup"],
        "_1051": ["GeometrySpecificationType"],
        "_1052": ["HardenedMaterialProperties"],
        "_1053": ["HardnessProfileCalculationMethod"],
        "_1054": ["HeatTreatmentType"],
        "_1055": ["ISO6336Geometry"],
        "_1056": ["ISO6336GeometryBase"],
        "_1057": ["ISO6336GeometryForShapedGears"],
        "_1058": ["ISO6336GeometryManufactured"],
        "_1059": ["LinearBacklashSpecification"],
        "_1060": ["LTCALoadCaseModifiableSettings"],
        "_1061": ["LTCASettings"],
        "_1062": ["MicroGeometryConvention"],
        "_1063": ["MicroGeometryProfileConvention"],
        "_1064": ["Micropitting"],
        "_1065": ["NamedPlanetAssemblyIndex"],
        "_1066": ["NamedPlanetSideBandAmplitudeFactor"],
        "_1067": ["ReadonlyToothThicknessSpecification"],
        "_1068": ["RelativeMeasurementViewModel"],
        "_1069": ["RelativeValuesSpecification"],
        "_1070": ["RootStressSurfaceChartOption"],
        "_1071": ["Scuffing"],
        "_1072": ["ScuffingCoefficientOfFrictionMethods"],
        "_1073": ["ScuffingTemperatureMethodsAGMA"],
        "_1074": ["ScuffingTemperatureMethodsISO"],
        "_1075": ["ShaperEdgeTypes"],
        "_1076": ["SpurGearLoadSharingCodes"],
        "_1077": ["StandardRack"],
        "_1078": ["StandardRackFlank"],
        "_1079": ["SurfaceRoughness"],
        "_1080": ["ThicknessType"],
        "_1081": ["TiffAnalysisSettings"],
        "_1082": ["TipAlterationCoefficientMethod"],
        "_1083": ["TolerancedMetalMeasurements"],
        "_1084": ["TolerancedValueSpecification"],
        "_1085": ["ToothFlankFractureAnalysisSettings"],
        "_1086": ["ToothThicknessSpecification"],
        "_1087": ["ToothThicknessSpecificationBase"],
        "_1088": ["TypeOfMechanismHousing"],
        "_1089": ["Usage"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AddendumModificationDistributionRule",
    "BacklashSpecification",
    "BasicRackProfiles",
    "CaseHardeningProperties",
    "CreateNewSuitableCutterOption",
    "CrossedAxisCylindricalGearPair",
    "CrossedAxisCylindricalGearPairLineContact",
    "CrossedAxisCylindricalGearPairPointContact",
    "CylindricalGearAbstractRack",
    "CylindricalGearAbstractRackFlank",
    "CylindricalGearBasicRack",
    "CylindricalGearBasicRackFlank",
    "CylindricalGearCuttingOptions",
    "CylindricalGearDefaults",
    "CylindricalGearDesign",
    "CylindricalGearDesignConstraint",
    "CylindricalGearDesignConstraints",
    "CylindricalGearDesignConstraintsDatabase",
    "CylindricalGearDesignConstraintSettings",
    "CylindricalGearFlankDesign",
    "CylindricalGearMeshDesign",
    "CylindricalGearMeshFlankDesign",
    "CylindricalGearMicroGeometrySettings",
    "CylindricalGearMicroGeometrySettingsDatabase",
    "CylindricalGearMicroGeometrySettingsItem",
    "CylindricalGearPinionTypeCutter",
    "CylindricalGearPinionTypeCutterFlank",
    "CylindricalGearProfileMeasurement",
    "CylindricalGearProfileMeasurementType",
    "CylindricalGearProfileModifications",
    "CylindricalGearSetDesign",
    "CylindricalGearSetFlankDesign",
    "CylindricalGearSetMacroGeometryOptimiser",
    "CylindricalGearSetManufacturingConfigurationSelection",
    "CylindricalGearSetMicroGeometrySettings",
    "CylindricalGearSetOptimisationWrapper",
    "CylindricalGearTableMGItemDetail",
    "CylindricalGearTableWithMGCharts",
    "CylindricalGearToothThicknessSpecification",
    "CylindricalMeshAngularBacklash",
    "CylindricalMeshedGear",
    "CylindricalMeshedGearFlank",
    "CylindricalMeshLinearBacklashSpecification",
    "CylindricalPlanetaryGearSetDesign",
    "CylindricalPlanetGearDesign",
    "DIN3967AllowanceSeries",
    "DIN3967ToleranceSeries",
    "DoubleAxisScaleAndRange",
    "FinishToothThicknessDesignSpecification",
    "GearFitSystems",
    "GearManufacturingConfigSetupViewModel",
    "GearSetManufacturingConfigurationSetup",
    "GeometrySpecificationType",
    "HardenedMaterialProperties",
    "HardnessProfileCalculationMethod",
    "HeatTreatmentType",
    "ISO6336Geometry",
    "ISO6336GeometryBase",
    "ISO6336GeometryForShapedGears",
    "ISO6336GeometryManufactured",
    "LinearBacklashSpecification",
    "LTCALoadCaseModifiableSettings",
    "LTCASettings",
    "MicroGeometryConvention",
    "MicroGeometryProfileConvention",
    "Micropitting",
    "NamedPlanetAssemblyIndex",
    "NamedPlanetSideBandAmplitudeFactor",
    "ReadonlyToothThicknessSpecification",
    "RelativeMeasurementViewModel",
    "RelativeValuesSpecification",
    "RootStressSurfaceChartOption",
    "Scuffing",
    "ScuffingCoefficientOfFrictionMethods",
    "ScuffingTemperatureMethodsAGMA",
    "ScuffingTemperatureMethodsISO",
    "ShaperEdgeTypes",
    "SpurGearLoadSharingCodes",
    "StandardRack",
    "StandardRackFlank",
    "SurfaceRoughness",
    "ThicknessType",
    "TiffAnalysisSettings",
    "TipAlterationCoefficientMethod",
    "TolerancedMetalMeasurements",
    "TolerancedValueSpecification",
    "ToothFlankFractureAnalysisSettings",
    "ToothThicknessSpecification",
    "ToothThicknessSpecificationBase",
    "TypeOfMechanismHousing",
    "Usage",
)
