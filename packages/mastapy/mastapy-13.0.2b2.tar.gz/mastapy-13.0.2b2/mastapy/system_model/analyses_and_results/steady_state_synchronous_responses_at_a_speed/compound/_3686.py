"""CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3683,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3556,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3694,
        _3713,
        _3661,
        _3715,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed"
)


class CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed(
    _3683.CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed
):
    """CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = (
        _CYLINDRICAL_PLANET_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3683.CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3683.CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3694.GearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3694,
            )

            return self._parent._cast(
                _3694.GearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3713.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3713,
            )

            return self._parent._cast(
                _3713.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_compound_steady_state_synchronous_response_at_a_speed(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3661.ComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3661,
            )

            return self._parent._cast(
                _3661.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3715.PartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3715,
            )

            return self._parent._cast(
                _3715.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3556.CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "List[_3556.CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed(
            self
        )
