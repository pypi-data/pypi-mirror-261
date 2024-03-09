"""DesignEntity"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from PIL.Image import Image

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DESIGN_ENTITY = python_net_import("SMT.MastaAPI.SystemModel", "DesignEntity")

if TYPE_CHECKING:
    from mastapy.system_model import _2202
    from mastapy.utility.model_validation import _1796, _1795
    from mastapy.utility.scripting import _1743
    from mastapy.system_model.connections_and_sockets import (
        _2267,
        _2270,
        _2271,
        _2274,
        _2275,
        _2283,
        _2289,
        _2294,
        _2297,
    )
    from mastapy.system_model.connections_and_sockets.gears import (
        _2301,
        _2303,
        _2305,
        _2307,
        _2309,
        _2311,
        _2313,
        _2315,
        _2317,
        _2320,
        _2321,
        _2322,
        _2325,
        _2327,
        _2329,
        _2331,
        _2333,
    )
    from mastapy.system_model.connections_and_sockets.cycloidal import (
        _2337,
        _2340,
        _2343,
    )
    from mastapy.system_model.connections_and_sockets.couplings import (
        _2344,
        _2346,
        _2348,
        _2350,
        _2352,
        _2354,
    )
    from mastapy.system_model.part_model import (
        _2435,
        _2436,
        _2437,
        _2438,
        _2441,
        _2444,
        _2445,
        _2446,
        _2449,
        _2450,
        _2454,
        _2455,
        _2456,
        _2457,
        _2464,
        _2465,
        _2466,
        _2468,
        _2470,
        _2471,
        _2473,
        _2474,
        _2476,
        _2478,
        _2479,
        _2481,
    )
    from mastapy.system_model.part_model.shaft_model import _2484
    from mastapy.system_model.part_model.gears import (
        _2515,
        _2516,
        _2517,
        _2518,
        _2519,
        _2520,
        _2521,
        _2522,
        _2523,
        _2524,
        _2525,
        _2526,
        _2527,
        _2528,
        _2529,
        _2530,
        _2531,
        _2532,
        _2534,
        _2536,
        _2537,
        _2538,
        _2539,
        _2540,
        _2541,
        _2542,
        _2543,
        _2544,
        _2545,
        _2546,
        _2547,
        _2548,
        _2549,
        _2550,
        _2551,
        _2552,
        _2553,
        _2554,
        _2555,
        _2556,
    )
    from mastapy.system_model.part_model.cycloidal import _2570, _2571, _2572
    from mastapy.system_model.part_model.couplings import (
        _2578,
        _2580,
        _2581,
        _2583,
        _2584,
        _2585,
        _2586,
        _2588,
        _2589,
        _2590,
        _2591,
        _2592,
        _2598,
        _2599,
        _2600,
        _2602,
        _2603,
        _2604,
        _2606,
        _2607,
        _2608,
        _2609,
        _2610,
        _2612,
    )


__docformat__ = "restructuredtext en"
__all__ = ("DesignEntity",)


Self = TypeVar("Self", bound="DesignEntity")


class DesignEntity(_0.APIBase):
    """DesignEntity

    This is a mastapy class.
    """

    TYPE = _DESIGN_ENTITY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DesignEntity")

    class _Cast_DesignEntity:
        """Special nested class for casting DesignEntity to subclasses."""

        def __init__(self: "DesignEntity._Cast_DesignEntity", parent: "DesignEntity"):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2267.AbstractShaftToMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2267

            return self._parent._cast(_2267.AbstractShaftToMountableComponentConnection)

        @property
        def belt_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2270.BeltConnection":
            from mastapy.system_model.connections_and_sockets import _2270

            return self._parent._cast(_2270.BeltConnection)

        @property
        def coaxial_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2271.CoaxialConnection":
            from mastapy.system_model.connections_and_sockets import _2271

            return self._parent._cast(_2271.CoaxialConnection)

        @property
        def connection(self: "DesignEntity._Cast_DesignEntity") -> "_2274.Connection":
            from mastapy.system_model.connections_and_sockets import _2274

            return self._parent._cast(_2274.Connection)

        @property
        def cvt_belt_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2275.CVTBeltConnection":
            from mastapy.system_model.connections_and_sockets import _2275

            return self._parent._cast(_2275.CVTBeltConnection)

        @property
        def inter_mountable_component_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2283.InterMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2283

            return self._parent._cast(_2283.InterMountableComponentConnection)

        @property
        def planetary_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2289.PlanetaryConnection":
            from mastapy.system_model.connections_and_sockets import _2289

            return self._parent._cast(_2289.PlanetaryConnection)

        @property
        def rolling_ring_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2294.RollingRingConnection":
            from mastapy.system_model.connections_and_sockets import _2294

            return self._parent._cast(_2294.RollingRingConnection)

        @property
        def shaft_to_mountable_component_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2297.ShaftToMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2297

            return self._parent._cast(_2297.ShaftToMountableComponentConnection)

        @property
        def agma_gleason_conical_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2301.AGMAGleasonConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2301

            return self._parent._cast(_2301.AGMAGleasonConicalGearMesh)

        @property
        def bevel_differential_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2303.BevelDifferentialGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2303

            return self._parent._cast(_2303.BevelDifferentialGearMesh)

        @property
        def bevel_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2305.BevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2305

            return self._parent._cast(_2305.BevelGearMesh)

        @property
        def concept_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2307.ConceptGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2307

            return self._parent._cast(_2307.ConceptGearMesh)

        @property
        def conical_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2309.ConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2309

            return self._parent._cast(_2309.ConicalGearMesh)

        @property
        def cylindrical_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2311.CylindricalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2311

            return self._parent._cast(_2311.CylindricalGearMesh)

        @property
        def face_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2313.FaceGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2313

            return self._parent._cast(_2313.FaceGearMesh)

        @property
        def gear_mesh(self: "DesignEntity._Cast_DesignEntity") -> "_2315.GearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2315

            return self._parent._cast(_2315.GearMesh)

        @property
        def hypoid_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2317.HypoidGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2317

            return self._parent._cast(_2317.HypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2320.KlingelnbergCycloPalloidConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2320

            return self._parent._cast(_2320.KlingelnbergCycloPalloidConicalGearMesh)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2321.KlingelnbergCycloPalloidHypoidGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2321

            return self._parent._cast(_2321.KlingelnbergCycloPalloidHypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2322.KlingelnbergCycloPalloidSpiralBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2322

            return self._parent._cast(_2322.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        @property
        def spiral_bevel_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2325.SpiralBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2325

            return self._parent._cast(_2325.SpiralBevelGearMesh)

        @property
        def straight_bevel_diff_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2327.StraightBevelDiffGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2327

            return self._parent._cast(_2327.StraightBevelDiffGearMesh)

        @property
        def straight_bevel_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2329.StraightBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2329

            return self._parent._cast(_2329.StraightBevelGearMesh)

        @property
        def worm_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2331.WormGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2331

            return self._parent._cast(_2331.WormGearMesh)

        @property
        def zerol_bevel_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2333.ZerolBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2333

            return self._parent._cast(_2333.ZerolBevelGearMesh)

        @property
        def cycloidal_disc_central_bearing_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2337.CycloidalDiscCentralBearingConnection":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2337

            return self._parent._cast(_2337.CycloidalDiscCentralBearingConnection)

        @property
        def cycloidal_disc_planetary_bearing_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2340.CycloidalDiscPlanetaryBearingConnection":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2340

            return self._parent._cast(_2340.CycloidalDiscPlanetaryBearingConnection)

        @property
        def ring_pins_to_disc_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2343.RingPinsToDiscConnection":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2343

            return self._parent._cast(_2343.RingPinsToDiscConnection)

        @property
        def clutch_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2344.ClutchConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2344

            return self._parent._cast(_2344.ClutchConnection)

        @property
        def concept_coupling_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2346.ConceptCouplingConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2346

            return self._parent._cast(_2346.ConceptCouplingConnection)

        @property
        def coupling_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2348.CouplingConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2348

            return self._parent._cast(_2348.CouplingConnection)

        @property
        def part_to_part_shear_coupling_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2350.PartToPartShearCouplingConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2350

            return self._parent._cast(_2350.PartToPartShearCouplingConnection)

        @property
        def spring_damper_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2352.SpringDamperConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2352

            return self._parent._cast(_2352.SpringDamperConnection)

        @property
        def torque_converter_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2354.TorqueConverterConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2354

            return self._parent._cast(_2354.TorqueConverterConnection)

        @property
        def assembly(self: "DesignEntity._Cast_DesignEntity") -> "_2435.Assembly":
            from mastapy.system_model.part_model import _2435

            return self._parent._cast(_2435.Assembly)

        @property
        def abstract_assembly(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2436.AbstractAssembly":
            from mastapy.system_model.part_model import _2436

            return self._parent._cast(_2436.AbstractAssembly)

        @property
        def abstract_shaft(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2437.AbstractShaft":
            from mastapy.system_model.part_model import _2437

            return self._parent._cast(_2437.AbstractShaft)

        @property
        def abstract_shaft_or_housing(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2438.AbstractShaftOrHousing":
            from mastapy.system_model.part_model import _2438

            return self._parent._cast(_2438.AbstractShaftOrHousing)

        @property
        def bearing(self: "DesignEntity._Cast_DesignEntity") -> "_2441.Bearing":
            from mastapy.system_model.part_model import _2441

            return self._parent._cast(_2441.Bearing)

        @property
        def bolt(self: "DesignEntity._Cast_DesignEntity") -> "_2444.Bolt":
            from mastapy.system_model.part_model import _2444

            return self._parent._cast(_2444.Bolt)

        @property
        def bolted_joint(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2445.BoltedJoint":
            from mastapy.system_model.part_model import _2445

            return self._parent._cast(_2445.BoltedJoint)

        @property
        def component(self: "DesignEntity._Cast_DesignEntity") -> "_2446.Component":
            from mastapy.system_model.part_model import _2446

            return self._parent._cast(_2446.Component)

        @property
        def connector(self: "DesignEntity._Cast_DesignEntity") -> "_2449.Connector":
            from mastapy.system_model.part_model import _2449

            return self._parent._cast(_2449.Connector)

        @property
        def datum(self: "DesignEntity._Cast_DesignEntity") -> "_2450.Datum":
            from mastapy.system_model.part_model import _2450

            return self._parent._cast(_2450.Datum)

        @property
        def external_cad_model(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2454.ExternalCADModel":
            from mastapy.system_model.part_model import _2454

            return self._parent._cast(_2454.ExternalCADModel)

        @property
        def fe_part(self: "DesignEntity._Cast_DesignEntity") -> "_2455.FEPart":
            from mastapy.system_model.part_model import _2455

            return self._parent._cast(_2455.FEPart)

        @property
        def flexible_pin_assembly(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2456.FlexiblePinAssembly":
            from mastapy.system_model.part_model import _2456

            return self._parent._cast(_2456.FlexiblePinAssembly)

        @property
        def guide_dxf_model(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2457.GuideDxfModel":
            from mastapy.system_model.part_model import _2457

            return self._parent._cast(_2457.GuideDxfModel)

        @property
        def mass_disc(self: "DesignEntity._Cast_DesignEntity") -> "_2464.MassDisc":
            from mastapy.system_model.part_model import _2464

            return self._parent._cast(_2464.MassDisc)

        @property
        def measurement_component(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2465.MeasurementComponent":
            from mastapy.system_model.part_model import _2465

            return self._parent._cast(_2465.MeasurementComponent)

        @property
        def mountable_component(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2466.MountableComponent":
            from mastapy.system_model.part_model import _2466

            return self._parent._cast(_2466.MountableComponent)

        @property
        def oil_seal(self: "DesignEntity._Cast_DesignEntity") -> "_2468.OilSeal":
            from mastapy.system_model.part_model import _2468

            return self._parent._cast(_2468.OilSeal)

        @property
        def part(self: "DesignEntity._Cast_DesignEntity") -> "_2470.Part":
            from mastapy.system_model.part_model import _2470

            return self._parent._cast(_2470.Part)

        @property
        def planet_carrier(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2471.PlanetCarrier":
            from mastapy.system_model.part_model import _2471

            return self._parent._cast(_2471.PlanetCarrier)

        @property
        def point_load(self: "DesignEntity._Cast_DesignEntity") -> "_2473.PointLoad":
            from mastapy.system_model.part_model import _2473

            return self._parent._cast(_2473.PointLoad)

        @property
        def power_load(self: "DesignEntity._Cast_DesignEntity") -> "_2474.PowerLoad":
            from mastapy.system_model.part_model import _2474

            return self._parent._cast(_2474.PowerLoad)

        @property
        def root_assembly(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2476.RootAssembly":
            from mastapy.system_model.part_model import _2476

            return self._parent._cast(_2476.RootAssembly)

        @property
        def specialised_assembly(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2478.SpecialisedAssembly":
            from mastapy.system_model.part_model import _2478

            return self._parent._cast(_2478.SpecialisedAssembly)

        @property
        def unbalanced_mass(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2479.UnbalancedMass":
            from mastapy.system_model.part_model import _2479

            return self._parent._cast(_2479.UnbalancedMass)

        @property
        def virtual_component(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2481.VirtualComponent":
            from mastapy.system_model.part_model import _2481

            return self._parent._cast(_2481.VirtualComponent)

        @property
        def shaft(self: "DesignEntity._Cast_DesignEntity") -> "_2484.Shaft":
            from mastapy.system_model.part_model.shaft_model import _2484

            return self._parent._cast(_2484.Shaft)

        @property
        def agma_gleason_conical_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2515.AGMAGleasonConicalGear":
            from mastapy.system_model.part_model.gears import _2515

            return self._parent._cast(_2515.AGMAGleasonConicalGear)

        @property
        def agma_gleason_conical_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2516.AGMAGleasonConicalGearSet":
            from mastapy.system_model.part_model.gears import _2516

            return self._parent._cast(_2516.AGMAGleasonConicalGearSet)

        @property
        def bevel_differential_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2517.BevelDifferentialGear":
            from mastapy.system_model.part_model.gears import _2517

            return self._parent._cast(_2517.BevelDifferentialGear)

        @property
        def bevel_differential_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2518.BevelDifferentialGearSet":
            from mastapy.system_model.part_model.gears import _2518

            return self._parent._cast(_2518.BevelDifferentialGearSet)

        @property
        def bevel_differential_planet_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2519.BevelDifferentialPlanetGear":
            from mastapy.system_model.part_model.gears import _2519

            return self._parent._cast(_2519.BevelDifferentialPlanetGear)

        @property
        def bevel_differential_sun_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2520.BevelDifferentialSunGear":
            from mastapy.system_model.part_model.gears import _2520

            return self._parent._cast(_2520.BevelDifferentialSunGear)

        @property
        def bevel_gear(self: "DesignEntity._Cast_DesignEntity") -> "_2521.BevelGear":
            from mastapy.system_model.part_model.gears import _2521

            return self._parent._cast(_2521.BevelGear)

        @property
        def bevel_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2522.BevelGearSet":
            from mastapy.system_model.part_model.gears import _2522

            return self._parent._cast(_2522.BevelGearSet)

        @property
        def concept_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2523.ConceptGear":
            from mastapy.system_model.part_model.gears import _2523

            return self._parent._cast(_2523.ConceptGear)

        @property
        def concept_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2524.ConceptGearSet":
            from mastapy.system_model.part_model.gears import _2524

            return self._parent._cast(_2524.ConceptGearSet)

        @property
        def conical_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2525.ConicalGear":
            from mastapy.system_model.part_model.gears import _2525

            return self._parent._cast(_2525.ConicalGear)

        @property
        def conical_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2526.ConicalGearSet":
            from mastapy.system_model.part_model.gears import _2526

            return self._parent._cast(_2526.ConicalGearSet)

        @property
        def cylindrical_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2527.CylindricalGear":
            from mastapy.system_model.part_model.gears import _2527

            return self._parent._cast(_2527.CylindricalGear)

        @property
        def cylindrical_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2528.CylindricalGearSet":
            from mastapy.system_model.part_model.gears import _2528

            return self._parent._cast(_2528.CylindricalGearSet)

        @property
        def cylindrical_planet_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2529.CylindricalPlanetGear":
            from mastapy.system_model.part_model.gears import _2529

            return self._parent._cast(_2529.CylindricalPlanetGear)

        @property
        def face_gear(self: "DesignEntity._Cast_DesignEntity") -> "_2530.FaceGear":
            from mastapy.system_model.part_model.gears import _2530

            return self._parent._cast(_2530.FaceGear)

        @property
        def face_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2531.FaceGearSet":
            from mastapy.system_model.part_model.gears import _2531

            return self._parent._cast(_2531.FaceGearSet)

        @property
        def gear(self: "DesignEntity._Cast_DesignEntity") -> "_2532.Gear":
            from mastapy.system_model.part_model.gears import _2532

            return self._parent._cast(_2532.Gear)

        @property
        def gear_set(self: "DesignEntity._Cast_DesignEntity") -> "_2534.GearSet":
            from mastapy.system_model.part_model.gears import _2534

            return self._parent._cast(_2534.GearSet)

        @property
        def hypoid_gear(self: "DesignEntity._Cast_DesignEntity") -> "_2536.HypoidGear":
            from mastapy.system_model.part_model.gears import _2536

            return self._parent._cast(_2536.HypoidGear)

        @property
        def hypoid_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2537.HypoidGearSet":
            from mastapy.system_model.part_model.gears import _2537

            return self._parent._cast(_2537.HypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_conical_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2538.KlingelnbergCycloPalloidConicalGear":
            from mastapy.system_model.part_model.gears import _2538

            return self._parent._cast(_2538.KlingelnbergCycloPalloidConicalGear)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2539.KlingelnbergCycloPalloidConicalGearSet":
            from mastapy.system_model.part_model.gears import _2539

            return self._parent._cast(_2539.KlingelnbergCycloPalloidConicalGearSet)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2540.KlingelnbergCycloPalloidHypoidGear":
            from mastapy.system_model.part_model.gears import _2540

            return self._parent._cast(_2540.KlingelnbergCycloPalloidHypoidGear)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2541.KlingelnbergCycloPalloidHypoidGearSet":
            from mastapy.system_model.part_model.gears import _2541

            return self._parent._cast(_2541.KlingelnbergCycloPalloidHypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2542.KlingelnbergCycloPalloidSpiralBevelGear":
            from mastapy.system_model.part_model.gears import _2542

            return self._parent._cast(_2542.KlingelnbergCycloPalloidSpiralBevelGear)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2543.KlingelnbergCycloPalloidSpiralBevelGearSet":
            from mastapy.system_model.part_model.gears import _2543

            return self._parent._cast(_2543.KlingelnbergCycloPalloidSpiralBevelGearSet)

        @property
        def planetary_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2544.PlanetaryGearSet":
            from mastapy.system_model.part_model.gears import _2544

            return self._parent._cast(_2544.PlanetaryGearSet)

        @property
        def spiral_bevel_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2545.SpiralBevelGear":
            from mastapy.system_model.part_model.gears import _2545

            return self._parent._cast(_2545.SpiralBevelGear)

        @property
        def spiral_bevel_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2546.SpiralBevelGearSet":
            from mastapy.system_model.part_model.gears import _2546

            return self._parent._cast(_2546.SpiralBevelGearSet)

        @property
        def straight_bevel_diff_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2547.StraightBevelDiffGear":
            from mastapy.system_model.part_model.gears import _2547

            return self._parent._cast(_2547.StraightBevelDiffGear)

        @property
        def straight_bevel_diff_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2548.StraightBevelDiffGearSet":
            from mastapy.system_model.part_model.gears import _2548

            return self._parent._cast(_2548.StraightBevelDiffGearSet)

        @property
        def straight_bevel_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2549.StraightBevelGear":
            from mastapy.system_model.part_model.gears import _2549

            return self._parent._cast(_2549.StraightBevelGear)

        @property
        def straight_bevel_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2550.StraightBevelGearSet":
            from mastapy.system_model.part_model.gears import _2550

            return self._parent._cast(_2550.StraightBevelGearSet)

        @property
        def straight_bevel_planet_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2551.StraightBevelPlanetGear":
            from mastapy.system_model.part_model.gears import _2551

            return self._parent._cast(_2551.StraightBevelPlanetGear)

        @property
        def straight_bevel_sun_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2552.StraightBevelSunGear":
            from mastapy.system_model.part_model.gears import _2552

            return self._parent._cast(_2552.StraightBevelSunGear)

        @property
        def worm_gear(self: "DesignEntity._Cast_DesignEntity") -> "_2553.WormGear":
            from mastapy.system_model.part_model.gears import _2553

            return self._parent._cast(_2553.WormGear)

        @property
        def worm_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2554.WormGearSet":
            from mastapy.system_model.part_model.gears import _2554

            return self._parent._cast(_2554.WormGearSet)

        @property
        def zerol_bevel_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2555.ZerolBevelGear":
            from mastapy.system_model.part_model.gears import _2555

            return self._parent._cast(_2555.ZerolBevelGear)

        @property
        def zerol_bevel_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2556.ZerolBevelGearSet":
            from mastapy.system_model.part_model.gears import _2556

            return self._parent._cast(_2556.ZerolBevelGearSet)

        @property
        def cycloidal_assembly(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2570.CycloidalAssembly":
            from mastapy.system_model.part_model.cycloidal import _2570

            return self._parent._cast(_2570.CycloidalAssembly)

        @property
        def cycloidal_disc(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2571.CycloidalDisc":
            from mastapy.system_model.part_model.cycloidal import _2571

            return self._parent._cast(_2571.CycloidalDisc)

        @property
        def ring_pins(self: "DesignEntity._Cast_DesignEntity") -> "_2572.RingPins":
            from mastapy.system_model.part_model.cycloidal import _2572

            return self._parent._cast(_2572.RingPins)

        @property
        def belt_drive(self: "DesignEntity._Cast_DesignEntity") -> "_2578.BeltDrive":
            from mastapy.system_model.part_model.couplings import _2578

            return self._parent._cast(_2578.BeltDrive)

        @property
        def clutch(self: "DesignEntity._Cast_DesignEntity") -> "_2580.Clutch":
            from mastapy.system_model.part_model.couplings import _2580

            return self._parent._cast(_2580.Clutch)

        @property
        def clutch_half(self: "DesignEntity._Cast_DesignEntity") -> "_2581.ClutchHalf":
            from mastapy.system_model.part_model.couplings import _2581

            return self._parent._cast(_2581.ClutchHalf)

        @property
        def concept_coupling(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2583.ConceptCoupling":
            from mastapy.system_model.part_model.couplings import _2583

            return self._parent._cast(_2583.ConceptCoupling)

        @property
        def concept_coupling_half(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2584.ConceptCouplingHalf":
            from mastapy.system_model.part_model.couplings import _2584

            return self._parent._cast(_2584.ConceptCouplingHalf)

        @property
        def coupling(self: "DesignEntity._Cast_DesignEntity") -> "_2585.Coupling":
            from mastapy.system_model.part_model.couplings import _2585

            return self._parent._cast(_2585.Coupling)

        @property
        def coupling_half(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2586.CouplingHalf":
            from mastapy.system_model.part_model.couplings import _2586

            return self._parent._cast(_2586.CouplingHalf)

        @property
        def cvt(self: "DesignEntity._Cast_DesignEntity") -> "_2588.CVT":
            from mastapy.system_model.part_model.couplings import _2588

            return self._parent._cast(_2588.CVT)

        @property
        def cvt_pulley(self: "DesignEntity._Cast_DesignEntity") -> "_2589.CVTPulley":
            from mastapy.system_model.part_model.couplings import _2589

            return self._parent._cast(_2589.CVTPulley)

        @property
        def part_to_part_shear_coupling(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2590.PartToPartShearCoupling":
            from mastapy.system_model.part_model.couplings import _2590

            return self._parent._cast(_2590.PartToPartShearCoupling)

        @property
        def part_to_part_shear_coupling_half(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2591.PartToPartShearCouplingHalf":
            from mastapy.system_model.part_model.couplings import _2591

            return self._parent._cast(_2591.PartToPartShearCouplingHalf)

        @property
        def pulley(self: "DesignEntity._Cast_DesignEntity") -> "_2592.Pulley":
            from mastapy.system_model.part_model.couplings import _2592

            return self._parent._cast(_2592.Pulley)

        @property
        def rolling_ring(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2598.RollingRing":
            from mastapy.system_model.part_model.couplings import _2598

            return self._parent._cast(_2598.RollingRing)

        @property
        def rolling_ring_assembly(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2599.RollingRingAssembly":
            from mastapy.system_model.part_model.couplings import _2599

            return self._parent._cast(_2599.RollingRingAssembly)

        @property
        def shaft_hub_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2600.ShaftHubConnection":
            from mastapy.system_model.part_model.couplings import _2600

            return self._parent._cast(_2600.ShaftHubConnection)

        @property
        def spring_damper(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2602.SpringDamper":
            from mastapy.system_model.part_model.couplings import _2602

            return self._parent._cast(_2602.SpringDamper)

        @property
        def spring_damper_half(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2603.SpringDamperHalf":
            from mastapy.system_model.part_model.couplings import _2603

            return self._parent._cast(_2603.SpringDamperHalf)

        @property
        def synchroniser(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2604.Synchroniser":
            from mastapy.system_model.part_model.couplings import _2604

            return self._parent._cast(_2604.Synchroniser)

        @property
        def synchroniser_half(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2606.SynchroniserHalf":
            from mastapy.system_model.part_model.couplings import _2606

            return self._parent._cast(_2606.SynchroniserHalf)

        @property
        def synchroniser_part(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2607.SynchroniserPart":
            from mastapy.system_model.part_model.couplings import _2607

            return self._parent._cast(_2607.SynchroniserPart)

        @property
        def synchroniser_sleeve(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2608.SynchroniserSleeve":
            from mastapy.system_model.part_model.couplings import _2608

            return self._parent._cast(_2608.SynchroniserSleeve)

        @property
        def torque_converter(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2609.TorqueConverter":
            from mastapy.system_model.part_model.couplings import _2609

            return self._parent._cast(_2609.TorqueConverter)

        @property
        def torque_converter_pump(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2610.TorqueConverterPump":
            from mastapy.system_model.part_model.couplings import _2610

            return self._parent._cast(_2610.TorqueConverterPump)

        @property
        def torque_converter_turbine(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2612.TorqueConverterTurbine":
            from mastapy.system_model.part_model.couplings import _2612

            return self._parent._cast(_2612.TorqueConverterTurbine)

        @property
        def design_entity(self: "DesignEntity._Cast_DesignEntity") -> "DesignEntity":
            return self._parent

        def __getattr__(self: "DesignEntity._Cast_DesignEntity", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DesignEntity.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def comment(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Comment

        if temp is None:
            return ""

        return temp

    @comment.setter
    @enforce_parameter_types
    def comment(self: Self, value: "str"):
        self.wrapped.Comment = str(value) if value is not None else ""

    @property
    def id(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ID

        if temp is None:
            return ""

        return temp

    @property
    def icon(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Icon

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def small_icon(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SmallIcon

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def unique_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UniqueName

        if temp is None:
            return ""

        return temp

    @property
    def design_properties(self: Self) -> "_2202.Design":
        """mastapy.system_model.Design

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DesignProperties

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def all_design_entities(self: Self) -> "List[DesignEntity]":
        """List[mastapy.system_model.DesignEntity]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllDesignEntities

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def all_status_errors(self: Self) -> "List[_1796.StatusItem]":
        """List[mastapy.utility.model_validation.StatusItem]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllStatusErrors

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def status(self: Self) -> "_1795.Status":
        """mastapy.utility.model_validation.Status

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Status

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def user_specified_data(self: Self) -> "_1743.UserSpecifiedData":
        """mastapy.utility.scripting.UserSpecifiedData

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UserSpecifiedData

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    def delete(self: Self):
        """Method does not return."""
        self.wrapped.Delete()

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(self: Self) -> "DesignEntity._Cast_DesignEntity":
        return self._Cast_DesignEntity(self)
