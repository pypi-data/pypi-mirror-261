"""ConicalGearMesh"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.system_model.connections_and_sockets.gears import _2315
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "ConicalGearMesh"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import (
        _2301,
        _2303,
        _2305,
        _2317,
        _2320,
        _2321,
        _2322,
        _2325,
        _2327,
        _2329,
        _2333,
    )
    from mastapy.system_model.connections_and_sockets import _2283, _2274
    from mastapy.system_model import _2205


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMesh",)


Self = TypeVar("Self", bound="ConicalGearMesh")


class ConicalGearMesh(_2315.GearMesh):
    """ConicalGearMesh

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearMesh")

    class _Cast_ConicalGearMesh:
        """Special nested class for casting ConicalGearMesh to subclasses."""

        def __init__(
            self: "ConicalGearMesh._Cast_ConicalGearMesh", parent: "ConicalGearMesh"
        ):
            self._parent = parent

        @property
        def gear_mesh(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ) -> "_2315.GearMesh":
            return self._parent._cast(_2315.GearMesh)

        @property
        def inter_mountable_component_connection(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ) -> "_2283.InterMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2283

            return self._parent._cast(_2283.InterMountableComponentConnection)

        @property
        def connection(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ) -> "_2274.Connection":
            from mastapy.system_model.connections_and_sockets import _2274

            return self._parent._cast(_2274.Connection)

        @property
        def design_entity(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ) -> "_2205.DesignEntity":
            from mastapy.system_model import _2205

            return self._parent._cast(_2205.DesignEntity)

        @property
        def agma_gleason_conical_gear_mesh(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ) -> "_2301.AGMAGleasonConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2301

            return self._parent._cast(_2301.AGMAGleasonConicalGearMesh)

        @property
        def bevel_differential_gear_mesh(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ) -> "_2303.BevelDifferentialGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2303

            return self._parent._cast(_2303.BevelDifferentialGearMesh)

        @property
        def bevel_gear_mesh(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ) -> "_2305.BevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2305

            return self._parent._cast(_2305.BevelGearMesh)

        @property
        def hypoid_gear_mesh(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ) -> "_2317.HypoidGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2317

            return self._parent._cast(_2317.HypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ) -> "_2320.KlingelnbergCycloPalloidConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2320

            return self._parent._cast(_2320.KlingelnbergCycloPalloidConicalGearMesh)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ) -> "_2321.KlingelnbergCycloPalloidHypoidGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2321

            return self._parent._cast(_2321.KlingelnbergCycloPalloidHypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ) -> "_2322.KlingelnbergCycloPalloidSpiralBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2322

            return self._parent._cast(_2322.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        @property
        def spiral_bevel_gear_mesh(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ) -> "_2325.SpiralBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2325

            return self._parent._cast(_2325.SpiralBevelGearMesh)

        @property
        def straight_bevel_diff_gear_mesh(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ) -> "_2327.StraightBevelDiffGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2327

            return self._parent._cast(_2327.StraightBevelDiffGearMesh)

        @property
        def straight_bevel_gear_mesh(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ) -> "_2329.StraightBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2329

            return self._parent._cast(_2329.StraightBevelGearMesh)

        @property
        def zerol_bevel_gear_mesh(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ) -> "_2333.ZerolBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2333

            return self._parent._cast(_2333.ZerolBevelGearMesh)

        @property
        def conical_gear_mesh(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ) -> "ConicalGearMesh":
            return self._parent

        def __getattr__(self: "ConicalGearMesh._Cast_ConicalGearMesh", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def crowning(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Crowning

        if temp is None:
            return 0.0

        return temp

    @crowning.setter
    @enforce_parameter_types
    def crowning(self: Self, value: "float"):
        self.wrapped.Crowning = float(value) if value is not None else 0.0

    @property
    def pinion_drop_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PinionDropAngle

        if temp is None:
            return 0.0

        return temp

    @pinion_drop_angle.setter
    @enforce_parameter_types
    def pinion_drop_angle(self: Self, value: "float"):
        self.wrapped.PinionDropAngle = float(value) if value is not None else 0.0

    @property
    def wheel_drop_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WheelDropAngle

        if temp is None:
            return 0.0

        return temp

    @wheel_drop_angle.setter
    @enforce_parameter_types
    def wheel_drop_angle(self: Self, value: "float"):
        self.wrapped.WheelDropAngle = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "ConicalGearMesh._Cast_ConicalGearMesh":
        return self._Cast_ConicalGearMesh(self)
