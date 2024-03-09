"""PartCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7548
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "PartCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6360
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6410,
        _6411,
        _6412,
        _6414,
        _6416,
        _6417,
        _6418,
        _6420,
        _6421,
        _6423,
        _6424,
        _6425,
        _6426,
        _6428,
        _6429,
        _6430,
        _6431,
        _6433,
        _6435,
        _6436,
        _6438,
        _6439,
        _6441,
        _6442,
        _6444,
        _6446,
        _6447,
        _6449,
        _6451,
        _6452,
        _6453,
        _6455,
        _6457,
        _6459,
        _6460,
        _6461,
        _6462,
        _6463,
        _6465,
        _6466,
        _6467,
        _6468,
        _6470,
        _6471,
        _6472,
        _6474,
        _6476,
        _6478,
        _6479,
        _6481,
        _6482,
        _6484,
        _6485,
        _6486,
        _6487,
        _6488,
        _6490,
        _6492,
        _6494,
        _6495,
        _6496,
        _6497,
        _6498,
        _6499,
        _6501,
        _6502,
        _6504,
        _6505,
        _6506,
        _6508,
        _6509,
        _6511,
        _6512,
        _6514,
        _6515,
        _6517,
        _6518,
        _6520,
        _6521,
        _6522,
        _6523,
        _6524,
        _6525,
        _6526,
        _6527,
        _6529,
        _6530,
        _6531,
        _6532,
        _6533,
        _6535,
        _6536,
        _6538,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("PartCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="PartCompoundDynamicAnalysis")


class PartCompoundDynamicAnalysis(_7548.PartCompoundAnalysis):
    """PartCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartCompoundDynamicAnalysis")

    class _Cast_PartCompoundDynamicAnalysis:
        """Special nested class for casting PartCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
            parent: "PartCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def part_compound_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_7548.PartCompoundAnalysis":
            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def abstract_assembly_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6410.AbstractAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6410,
            )

            return self._parent._cast(_6410.AbstractAssemblyCompoundDynamicAnalysis)

        @property
        def abstract_shaft_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6411.AbstractShaftCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6411,
            )

            return self._parent._cast(_6411.AbstractShaftCompoundDynamicAnalysis)

        @property
        def abstract_shaft_or_housing_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6412.AbstractShaftOrHousingCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6412,
            )

            return self._parent._cast(
                _6412.AbstractShaftOrHousingCompoundDynamicAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6414.AGMAGleasonConicalGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6414,
            )

            return self._parent._cast(
                _6414.AGMAGleasonConicalGearCompoundDynamicAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6416.AGMAGleasonConicalGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6416,
            )

            return self._parent._cast(
                _6416.AGMAGleasonConicalGearSetCompoundDynamicAnalysis
            )

        @property
        def assembly_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6417.AssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6417,
            )

            return self._parent._cast(_6417.AssemblyCompoundDynamicAnalysis)

        @property
        def bearing_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6418.BearingCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6418,
            )

            return self._parent._cast(_6418.BearingCompoundDynamicAnalysis)

        @property
        def belt_drive_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6420.BeltDriveCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6420,
            )

            return self._parent._cast(_6420.BeltDriveCompoundDynamicAnalysis)

        @property
        def bevel_differential_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6421.BevelDifferentialGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6421,
            )

            return self._parent._cast(
                _6421.BevelDifferentialGearCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6423.BevelDifferentialGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6423,
            )

            return self._parent._cast(
                _6423.BevelDifferentialGearSetCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6424.BevelDifferentialPlanetGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6424,
            )

            return self._parent._cast(
                _6424.BevelDifferentialPlanetGearCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6425.BevelDifferentialSunGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6425,
            )

            return self._parent._cast(
                _6425.BevelDifferentialSunGearCompoundDynamicAnalysis
            )

        @property
        def bevel_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6426.BevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6426,
            )

            return self._parent._cast(_6426.BevelGearCompoundDynamicAnalysis)

        @property
        def bevel_gear_set_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6428.BevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6428,
            )

            return self._parent._cast(_6428.BevelGearSetCompoundDynamicAnalysis)

        @property
        def bolt_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6429.BoltCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6429,
            )

            return self._parent._cast(_6429.BoltCompoundDynamicAnalysis)

        @property
        def bolted_joint_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6430.BoltedJointCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6430,
            )

            return self._parent._cast(_6430.BoltedJointCompoundDynamicAnalysis)

        @property
        def clutch_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6431.ClutchCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6431,
            )

            return self._parent._cast(_6431.ClutchCompoundDynamicAnalysis)

        @property
        def clutch_half_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6433.ClutchHalfCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6433,
            )

            return self._parent._cast(_6433.ClutchHalfCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6435.ComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6435,
            )

            return self._parent._cast(_6435.ComponentCompoundDynamicAnalysis)

        @property
        def concept_coupling_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6436.ConceptCouplingCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6436,
            )

            return self._parent._cast(_6436.ConceptCouplingCompoundDynamicAnalysis)

        @property
        def concept_coupling_half_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6438.ConceptCouplingHalfCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6438,
            )

            return self._parent._cast(_6438.ConceptCouplingHalfCompoundDynamicAnalysis)

        @property
        def concept_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6439.ConceptGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6439,
            )

            return self._parent._cast(_6439.ConceptGearCompoundDynamicAnalysis)

        @property
        def concept_gear_set_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6441.ConceptGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6441,
            )

            return self._parent._cast(_6441.ConceptGearSetCompoundDynamicAnalysis)

        @property
        def conical_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6442.ConicalGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6442,
            )

            return self._parent._cast(_6442.ConicalGearCompoundDynamicAnalysis)

        @property
        def conical_gear_set_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6444.ConicalGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6444,
            )

            return self._parent._cast(_6444.ConicalGearSetCompoundDynamicAnalysis)

        @property
        def connector_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6446.ConnectorCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6446,
            )

            return self._parent._cast(_6446.ConnectorCompoundDynamicAnalysis)

        @property
        def coupling_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6447.CouplingCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6447,
            )

            return self._parent._cast(_6447.CouplingCompoundDynamicAnalysis)

        @property
        def coupling_half_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6449.CouplingHalfCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6449,
            )

            return self._parent._cast(_6449.CouplingHalfCompoundDynamicAnalysis)

        @property
        def cvt_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6451.CVTCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6451,
            )

            return self._parent._cast(_6451.CVTCompoundDynamicAnalysis)

        @property
        def cvt_pulley_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6452.CVTPulleyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6452,
            )

            return self._parent._cast(_6452.CVTPulleyCompoundDynamicAnalysis)

        @property
        def cycloidal_assembly_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6453.CycloidalAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6453,
            )

            return self._parent._cast(_6453.CycloidalAssemblyCompoundDynamicAnalysis)

        @property
        def cycloidal_disc_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6455.CycloidalDiscCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6455,
            )

            return self._parent._cast(_6455.CycloidalDiscCompoundDynamicAnalysis)

        @property
        def cylindrical_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6457.CylindricalGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6457,
            )

            return self._parent._cast(_6457.CylindricalGearCompoundDynamicAnalysis)

        @property
        def cylindrical_gear_set_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6459.CylindricalGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6459,
            )

            return self._parent._cast(_6459.CylindricalGearSetCompoundDynamicAnalysis)

        @property
        def cylindrical_planet_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6460.CylindricalPlanetGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6460,
            )

            return self._parent._cast(
                _6460.CylindricalPlanetGearCompoundDynamicAnalysis
            )

        @property
        def datum_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6461.DatumCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6461,
            )

            return self._parent._cast(_6461.DatumCompoundDynamicAnalysis)

        @property
        def external_cad_model_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6462.ExternalCADModelCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6462,
            )

            return self._parent._cast(_6462.ExternalCADModelCompoundDynamicAnalysis)

        @property
        def face_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6463.FaceGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6463,
            )

            return self._parent._cast(_6463.FaceGearCompoundDynamicAnalysis)

        @property
        def face_gear_set_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6465.FaceGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6465,
            )

            return self._parent._cast(_6465.FaceGearSetCompoundDynamicAnalysis)

        @property
        def fe_part_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6466.FEPartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6466,
            )

            return self._parent._cast(_6466.FEPartCompoundDynamicAnalysis)

        @property
        def flexible_pin_assembly_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6467.FlexiblePinAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6467,
            )

            return self._parent._cast(_6467.FlexiblePinAssemblyCompoundDynamicAnalysis)

        @property
        def gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6468.GearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6468,
            )

            return self._parent._cast(_6468.GearCompoundDynamicAnalysis)

        @property
        def gear_set_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6470.GearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6470,
            )

            return self._parent._cast(_6470.GearSetCompoundDynamicAnalysis)

        @property
        def guide_dxf_model_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6471.GuideDxfModelCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6471,
            )

            return self._parent._cast(_6471.GuideDxfModelCompoundDynamicAnalysis)

        @property
        def hypoid_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6472.HypoidGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6472,
            )

            return self._parent._cast(_6472.HypoidGearCompoundDynamicAnalysis)

        @property
        def hypoid_gear_set_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6474.HypoidGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6474,
            )

            return self._parent._cast(_6474.HypoidGearSetCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6476.KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6476,
            )

            return self._parent._cast(
                _6476.KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6478.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6478,
            )

            return self._parent._cast(
                _6478.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6479.KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6479,
            )

            return self._parent._cast(
                _6479.KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6481.KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6481,
            )

            return self._parent._cast(
                _6481.KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6482.KlingelnbergCycloPalloidSpiralBevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6482,
            )

            return self._parent._cast(
                _6482.KlingelnbergCycloPalloidSpiralBevelGearCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6484.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6484,
            )

            return self._parent._cast(
                _6484.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis
            )

        @property
        def mass_disc_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6485.MassDiscCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6485,
            )

            return self._parent._cast(_6485.MassDiscCompoundDynamicAnalysis)

        @property
        def measurement_component_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6486.MeasurementComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6486,
            )

            return self._parent._cast(_6486.MeasurementComponentCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6487.MountableComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6487,
            )

            return self._parent._cast(_6487.MountableComponentCompoundDynamicAnalysis)

        @property
        def oil_seal_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6488.OilSealCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6488,
            )

            return self._parent._cast(_6488.OilSealCompoundDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6490.PartToPartShearCouplingCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6490,
            )

            return self._parent._cast(
                _6490.PartToPartShearCouplingCompoundDynamicAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6492.PartToPartShearCouplingHalfCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6492,
            )

            return self._parent._cast(
                _6492.PartToPartShearCouplingHalfCompoundDynamicAnalysis
            )

        @property
        def planetary_gear_set_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6494.PlanetaryGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6494,
            )

            return self._parent._cast(_6494.PlanetaryGearSetCompoundDynamicAnalysis)

        @property
        def planet_carrier_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6495.PlanetCarrierCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6495,
            )

            return self._parent._cast(_6495.PlanetCarrierCompoundDynamicAnalysis)

        @property
        def point_load_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6496.PointLoadCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6496,
            )

            return self._parent._cast(_6496.PointLoadCompoundDynamicAnalysis)

        @property
        def power_load_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6497.PowerLoadCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6497,
            )

            return self._parent._cast(_6497.PowerLoadCompoundDynamicAnalysis)

        @property
        def pulley_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6498.PulleyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6498,
            )

            return self._parent._cast(_6498.PulleyCompoundDynamicAnalysis)

        @property
        def ring_pins_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6499.RingPinsCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6499,
            )

            return self._parent._cast(_6499.RingPinsCompoundDynamicAnalysis)

        @property
        def rolling_ring_assembly_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6501.RollingRingAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6501,
            )

            return self._parent._cast(_6501.RollingRingAssemblyCompoundDynamicAnalysis)

        @property
        def rolling_ring_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6502.RollingRingCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6502,
            )

            return self._parent._cast(_6502.RollingRingCompoundDynamicAnalysis)

        @property
        def root_assembly_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6504.RootAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6504,
            )

            return self._parent._cast(_6504.RootAssemblyCompoundDynamicAnalysis)

        @property
        def shaft_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6505.ShaftCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6505,
            )

            return self._parent._cast(_6505.ShaftCompoundDynamicAnalysis)

        @property
        def shaft_hub_connection_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6506.ShaftHubConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6506,
            )

            return self._parent._cast(_6506.ShaftHubConnectionCompoundDynamicAnalysis)

        @property
        def specialised_assembly_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6508.SpecialisedAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6508,
            )

            return self._parent._cast(_6508.SpecialisedAssemblyCompoundDynamicAnalysis)

        @property
        def spiral_bevel_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6509.SpiralBevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6509,
            )

            return self._parent._cast(_6509.SpiralBevelGearCompoundDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6511.SpiralBevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6511,
            )

            return self._parent._cast(_6511.SpiralBevelGearSetCompoundDynamicAnalysis)

        @property
        def spring_damper_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6512.SpringDamperCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6512,
            )

            return self._parent._cast(_6512.SpringDamperCompoundDynamicAnalysis)

        @property
        def spring_damper_half_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6514.SpringDamperHalfCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6514,
            )

            return self._parent._cast(_6514.SpringDamperHalfCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6515.StraightBevelDiffGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6515,
            )

            return self._parent._cast(
                _6515.StraightBevelDiffGearCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6517.StraightBevelDiffGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6517,
            )

            return self._parent._cast(
                _6517.StraightBevelDiffGearSetCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6518.StraightBevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6518,
            )

            return self._parent._cast(_6518.StraightBevelGearCompoundDynamicAnalysis)

        @property
        def straight_bevel_gear_set_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6520.StraightBevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6520,
            )

            return self._parent._cast(_6520.StraightBevelGearSetCompoundDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6521.StraightBevelPlanetGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6521,
            )

            return self._parent._cast(
                _6521.StraightBevelPlanetGearCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6522.StraightBevelSunGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6522,
            )

            return self._parent._cast(_6522.StraightBevelSunGearCompoundDynamicAnalysis)

        @property
        def synchroniser_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6523.SynchroniserCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6523,
            )

            return self._parent._cast(_6523.SynchroniserCompoundDynamicAnalysis)

        @property
        def synchroniser_half_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6524.SynchroniserHalfCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6524,
            )

            return self._parent._cast(_6524.SynchroniserHalfCompoundDynamicAnalysis)

        @property
        def synchroniser_part_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6525.SynchroniserPartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6525,
            )

            return self._parent._cast(_6525.SynchroniserPartCompoundDynamicAnalysis)

        @property
        def synchroniser_sleeve_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6526.SynchroniserSleeveCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6526,
            )

            return self._parent._cast(_6526.SynchroniserSleeveCompoundDynamicAnalysis)

        @property
        def torque_converter_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6527.TorqueConverterCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6527,
            )

            return self._parent._cast(_6527.TorqueConverterCompoundDynamicAnalysis)

        @property
        def torque_converter_pump_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6529.TorqueConverterPumpCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6529,
            )

            return self._parent._cast(_6529.TorqueConverterPumpCompoundDynamicAnalysis)

        @property
        def torque_converter_turbine_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6530.TorqueConverterTurbineCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6530,
            )

            return self._parent._cast(
                _6530.TorqueConverterTurbineCompoundDynamicAnalysis
            )

        @property
        def unbalanced_mass_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6531.UnbalancedMassCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6531,
            )

            return self._parent._cast(_6531.UnbalancedMassCompoundDynamicAnalysis)

        @property
        def virtual_component_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6532.VirtualComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6532,
            )

            return self._parent._cast(_6532.VirtualComponentCompoundDynamicAnalysis)

        @property
        def worm_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6533.WormGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6533,
            )

            return self._parent._cast(_6533.WormGearCompoundDynamicAnalysis)

        @property
        def worm_gear_set_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6535.WormGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6535,
            )

            return self._parent._cast(_6535.WormGearSetCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6536.ZerolBevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6536,
            )

            return self._parent._cast(_6536.ZerolBevelGearCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "_6538.ZerolBevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6538,
            )

            return self._parent._cast(_6538.ZerolBevelGearSetCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "PartCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartCompoundDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_6360.PartDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.PartDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(self: Self) -> "List[_6360.PartDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.PartDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis":
        return self._Cast_PartCompoundDynamicAnalysis(self)
