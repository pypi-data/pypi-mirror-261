"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1094 import CylindricalGearBiasModification
    from ._1095 import CylindricalGearCommonFlankMicroGeometry
    from ._1096 import CylindricalGearFlankMicroGeometry
    from ._1097 import CylindricalGearLeadModification
    from ._1098 import CylindricalGearLeadModificationAtProfilePosition
    from ._1099 import CylindricalGearMeshMicroGeometry
    from ._1100 import CylindricalGearMeshMicroGeometryDutyCycle
    from ._1101 import CylindricalGearMicroGeometry
    from ._1102 import CylindricalGearMicroGeometryBase
    from ._1103 import CylindricalGearMicroGeometryDutyCycle
    from ._1104 import CylindricalGearMicroGeometryMap
    from ._1105 import CylindricalGearMicroGeometryPerTooth
    from ._1106 import CylindricalGearProfileModification
    from ._1107 import CylindricalGearProfileModificationAtFaceWidthPosition
    from ._1108 import CylindricalGearSetMicroGeometry
    from ._1109 import CylindricalGearSetMicroGeometryDutyCycle
    from ._1110 import CylindricalGearToothMicroGeometry
    from ._1111 import CylindricalGearTriangularEndModification
    from ._1112 import CylindricalGearTriangularEndModificationAtOrientation
    from ._1113 import DrawDefiningGearOrBoth
    from ._1114 import GearAlignment
    from ._1115 import LeadFormReliefWithDeviation
    from ._1116 import LeadReliefWithDeviation
    from ._1117 import LeadSlopeReliefWithDeviation
    from ._1118 import LinearCylindricalGearTriangularEndModification
    from ._1119 import MeasuredMapDataTypes
    from ._1120 import MeshAlignment
    from ._1121 import MeshedCylindricalGearFlankMicroGeometry
    from ._1122 import MeshedCylindricalGearMicroGeometry
    from ._1123 import MicroGeometryLeadToleranceChartView
    from ._1124 import MicroGeometryViewingOptions
    from ._1125 import ParabolicCylindricalGearTriangularEndModification
    from ._1126 import ProfileFormReliefWithDeviation
    from ._1127 import ProfileReliefWithDeviation
    from ._1128 import ProfileSlopeReliefWithDeviation
    from ._1129 import ReliefWithDeviation
    from ._1130 import SingleCylindricalGearTriangularEndModification
    from ._1131 import TotalLeadReliefWithDeviation
    from ._1132 import TotalProfileReliefWithDeviation
else:
    import_structure = {
        "_1094": ["CylindricalGearBiasModification"],
        "_1095": ["CylindricalGearCommonFlankMicroGeometry"],
        "_1096": ["CylindricalGearFlankMicroGeometry"],
        "_1097": ["CylindricalGearLeadModification"],
        "_1098": ["CylindricalGearLeadModificationAtProfilePosition"],
        "_1099": ["CylindricalGearMeshMicroGeometry"],
        "_1100": ["CylindricalGearMeshMicroGeometryDutyCycle"],
        "_1101": ["CylindricalGearMicroGeometry"],
        "_1102": ["CylindricalGearMicroGeometryBase"],
        "_1103": ["CylindricalGearMicroGeometryDutyCycle"],
        "_1104": ["CylindricalGearMicroGeometryMap"],
        "_1105": ["CylindricalGearMicroGeometryPerTooth"],
        "_1106": ["CylindricalGearProfileModification"],
        "_1107": ["CylindricalGearProfileModificationAtFaceWidthPosition"],
        "_1108": ["CylindricalGearSetMicroGeometry"],
        "_1109": ["CylindricalGearSetMicroGeometryDutyCycle"],
        "_1110": ["CylindricalGearToothMicroGeometry"],
        "_1111": ["CylindricalGearTriangularEndModification"],
        "_1112": ["CylindricalGearTriangularEndModificationAtOrientation"],
        "_1113": ["DrawDefiningGearOrBoth"],
        "_1114": ["GearAlignment"],
        "_1115": ["LeadFormReliefWithDeviation"],
        "_1116": ["LeadReliefWithDeviation"],
        "_1117": ["LeadSlopeReliefWithDeviation"],
        "_1118": ["LinearCylindricalGearTriangularEndModification"],
        "_1119": ["MeasuredMapDataTypes"],
        "_1120": ["MeshAlignment"],
        "_1121": ["MeshedCylindricalGearFlankMicroGeometry"],
        "_1122": ["MeshedCylindricalGearMicroGeometry"],
        "_1123": ["MicroGeometryLeadToleranceChartView"],
        "_1124": ["MicroGeometryViewingOptions"],
        "_1125": ["ParabolicCylindricalGearTriangularEndModification"],
        "_1126": ["ProfileFormReliefWithDeviation"],
        "_1127": ["ProfileReliefWithDeviation"],
        "_1128": ["ProfileSlopeReliefWithDeviation"],
        "_1129": ["ReliefWithDeviation"],
        "_1130": ["SingleCylindricalGearTriangularEndModification"],
        "_1131": ["TotalLeadReliefWithDeviation"],
        "_1132": ["TotalProfileReliefWithDeviation"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearBiasModification",
    "CylindricalGearCommonFlankMicroGeometry",
    "CylindricalGearFlankMicroGeometry",
    "CylindricalGearLeadModification",
    "CylindricalGearLeadModificationAtProfilePosition",
    "CylindricalGearMeshMicroGeometry",
    "CylindricalGearMeshMicroGeometryDutyCycle",
    "CylindricalGearMicroGeometry",
    "CylindricalGearMicroGeometryBase",
    "CylindricalGearMicroGeometryDutyCycle",
    "CylindricalGearMicroGeometryMap",
    "CylindricalGearMicroGeometryPerTooth",
    "CylindricalGearProfileModification",
    "CylindricalGearProfileModificationAtFaceWidthPosition",
    "CylindricalGearSetMicroGeometry",
    "CylindricalGearSetMicroGeometryDutyCycle",
    "CylindricalGearToothMicroGeometry",
    "CylindricalGearTriangularEndModification",
    "CylindricalGearTriangularEndModificationAtOrientation",
    "DrawDefiningGearOrBoth",
    "GearAlignment",
    "LeadFormReliefWithDeviation",
    "LeadReliefWithDeviation",
    "LeadSlopeReliefWithDeviation",
    "LinearCylindricalGearTriangularEndModification",
    "MeasuredMapDataTypes",
    "MeshAlignment",
    "MeshedCylindricalGearFlankMicroGeometry",
    "MeshedCylindricalGearMicroGeometry",
    "MicroGeometryLeadToleranceChartView",
    "MicroGeometryViewingOptions",
    "ParabolicCylindricalGearTriangularEndModification",
    "ProfileFormReliefWithDeviation",
    "ProfileReliefWithDeviation",
    "ProfileSlopeReliefWithDeviation",
    "ReliefWithDeviation",
    "SingleCylindricalGearTriangularEndModification",
    "TotalLeadReliefWithDeviation",
    "TotalProfileReliefWithDeviation",
)
