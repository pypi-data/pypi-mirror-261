"""MountableComponentCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5015,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "MountableComponentCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4938,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _4994,
        _4998,
        _5001,
        _5004,
        _5005,
        _5006,
        _5013,
        _5018,
        _5019,
        _5022,
        _5026,
        _5029,
        _5032,
        _5037,
        _5040,
        _5043,
        _5048,
        _5052,
        _5056,
        _5059,
        _5062,
        _5065,
        _5066,
        _5068,
        _5072,
        _5075,
        _5076,
        _5077,
        _5078,
        _5079,
        _5082,
        _5086,
        _5089,
        _5094,
        _5095,
        _5098,
        _5101,
        _5102,
        _5104,
        _5105,
        _5106,
        _5109,
        _5110,
        _5111,
        _5112,
        _5113,
        _5116,
        _5069,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="MountableComponentCompoundModalAnalysisAtAStiffness")


class MountableComponentCompoundModalAnalysisAtAStiffness(
    _5015.ComponentCompoundModalAnalysisAtAStiffness
):
    """MountableComponentCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MountableComponentCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_MountableComponentCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting MountableComponentCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
            parent: "MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5015.ComponentCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(_5015.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5069.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5069,
            )

            return self._parent._cast(_5069.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_4994.AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4994,
            )

            return self._parent._cast(
                _4994.AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bearing_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_4998.BearingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4998,
            )

            return self._parent._cast(_4998.BearingCompoundModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5001.BevelDifferentialGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5001,
            )

            return self._parent._cast(
                _5001.BevelDifferentialGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5004.BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5004,
            )

            return self._parent._cast(
                _5004.BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5005.BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5005,
            )

            return self._parent._cast(
                _5005.BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5006.BevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5006,
            )

            return self._parent._cast(_5006.BevelGearCompoundModalAnalysisAtAStiffness)

        @property
        def clutch_half_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5013.ClutchHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5013,
            )

            return self._parent._cast(_5013.ClutchHalfCompoundModalAnalysisAtAStiffness)

        @property
        def concept_coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5018.ConceptCouplingHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5018,
            )

            return self._parent._cast(
                _5018.ConceptCouplingHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5019.ConceptGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5019,
            )

            return self._parent._cast(
                _5019.ConceptGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5022.ConicalGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5022,
            )

            return self._parent._cast(
                _5022.ConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def connector_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5026.ConnectorCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5026,
            )

            return self._parent._cast(_5026.ConnectorCompoundModalAnalysisAtAStiffness)

        @property
        def coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5029.CouplingHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5029,
            )

            return self._parent._cast(
                _5029.CouplingHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def cvt_pulley_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5032.CVTPulleyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5032,
            )

            return self._parent._cast(_5032.CVTPulleyCompoundModalAnalysisAtAStiffness)

        @property
        def cylindrical_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5037.CylindricalGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5037,
            )

            return self._parent._cast(
                _5037.CylindricalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5040.CylindricalPlanetGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5040,
            )

            return self._parent._cast(
                _5040.CylindricalPlanetGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def face_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5043.FaceGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5043,
            )

            return self._parent._cast(_5043.FaceGearCompoundModalAnalysisAtAStiffness)

        @property
        def gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5048.GearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5048,
            )

            return self._parent._cast(_5048.GearCompoundModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5052.HypoidGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5052,
            )

            return self._parent._cast(_5052.HypoidGearCompoundModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> (
            "_5056.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5056,
            )

            return self._parent._cast(
                _5056.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> (
            "_5059.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5059,
            )

            return self._parent._cast(
                _5059.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5062.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5062,
            )

            return self._parent._cast(
                _5062.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def mass_disc_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5065.MassDiscCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5065,
            )

            return self._parent._cast(_5065.MassDiscCompoundModalAnalysisAtAStiffness)

        @property
        def measurement_component_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5066.MeasurementComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5066,
            )

            return self._parent._cast(
                _5066.MeasurementComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def oil_seal_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5068.OilSealCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5068,
            )

            return self._parent._cast(_5068.OilSealCompoundModalAnalysisAtAStiffness)

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5072.PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5072,
            )

            return self._parent._cast(
                _5072.PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def planet_carrier_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5075.PlanetCarrierCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5075,
            )

            return self._parent._cast(
                _5075.PlanetCarrierCompoundModalAnalysisAtAStiffness
            )

        @property
        def point_load_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5076.PointLoadCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5076,
            )

            return self._parent._cast(_5076.PointLoadCompoundModalAnalysisAtAStiffness)

        @property
        def power_load_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5077.PowerLoadCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5077,
            )

            return self._parent._cast(_5077.PowerLoadCompoundModalAnalysisAtAStiffness)

        @property
        def pulley_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5078.PulleyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5078,
            )

            return self._parent._cast(_5078.PulleyCompoundModalAnalysisAtAStiffness)

        @property
        def ring_pins_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5079.RingPinsCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5079,
            )

            return self._parent._cast(_5079.RingPinsCompoundModalAnalysisAtAStiffness)

        @property
        def rolling_ring_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5082.RollingRingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5082,
            )

            return self._parent._cast(
                _5082.RollingRingCompoundModalAnalysisAtAStiffness
            )

        @property
        def shaft_hub_connection_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5086.ShaftHubConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5086,
            )

            return self._parent._cast(
                _5086.ShaftHubConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5089.SpiralBevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5089,
            )

            return self._parent._cast(
                _5089.SpiralBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_half_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5094.SpringDamperHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5094,
            )

            return self._parent._cast(
                _5094.SpringDamperHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5095.StraightBevelDiffGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5095,
            )

            return self._parent._cast(
                _5095.StraightBevelDiffGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5098.StraightBevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5098,
            )

            return self._parent._cast(
                _5098.StraightBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5101.StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5101,
            )

            return self._parent._cast(
                _5101.StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5102.StraightBevelSunGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5102,
            )

            return self._parent._cast(
                _5102.StraightBevelSunGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_half_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5104.SynchroniserHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5104,
            )

            return self._parent._cast(
                _5104.SynchroniserHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_part_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5105.SynchroniserPartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5105,
            )

            return self._parent._cast(
                _5105.SynchroniserPartCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_sleeve_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5106.SynchroniserSleeveCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5106,
            )

            return self._parent._cast(
                _5106.SynchroniserSleeveCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_pump_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5109.TorqueConverterPumpCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5109,
            )

            return self._parent._cast(
                _5109.TorqueConverterPumpCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_turbine_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5110.TorqueConverterTurbineCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5110,
            )

            return self._parent._cast(
                _5110.TorqueConverterTurbineCompoundModalAnalysisAtAStiffness
            )

        @property
        def unbalanced_mass_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5111.UnbalancedMassCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5111,
            )

            return self._parent._cast(
                _5111.UnbalancedMassCompoundModalAnalysisAtAStiffness
            )

        @property
        def virtual_component_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5112.VirtualComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5112,
            )

            return self._parent._cast(
                _5112.VirtualComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def worm_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5113.WormGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5113,
            )

            return self._parent._cast(_5113.WormGearCompoundModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5116.ZerolBevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5116,
            )

            return self._parent._cast(
                _5116.ZerolBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "MountableComponentCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self,
        instance_to_wrap: "MountableComponentCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4938.MountableComponentModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.MountableComponentModalAnalysisAtAStiffness]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4938.MountableComponentModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.MountableComponentModalAnalysisAtAStiffness]

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
    ) -> "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness":
        return self._Cast_MountableComponentCompoundModalAnalysisAtAStiffness(self)
