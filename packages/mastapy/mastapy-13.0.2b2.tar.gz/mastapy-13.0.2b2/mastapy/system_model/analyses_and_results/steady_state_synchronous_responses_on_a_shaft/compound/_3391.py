"""BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3388,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3261,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3393,
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
__all__ = ("BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self",
    bound="BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
)


class BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft(
    _3388.BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft
):
    """BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "_3388.BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            return self._parent._cast(
                _3388.BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3393.BevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3393,
            )

            return self._parent._cast(
                _3393.BevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
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
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3409.ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3409,
            )

            return self._parent._cast(
                _3409.ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3435.GearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3435,
            )

            return self._parent._cast(
                _3435.GearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3454.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3454,
            )

            return self._parent._cast(
                _3454.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3402.ComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3402,
            )

            return self._parent._cast(
                _3402.ComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3456.PartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3456,
            )

            return self._parent._cast(
                _3456.PartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_analysis(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            return self._parent

        def __getattr__(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> (
        "List[_3261.BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft]"
    ):
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft]

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
    ) -> (
        "List[_3261.BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft]"
    ):
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft(
            self
        )
