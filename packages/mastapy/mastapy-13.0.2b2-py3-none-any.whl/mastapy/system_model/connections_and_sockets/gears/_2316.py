"""GearTeethSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets import _2298
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_TEETH_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "GearTeethSocket"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import (
        _2302,
        _2304,
        _2306,
        _2308,
        _2310,
        _2314,
        _2318,
        _2319,
        _2323,
        _2324,
        _2326,
        _2328,
        _2330,
        _2332,
        _2334,
    )


__docformat__ = "restructuredtext en"
__all__ = ("GearTeethSocket",)


Self = TypeVar("Self", bound="GearTeethSocket")


class GearTeethSocket(_2298.Socket):
    """GearTeethSocket

    This is a mastapy class.
    """

    TYPE = _GEAR_TEETH_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearTeethSocket")

    class _Cast_GearTeethSocket:
        """Special nested class for casting GearTeethSocket to subclasses."""

        def __init__(
            self: "GearTeethSocket._Cast_GearTeethSocket", parent: "GearTeethSocket"
        ):
            self._parent = parent

        @property
        def socket(self: "GearTeethSocket._Cast_GearTeethSocket") -> "_2298.Socket":
            return self._parent._cast(_2298.Socket)

        @property
        def agma_gleason_conical_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2302.AGMAGleasonConicalGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2302

            return self._parent._cast(_2302.AGMAGleasonConicalGearTeethSocket)

        @property
        def bevel_differential_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2304.BevelDifferentialGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2304

            return self._parent._cast(_2304.BevelDifferentialGearTeethSocket)

        @property
        def bevel_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2306.BevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2306

            return self._parent._cast(_2306.BevelGearTeethSocket)

        @property
        def concept_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2308.ConceptGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2308

            return self._parent._cast(_2308.ConceptGearTeethSocket)

        @property
        def conical_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2310.ConicalGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2310

            return self._parent._cast(_2310.ConicalGearTeethSocket)

        @property
        def face_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2314.FaceGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2314

            return self._parent._cast(_2314.FaceGearTeethSocket)

        @property
        def hypoid_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2318.HypoidGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2318

            return self._parent._cast(_2318.HypoidGearTeethSocket)

        @property
        def klingelnberg_conical_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2319.KlingelnbergConicalGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2319

            return self._parent._cast(_2319.KlingelnbergConicalGearTeethSocket)

        @property
        def klingelnberg_hypoid_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2323.KlingelnbergHypoidGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2323

            return self._parent._cast(_2323.KlingelnbergHypoidGearTeethSocket)

        @property
        def klingelnberg_spiral_bevel_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2324.KlingelnbergSpiralBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2324

            return self._parent._cast(_2324.KlingelnbergSpiralBevelGearTeethSocket)

        @property
        def spiral_bevel_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2326.SpiralBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2326

            return self._parent._cast(_2326.SpiralBevelGearTeethSocket)

        @property
        def straight_bevel_diff_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2328.StraightBevelDiffGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2328

            return self._parent._cast(_2328.StraightBevelDiffGearTeethSocket)

        @property
        def straight_bevel_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2330.StraightBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2330

            return self._parent._cast(_2330.StraightBevelGearTeethSocket)

        @property
        def worm_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2332.WormGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2332

            return self._parent._cast(_2332.WormGearTeethSocket)

        @property
        def zerol_bevel_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2334.ZerolBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2334

            return self._parent._cast(_2334.ZerolBevelGearTeethSocket)

        @property
        def gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "GearTeethSocket":
            return self._parent

        def __getattr__(self: "GearTeethSocket._Cast_GearTeethSocket", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearTeethSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "GearTeethSocket._Cast_GearTeethSocket":
        return self._Cast_GearTeethSocket(self)
