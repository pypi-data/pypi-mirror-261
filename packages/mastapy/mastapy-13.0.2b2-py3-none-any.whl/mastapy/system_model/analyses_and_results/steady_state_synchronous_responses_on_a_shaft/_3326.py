"""PartSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7550
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "PartSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2470
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3352,
        _3247,
        _3248,
        _3249,
        _3252,
        _3253,
        _3254,
        _3255,
        _3257,
        _3259,
        _3260,
        _3261,
        _3262,
        _3264,
        _3265,
        _3266,
        _3267,
        _3269,
        _3270,
        _3272,
        _3274,
        _3275,
        _3277,
        _3278,
        _3280,
        _3281,
        _3283,
        _3285,
        _3286,
        _3288,
        _3289,
        _3290,
        _3293,
        _3295,
        _3296,
        _3297,
        _3298,
        _3299,
        _3301,
        _3302,
        _3303,
        _3304,
        _3306,
        _3307,
        _3308,
        _3310,
        _3311,
        _3314,
        _3315,
        _3317,
        _3318,
        _3320,
        _3321,
        _3322,
        _3323,
        _3324,
        _3325,
        _3328,
        _3329,
        _3331,
        _3332,
        _3333,
        _3334,
        _3335,
        _3336,
        _3338,
        _3340,
        _3341,
        _3342,
        _3343,
        _3345,
        _3347,
        _3348,
        _3350,
        _3351,
        _3354,
        _3355,
        _3357,
        _3358,
        _3359,
        _3360,
        _3361,
        _3362,
        _3363,
        _3364,
        _3366,
        _3367,
        _3368,
        _3369,
        _3370,
        _3372,
        _3373,
        _3375,
        _3376,
    )
    from mastapy.system_model.drawing import _2260
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("PartSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="PartSteadyStateSynchronousResponseOnAShaft")


class PartSteadyStateSynchronousResponseOnAShaft(_7550.PartStaticLoadAnalysisCase):
    """PartSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _PART_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartSteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_PartSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting PartSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
            parent: "PartSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def part_static_load_analysis_case(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3247.AbstractAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3247,
            )

            return self._parent._cast(
                _3247.AbstractAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3248.AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3248,
            )

            return self._parent._cast(
                _3248.AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3249.AbstractShaftSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3249,
            )

            return self._parent._cast(
                _3249.AbstractShaftSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3252.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3252,
            )

            return self._parent._cast(
                _3252.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3253.AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3253,
            )

            return self._parent._cast(
                _3253.AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def assembly_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3254.AssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3254,
            )

            return self._parent._cast(
                _3254.AssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bearing_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3255.BearingSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3255,
            )

            return self._parent._cast(
                _3255.BearingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def belt_drive_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3257.BeltDriveSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3257,
            )

            return self._parent._cast(
                _3257.BeltDriveSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3259.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3259,
            )

            return self._parent._cast(
                _3259.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3260.BevelDifferentialGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3260,
            )

            return self._parent._cast(
                _3260.BevelDifferentialGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3261.BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3261,
            )

            return self._parent._cast(
                _3261.BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3262.BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3262,
            )

            return self._parent._cast(
                _3262.BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3264.BevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3264,
            )

            return self._parent._cast(
                _3264.BevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3265.BevelGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3265,
            )

            return self._parent._cast(
                _3265.BevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bolted_joint_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3266.BoltedJointSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3266,
            )

            return self._parent._cast(
                _3266.BoltedJointSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bolt_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3267.BoltSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3267,
            )

            return self._parent._cast(_3267.BoltSteadyStateSynchronousResponseOnAShaft)

        @property
        def clutch_half_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3269.ClutchHalfSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3269,
            )

            return self._parent._cast(
                _3269.ClutchHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def clutch_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3270.ClutchSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3270,
            )

            return self._parent._cast(
                _3270.ClutchSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3272.ComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3272,
            )

            return self._parent._cast(
                _3272.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_half_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3274.ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3274,
            )

            return self._parent._cast(
                _3274.ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3275.ConceptCouplingSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3275,
            )

            return self._parent._cast(
                _3275.ConceptCouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3277.ConceptGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3277,
            )

            return self._parent._cast(
                _3277.ConceptGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3278.ConceptGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3278,
            )

            return self._parent._cast(
                _3278.ConceptGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3280.ConicalGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3280,
            )

            return self._parent._cast(
                _3280.ConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3281.ConicalGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3281,
            )

            return self._parent._cast(
                _3281.ConicalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connector_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3283.ConnectorSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3283,
            )

            return self._parent._cast(
                _3283.ConnectorSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_half_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3285.CouplingHalfSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3285,
            )

            return self._parent._cast(
                _3285.CouplingHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3286.CouplingSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3286,
            )

            return self._parent._cast(
                _3286.CouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_pulley_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3288.CVTPulleySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3288,
            )

            return self._parent._cast(
                _3288.CVTPulleySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3289.CVTSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3289,
            )

            return self._parent._cast(_3289.CVTSteadyStateSynchronousResponseOnAShaft)

        @property
        def cycloidal_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3290.CycloidalAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3290,
            )

            return self._parent._cast(
                _3290.CycloidalAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_disc_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3293.CycloidalDiscSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3293,
            )

            return self._parent._cast(
                _3293.CycloidalDiscSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3295.CylindricalGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3295,
            )

            return self._parent._cast(
                _3295.CylindricalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3296.CylindricalGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3296,
            )

            return self._parent._cast(
                _3296.CylindricalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3297.CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3297,
            )

            return self._parent._cast(
                _3297.CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def datum_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3298.DatumSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3298,
            )

            return self._parent._cast(_3298.DatumSteadyStateSynchronousResponseOnAShaft)

        @property
        def external_cad_model_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3299.ExternalCADModelSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3299,
            )

            return self._parent._cast(
                _3299.ExternalCADModelSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3301.FaceGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3301,
            )

            return self._parent._cast(
                _3301.FaceGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3302.FaceGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3302,
            )

            return self._parent._cast(
                _3302.FaceGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def fe_part_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3303.FEPartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3303,
            )

            return self._parent._cast(
                _3303.FEPartSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def flexible_pin_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3304.FlexiblePinAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3304,
            )

            return self._parent._cast(
                _3304.FlexiblePinAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3306.GearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3306,
            )

            return self._parent._cast(
                _3306.GearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3307.GearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3307,
            )

            return self._parent._cast(_3307.GearSteadyStateSynchronousResponseOnAShaft)

        @property
        def guide_dxf_model_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3308.GuideDxfModelSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3308,
            )

            return self._parent._cast(
                _3308.GuideDxfModelSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3310.HypoidGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3310,
            )

            return self._parent._cast(
                _3310.HypoidGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3311.HypoidGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3311,
            )

            return self._parent._cast(
                _3311.HypoidGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3314.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3314,
            )

            return self._parent._cast(
                _3314.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3315.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3315,
            )

            return self._parent._cast(
                _3315.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3317.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3317,
            )

            return self._parent._cast(
                _3317.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3318.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3318,
            )

            return self._parent._cast(
                _3318.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3320.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3320,
            )

            return self._parent._cast(
                _3320.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3321.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3321,
            )

            return self._parent._cast(
                _3321.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mass_disc_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3322.MassDiscSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3322,
            )

            return self._parent._cast(
                _3322.MassDiscSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def measurement_component_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3323.MeasurementComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3323,
            )

            return self._parent._cast(
                _3323.MeasurementComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3324.MountableComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3324,
            )

            return self._parent._cast(
                _3324.MountableComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def oil_seal_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3325.OilSealSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3325,
            )

            return self._parent._cast(
                _3325.OilSealSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3328.PartToPartShearCouplingHalfSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3328,
            )

            return self._parent._cast(
                _3328.PartToPartShearCouplingHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3329.PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3329,
            )

            return self._parent._cast(
                _3329.PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planetary_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3331.PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3331,
            )

            return self._parent._cast(
                _3331.PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planet_carrier_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3332.PlanetCarrierSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3332,
            )

            return self._parent._cast(
                _3332.PlanetCarrierSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def point_load_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3333.PointLoadSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3333,
            )

            return self._parent._cast(
                _3333.PointLoadSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def power_load_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3334.PowerLoadSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3334,
            )

            return self._parent._cast(
                _3334.PowerLoadSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def pulley_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3335.PulleySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3335,
            )

            return self._parent._cast(
                _3335.PulleySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def ring_pins_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3336.RingPinsSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3336,
            )

            return self._parent._cast(
                _3336.RingPinsSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3338.RollingRingAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3338,
            )

            return self._parent._cast(
                _3338.RollingRingAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3340.RollingRingSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3340,
            )

            return self._parent._cast(
                _3340.RollingRingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def root_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3341.RootAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3341,
            )

            return self._parent._cast(
                _3341.RootAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_hub_connection_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3342.ShaftHubConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3342,
            )

            return self._parent._cast(
                _3342.ShaftHubConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3343.ShaftSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3343,
            )

            return self._parent._cast(_3343.ShaftSteadyStateSynchronousResponseOnAShaft)

        @property
        def specialised_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3345.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3345,
            )

            return self._parent._cast(
                _3345.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3347.SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3347,
            )

            return self._parent._cast(
                _3347.SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3348.SpiralBevelGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3348,
            )

            return self._parent._cast(
                _3348.SpiralBevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_half_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3350.SpringDamperHalfSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3350,
            )

            return self._parent._cast(
                _3350.SpringDamperHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3351.SpringDamperSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3351,
            )

            return self._parent._cast(
                _3351.SpringDamperSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3354.StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3354,
            )

            return self._parent._cast(
                _3354.StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3355.StraightBevelDiffGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3355,
            )

            return self._parent._cast(
                _3355.StraightBevelDiffGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3357.StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3357,
            )

            return self._parent._cast(
                _3357.StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3358.StraightBevelGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3358,
            )

            return self._parent._cast(
                _3358.StraightBevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3359.StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3359,
            )

            return self._parent._cast(
                _3359.StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3360.StraightBevelSunGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3360,
            )

            return self._parent._cast(
                _3360.StraightBevelSunGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_half_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3361.SynchroniserHalfSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3361,
            )

            return self._parent._cast(
                _3361.SynchroniserHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_part_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3362.SynchroniserPartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3362,
            )

            return self._parent._cast(
                _3362.SynchroniserPartSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_sleeve_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3363.SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3363,
            )

            return self._parent._cast(
                _3363.SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3364.SynchroniserSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3364,
            )

            return self._parent._cast(
                _3364.SynchroniserSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_pump_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3366.TorqueConverterPumpSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3366,
            )

            return self._parent._cast(
                _3366.TorqueConverterPumpSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3367.TorqueConverterSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3367,
            )

            return self._parent._cast(
                _3367.TorqueConverterSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_turbine_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3368.TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3368,
            )

            return self._parent._cast(
                _3368.TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def unbalanced_mass_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3369.UnbalancedMassSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3369,
            )

            return self._parent._cast(
                _3369.UnbalancedMassSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def virtual_component_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3370.VirtualComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3370,
            )

            return self._parent._cast(
                _3370.VirtualComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3372.WormGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3372,
            )

            return self._parent._cast(
                _3372.WormGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3373.WormGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3373,
            )

            return self._parent._cast(
                _3373.WormGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3375.ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3375,
            )

            return self._parent._cast(
                _3375.ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3376.ZerolBevelGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3376,
            )

            return self._parent._cast(
                _3376.ZerolBevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
        ) -> "PartSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft",
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
        self: Self, instance_to_wrap: "PartSteadyStateSynchronousResponseOnAShaft.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2470.Part":
        """mastapy.system_model.part_model.Part

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def steady_state_synchronous_response_on_a_shaft(
        self: Self,
    ) -> "_3352.SteadyStateSynchronousResponseOnAShaft":
        """mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.SteadyStateSynchronousResponseOnAShaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SteadyStateSynchronousResponseOnAShaft

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def create_viewable(self: Self) -> "_2260.SteadyStateSynchronousResponseViewable":
        """mastapy.system_model.drawing.SteadyStateSynchronousResponseViewable"""
        method_result = self.wrapped.CreateViewable()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(
        self: Self,
    ) -> "PartSteadyStateSynchronousResponseOnAShaft._Cast_PartSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_PartSteadyStateSynchronousResponseOnAShaft(self)
