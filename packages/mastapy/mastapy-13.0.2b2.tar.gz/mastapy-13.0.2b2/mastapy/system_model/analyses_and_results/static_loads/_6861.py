"""CycloidalDiscCentralBearingConnectionLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6839
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CycloidalDiscCentralBearingConnectionLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2337
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6954,
        _6812,
        _6852,
    )
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionLoadCase",)


Self = TypeVar("Self", bound="CycloidalDiscCentralBearingConnectionLoadCase")


class CycloidalDiscCentralBearingConnectionLoadCase(_6839.CoaxialConnectionLoadCase):
    """CycloidalDiscCentralBearingConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_LOAD_CASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CycloidalDiscCentralBearingConnectionLoadCase"
    )

    class _Cast_CycloidalDiscCentralBearingConnectionLoadCase:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionLoadCase to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionLoadCase._Cast_CycloidalDiscCentralBearingConnectionLoadCase",
            parent: "CycloidalDiscCentralBearingConnectionLoadCase",
        ):
            self._parent = parent

        @property
        def coaxial_connection_load_case(
            self: "CycloidalDiscCentralBearingConnectionLoadCase._Cast_CycloidalDiscCentralBearingConnectionLoadCase",
        ) -> "_6839.CoaxialConnectionLoadCase":
            return self._parent._cast(_6839.CoaxialConnectionLoadCase)

        @property
        def shaft_to_mountable_component_connection_load_case(
            self: "CycloidalDiscCentralBearingConnectionLoadCase._Cast_CycloidalDiscCentralBearingConnectionLoadCase",
        ) -> "_6954.ShaftToMountableComponentConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6954

            return self._parent._cast(_6954.ShaftToMountableComponentConnectionLoadCase)

        @property
        def abstract_shaft_to_mountable_component_connection_load_case(
            self: "CycloidalDiscCentralBearingConnectionLoadCase._Cast_CycloidalDiscCentralBearingConnectionLoadCase",
        ) -> "_6812.AbstractShaftToMountableComponentConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6812

            return self._parent._cast(
                _6812.AbstractShaftToMountableComponentConnectionLoadCase
            )

        @property
        def connection_load_case(
            self: "CycloidalDiscCentralBearingConnectionLoadCase._Cast_CycloidalDiscCentralBearingConnectionLoadCase",
        ) -> "_6852.ConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6852

            return self._parent._cast(_6852.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "CycloidalDiscCentralBearingConnectionLoadCase._Cast_CycloidalDiscCentralBearingConnectionLoadCase",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscCentralBearingConnectionLoadCase._Cast_CycloidalDiscCentralBearingConnectionLoadCase",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionLoadCase._Cast_CycloidalDiscCentralBearingConnectionLoadCase",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_load_case(
            self: "CycloidalDiscCentralBearingConnectionLoadCase._Cast_CycloidalDiscCentralBearingConnectionLoadCase",
        ) -> "CycloidalDiscCentralBearingConnectionLoadCase":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionLoadCase._Cast_CycloidalDiscCentralBearingConnectionLoadCase",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionLoadCase.TYPE",
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
    ) -> "CycloidalDiscCentralBearingConnectionLoadCase._Cast_CycloidalDiscCentralBearingConnectionLoadCase":
        return self._Cast_CycloidalDiscCentralBearingConnectionLoadCase(self)
