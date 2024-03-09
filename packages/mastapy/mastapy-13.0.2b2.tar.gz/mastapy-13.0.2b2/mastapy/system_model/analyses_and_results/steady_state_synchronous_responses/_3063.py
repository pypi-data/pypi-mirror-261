"""MountableComponentSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3010,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "MountableComponentSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2466
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _2991,
        _2993,
        _2998,
        _2999,
        _3000,
        _3003,
        _3007,
        _3012,
        _3016,
        _3019,
        _3021,
        _3023,
        _3026,
        _3034,
        _3035,
        _3041,
        _3046,
        _3050,
        _3054,
        _3057,
        _3060,
        _3061,
        _3062,
        _3064,
        _3067,
        _3071,
        _3072,
        _3073,
        _3074,
        _3075,
        _3079,
        _3081,
        _3087,
        _3089,
        _3096,
        _3099,
        _3100,
        _3101,
        _3102,
        _3103,
        _3104,
        _3107,
        _3109,
        _3110,
        _3111,
        _3114,
        _3117,
        _3065,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="MountableComponentSteadyStateSynchronousResponse")


class MountableComponentSteadyStateSynchronousResponse(
    _3010.ComponentSteadyStateSynchronousResponse
):
    """MountableComponentSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MountableComponentSteadyStateSynchronousResponse"
    )

    class _Cast_MountableComponentSteadyStateSynchronousResponse:
        """Special nested class for casting MountableComponentSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
            parent: "MountableComponentSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def component_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3010.ComponentSteadyStateSynchronousResponse":
            return self._parent._cast(_3010.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3065.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3065,
            )

            return self._parent._cast(_3065.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_2991.AGMAGleasonConicalGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2991,
            )

            return self._parent._cast(
                _2991.AGMAGleasonConicalGearSteadyStateSynchronousResponse
            )

        @property
        def bearing_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_2993.BearingSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2993,
            )

            return self._parent._cast(_2993.BearingSteadyStateSynchronousResponse)

        @property
        def bevel_differential_gear_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_2998.BevelDifferentialGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2998,
            )

            return self._parent._cast(
                _2998.BevelDifferentialGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_2999.BevelDifferentialPlanetGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2999,
            )

            return self._parent._cast(
                _2999.BevelDifferentialPlanetGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3000.BevelDifferentialSunGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3000,
            )

            return self._parent._cast(
                _3000.BevelDifferentialSunGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3003.BevelGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3003,
            )

            return self._parent._cast(_3003.BevelGearSteadyStateSynchronousResponse)

        @property
        def clutch_half_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3007.ClutchHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3007,
            )

            return self._parent._cast(_3007.ClutchHalfSteadyStateSynchronousResponse)

        @property
        def concept_coupling_half_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3012.ConceptCouplingHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3012,
            )

            return self._parent._cast(
                _3012.ConceptCouplingHalfSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3016.ConceptGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3016,
            )

            return self._parent._cast(_3016.ConceptGearSteadyStateSynchronousResponse)

        @property
        def conical_gear_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3019.ConicalGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3019,
            )

            return self._parent._cast(_3019.ConicalGearSteadyStateSynchronousResponse)

        @property
        def connector_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3021.ConnectorSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3021,
            )

            return self._parent._cast(_3021.ConnectorSteadyStateSynchronousResponse)

        @property
        def coupling_half_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3023.CouplingHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3023,
            )

            return self._parent._cast(_3023.CouplingHalfSteadyStateSynchronousResponse)

        @property
        def cvt_pulley_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3026.CVTPulleySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3026,
            )

            return self._parent._cast(_3026.CVTPulleySteadyStateSynchronousResponse)

        @property
        def cylindrical_gear_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3034.CylindricalGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3034,
            )

            return self._parent._cast(
                _3034.CylindricalGearSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3035.CylindricalPlanetGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3035,
            )

            return self._parent._cast(
                _3035.CylindricalPlanetGearSteadyStateSynchronousResponse
            )

        @property
        def face_gear_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3041.FaceGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3041,
            )

            return self._parent._cast(_3041.FaceGearSteadyStateSynchronousResponse)

        @property
        def gear_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3046.GearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3046,
            )

            return self._parent._cast(_3046.GearSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3050.HypoidGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3050,
            )

            return self._parent._cast(_3050.HypoidGearSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3054.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3054,
            )

            return self._parent._cast(
                _3054.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3057.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3057,
            )

            return self._parent._cast(
                _3057.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3060.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3060,
            )

            return self._parent._cast(
                _3060.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse
            )

        @property
        def mass_disc_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3061.MassDiscSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3061,
            )

            return self._parent._cast(_3061.MassDiscSteadyStateSynchronousResponse)

        @property
        def measurement_component_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3062.MeasurementComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3062,
            )

            return self._parent._cast(
                _3062.MeasurementComponentSteadyStateSynchronousResponse
            )

        @property
        def oil_seal_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3064.OilSealSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3064,
            )

            return self._parent._cast(_3064.OilSealSteadyStateSynchronousResponse)

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3067.PartToPartShearCouplingHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3067,
            )

            return self._parent._cast(
                _3067.PartToPartShearCouplingHalfSteadyStateSynchronousResponse
            )

        @property
        def planet_carrier_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3071.PlanetCarrierSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3071,
            )

            return self._parent._cast(_3071.PlanetCarrierSteadyStateSynchronousResponse)

        @property
        def point_load_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3072.PointLoadSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3072,
            )

            return self._parent._cast(_3072.PointLoadSteadyStateSynchronousResponse)

        @property
        def power_load_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3073.PowerLoadSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3073,
            )

            return self._parent._cast(_3073.PowerLoadSteadyStateSynchronousResponse)

        @property
        def pulley_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3074.PulleySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3074,
            )

            return self._parent._cast(_3074.PulleySteadyStateSynchronousResponse)

        @property
        def ring_pins_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3075.RingPinsSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3075,
            )

            return self._parent._cast(_3075.RingPinsSteadyStateSynchronousResponse)

        @property
        def rolling_ring_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3079.RollingRingSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3079,
            )

            return self._parent._cast(_3079.RollingRingSteadyStateSynchronousResponse)

        @property
        def shaft_hub_connection_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3081.ShaftHubConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3081,
            )

            return self._parent._cast(
                _3081.ShaftHubConnectionSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3087.SpiralBevelGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3087,
            )

            return self._parent._cast(
                _3087.SpiralBevelGearSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_half_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3089.SpringDamperHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3089,
            )

            return self._parent._cast(
                _3089.SpringDamperHalfSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3096.StraightBevelDiffGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3096,
            )

            return self._parent._cast(
                _3096.StraightBevelDiffGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3099.StraightBevelGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3099,
            )

            return self._parent._cast(
                _3099.StraightBevelGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3100.StraightBevelPlanetGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3100,
            )

            return self._parent._cast(
                _3100.StraightBevelPlanetGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3101.StraightBevelSunGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3101,
            )

            return self._parent._cast(
                _3101.StraightBevelSunGearSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_half_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3102.SynchroniserHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3102,
            )

            return self._parent._cast(
                _3102.SynchroniserHalfSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_part_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3103.SynchroniserPartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3103,
            )

            return self._parent._cast(
                _3103.SynchroniserPartSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_sleeve_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3104.SynchroniserSleeveSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3104,
            )

            return self._parent._cast(
                _3104.SynchroniserSleeveSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_pump_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3107.TorqueConverterPumpSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3107,
            )

            return self._parent._cast(
                _3107.TorqueConverterPumpSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_turbine_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3109.TorqueConverterTurbineSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3109,
            )

            return self._parent._cast(
                _3109.TorqueConverterTurbineSteadyStateSynchronousResponse
            )

        @property
        def unbalanced_mass_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3110.UnbalancedMassSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3110,
            )

            return self._parent._cast(
                _3110.UnbalancedMassSteadyStateSynchronousResponse
            )

        @property
        def virtual_component_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3111.VirtualComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3111,
            )

            return self._parent._cast(
                _3111.VirtualComponentSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3114.WormGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3114,
            )

            return self._parent._cast(_3114.WormGearSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "_3117.ZerolBevelGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3117,
            )

            return self._parent._cast(
                _3117.ZerolBevelGearSteadyStateSynchronousResponse
            )

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
        ) -> "MountableComponentSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse",
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
        instance_to_wrap: "MountableComponentSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2466.MountableComponent":
        """mastapy.system_model.part_model.MountableComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "MountableComponentSteadyStateSynchronousResponse._Cast_MountableComponentSteadyStateSynchronousResponse":
        return self._Cast_MountableComponentSteadyStateSynchronousResponse(self)
