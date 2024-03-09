"""ComponentSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3585,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "ComponentSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2446
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3507,
        _3508,
        _3512,
        _3514,
        _3519,
        _3520,
        _3521,
        _3524,
        _3526,
        _3528,
        _3533,
        _3537,
        _3540,
        _3542,
        _3544,
        _3547,
        _3552,
        _3555,
        _3556,
        _3557,
        _3558,
        _3561,
        _3562,
        _3566,
        _3567,
        _3570,
        _3574,
        _3577,
        _3580,
        _3581,
        _3582,
        _3583,
        _3584,
        _3587,
        _3591,
        _3592,
        _3593,
        _3594,
        _3595,
        _3599,
        _3601,
        _3602,
        _3607,
        _3609,
        _3614,
        _3617,
        _3618,
        _3619,
        _3620,
        _3621,
        _3622,
        _3625,
        _3627,
        _3628,
        _3629,
        _3632,
        _3635,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("ComponentSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="ComponentSteadyStateSynchronousResponseAtASpeed")


class ComponentSteadyStateSynchronousResponseAtASpeed(
    _3585.PartSteadyStateSynchronousResponseAtASpeed
):
    """ComponentSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ComponentSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_ComponentSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting ComponentSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
            parent: "ComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3585.PartSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(_3585.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3507.AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3507,
            )

            return self._parent._cast(
                _3507.AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3508.AbstractShaftSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3508,
            )

            return self._parent._cast(
                _3508.AbstractShaftSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3512.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3512,
            )

            return self._parent._cast(
                _3512.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bearing_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3514.BearingSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3514,
            )

            return self._parent._cast(
                _3514.BearingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3519.BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3519,
            )

            return self._parent._cast(
                _3519.BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3520.BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3520,
            )

            return self._parent._cast(
                _3520.BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3521.BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3521,
            )

            return self._parent._cast(
                _3521.BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3524.BevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3524,
            )

            return self._parent._cast(
                _3524.BevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bolt_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3526.BoltSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3526,
            )

            return self._parent._cast(_3526.BoltSteadyStateSynchronousResponseAtASpeed)

        @property
        def clutch_half_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3528.ClutchHalfSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3528,
            )

            return self._parent._cast(
                _3528.ClutchHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3533.ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3533,
            )

            return self._parent._cast(
                _3533.ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3537.ConceptGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3537,
            )

            return self._parent._cast(
                _3537.ConceptGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3540.ConicalGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3540,
            )

            return self._parent._cast(
                _3540.ConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connector_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3542.ConnectorSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3542,
            )

            return self._parent._cast(
                _3542.ConnectorSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3544.CouplingHalfSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3544,
            )

            return self._parent._cast(
                _3544.CouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_pulley_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3547.CVTPulleySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3547,
            )

            return self._parent._cast(
                _3547.CVTPulleySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_disc_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3552.CycloidalDiscSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3552,
            )

            return self._parent._cast(
                _3552.CycloidalDiscSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3555.CylindricalGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3555,
            )

            return self._parent._cast(
                _3555.CylindricalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3556.CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3556,
            )

            return self._parent._cast(
                _3556.CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def datum_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3557.DatumSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3557,
            )

            return self._parent._cast(_3557.DatumSteadyStateSynchronousResponseAtASpeed)

        @property
        def external_cad_model_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3558.ExternalCADModelSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3558,
            )

            return self._parent._cast(
                _3558.ExternalCADModelSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3561.FaceGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3561,
            )

            return self._parent._cast(
                _3561.FaceGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def fe_part_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3562.FEPartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3562,
            )

            return self._parent._cast(
                _3562.FEPartSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3566.GearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3566,
            )

            return self._parent._cast(_3566.GearSteadyStateSynchronousResponseAtASpeed)

        @property
        def guide_dxf_model_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3567.GuideDxfModelSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3567,
            )

            return self._parent._cast(
                _3567.GuideDxfModelSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3570.HypoidGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3570,
            )

            return self._parent._cast(
                _3570.HypoidGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3574.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3574,
            )

            return self._parent._cast(
                _3574.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3577.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3577,
            )

            return self._parent._cast(
                _3577.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3580.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3580,
            )

            return self._parent._cast(
                _3580.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mass_disc_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3581.MassDiscSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3581,
            )

            return self._parent._cast(
                _3581.MassDiscSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def measurement_component_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3582.MeasurementComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3582,
            )

            return self._parent._cast(
                _3582.MeasurementComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3583.MountableComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3583,
            )

            return self._parent._cast(
                _3583.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def oil_seal_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3584.OilSealSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3584,
            )

            return self._parent._cast(
                _3584.OilSealSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3587.PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3587,
            )

            return self._parent._cast(
                _3587.PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planet_carrier_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3591.PlanetCarrierSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3591,
            )

            return self._parent._cast(
                _3591.PlanetCarrierSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def point_load_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3592.PointLoadSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3592,
            )

            return self._parent._cast(
                _3592.PointLoadSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def power_load_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3593.PowerLoadSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3593,
            )

            return self._parent._cast(
                _3593.PowerLoadSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def pulley_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3594.PulleySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3594,
            )

            return self._parent._cast(
                _3594.PulleySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def ring_pins_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3595.RingPinsSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3595,
            )

            return self._parent._cast(
                _3595.RingPinsSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3599.RollingRingSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3599,
            )

            return self._parent._cast(
                _3599.RollingRingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_hub_connection_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3601.ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3601,
            )

            return self._parent._cast(
                _3601.ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3602.ShaftSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3602,
            )

            return self._parent._cast(_3602.ShaftSteadyStateSynchronousResponseAtASpeed)

        @property
        def spiral_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3607.SpiralBevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3607,
            )

            return self._parent._cast(
                _3607.SpiralBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_half_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3609.SpringDamperHalfSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3609,
            )

            return self._parent._cast(
                _3609.SpringDamperHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3614.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3614,
            )

            return self._parent._cast(
                _3614.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3617.StraightBevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3617,
            )

            return self._parent._cast(
                _3617.StraightBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3618.StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3618,
            )

            return self._parent._cast(
                _3618.StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3619.StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3619,
            )

            return self._parent._cast(
                _3619.StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_half_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3620.SynchroniserHalfSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3620,
            )

            return self._parent._cast(
                _3620.SynchroniserHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_part_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3621.SynchroniserPartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3621,
            )

            return self._parent._cast(
                _3621.SynchroniserPartSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_sleeve_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3622.SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3622,
            )

            return self._parent._cast(
                _3622.SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_pump_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3625.TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3625,
            )

            return self._parent._cast(
                _3625.TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_turbine_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3627.TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3627,
            )

            return self._parent._cast(
                _3627.TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def unbalanced_mass_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3628.UnbalancedMassSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3628,
            )

            return self._parent._cast(
                _3628.UnbalancedMassSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def virtual_component_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3629.VirtualComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3629,
            )

            return self._parent._cast(
                _3629.VirtualComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3632.WormGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3632,
            )

            return self._parent._cast(
                _3632.WormGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3635.ZerolBevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3635,
            )

            return self._parent._cast(
                _3635.ZerolBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "ComponentSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "ComponentSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2446.Component":
        """mastapy.system_model.part_model.Component

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
    ) -> "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_ComponentSteadyStateSynchronousResponseAtASpeed(self)
