"""ConicalGearMeshDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.gear_designs import _950
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Conical", "ConicalGearMeshDesign"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.bevel import _1188, _1185, _1189, _1182
    from mastapy.gears.gear_designs.zerol_bevel import _954
    from mastapy.gears.gear_designs.straight_bevel import _963
    from mastapy.gears.gear_designs.straight_bevel_diff import _967
    from mastapy.gears.gear_designs.spiral_bevel import _971
    from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _975
    from mastapy.gears.gear_designs.klingelnberg_hypoid import _979
    from mastapy.gears.gear_designs.klingelnberg_conical import _983
    from mastapy.gears.gear_designs.hypoid import _987
    from mastapy.gears.gear_designs.agma_gleason_conical import _1195
    from mastapy.gears.gear_designs import _949


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshDesign",)


Self = TypeVar("Self", bound="ConicalGearMeshDesign")


class ConicalGearMeshDesign(_950.GearMeshDesign):
    """ConicalGearMeshDesign

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearMeshDesign")

    class _Cast_ConicalGearMeshDesign:
        """Special nested class for casting ConicalGearMeshDesign to subclasses."""

        def __init__(
            self: "ConicalGearMeshDesign._Cast_ConicalGearMeshDesign",
            parent: "ConicalGearMeshDesign",
        ):
            self._parent = parent

        @property
        def gear_mesh_design(
            self: "ConicalGearMeshDesign._Cast_ConicalGearMeshDesign",
        ) -> "_950.GearMeshDesign":
            return self._parent._cast(_950.GearMeshDesign)

        @property
        def gear_design_component(
            self: "ConicalGearMeshDesign._Cast_ConicalGearMeshDesign",
        ) -> "_949.GearDesignComponent":
            from mastapy.gears.gear_designs import _949

            return self._parent._cast(_949.GearDesignComponent)

        @property
        def zerol_bevel_gear_mesh_design(
            self: "ConicalGearMeshDesign._Cast_ConicalGearMeshDesign",
        ) -> "_954.ZerolBevelGearMeshDesign":
            from mastapy.gears.gear_designs.zerol_bevel import _954

            return self._parent._cast(_954.ZerolBevelGearMeshDesign)

        @property
        def straight_bevel_gear_mesh_design(
            self: "ConicalGearMeshDesign._Cast_ConicalGearMeshDesign",
        ) -> "_963.StraightBevelGearMeshDesign":
            from mastapy.gears.gear_designs.straight_bevel import _963

            return self._parent._cast(_963.StraightBevelGearMeshDesign)

        @property
        def straight_bevel_diff_gear_mesh_design(
            self: "ConicalGearMeshDesign._Cast_ConicalGearMeshDesign",
        ) -> "_967.StraightBevelDiffGearMeshDesign":
            from mastapy.gears.gear_designs.straight_bevel_diff import _967

            return self._parent._cast(_967.StraightBevelDiffGearMeshDesign)

        @property
        def spiral_bevel_gear_mesh_design(
            self: "ConicalGearMeshDesign._Cast_ConicalGearMeshDesign",
        ) -> "_971.SpiralBevelGearMeshDesign":
            from mastapy.gears.gear_designs.spiral_bevel import _971

            return self._parent._cast(_971.SpiralBevelGearMeshDesign)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_design(
            self: "ConicalGearMeshDesign._Cast_ConicalGearMeshDesign",
        ) -> "_975.KlingelnbergCycloPalloidSpiralBevelGearMeshDesign":
            from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _975

            return self._parent._cast(
                _975.KlingelnbergCycloPalloidSpiralBevelGearMeshDesign
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_design(
            self: "ConicalGearMeshDesign._Cast_ConicalGearMeshDesign",
        ) -> "_979.KlingelnbergCycloPalloidHypoidGearMeshDesign":
            from mastapy.gears.gear_designs.klingelnberg_hypoid import _979

            return self._parent._cast(_979.KlingelnbergCycloPalloidHypoidGearMeshDesign)

        @property
        def klingelnberg_conical_gear_mesh_design(
            self: "ConicalGearMeshDesign._Cast_ConicalGearMeshDesign",
        ) -> "_983.KlingelnbergConicalGearMeshDesign":
            from mastapy.gears.gear_designs.klingelnberg_conical import _983

            return self._parent._cast(_983.KlingelnbergConicalGearMeshDesign)

        @property
        def hypoid_gear_mesh_design(
            self: "ConicalGearMeshDesign._Cast_ConicalGearMeshDesign",
        ) -> "_987.HypoidGearMeshDesign":
            from mastapy.gears.gear_designs.hypoid import _987

            return self._parent._cast(_987.HypoidGearMeshDesign)

        @property
        def bevel_gear_mesh_design(
            self: "ConicalGearMeshDesign._Cast_ConicalGearMeshDesign",
        ) -> "_1182.BevelGearMeshDesign":
            from mastapy.gears.gear_designs.bevel import _1182

            return self._parent._cast(_1182.BevelGearMeshDesign)

        @property
        def agma_gleason_conical_gear_mesh_design(
            self: "ConicalGearMeshDesign._Cast_ConicalGearMeshDesign",
        ) -> "_1195.AGMAGleasonConicalGearMeshDesign":
            from mastapy.gears.gear_designs.agma_gleason_conical import _1195

            return self._parent._cast(_1195.AGMAGleasonConicalGearMeshDesign)

        @property
        def conical_gear_mesh_design(
            self: "ConicalGearMeshDesign._Cast_ConicalGearMeshDesign",
        ) -> "ConicalGearMeshDesign":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshDesign._Cast_ConicalGearMeshDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearMeshDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def driven_machine_characteristic(
        self: Self,
    ) -> "_1188.MachineCharacteristicAGMAKlingelnberg":
        """mastapy.gears.gear_designs.bevel.MachineCharacteristicAGMAKlingelnberg"""
        temp = self.wrapped.DrivenMachineCharacteristic

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Bevel.MachineCharacteristicAGMAKlingelnberg",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.bevel._1188",
            "MachineCharacteristicAGMAKlingelnberg",
        )(value)

    @driven_machine_characteristic.setter
    @enforce_parameter_types
    def driven_machine_characteristic(
        self: Self, value: "_1188.MachineCharacteristicAGMAKlingelnberg"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Bevel.MachineCharacteristicAGMAKlingelnberg",
        )
        self.wrapped.DrivenMachineCharacteristic = value

    @property
    def driven_machine_characteristic_gleason(
        self: Self,
    ) -> "_1185.DrivenMachineCharacteristicGleason":
        """mastapy.gears.gear_designs.bevel.DrivenMachineCharacteristicGleason"""
        temp = self.wrapped.DrivenMachineCharacteristicGleason

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Bevel.DrivenMachineCharacteristicGleason",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.bevel._1185",
            "DrivenMachineCharacteristicGleason",
        )(value)

    @driven_machine_characteristic_gleason.setter
    @enforce_parameter_types
    def driven_machine_characteristic_gleason(
        self: Self, value: "_1185.DrivenMachineCharacteristicGleason"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Bevel.DrivenMachineCharacteristicGleason",
        )
        self.wrapped.DrivenMachineCharacteristicGleason = value

    @property
    def maximum_normal_backlash(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalBacklash

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_normal_backlash(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumNormalBacklash

        if temp is None:
            return 0.0

        return temp

    @property
    def overload_factor(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.OverloadFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @overload_factor.setter
    @enforce_parameter_types
    def overload_factor(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.OverloadFactor = value

    @property
    def pinion_full_circle_edge_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionFullCircleEdgeRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def prime_mover_characteristic(
        self: Self,
    ) -> "_1188.MachineCharacteristicAGMAKlingelnberg":
        """mastapy.gears.gear_designs.bevel.MachineCharacteristicAGMAKlingelnberg"""
        temp = self.wrapped.PrimeMoverCharacteristic

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Bevel.MachineCharacteristicAGMAKlingelnberg",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.bevel._1188",
            "MachineCharacteristicAGMAKlingelnberg",
        )(value)

    @prime_mover_characteristic.setter
    @enforce_parameter_types
    def prime_mover_characteristic(
        self: Self, value: "_1188.MachineCharacteristicAGMAKlingelnberg"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Bevel.MachineCharacteristicAGMAKlingelnberg",
        )
        self.wrapped.PrimeMoverCharacteristic = value

    @property
    def prime_mover_characteristic_gleason(
        self: Self,
    ) -> "_1189.PrimeMoverCharacteristicGleason":
        """mastapy.gears.gear_designs.bevel.PrimeMoverCharacteristicGleason"""
        temp = self.wrapped.PrimeMoverCharacteristicGleason

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Bevel.PrimeMoverCharacteristicGleason"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.bevel._1189", "PrimeMoverCharacteristicGleason"
        )(value)

    @prime_mover_characteristic_gleason.setter
    @enforce_parameter_types
    def prime_mover_characteristic_gleason(
        self: Self, value: "_1189.PrimeMoverCharacteristicGleason"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Bevel.PrimeMoverCharacteristicGleason",
        )
        self.wrapped.PrimeMoverCharacteristicGleason = value

    @property
    def shaft_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ShaftAngle

        if temp is None:
            return 0.0

        return temp

    @shaft_angle.setter
    @enforce_parameter_types
    def shaft_angle(self: Self, value: "float"):
        self.wrapped.ShaftAngle = float(value) if value is not None else 0.0

    @property
    def specified_backlash_range_max(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SpecifiedBacklashRangeMax

        if temp is None:
            return 0.0

        return temp

    @specified_backlash_range_max.setter
    @enforce_parameter_types
    def specified_backlash_range_max(self: Self, value: "float"):
        self.wrapped.SpecifiedBacklashRangeMax = (
            float(value) if value is not None else 0.0
        )

    @property
    def specified_backlash_range_min(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SpecifiedBacklashRangeMin

        if temp is None:
            return 0.0

        return temp

    @specified_backlash_range_min.setter
    @enforce_parameter_types
    def specified_backlash_range_min(self: Self, value: "float"):
        self.wrapped.SpecifiedBacklashRangeMin = (
            float(value) if value is not None else 0.0
        )

    @property
    def specify_backlash(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SpecifyBacklash

        if temp is None:
            return False

        return temp

    @specify_backlash.setter
    @enforce_parameter_types
    def specify_backlash(self: Self, value: "bool"):
        self.wrapped.SpecifyBacklash = bool(value) if value is not None else False

    @property
    def cast_to(self: Self) -> "ConicalGearMeshDesign._Cast_ConicalGearMeshDesign":
        return self._Cast_ConicalGearMeshDesign(self)
