"""CycloidalDiscCentralBearingConnectionDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6303
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "CycloidalDiscCentralBearingConnectionDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2337
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6378,
        _6282,
        _6314,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7542,
        _7543,
        _7540,
    )
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionDynamicAnalysis",)


Self = TypeVar("Self", bound="CycloidalDiscCentralBearingConnectionDynamicAnalysis")


class CycloidalDiscCentralBearingConnectionDynamicAnalysis(
    _6303.CoaxialConnectionDynamicAnalysis
):
    """CycloidalDiscCentralBearingConnectionDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CycloidalDiscCentralBearingConnectionDynamicAnalysis"
    )

    class _Cast_CycloidalDiscCentralBearingConnectionDynamicAnalysis:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionDynamicAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionDynamicAnalysis._Cast_CycloidalDiscCentralBearingConnectionDynamicAnalysis",
            parent: "CycloidalDiscCentralBearingConnectionDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def coaxial_connection_dynamic_analysis(
            self: "CycloidalDiscCentralBearingConnectionDynamicAnalysis._Cast_CycloidalDiscCentralBearingConnectionDynamicAnalysis",
        ) -> "_6303.CoaxialConnectionDynamicAnalysis":
            return self._parent._cast(_6303.CoaxialConnectionDynamicAnalysis)

        @property
        def shaft_to_mountable_component_connection_dynamic_analysis(
            self: "CycloidalDiscCentralBearingConnectionDynamicAnalysis._Cast_CycloidalDiscCentralBearingConnectionDynamicAnalysis",
        ) -> "_6378.ShaftToMountableComponentConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6378

            return self._parent._cast(
                _6378.ShaftToMountableComponentConnectionDynamicAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_dynamic_analysis(
            self: "CycloidalDiscCentralBearingConnectionDynamicAnalysis._Cast_CycloidalDiscCentralBearingConnectionDynamicAnalysis",
        ) -> "_6282.AbstractShaftToMountableComponentConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6282

            return self._parent._cast(
                _6282.AbstractShaftToMountableComponentConnectionDynamicAnalysis
            )

        @property
        def connection_dynamic_analysis(
            self: "CycloidalDiscCentralBearingConnectionDynamicAnalysis._Cast_CycloidalDiscCentralBearingConnectionDynamicAnalysis",
        ) -> "_6314.ConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6314

            return self._parent._cast(_6314.ConnectionDynamicAnalysis)

        @property
        def connection_fe_analysis(
            self: "CycloidalDiscCentralBearingConnectionDynamicAnalysis._Cast_CycloidalDiscCentralBearingConnectionDynamicAnalysis",
        ) -> "_7542.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CycloidalDiscCentralBearingConnectionDynamicAnalysis._Cast_CycloidalDiscCentralBearingConnectionDynamicAnalysis",
        ) -> "_7543.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CycloidalDiscCentralBearingConnectionDynamicAnalysis._Cast_CycloidalDiscCentralBearingConnectionDynamicAnalysis",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CycloidalDiscCentralBearingConnectionDynamicAnalysis._Cast_CycloidalDiscCentralBearingConnectionDynamicAnalysis",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscCentralBearingConnectionDynamicAnalysis._Cast_CycloidalDiscCentralBearingConnectionDynamicAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionDynamicAnalysis._Cast_CycloidalDiscCentralBearingConnectionDynamicAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_dynamic_analysis(
            self: "CycloidalDiscCentralBearingConnectionDynamicAnalysis._Cast_CycloidalDiscCentralBearingConnectionDynamicAnalysis",
        ) -> "CycloidalDiscCentralBearingConnectionDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionDynamicAnalysis._Cast_CycloidalDiscCentralBearingConnectionDynamicAnalysis",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2337.CycloidalDiscCentralBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscCentralBearingConnection

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
    ) -> "CycloidalDiscCentralBearingConnectionDynamicAnalysis._Cast_CycloidalDiscCentralBearingConnectionDynamicAnalysis":
        return self._Cast_CycloidalDiscCentralBearingConnectionDynamicAnalysis(self)
