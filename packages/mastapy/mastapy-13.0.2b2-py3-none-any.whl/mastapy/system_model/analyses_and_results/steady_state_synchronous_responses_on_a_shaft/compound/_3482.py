"""StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3393,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2547
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3355,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3488,
        _3489,
        _3381,
        _3409,
        _3435,
        _3454,
        _3402,
        _3456,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft"
)


class StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft(
    _3393.BevelGearCompoundSteadyStateSynchronousResponseOnAShaft
):
    """StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = (
        _STRAIGHT_BEVEL_DIFF_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3393.BevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3393.BevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "_3381.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3381,
            )

            return self._parent._cast(
                _3381.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3409.ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3409,
            )

            return self._parent._cast(
                _3409.ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3435.GearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3435,
            )

            return self._parent._cast(
                _3435.GearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3454.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3454,
            )

            return self._parent._cast(
                _3454.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3402.ComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3402,
            )

            return self._parent._cast(
                _3402.ComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3456.PartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3456,
            )

            return self._parent._cast(
                _3456.PartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_analysis(
            self: "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3488.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3488,
            )

            return self._parent._cast(
                _3488.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3489.StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3489,
            )

            return self._parent._cast(
                _3489.StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2547.StraightBevelDiffGear":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3355.StraightBevelDiffGearSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.StraightBevelDiffGearSteadyStateSynchronousResponseOnAShaft]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3355.StraightBevelDiffGearSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.StraightBevelDiffGearSteadyStateSynchronousResponseOnAShaft]

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
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft(
            self
        )
