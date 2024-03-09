"""CouplingConnectionSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3051,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "CouplingConnectionSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2348
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3006,
        _3011,
        _3066,
        _3088,
        _3106,
        _3020,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543, _7540
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="CouplingConnectionSteadyStateSynchronousResponse")


class CouplingConnectionSteadyStateSynchronousResponse(
    _3051.InterMountableComponentConnectionSteadyStateSynchronousResponse
):
    """CouplingConnectionSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingConnectionSteadyStateSynchronousResponse"
    )

    class _Cast_CouplingConnectionSteadyStateSynchronousResponse:
        """Special nested class for casting CouplingConnectionSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
            parent: "CouplingConnectionSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_3051.InterMountableComponentConnectionSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3051.InterMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_3020.ConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3020,
            )

            return self._parent._cast(_3020.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_7543.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def clutch_connection_steady_state_synchronous_response(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_3006.ClutchConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3006,
            )

            return self._parent._cast(
                _3006.ClutchConnectionSteadyStateSynchronousResponse
            )

        @property
        def concept_coupling_connection_steady_state_synchronous_response(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_3011.ConceptCouplingConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3011,
            )

            return self._parent._cast(
                _3011.ConceptCouplingConnectionSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_connection_steady_state_synchronous_response(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_3066.PartToPartShearCouplingConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3066,
            )

            return self._parent._cast(
                _3066.PartToPartShearCouplingConnectionSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_connection_steady_state_synchronous_response(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_3088.SpringDamperConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3088,
            )

            return self._parent._cast(
                _3088.SpringDamperConnectionSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_connection_steady_state_synchronous_response(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_3106.TorqueConverterConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3106,
            )

            return self._parent._cast(
                _3106.TorqueConverterConnectionSteadyStateSynchronousResponse
            )

        @property
        def coupling_connection_steady_state_synchronous_response(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "CouplingConnectionSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
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
        instance_to_wrap: "CouplingConnectionSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2348.CouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.CouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse":
        return self._Cast_CouplingConnectionSteadyStateSynchronousResponse(self)
