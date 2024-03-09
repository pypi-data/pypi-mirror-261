"""BeltConnectionModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4644
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "BeltConnectionModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2270
    from mastapy.system_model.analyses_and_results.static_loads import _6823
    from mastapy.system_model.analyses_and_results.system_deflections import _2701
    from mastapy.system_model.analyses_and_results.modal_analyses import _4615, _4609
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543, _7540
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("BeltConnectionModalAnalysis",)


Self = TypeVar("Self", bound="BeltConnectionModalAnalysis")


class BeltConnectionModalAnalysis(_4644.InterMountableComponentConnectionModalAnalysis):
    """BeltConnectionModalAnalysis

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BeltConnectionModalAnalysis")

    class _Cast_BeltConnectionModalAnalysis:
        """Special nested class for casting BeltConnectionModalAnalysis to subclasses."""

        def __init__(
            self: "BeltConnectionModalAnalysis._Cast_BeltConnectionModalAnalysis",
            parent: "BeltConnectionModalAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_modal_analysis(
            self: "BeltConnectionModalAnalysis._Cast_BeltConnectionModalAnalysis",
        ) -> "_4644.InterMountableComponentConnectionModalAnalysis":
            return self._parent._cast(
                _4644.InterMountableComponentConnectionModalAnalysis
            )

        @property
        def connection_modal_analysis(
            self: "BeltConnectionModalAnalysis._Cast_BeltConnectionModalAnalysis",
        ) -> "_4609.ConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4609

            return self._parent._cast(_4609.ConnectionModalAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "BeltConnectionModalAnalysis._Cast_BeltConnectionModalAnalysis",
        ) -> "_7543.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BeltConnectionModalAnalysis._Cast_BeltConnectionModalAnalysis",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BeltConnectionModalAnalysis._Cast_BeltConnectionModalAnalysis",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BeltConnectionModalAnalysis._Cast_BeltConnectionModalAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltConnectionModalAnalysis._Cast_BeltConnectionModalAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_modal_analysis(
            self: "BeltConnectionModalAnalysis._Cast_BeltConnectionModalAnalysis",
        ) -> "_4615.CVTBeltConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4615

            return self._parent._cast(_4615.CVTBeltConnectionModalAnalysis)

        @property
        def belt_connection_modal_analysis(
            self: "BeltConnectionModalAnalysis._Cast_BeltConnectionModalAnalysis",
        ) -> "BeltConnectionModalAnalysis":
            return self._parent

        def __getattr__(
            self: "BeltConnectionModalAnalysis._Cast_BeltConnectionModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BeltConnectionModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2270.BeltConnection":
        """mastapy.system_model.connections_and_sockets.BeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6823.BeltConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BeltConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2701.BeltConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BeltConnectionSystemDeflection

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
    ) -> "BeltConnectionModalAnalysis._Cast_BeltConnectionModalAnalysis":
        return self._Cast_BeltConnectionModalAnalysis(self)
