"""BevelGearSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3512,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "BevelGearSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2521
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3519,
        _3520,
        _3521,
        _3607,
        _3614,
        _3617,
        _3618,
        _3619,
        _3635,
        _3540,
        _3566,
        _3583,
        _3531,
        _3585,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="BevelGearSteadyStateSynchronousResponseAtASpeed")


class BevelGearSteadyStateSynchronousResponseAtASpeed(
    _3512.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed
):
    """BevelGearSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_BevelGearSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting BevelGearSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "BevelGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearSteadyStateSynchronousResponseAtASpeed",
            parent: "BevelGearSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "BevelGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3512.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3512.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "BevelGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3540.ConicalGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3540,
            )

            return self._parent._cast(
                _3540.ConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_steady_state_synchronous_response_at_a_speed(
            self: "BevelGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3566.GearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3566,
            )

            return self._parent._cast(_3566.GearSteadyStateSynchronousResponseAtASpeed)

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "BevelGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3583.MountableComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3583,
            )

            return self._parent._cast(
                _3583.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "BevelGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3531.ComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3531,
            )

            return self._parent._cast(
                _3531.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "BevelGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3585.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3585,
            )

            return self._parent._cast(_3585.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "BevelGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_steady_state_synchronous_response_at_a_speed(
            self: "BevelGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3519.BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3519,
            )

            return self._parent._cast(
                _3519.BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "BevelGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3520.BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3520,
            )

            return self._parent._cast(
                _3520.BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response_at_a_speed(
            self: "BevelGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3521.BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3521,
            )

            return self._parent._cast(
                _3521.BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "BevelGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3607.SpiralBevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3607,
            )

            return self._parent._cast(
                _3607.SpiralBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response_at_a_speed(
            self: "BevelGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3614.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3614,
            )

            return self._parent._cast(
                _3614.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "BevelGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3617.StraightBevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3617,
            )

            return self._parent._cast(
                _3617.StraightBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "BevelGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3618.StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3618,
            )

            return self._parent._cast(
                _3618.StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response_at_a_speed(
            self: "BevelGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3619.StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3619,
            )

            return self._parent._cast(
                _3619.StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "BevelGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3635.ZerolBevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3635,
            )

            return self._parent._cast(
                _3635.ZerolBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "BevelGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "BevelGearSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "BevelGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "BevelGearSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2521.BevelGear":
        """mastapy.system_model.part_model.gears.BevelGear

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
    ) -> "BevelGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_BevelGearSteadyStateSynchronousResponseAtASpeed(self)
