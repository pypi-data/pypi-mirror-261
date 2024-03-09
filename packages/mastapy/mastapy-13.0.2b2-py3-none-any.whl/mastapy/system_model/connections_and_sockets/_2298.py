"""Socket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.python_net import python_net_import
from mastapy import _0
from mastapy._internal.cast_exception import CastException

_COMPONENT = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Component")
_SOCKET = python_net_import("SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "Socket")

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2446, _2447
    from mastapy.system_model.connections_and_sockets import (
        _2274,
        _2268,
        _2269,
        _2276,
        _2278,
        _2280,
        _2281,
        _2282,
        _2284,
        _2285,
        _2286,
        _2287,
        _2288,
        _2290,
        _2291,
        _2292,
        _2295,
        _2296,
    )
    from mastapy.system_model.connections_and_sockets.gears import (
        _2302,
        _2304,
        _2306,
        _2308,
        _2310,
        _2312,
        _2314,
        _2316,
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
    from mastapy.system_model.connections_and_sockets.cycloidal import (
        _2335,
        _2336,
        _2338,
        _2339,
        _2341,
        _2342,
    )
    from mastapy.system_model.connections_and_sockets.couplings import (
        _2345,
        _2347,
        _2349,
        _2351,
        _2353,
        _2355,
        _2356,
    )


__docformat__ = "restructuredtext en"
__all__ = ("Socket",)


Self = TypeVar("Self", bound="Socket")


class Socket(_0.APIBase):
    """Socket

    This is a mastapy class.
    """

    TYPE = _SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Socket")

    class _Cast_Socket:
        """Special nested class for casting Socket to subclasses."""

        def __init__(self: "Socket._Cast_Socket", parent: "Socket"):
            self._parent = parent

        @property
        def bearing_inner_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2268.BearingInnerSocket":
            from mastapy.system_model.connections_and_sockets import _2268

            return self._parent._cast(_2268.BearingInnerSocket)

        @property
        def bearing_outer_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2269.BearingOuterSocket":
            from mastapy.system_model.connections_and_sockets import _2269

            return self._parent._cast(_2269.BearingOuterSocket)

        @property
        def cvt_pulley_socket(self: "Socket._Cast_Socket") -> "_2276.CVTPulleySocket":
            from mastapy.system_model.connections_and_sockets import _2276

            return self._parent._cast(_2276.CVTPulleySocket)

        @property
        def cylindrical_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2278.CylindricalSocket":
            from mastapy.system_model.connections_and_sockets import _2278

            return self._parent._cast(_2278.CylindricalSocket)

        @property
        def electric_machine_stator_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2280.ElectricMachineStatorSocket":
            from mastapy.system_model.connections_and_sockets import _2280

            return self._parent._cast(_2280.ElectricMachineStatorSocket)

        @property
        def inner_shaft_socket(self: "Socket._Cast_Socket") -> "_2281.InnerShaftSocket":
            from mastapy.system_model.connections_and_sockets import _2281

            return self._parent._cast(_2281.InnerShaftSocket)

        @property
        def inner_shaft_socket_base(
            self: "Socket._Cast_Socket",
        ) -> "_2282.InnerShaftSocketBase":
            from mastapy.system_model.connections_and_sockets import _2282

            return self._parent._cast(_2282.InnerShaftSocketBase)

        @property
        def mountable_component_inner_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2284.MountableComponentInnerSocket":
            from mastapy.system_model.connections_and_sockets import _2284

            return self._parent._cast(_2284.MountableComponentInnerSocket)

        @property
        def mountable_component_outer_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2285.MountableComponentOuterSocket":
            from mastapy.system_model.connections_and_sockets import _2285

            return self._parent._cast(_2285.MountableComponentOuterSocket)

        @property
        def mountable_component_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2286.MountableComponentSocket":
            from mastapy.system_model.connections_and_sockets import _2286

            return self._parent._cast(_2286.MountableComponentSocket)

        @property
        def outer_shaft_socket(self: "Socket._Cast_Socket") -> "_2287.OuterShaftSocket":
            from mastapy.system_model.connections_and_sockets import _2287

            return self._parent._cast(_2287.OuterShaftSocket)

        @property
        def outer_shaft_socket_base(
            self: "Socket._Cast_Socket",
        ) -> "_2288.OuterShaftSocketBase":
            from mastapy.system_model.connections_and_sockets import _2288

            return self._parent._cast(_2288.OuterShaftSocketBase)

        @property
        def planetary_socket(self: "Socket._Cast_Socket") -> "_2290.PlanetarySocket":
            from mastapy.system_model.connections_and_sockets import _2290

            return self._parent._cast(_2290.PlanetarySocket)

        @property
        def planetary_socket_base(
            self: "Socket._Cast_Socket",
        ) -> "_2291.PlanetarySocketBase":
            from mastapy.system_model.connections_and_sockets import _2291

            return self._parent._cast(_2291.PlanetarySocketBase)

        @property
        def pulley_socket(self: "Socket._Cast_Socket") -> "_2292.PulleySocket":
            from mastapy.system_model.connections_and_sockets import _2292

            return self._parent._cast(_2292.PulleySocket)

        @property
        def rolling_ring_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2295.RollingRingSocket":
            from mastapy.system_model.connections_and_sockets import _2295

            return self._parent._cast(_2295.RollingRingSocket)

        @property
        def shaft_socket(self: "Socket._Cast_Socket") -> "_2296.ShaftSocket":
            from mastapy.system_model.connections_and_sockets import _2296

            return self._parent._cast(_2296.ShaftSocket)

        @property
        def agma_gleason_conical_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2302.AGMAGleasonConicalGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2302

            return self._parent._cast(_2302.AGMAGleasonConicalGearTeethSocket)

        @property
        def bevel_differential_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2304.BevelDifferentialGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2304

            return self._parent._cast(_2304.BevelDifferentialGearTeethSocket)

        @property
        def bevel_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2306.BevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2306

            return self._parent._cast(_2306.BevelGearTeethSocket)

        @property
        def concept_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2308.ConceptGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2308

            return self._parent._cast(_2308.ConceptGearTeethSocket)

        @property
        def conical_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2310.ConicalGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2310

            return self._parent._cast(_2310.ConicalGearTeethSocket)

        @property
        def cylindrical_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2312.CylindricalGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2312

            return self._parent._cast(_2312.CylindricalGearTeethSocket)

        @property
        def face_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2314.FaceGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2314

            return self._parent._cast(_2314.FaceGearTeethSocket)

        @property
        def gear_teeth_socket(self: "Socket._Cast_Socket") -> "_2316.GearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2316

            return self._parent._cast(_2316.GearTeethSocket)

        @property
        def hypoid_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2318.HypoidGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2318

            return self._parent._cast(_2318.HypoidGearTeethSocket)

        @property
        def klingelnberg_conical_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2319.KlingelnbergConicalGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2319

            return self._parent._cast(_2319.KlingelnbergConicalGearTeethSocket)

        @property
        def klingelnberg_hypoid_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2323.KlingelnbergHypoidGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2323

            return self._parent._cast(_2323.KlingelnbergHypoidGearTeethSocket)

        @property
        def klingelnberg_spiral_bevel_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2324.KlingelnbergSpiralBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2324

            return self._parent._cast(_2324.KlingelnbergSpiralBevelGearTeethSocket)

        @property
        def spiral_bevel_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2326.SpiralBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2326

            return self._parent._cast(_2326.SpiralBevelGearTeethSocket)

        @property
        def straight_bevel_diff_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2328.StraightBevelDiffGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2328

            return self._parent._cast(_2328.StraightBevelDiffGearTeethSocket)

        @property
        def straight_bevel_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2330.StraightBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2330

            return self._parent._cast(_2330.StraightBevelGearTeethSocket)

        @property
        def worm_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2332.WormGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2332

            return self._parent._cast(_2332.WormGearTeethSocket)

        @property
        def zerol_bevel_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2334.ZerolBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2334

            return self._parent._cast(_2334.ZerolBevelGearTeethSocket)

        @property
        def cycloidal_disc_axial_left_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2335.CycloidalDiscAxialLeftSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2335

            return self._parent._cast(_2335.CycloidalDiscAxialLeftSocket)

        @property
        def cycloidal_disc_axial_right_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2336.CycloidalDiscAxialRightSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2336

            return self._parent._cast(_2336.CycloidalDiscAxialRightSocket)

        @property
        def cycloidal_disc_inner_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2338.CycloidalDiscInnerSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2338

            return self._parent._cast(_2338.CycloidalDiscInnerSocket)

        @property
        def cycloidal_disc_outer_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2339.CycloidalDiscOuterSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2339

            return self._parent._cast(_2339.CycloidalDiscOuterSocket)

        @property
        def cycloidal_disc_planetary_bearing_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2341.CycloidalDiscPlanetaryBearingSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2341

            return self._parent._cast(_2341.CycloidalDiscPlanetaryBearingSocket)

        @property
        def ring_pins_socket(self: "Socket._Cast_Socket") -> "_2342.RingPinsSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2342

            return self._parent._cast(_2342.RingPinsSocket)

        @property
        def clutch_socket(self: "Socket._Cast_Socket") -> "_2345.ClutchSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2345

            return self._parent._cast(_2345.ClutchSocket)

        @property
        def concept_coupling_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2347.ConceptCouplingSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2347

            return self._parent._cast(_2347.ConceptCouplingSocket)

        @property
        def coupling_socket(self: "Socket._Cast_Socket") -> "_2349.CouplingSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2349

            return self._parent._cast(_2349.CouplingSocket)

        @property
        def part_to_part_shear_coupling_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2351.PartToPartShearCouplingSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2351

            return self._parent._cast(_2351.PartToPartShearCouplingSocket)

        @property
        def spring_damper_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2353.SpringDamperSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2353

            return self._parent._cast(_2353.SpringDamperSocket)

        @property
        def torque_converter_pump_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2355.TorqueConverterPumpSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2355

            return self._parent._cast(_2355.TorqueConverterPumpSocket)

        @property
        def torque_converter_turbine_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2356.TorqueConverterTurbineSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2356

            return self._parent._cast(_2356.TorqueConverterTurbineSocket)

        @property
        def socket(self: "Socket._Cast_Socket") -> "Socket":
            return self._parent

        def __getattr__(self: "Socket._Cast_Socket", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Socket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def connected_components(self: Self) -> "List[_2446.Component]":
        """List[mastapy.system_model.part_model.Component]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectedComponents

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connections(self: Self) -> "List[_2274.Connection]":
        """List[mastapy.system_model.connections_and_sockets.Connection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Connections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def owner(self: Self) -> "_2446.Component":
        """mastapy.system_model.part_model.Component

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Owner

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @enforce_parameter_types
    def connect_to(
        self: Self, component: "_2446.Component"
    ) -> "_2447.ComponentsConnectedResult":
        """mastapy.system_model.part_model.ComponentsConnectedResult

        Args:
            component (mastapy.system_model.part_model.Component)
        """
        method_result = self.wrapped.ConnectTo.Overloads[_COMPONENT](
            component.wrapped if component else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def connect_to_socket(
        self: Self, socket: "Socket"
    ) -> "_2447.ComponentsConnectedResult":
        """mastapy.system_model.part_model.ComponentsConnectedResult

        Args:
            socket (mastapy.system_model.connections_and_sockets.Socket)
        """
        method_result = self.wrapped.ConnectTo.Overloads[_SOCKET](
            socket.wrapped if socket else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def connection_to(self: Self, socket: "Socket") -> "_2274.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Args:
            socket (mastapy.system_model.connections_and_sockets.Socket)
        """
        method_result = self.wrapped.ConnectionTo(socket.wrapped if socket else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def get_possible_sockets_to_connect_to(
        self: Self, component_to_connect_to: "_2446.Component"
    ) -> "List[Socket]":
        """List[mastapy.system_model.connections_and_sockets.Socket]

        Args:
            component_to_connect_to (mastapy.system_model.part_model.Component)
        """
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.GetPossibleSocketsToConnectTo(
                component_to_connect_to.wrapped if component_to_connect_to else None
            )
        )

    @property
    def cast_to(self: Self) -> "Socket._Cast_Socket":
        return self._Cast_Socket(self)
