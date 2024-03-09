"""ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3135,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2333
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3115,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3123,
        _3151,
        _3177,
        _3183,
        _3153,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse")


class ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse(
    _3135.BevelGearMeshCompoundSteadyStateSynchronousResponse
):
    """ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse",
            parent: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3135.BevelGearMeshCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3135.BevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3123.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3123,
            )

            return self._parent._cast(
                _3123.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3151.ConicalGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3151,
            )

            return self._parent._cast(
                _3151.ConicalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_mesh_compound_steady_state_synchronous_response(
            self: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3177.GearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3177,
            )

            return self._parent._cast(
                _3177.GearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3183.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3183,
            )

            return self._parent._cast(
                _3183.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_steady_state_synchronous_response(
            self: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3153.ConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3153,
            )

            return self._parent._cast(
                _3153.ConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_analysis(
            self: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_7541.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2333.ZerolBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2333.ZerolBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3115.ZerolBevelGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ZerolBevelGearMeshSteadyStateSynchronousResponse]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3115.ZerolBevelGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ZerolBevelGearMeshSteadyStateSynchronousResponse]

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
    def cast_to(
        self: Self,
    ) -> "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse":
        return self._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse(self)
