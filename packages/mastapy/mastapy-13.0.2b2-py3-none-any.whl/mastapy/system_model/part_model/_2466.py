"""MountableComponent"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.system_model.part_model import _2446
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "MountableComponent"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import (
        _2437,
        _2447,
        _2441,
        _2449,
        _2464,
        _2465,
        _2468,
        _2471,
        _2473,
        _2474,
        _2479,
        _2481,
        _2470,
    )
    from mastapy.system_model.connections_and_sockets import _2274, _2278, _2271
    from mastapy.system_model.part_model.gears import (
        _2515,
        _2517,
        _2519,
        _2520,
        _2521,
        _2523,
        _2525,
        _2527,
        _2529,
        _2530,
        _2532,
        _2536,
        _2538,
        _2540,
        _2542,
        _2545,
        _2547,
        _2549,
        _2551,
        _2552,
        _2553,
        _2555,
    )
    from mastapy.system_model.part_model.cycloidal import _2572
    from mastapy.system_model.part_model.couplings import (
        _2581,
        _2584,
        _2586,
        _2589,
        _2591,
        _2592,
        _2598,
        _2600,
        _2603,
        _2606,
        _2607,
        _2608,
        _2610,
        _2612,
    )
    from mastapy.system_model import _2205


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponent",)


Self = TypeVar("Self", bound="MountableComponent")


class MountableComponent(_2446.Component):
    """MountableComponent

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MountableComponent")

    class _Cast_MountableComponent:
        """Special nested class for casting MountableComponent to subclasses."""

        def __init__(
            self: "MountableComponent._Cast_MountableComponent",
            parent: "MountableComponent",
        ):
            self._parent = parent

        @property
        def component(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2446.Component":
            return self._parent._cast(_2446.Component)

        @property
        def part(self: "MountableComponent._Cast_MountableComponent") -> "_2470.Part":
            from mastapy.system_model.part_model import _2470

            return self._parent._cast(_2470.Part)

        @property
        def design_entity(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2205.DesignEntity":
            from mastapy.system_model import _2205

            return self._parent._cast(_2205.DesignEntity)

        @property
        def bearing(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2441.Bearing":
            from mastapy.system_model.part_model import _2441

            return self._parent._cast(_2441.Bearing)

        @property
        def connector(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2449.Connector":
            from mastapy.system_model.part_model import _2449

            return self._parent._cast(_2449.Connector)

        @property
        def mass_disc(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2464.MassDisc":
            from mastapy.system_model.part_model import _2464

            return self._parent._cast(_2464.MassDisc)

        @property
        def measurement_component(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2465.MeasurementComponent":
            from mastapy.system_model.part_model import _2465

            return self._parent._cast(_2465.MeasurementComponent)

        @property
        def oil_seal(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2468.OilSeal":
            from mastapy.system_model.part_model import _2468

            return self._parent._cast(_2468.OilSeal)

        @property
        def planet_carrier(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2471.PlanetCarrier":
            from mastapy.system_model.part_model import _2471

            return self._parent._cast(_2471.PlanetCarrier)

        @property
        def point_load(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2473.PointLoad":
            from mastapy.system_model.part_model import _2473

            return self._parent._cast(_2473.PointLoad)

        @property
        def power_load(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2474.PowerLoad":
            from mastapy.system_model.part_model import _2474

            return self._parent._cast(_2474.PowerLoad)

        @property
        def unbalanced_mass(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2479.UnbalancedMass":
            from mastapy.system_model.part_model import _2479

            return self._parent._cast(_2479.UnbalancedMass)

        @property
        def virtual_component(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2481.VirtualComponent":
            from mastapy.system_model.part_model import _2481

            return self._parent._cast(_2481.VirtualComponent)

        @property
        def agma_gleason_conical_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2515.AGMAGleasonConicalGear":
            from mastapy.system_model.part_model.gears import _2515

            return self._parent._cast(_2515.AGMAGleasonConicalGear)

        @property
        def bevel_differential_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2517.BevelDifferentialGear":
            from mastapy.system_model.part_model.gears import _2517

            return self._parent._cast(_2517.BevelDifferentialGear)

        @property
        def bevel_differential_planet_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2519.BevelDifferentialPlanetGear":
            from mastapy.system_model.part_model.gears import _2519

            return self._parent._cast(_2519.BevelDifferentialPlanetGear)

        @property
        def bevel_differential_sun_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2520.BevelDifferentialSunGear":
            from mastapy.system_model.part_model.gears import _2520

            return self._parent._cast(_2520.BevelDifferentialSunGear)

        @property
        def bevel_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2521.BevelGear":
            from mastapy.system_model.part_model.gears import _2521

            return self._parent._cast(_2521.BevelGear)

        @property
        def concept_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2523.ConceptGear":
            from mastapy.system_model.part_model.gears import _2523

            return self._parent._cast(_2523.ConceptGear)

        @property
        def conical_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2525.ConicalGear":
            from mastapy.system_model.part_model.gears import _2525

            return self._parent._cast(_2525.ConicalGear)

        @property
        def cylindrical_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2527.CylindricalGear":
            from mastapy.system_model.part_model.gears import _2527

            return self._parent._cast(_2527.CylindricalGear)

        @property
        def cylindrical_planet_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2529.CylindricalPlanetGear":
            from mastapy.system_model.part_model.gears import _2529

            return self._parent._cast(_2529.CylindricalPlanetGear)

        @property
        def face_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2530.FaceGear":
            from mastapy.system_model.part_model.gears import _2530

            return self._parent._cast(_2530.FaceGear)

        @property
        def gear(self: "MountableComponent._Cast_MountableComponent") -> "_2532.Gear":
            from mastapy.system_model.part_model.gears import _2532

            return self._parent._cast(_2532.Gear)

        @property
        def hypoid_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2536.HypoidGear":
            from mastapy.system_model.part_model.gears import _2536

            return self._parent._cast(_2536.HypoidGear)

        @property
        def klingelnberg_cyclo_palloid_conical_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2538.KlingelnbergCycloPalloidConicalGear":
            from mastapy.system_model.part_model.gears import _2538

            return self._parent._cast(_2538.KlingelnbergCycloPalloidConicalGear)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2540.KlingelnbergCycloPalloidHypoidGear":
            from mastapy.system_model.part_model.gears import _2540

            return self._parent._cast(_2540.KlingelnbergCycloPalloidHypoidGear)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2542.KlingelnbergCycloPalloidSpiralBevelGear":
            from mastapy.system_model.part_model.gears import _2542

            return self._parent._cast(_2542.KlingelnbergCycloPalloidSpiralBevelGear)

        @property
        def spiral_bevel_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2545.SpiralBevelGear":
            from mastapy.system_model.part_model.gears import _2545

            return self._parent._cast(_2545.SpiralBevelGear)

        @property
        def straight_bevel_diff_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2547.StraightBevelDiffGear":
            from mastapy.system_model.part_model.gears import _2547

            return self._parent._cast(_2547.StraightBevelDiffGear)

        @property
        def straight_bevel_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2549.StraightBevelGear":
            from mastapy.system_model.part_model.gears import _2549

            return self._parent._cast(_2549.StraightBevelGear)

        @property
        def straight_bevel_planet_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2551.StraightBevelPlanetGear":
            from mastapy.system_model.part_model.gears import _2551

            return self._parent._cast(_2551.StraightBevelPlanetGear)

        @property
        def straight_bevel_sun_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2552.StraightBevelSunGear":
            from mastapy.system_model.part_model.gears import _2552

            return self._parent._cast(_2552.StraightBevelSunGear)

        @property
        def worm_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2553.WormGear":
            from mastapy.system_model.part_model.gears import _2553

            return self._parent._cast(_2553.WormGear)

        @property
        def zerol_bevel_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2555.ZerolBevelGear":
            from mastapy.system_model.part_model.gears import _2555

            return self._parent._cast(_2555.ZerolBevelGear)

        @property
        def ring_pins(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2572.RingPins":
            from mastapy.system_model.part_model.cycloidal import _2572

            return self._parent._cast(_2572.RingPins)

        @property
        def clutch_half(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2581.ClutchHalf":
            from mastapy.system_model.part_model.couplings import _2581

            return self._parent._cast(_2581.ClutchHalf)

        @property
        def concept_coupling_half(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2584.ConceptCouplingHalf":
            from mastapy.system_model.part_model.couplings import _2584

            return self._parent._cast(_2584.ConceptCouplingHalf)

        @property
        def coupling_half(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2586.CouplingHalf":
            from mastapy.system_model.part_model.couplings import _2586

            return self._parent._cast(_2586.CouplingHalf)

        @property
        def cvt_pulley(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2589.CVTPulley":
            from mastapy.system_model.part_model.couplings import _2589

            return self._parent._cast(_2589.CVTPulley)

        @property
        def part_to_part_shear_coupling_half(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2591.PartToPartShearCouplingHalf":
            from mastapy.system_model.part_model.couplings import _2591

            return self._parent._cast(_2591.PartToPartShearCouplingHalf)

        @property
        def pulley(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2592.Pulley":
            from mastapy.system_model.part_model.couplings import _2592

            return self._parent._cast(_2592.Pulley)

        @property
        def rolling_ring(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2598.RollingRing":
            from mastapy.system_model.part_model.couplings import _2598

            return self._parent._cast(_2598.RollingRing)

        @property
        def shaft_hub_connection(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2600.ShaftHubConnection":
            from mastapy.system_model.part_model.couplings import _2600

            return self._parent._cast(_2600.ShaftHubConnection)

        @property
        def spring_damper_half(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2603.SpringDamperHalf":
            from mastapy.system_model.part_model.couplings import _2603

            return self._parent._cast(_2603.SpringDamperHalf)

        @property
        def synchroniser_half(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2606.SynchroniserHalf":
            from mastapy.system_model.part_model.couplings import _2606

            return self._parent._cast(_2606.SynchroniserHalf)

        @property
        def synchroniser_part(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2607.SynchroniserPart":
            from mastapy.system_model.part_model.couplings import _2607

            return self._parent._cast(_2607.SynchroniserPart)

        @property
        def synchroniser_sleeve(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2608.SynchroniserSleeve":
            from mastapy.system_model.part_model.couplings import _2608

            return self._parent._cast(_2608.SynchroniserSleeve)

        @property
        def torque_converter_pump(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2610.TorqueConverterPump":
            from mastapy.system_model.part_model.couplings import _2610

            return self._parent._cast(_2610.TorqueConverterPump)

        @property
        def torque_converter_turbine(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2612.TorqueConverterTurbine":
            from mastapy.system_model.part_model.couplings import _2612

            return self._parent._cast(_2612.TorqueConverterTurbine)

        @property
        def mountable_component(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "MountableComponent":
            return self._parent

        def __getattr__(self: "MountableComponent._Cast_MountableComponent", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MountableComponent.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rotation_about_axis(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RotationAboutAxis

        if temp is None:
            return 0.0

        return temp

    @rotation_about_axis.setter
    @enforce_parameter_types
    def rotation_about_axis(self: Self, value: "float"):
        self.wrapped.RotationAboutAxis = float(value) if value is not None else 0.0

    @property
    def inner_component(self: Self) -> "_2437.AbstractShaft":
        """mastapy.system_model.part_model.AbstractShaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerComponent

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_connection(self: Self) -> "_2274.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerConnection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_socket(self: Self) -> "_2278.CylindricalSocket":
        """mastapy.system_model.connections_and_sockets.CylindricalSocket

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerSocket

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def is_mounted(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsMounted

        if temp is None:
            return False

        return temp

    @enforce_parameter_types
    def mount_on(
        self: Self, shaft: "_2437.AbstractShaft", offset: "float" = float("nan")
    ) -> "_2271.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Args:
            shaft (mastapy.system_model.part_model.AbstractShaft)
            offset (float, optional)
        """
        offset = float(offset)
        method_result = self.wrapped.MountOn(
            shaft.wrapped if shaft else None, offset if offset else 0.0
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def try_mount_on(
        self: Self, shaft: "_2437.AbstractShaft", offset: "float" = float("nan")
    ) -> "_2447.ComponentsConnectedResult":
        """mastapy.system_model.part_model.ComponentsConnectedResult

        Args:
            shaft (mastapy.system_model.part_model.AbstractShaft)
            offset (float, optional)
        """
        offset = float(offset)
        method_result = self.wrapped.TryMountOn(
            shaft.wrapped if shaft else None, offset if offset else 0.0
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "MountableComponent._Cast_MountableComponent":
        return self._Cast_MountableComponent(self)
