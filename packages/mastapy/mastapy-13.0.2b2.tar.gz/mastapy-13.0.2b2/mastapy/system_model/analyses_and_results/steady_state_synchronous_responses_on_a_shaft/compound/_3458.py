"""PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3415,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2350
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3327,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3442,
        _3412,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = (
    "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
)


Self = TypeVar(
    "Self",
    bound="PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
)


class PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft(
    _3415.CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
):
    """PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3415.CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3415.CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3442.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3442,
            )

            return self._parent._cast(
                _3442.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3412.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3412,
            )

            return self._parent._cast(
                _3412.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_compound_analysis(
            self: "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7541.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2350.PartToPartShearCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2350.PartToPartShearCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection

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
    ) -> "List[_3327.PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3327.PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft(
            self
        )
