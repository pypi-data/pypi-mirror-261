"""CVTBeltConnectionCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _4999,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "CVTBeltConnectionCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4899,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5055,
        _5025,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="CVTBeltConnectionCompoundModalAnalysisAtAStiffness")


class CVTBeltConnectionCompoundModalAnalysisAtAStiffness(
    _4999.BeltConnectionCompoundModalAnalysisAtAStiffness
):
    """CVTBeltConnectionCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTBeltConnectionCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_CVTBeltConnectionCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting CVTBeltConnectionCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "CVTBeltConnectionCompoundModalAnalysisAtAStiffness._Cast_CVTBeltConnectionCompoundModalAnalysisAtAStiffness",
            parent: "CVTBeltConnectionCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def belt_connection_compound_modal_analysis_at_a_stiffness(
            self: "CVTBeltConnectionCompoundModalAnalysisAtAStiffness._Cast_CVTBeltConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_4999.BeltConnectionCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(
                _4999.BeltConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "CVTBeltConnectionCompoundModalAnalysisAtAStiffness._Cast_CVTBeltConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5055.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5055,
            )

            return self._parent._cast(
                _5055.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def connection_compound_modal_analysis_at_a_stiffness(
            self: "CVTBeltConnectionCompoundModalAnalysisAtAStiffness._Cast_CVTBeltConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5025.ConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5025,
            )

            return self._parent._cast(_5025.ConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def connection_compound_analysis(
            self: "CVTBeltConnectionCompoundModalAnalysisAtAStiffness._Cast_CVTBeltConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_7541.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTBeltConnectionCompoundModalAnalysisAtAStiffness._Cast_CVTBeltConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionCompoundModalAnalysisAtAStiffness._Cast_CVTBeltConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_compound_modal_analysis_at_a_stiffness(
            self: "CVTBeltConnectionCompoundModalAnalysisAtAStiffness._Cast_CVTBeltConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "CVTBeltConnectionCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionCompoundModalAnalysisAtAStiffness._Cast_CVTBeltConnectionCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "CVTBeltConnectionCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4899.CVTBeltConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.CVTBeltConnectionModalAnalysisAtAStiffness]

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
    ) -> "List[_4899.CVTBeltConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.CVTBeltConnectionModalAnalysisAtAStiffness]

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
    ) -> "CVTBeltConnectionCompoundModalAnalysisAtAStiffness._Cast_CVTBeltConnectionCompoundModalAnalysisAtAStiffness":
        return self._Cast_CVTBeltConnectionCompoundModalAnalysisAtAStiffness(self)
