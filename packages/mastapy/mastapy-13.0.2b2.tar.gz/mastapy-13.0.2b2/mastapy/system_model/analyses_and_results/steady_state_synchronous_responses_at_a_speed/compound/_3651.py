"""BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3647,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3521,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3652,
        _3640,
        _3668,
        _3694,
        _3713,
        _3661,
        _3715,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self",
    bound="BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
)


class BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed(
    _3647.BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed
):
    """BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> (
            "_3647.BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            return self._parent._cast(
                _3647.BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3652.BevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3652,
            )

            return self._parent._cast(
                _3652.BevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> (
            "_3640.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3640,
            )

            return self._parent._cast(
                _3640.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3668.ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3668,
            )

            return self._parent._cast(
                _3668.ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3694.GearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3694,
            )

            return self._parent._cast(
                _3694.GearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3713.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3713,
            )

            return self._parent._cast(
                _3713.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_compound_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3661.ComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3661,
            )

            return self._parent._cast(
                _3661.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3715.PartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3715,
            )

            return self._parent._cast(
                _3715.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bevel_differential_sun_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3521.BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "List[_3521.BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed(
            self
        )
