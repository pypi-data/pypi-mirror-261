"""BeltConnectionModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5184
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "BeltConnectionModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2270
    from mastapy.system_model.analyses_and_results.static_loads import _6823
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5159,
        _5154,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543, _7540
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("BeltConnectionModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="BeltConnectionModalAnalysisAtASpeed")


class BeltConnectionModalAnalysisAtASpeed(
    _5184.InterMountableComponentConnectionModalAnalysisAtASpeed
):
    """BeltConnectionModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BeltConnectionModalAnalysisAtASpeed")

    class _Cast_BeltConnectionModalAnalysisAtASpeed:
        """Special nested class for casting BeltConnectionModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "BeltConnectionModalAnalysisAtASpeed._Cast_BeltConnectionModalAnalysisAtASpeed",
            parent: "BeltConnectionModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_speed(
            self: "BeltConnectionModalAnalysisAtASpeed._Cast_BeltConnectionModalAnalysisAtASpeed",
        ) -> "_5184.InterMountableComponentConnectionModalAnalysisAtASpeed":
            return self._parent._cast(
                _5184.InterMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def connection_modal_analysis_at_a_speed(
            self: "BeltConnectionModalAnalysisAtASpeed._Cast_BeltConnectionModalAnalysisAtASpeed",
        ) -> "_5154.ConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5154,
            )

            return self._parent._cast(_5154.ConnectionModalAnalysisAtASpeed)

        @property
        def connection_static_load_analysis_case(
            self: "BeltConnectionModalAnalysisAtASpeed._Cast_BeltConnectionModalAnalysisAtASpeed",
        ) -> "_7543.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BeltConnectionModalAnalysisAtASpeed._Cast_BeltConnectionModalAnalysisAtASpeed",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BeltConnectionModalAnalysisAtASpeed._Cast_BeltConnectionModalAnalysisAtASpeed",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BeltConnectionModalAnalysisAtASpeed._Cast_BeltConnectionModalAnalysisAtASpeed",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltConnectionModalAnalysisAtASpeed._Cast_BeltConnectionModalAnalysisAtASpeed",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_modal_analysis_at_a_speed(
            self: "BeltConnectionModalAnalysisAtASpeed._Cast_BeltConnectionModalAnalysisAtASpeed",
        ) -> "_5159.CVTBeltConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5159,
            )

            return self._parent._cast(_5159.CVTBeltConnectionModalAnalysisAtASpeed)

        @property
        def belt_connection_modal_analysis_at_a_speed(
            self: "BeltConnectionModalAnalysisAtASpeed._Cast_BeltConnectionModalAnalysisAtASpeed",
        ) -> "BeltConnectionModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "BeltConnectionModalAnalysisAtASpeed._Cast_BeltConnectionModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "BeltConnectionModalAnalysisAtASpeed.TYPE"
    ):
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
    def cast_to(
        self: Self,
    ) -> (
        "BeltConnectionModalAnalysisAtASpeed._Cast_BeltConnectionModalAnalysisAtASpeed"
    ):
        return self._Cast_BeltConnectionModalAnalysisAtASpeed(self)
