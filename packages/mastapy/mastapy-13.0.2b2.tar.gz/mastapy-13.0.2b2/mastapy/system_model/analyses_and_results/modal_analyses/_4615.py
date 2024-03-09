"""CVTBeltConnectionModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4583
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "CVTBeltConnectionModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2275
    from mastapy.system_model.analyses_and_results.system_deflections import _2734
    from mastapy.system_model.analyses_and_results.modal_analyses import _4644, _4609
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543, _7540
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionModalAnalysis",)


Self = TypeVar("Self", bound="CVTBeltConnectionModalAnalysis")


class CVTBeltConnectionModalAnalysis(_4583.BeltConnectionModalAnalysis):
    """CVTBeltConnectionModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTBeltConnectionModalAnalysis")

    class _Cast_CVTBeltConnectionModalAnalysis:
        """Special nested class for casting CVTBeltConnectionModalAnalysis to subclasses."""

        def __init__(
            self: "CVTBeltConnectionModalAnalysis._Cast_CVTBeltConnectionModalAnalysis",
            parent: "CVTBeltConnectionModalAnalysis",
        ):
            self._parent = parent

        @property
        def belt_connection_modal_analysis(
            self: "CVTBeltConnectionModalAnalysis._Cast_CVTBeltConnectionModalAnalysis",
        ) -> "_4583.BeltConnectionModalAnalysis":
            return self._parent._cast(_4583.BeltConnectionModalAnalysis)

        @property
        def inter_mountable_component_connection_modal_analysis(
            self: "CVTBeltConnectionModalAnalysis._Cast_CVTBeltConnectionModalAnalysis",
        ) -> "_4644.InterMountableComponentConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4644

            return self._parent._cast(
                _4644.InterMountableComponentConnectionModalAnalysis
            )

        @property
        def connection_modal_analysis(
            self: "CVTBeltConnectionModalAnalysis._Cast_CVTBeltConnectionModalAnalysis",
        ) -> "_4609.ConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4609

            return self._parent._cast(_4609.ConnectionModalAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CVTBeltConnectionModalAnalysis._Cast_CVTBeltConnectionModalAnalysis",
        ) -> "_7543.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CVTBeltConnectionModalAnalysis._Cast_CVTBeltConnectionModalAnalysis",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CVTBeltConnectionModalAnalysis._Cast_CVTBeltConnectionModalAnalysis",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTBeltConnectionModalAnalysis._Cast_CVTBeltConnectionModalAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionModalAnalysis._Cast_CVTBeltConnectionModalAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_modal_analysis(
            self: "CVTBeltConnectionModalAnalysis._Cast_CVTBeltConnectionModalAnalysis",
        ) -> "CVTBeltConnectionModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionModalAnalysis._Cast_CVTBeltConnectionModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTBeltConnectionModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2275.CVTBeltConnection":
        """mastapy.system_model.connections_and_sockets.CVTBeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2734.CVTBeltConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CVTBeltConnectionSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CVTBeltConnectionModalAnalysis._Cast_CVTBeltConnectionModalAnalysis":
        return self._Cast_CVTBeltConnectionModalAnalysis(self)
