"""TorqueConverterConnectionCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6582
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "TorqueConverterConnectionCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2354
    from mastapy.system_model.analyses_and_results.static_loads import _6975
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6613,
        _6580,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543, _7540
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterConnectionCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="TorqueConverterConnectionCriticalSpeedAnalysis")


class TorqueConverterConnectionCriticalSpeedAnalysis(
    _6582.CouplingConnectionCriticalSpeedAnalysis
):
    """TorqueConverterConnectionCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterConnectionCriticalSpeedAnalysis"
    )

    class _Cast_TorqueConverterConnectionCriticalSpeedAnalysis:
        """Special nested class for casting TorqueConverterConnectionCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "TorqueConverterConnectionCriticalSpeedAnalysis._Cast_TorqueConverterConnectionCriticalSpeedAnalysis",
            parent: "TorqueConverterConnectionCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_critical_speed_analysis(
            self: "TorqueConverterConnectionCriticalSpeedAnalysis._Cast_TorqueConverterConnectionCriticalSpeedAnalysis",
        ) -> "_6582.CouplingConnectionCriticalSpeedAnalysis":
            return self._parent._cast(_6582.CouplingConnectionCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_critical_speed_analysis(
            self: "TorqueConverterConnectionCriticalSpeedAnalysis._Cast_TorqueConverterConnectionCriticalSpeedAnalysis",
        ) -> "_6613.InterMountableComponentConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6613,
            )

            return self._parent._cast(
                _6613.InterMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def connection_critical_speed_analysis(
            self: "TorqueConverterConnectionCriticalSpeedAnalysis._Cast_TorqueConverterConnectionCriticalSpeedAnalysis",
        ) -> "_6580.ConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6580,
            )

            return self._parent._cast(_6580.ConnectionCriticalSpeedAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "TorqueConverterConnectionCriticalSpeedAnalysis._Cast_TorqueConverterConnectionCriticalSpeedAnalysis",
        ) -> "_7543.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "TorqueConverterConnectionCriticalSpeedAnalysis._Cast_TorqueConverterConnectionCriticalSpeedAnalysis",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "TorqueConverterConnectionCriticalSpeedAnalysis._Cast_TorqueConverterConnectionCriticalSpeedAnalysis",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterConnectionCriticalSpeedAnalysis._Cast_TorqueConverterConnectionCriticalSpeedAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterConnectionCriticalSpeedAnalysis._Cast_TorqueConverterConnectionCriticalSpeedAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def torque_converter_connection_critical_speed_analysis(
            self: "TorqueConverterConnectionCriticalSpeedAnalysis._Cast_TorqueConverterConnectionCriticalSpeedAnalysis",
        ) -> "TorqueConverterConnectionCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "TorqueConverterConnectionCriticalSpeedAnalysis._Cast_TorqueConverterConnectionCriticalSpeedAnalysis",
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
        instance_to_wrap: "TorqueConverterConnectionCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2354.TorqueConverterConnection":
        """mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6975.TorqueConverterConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterConnectionLoadCase

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
    ) -> "TorqueConverterConnectionCriticalSpeedAnalysis._Cast_TorqueConverterConnectionCriticalSpeedAnalysis":
        return self._Cast_TorqueConverterConnectionCriticalSpeedAnalysis(self)
