"""BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3382,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3263,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3389,
        _3477,
        _3483,
        _3486,
        _3504,
        _3410,
        _3436,
        _3442,
        _3412,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
)


class BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft(
    _3382.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
):
    """BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3382.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3382.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3410.ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3410,
            )

            return self._parent._cast(
                _3410.ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3436.GearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3436,
            )

            return self._parent._cast(
                _3436.GearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3442.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3442,
            )

            return self._parent._cast(
                _3442.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3412.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3412,
            )

            return self._parent._cast(
                _3412.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_compound_analysis(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7541.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3389.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3389,
            )

            return self._parent._cast(
                _3389.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3477.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3477,
            )

            return self._parent._cast(
                _3477.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3483.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3483,
            )

            return self._parent._cast(
                _3483.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "_3486.StraightBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3486,
            )

            return self._parent._cast(
                _3486.StraightBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3504.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3504,
            )

            return self._parent._cast(
                _3504.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3263.BevelGearMeshSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.BevelGearMeshSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3263.BevelGearMeshSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.BevelGearMeshSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft(
            self
        )
