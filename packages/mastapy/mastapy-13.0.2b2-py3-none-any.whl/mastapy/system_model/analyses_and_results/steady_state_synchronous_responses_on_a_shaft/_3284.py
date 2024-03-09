"""CouplingConnectionSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3312,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2348
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3268,
        _3273,
        _3327,
        _3349,
        _3365,
        _3282,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543, _7540
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="CouplingConnectionSteadyStateSynchronousResponseOnAShaft")


class CouplingConnectionSteadyStateSynchronousResponseOnAShaft(
    _3312.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
):
    """CouplingConnectionSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting CouplingConnectionSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
            parent: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3312.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3312.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3282.ConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3282,
            )

            return self._parent._cast(
                _3282.ConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_static_load_analysis_case(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7543.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def clutch_connection_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3268.ClutchConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3268,
            )

            return self._parent._cast(
                _3268.ClutchConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_connection_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3273.ConceptCouplingConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3273,
            )

            return self._parent._cast(
                _3273.ConceptCouplingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_connection_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3327.PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3327,
            )

            return self._parent._cast(
                _3327.PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_connection_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3349.SpringDamperConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3349,
            )

            return self._parent._cast(
                _3349.SpringDamperConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_connection_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3365.TorqueConverterConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3365,
            )

            return self._parent._cast(
                _3365.TorqueConverterConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_connection_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "CouplingConnectionSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft.TYPE",
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
    ) -> "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft(self)
