"""CVTBeltConnectionCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4739
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "CVTBeltConnectionCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4615
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4795,
        _4765,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionCompoundModalAnalysis",)


Self = TypeVar("Self", bound="CVTBeltConnectionCompoundModalAnalysis")


class CVTBeltConnectionCompoundModalAnalysis(_4739.BeltConnectionCompoundModalAnalysis):
    """CVTBeltConnectionCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTBeltConnectionCompoundModalAnalysis"
    )

    class _Cast_CVTBeltConnectionCompoundModalAnalysis:
        """Special nested class for casting CVTBeltConnectionCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "CVTBeltConnectionCompoundModalAnalysis._Cast_CVTBeltConnectionCompoundModalAnalysis",
            parent: "CVTBeltConnectionCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def belt_connection_compound_modal_analysis(
            self: "CVTBeltConnectionCompoundModalAnalysis._Cast_CVTBeltConnectionCompoundModalAnalysis",
        ) -> "_4739.BeltConnectionCompoundModalAnalysis":
            return self._parent._cast(_4739.BeltConnectionCompoundModalAnalysis)

        @property
        def inter_mountable_component_connection_compound_modal_analysis(
            self: "CVTBeltConnectionCompoundModalAnalysis._Cast_CVTBeltConnectionCompoundModalAnalysis",
        ) -> "_4795.InterMountableComponentConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4795,
            )

            return self._parent._cast(
                _4795.InterMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def connection_compound_modal_analysis(
            self: "CVTBeltConnectionCompoundModalAnalysis._Cast_CVTBeltConnectionCompoundModalAnalysis",
        ) -> "_4765.ConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4765,
            )

            return self._parent._cast(_4765.ConnectionCompoundModalAnalysis)

        @property
        def connection_compound_analysis(
            self: "CVTBeltConnectionCompoundModalAnalysis._Cast_CVTBeltConnectionCompoundModalAnalysis",
        ) -> "_7541.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTBeltConnectionCompoundModalAnalysis._Cast_CVTBeltConnectionCompoundModalAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionCompoundModalAnalysis._Cast_CVTBeltConnectionCompoundModalAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_compound_modal_analysis(
            self: "CVTBeltConnectionCompoundModalAnalysis._Cast_CVTBeltConnectionCompoundModalAnalysis",
        ) -> "CVTBeltConnectionCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionCompoundModalAnalysis._Cast_CVTBeltConnectionCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "CVTBeltConnectionCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4615.CVTBeltConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CVTBeltConnectionModalAnalysis]

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
    ) -> "List[_4615.CVTBeltConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CVTBeltConnectionModalAnalysis]

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
    ) -> "CVTBeltConnectionCompoundModalAnalysis._Cast_CVTBeltConnectionCompoundModalAnalysis":
        return self._Cast_CVTBeltConnectionCompoundModalAnalysis(self)
