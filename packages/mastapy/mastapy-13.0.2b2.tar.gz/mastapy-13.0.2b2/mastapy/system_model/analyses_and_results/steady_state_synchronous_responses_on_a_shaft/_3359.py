"""StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3355,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2551
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3265,
        _3253,
        _3281,
        _3307,
        _3324,
        _3272,
        _3326,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft"
)


class StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft(
    _3355.StraightBevelDiffGearSteadyStateSynchronousResponseOnAShaft
):
    """StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
            parent: "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3355.StraightBevelDiffGearSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3355.StraightBevelDiffGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3265.BevelGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3265,
            )

            return self._parent._cast(
                _3265.BevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3253.AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3253,
            )

            return self._parent._cast(
                _3253.AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3281.ConicalGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3281,
            )

            return self._parent._cast(
                _3281.ConicalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3307.GearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3307,
            )

            return self._parent._cast(_3307.GearSteadyStateSynchronousResponseOnAShaft)

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3324.MountableComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3324,
            )

            return self._parent._cast(
                _3324.MountableComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3272.ComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3272,
            )

            return self._parent._cast(
                _3272.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3326.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3326,
            )

            return self._parent._cast(_3326.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2551.StraightBevelPlanetGear":
        """mastapy.system_model.part_model.gears.StraightBevelPlanetGear

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
    ) -> "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft(
            self
        )
