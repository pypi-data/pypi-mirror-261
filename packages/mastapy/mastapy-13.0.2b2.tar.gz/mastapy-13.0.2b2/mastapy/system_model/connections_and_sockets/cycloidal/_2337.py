"""CycloidalDiscCentralBearingConnection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets import _2271
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal",
    "CycloidalDiscCentralBearingConnection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2297, _2267, _2274
    from mastapy.system_model import _2205


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnection",)


Self = TypeVar("Self", bound="CycloidalDiscCentralBearingConnection")


class CycloidalDiscCentralBearingConnection(_2271.CoaxialConnection):
    """CycloidalDiscCentralBearingConnection

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CycloidalDiscCentralBearingConnection"
    )

    class _Cast_CycloidalDiscCentralBearingConnection:
        """Special nested class for casting CycloidalDiscCentralBearingConnection to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnection._Cast_CycloidalDiscCentralBearingConnection",
            parent: "CycloidalDiscCentralBearingConnection",
        ):
            self._parent = parent

        @property
        def coaxial_connection(
            self: "CycloidalDiscCentralBearingConnection._Cast_CycloidalDiscCentralBearingConnection",
        ) -> "_2271.CoaxialConnection":
            return self._parent._cast(_2271.CoaxialConnection)

        @property
        def shaft_to_mountable_component_connection(
            self: "CycloidalDiscCentralBearingConnection._Cast_CycloidalDiscCentralBearingConnection",
        ) -> "_2297.ShaftToMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2297

            return self._parent._cast(_2297.ShaftToMountableComponentConnection)

        @property
        def abstract_shaft_to_mountable_component_connection(
            self: "CycloidalDiscCentralBearingConnection._Cast_CycloidalDiscCentralBearingConnection",
        ) -> "_2267.AbstractShaftToMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2267

            return self._parent._cast(_2267.AbstractShaftToMountableComponentConnection)

        @property
        def connection(
            self: "CycloidalDiscCentralBearingConnection._Cast_CycloidalDiscCentralBearingConnection",
        ) -> "_2274.Connection":
            from mastapy.system_model.connections_and_sockets import _2274

            return self._parent._cast(_2274.Connection)

        @property
        def design_entity(
            self: "CycloidalDiscCentralBearingConnection._Cast_CycloidalDiscCentralBearingConnection",
        ) -> "_2205.DesignEntity":
            from mastapy.system_model import _2205

            return self._parent._cast(_2205.DesignEntity)

        @property
        def cycloidal_disc_central_bearing_connection(
            self: "CycloidalDiscCentralBearingConnection._Cast_CycloidalDiscCentralBearingConnection",
        ) -> "CycloidalDiscCentralBearingConnection":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnection._Cast_CycloidalDiscCentralBearingConnection",
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
        self: Self, instance_to_wrap: "CycloidalDiscCentralBearingConnection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscCentralBearingConnection._Cast_CycloidalDiscCentralBearingConnection":
        return self._Cast_CycloidalDiscCentralBearingConnection(self)
