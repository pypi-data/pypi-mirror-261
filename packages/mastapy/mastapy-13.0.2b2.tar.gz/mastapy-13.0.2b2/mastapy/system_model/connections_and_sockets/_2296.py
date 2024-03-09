"""ShaftSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets import _2278
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "ShaftSocket"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import (
        _2281,
        _2282,
        _2287,
        _2288,
        _2298,
    )
    from mastapy.system_model.connections_and_sockets.cycloidal import (
        _2335,
        _2336,
        _2338,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ShaftSocket",)


Self = TypeVar("Self", bound="ShaftSocket")


class ShaftSocket(_2278.CylindricalSocket):
    """ShaftSocket

    This is a mastapy class.
    """

    TYPE = _SHAFT_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftSocket")

    class _Cast_ShaftSocket:
        """Special nested class for casting ShaftSocket to subclasses."""

        def __init__(self: "ShaftSocket._Cast_ShaftSocket", parent: "ShaftSocket"):
            self._parent = parent

        @property
        def cylindrical_socket(
            self: "ShaftSocket._Cast_ShaftSocket",
        ) -> "_2278.CylindricalSocket":
            return self._parent._cast(_2278.CylindricalSocket)

        @property
        def socket(self: "ShaftSocket._Cast_ShaftSocket") -> "_2298.Socket":
            from mastapy.system_model.connections_and_sockets import _2298

            return self._parent._cast(_2298.Socket)

        @property
        def inner_shaft_socket(
            self: "ShaftSocket._Cast_ShaftSocket",
        ) -> "_2281.InnerShaftSocket":
            from mastapy.system_model.connections_and_sockets import _2281

            return self._parent._cast(_2281.InnerShaftSocket)

        @property
        def inner_shaft_socket_base(
            self: "ShaftSocket._Cast_ShaftSocket",
        ) -> "_2282.InnerShaftSocketBase":
            from mastapy.system_model.connections_and_sockets import _2282

            return self._parent._cast(_2282.InnerShaftSocketBase)

        @property
        def outer_shaft_socket(
            self: "ShaftSocket._Cast_ShaftSocket",
        ) -> "_2287.OuterShaftSocket":
            from mastapy.system_model.connections_and_sockets import _2287

            return self._parent._cast(_2287.OuterShaftSocket)

        @property
        def outer_shaft_socket_base(
            self: "ShaftSocket._Cast_ShaftSocket",
        ) -> "_2288.OuterShaftSocketBase":
            from mastapy.system_model.connections_and_sockets import _2288

            return self._parent._cast(_2288.OuterShaftSocketBase)

        @property
        def cycloidal_disc_axial_left_socket(
            self: "ShaftSocket._Cast_ShaftSocket",
        ) -> "_2335.CycloidalDiscAxialLeftSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2335

            return self._parent._cast(_2335.CycloidalDiscAxialLeftSocket)

        @property
        def cycloidal_disc_axial_right_socket(
            self: "ShaftSocket._Cast_ShaftSocket",
        ) -> "_2336.CycloidalDiscAxialRightSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2336

            return self._parent._cast(_2336.CycloidalDiscAxialRightSocket)

        @property
        def cycloidal_disc_inner_socket(
            self: "ShaftSocket._Cast_ShaftSocket",
        ) -> "_2338.CycloidalDiscInnerSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2338

            return self._parent._cast(_2338.CycloidalDiscInnerSocket)

        @property
        def shaft_socket(self: "ShaftSocket._Cast_ShaftSocket") -> "ShaftSocket":
            return self._parent

        def __getattr__(self: "ShaftSocket._Cast_ShaftSocket", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ShaftSocket._Cast_ShaftSocket":
        return self._Cast_ShaftSocket(self)
