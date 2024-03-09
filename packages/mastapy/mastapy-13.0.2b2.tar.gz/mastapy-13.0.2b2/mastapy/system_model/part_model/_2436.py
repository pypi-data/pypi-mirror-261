"""AbstractAssembly"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.part_model import _2470
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "AbstractAssembly"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2446, _2435, _2445, _2456, _2476, _2478
    from mastapy.system_model.part_model.gears import (
        _2516,
        _2518,
        _2522,
        _2524,
        _2526,
        _2528,
        _2531,
        _2534,
        _2537,
        _2539,
        _2541,
        _2543,
        _2544,
        _2546,
        _2548,
        _2550,
        _2554,
        _2556,
    )
    from mastapy.system_model.part_model.cycloidal import _2570
    from mastapy.system_model.part_model.couplings import (
        _2578,
        _2580,
        _2583,
        _2585,
        _2588,
        _2590,
        _2599,
        _2602,
        _2604,
        _2609,
    )
    from mastapy.system_model import _2205


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssembly",)


Self = TypeVar("Self", bound="AbstractAssembly")


class AbstractAssembly(_2470.Part):
    """AbstractAssembly

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractAssembly")

    class _Cast_AbstractAssembly:
        """Special nested class for casting AbstractAssembly to subclasses."""

        def __init__(
            self: "AbstractAssembly._Cast_AbstractAssembly", parent: "AbstractAssembly"
        ):
            self._parent = parent

        @property
        def part(self: "AbstractAssembly._Cast_AbstractAssembly") -> "_2470.Part":
            return self._parent._cast(_2470.Part)

        @property
        def design_entity(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2205.DesignEntity":
            from mastapy.system_model import _2205

            return self._parent._cast(_2205.DesignEntity)

        @property
        def assembly(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2435.Assembly":
            from mastapy.system_model.part_model import _2435

            return self._parent._cast(_2435.Assembly)

        @property
        def bolted_joint(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2445.BoltedJoint":
            from mastapy.system_model.part_model import _2445

            return self._parent._cast(_2445.BoltedJoint)

        @property
        def flexible_pin_assembly(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2456.FlexiblePinAssembly":
            from mastapy.system_model.part_model import _2456

            return self._parent._cast(_2456.FlexiblePinAssembly)

        @property
        def root_assembly(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2476.RootAssembly":
            from mastapy.system_model.part_model import _2476

            return self._parent._cast(_2476.RootAssembly)

        @property
        def specialised_assembly(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2478.SpecialisedAssembly":
            from mastapy.system_model.part_model import _2478

            return self._parent._cast(_2478.SpecialisedAssembly)

        @property
        def agma_gleason_conical_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2516.AGMAGleasonConicalGearSet":
            from mastapy.system_model.part_model.gears import _2516

            return self._parent._cast(_2516.AGMAGleasonConicalGearSet)

        @property
        def bevel_differential_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2518.BevelDifferentialGearSet":
            from mastapy.system_model.part_model.gears import _2518

            return self._parent._cast(_2518.BevelDifferentialGearSet)

        @property
        def bevel_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2522.BevelGearSet":
            from mastapy.system_model.part_model.gears import _2522

            return self._parent._cast(_2522.BevelGearSet)

        @property
        def concept_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2524.ConceptGearSet":
            from mastapy.system_model.part_model.gears import _2524

            return self._parent._cast(_2524.ConceptGearSet)

        @property
        def conical_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2526.ConicalGearSet":
            from mastapy.system_model.part_model.gears import _2526

            return self._parent._cast(_2526.ConicalGearSet)

        @property
        def cylindrical_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2528.CylindricalGearSet":
            from mastapy.system_model.part_model.gears import _2528

            return self._parent._cast(_2528.CylindricalGearSet)

        @property
        def face_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2531.FaceGearSet":
            from mastapy.system_model.part_model.gears import _2531

            return self._parent._cast(_2531.FaceGearSet)

        @property
        def gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2534.GearSet":
            from mastapy.system_model.part_model.gears import _2534

            return self._parent._cast(_2534.GearSet)

        @property
        def hypoid_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2537.HypoidGearSet":
            from mastapy.system_model.part_model.gears import _2537

            return self._parent._cast(_2537.HypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2539.KlingelnbergCycloPalloidConicalGearSet":
            from mastapy.system_model.part_model.gears import _2539

            return self._parent._cast(_2539.KlingelnbergCycloPalloidConicalGearSet)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2541.KlingelnbergCycloPalloidHypoidGearSet":
            from mastapy.system_model.part_model.gears import _2541

            return self._parent._cast(_2541.KlingelnbergCycloPalloidHypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2543.KlingelnbergCycloPalloidSpiralBevelGearSet":
            from mastapy.system_model.part_model.gears import _2543

            return self._parent._cast(_2543.KlingelnbergCycloPalloidSpiralBevelGearSet)

        @property
        def planetary_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2544.PlanetaryGearSet":
            from mastapy.system_model.part_model.gears import _2544

            return self._parent._cast(_2544.PlanetaryGearSet)

        @property
        def spiral_bevel_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2546.SpiralBevelGearSet":
            from mastapy.system_model.part_model.gears import _2546

            return self._parent._cast(_2546.SpiralBevelGearSet)

        @property
        def straight_bevel_diff_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2548.StraightBevelDiffGearSet":
            from mastapy.system_model.part_model.gears import _2548

            return self._parent._cast(_2548.StraightBevelDiffGearSet)

        @property
        def straight_bevel_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2550.StraightBevelGearSet":
            from mastapy.system_model.part_model.gears import _2550

            return self._parent._cast(_2550.StraightBevelGearSet)

        @property
        def worm_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2554.WormGearSet":
            from mastapy.system_model.part_model.gears import _2554

            return self._parent._cast(_2554.WormGearSet)

        @property
        def zerol_bevel_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2556.ZerolBevelGearSet":
            from mastapy.system_model.part_model.gears import _2556

            return self._parent._cast(_2556.ZerolBevelGearSet)

        @property
        def cycloidal_assembly(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2570.CycloidalAssembly":
            from mastapy.system_model.part_model.cycloidal import _2570

            return self._parent._cast(_2570.CycloidalAssembly)

        @property
        def belt_drive(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2578.BeltDrive":
            from mastapy.system_model.part_model.couplings import _2578

            return self._parent._cast(_2578.BeltDrive)

        @property
        def clutch(self: "AbstractAssembly._Cast_AbstractAssembly") -> "_2580.Clutch":
            from mastapy.system_model.part_model.couplings import _2580

            return self._parent._cast(_2580.Clutch)

        @property
        def concept_coupling(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2583.ConceptCoupling":
            from mastapy.system_model.part_model.couplings import _2583

            return self._parent._cast(_2583.ConceptCoupling)

        @property
        def coupling(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2585.Coupling":
            from mastapy.system_model.part_model.couplings import _2585

            return self._parent._cast(_2585.Coupling)

        @property
        def cvt(self: "AbstractAssembly._Cast_AbstractAssembly") -> "_2588.CVT":
            from mastapy.system_model.part_model.couplings import _2588

            return self._parent._cast(_2588.CVT)

        @property
        def part_to_part_shear_coupling(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2590.PartToPartShearCoupling":
            from mastapy.system_model.part_model.couplings import _2590

            return self._parent._cast(_2590.PartToPartShearCoupling)

        @property
        def rolling_ring_assembly(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2599.RollingRingAssembly":
            from mastapy.system_model.part_model.couplings import _2599

            return self._parent._cast(_2599.RollingRingAssembly)

        @property
        def spring_damper(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2602.SpringDamper":
            from mastapy.system_model.part_model.couplings import _2602

            return self._parent._cast(_2602.SpringDamper)

        @property
        def synchroniser(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2604.Synchroniser":
            from mastapy.system_model.part_model.couplings import _2604

            return self._parent._cast(_2604.Synchroniser)

        @property
        def torque_converter(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2609.TorqueConverter":
            from mastapy.system_model.part_model.couplings import _2609

            return self._parent._cast(_2609.TorqueConverter)

        @property
        def abstract_assembly(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "AbstractAssembly":
            return self._parent

        def __getattr__(self: "AbstractAssembly._Cast_AbstractAssembly", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractAssembly.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mass_of_assembly(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassOfAssembly

        if temp is None:
            return 0.0

        return temp

    @property
    def components_with_unknown_mass_properties(self: Self) -> "List[_2446.Component]":
        """List[mastapy.system_model.part_model.Component]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentsWithUnknownMassProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def components_with_zero_mass_properties(self: Self) -> "List[_2446.Component]":
        """List[mastapy.system_model.part_model.Component]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentsWithZeroMassProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "AbstractAssembly._Cast_AbstractAssembly":
        return self._Cast_AbstractAssembly(self)
