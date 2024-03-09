"""HypoidGearSet"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2516
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "HypoidGearSet"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.hypoid import _988
    from mastapy.system_model.part_model.gears import _2536, _2526, _2534
    from mastapy.system_model.connections_and_sockets.gears import _2317
    from mastapy.system_model.part_model import _2478, _2436, _2470
    from mastapy.system_model import _2205


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearSet",)


Self = TypeVar("Self", bound="HypoidGearSet")


class HypoidGearSet(_2516.AGMAGleasonConicalGearSet):
    """HypoidGearSet

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearSet")

    class _Cast_HypoidGearSet:
        """Special nested class for casting HypoidGearSet to subclasses."""

        def __init__(
            self: "HypoidGearSet._Cast_HypoidGearSet", parent: "HypoidGearSet"
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set(
            self: "HypoidGearSet._Cast_HypoidGearSet",
        ) -> "_2516.AGMAGleasonConicalGearSet":
            return self._parent._cast(_2516.AGMAGleasonConicalGearSet)

        @property
        def conical_gear_set(
            self: "HypoidGearSet._Cast_HypoidGearSet",
        ) -> "_2526.ConicalGearSet":
            from mastapy.system_model.part_model.gears import _2526

            return self._parent._cast(_2526.ConicalGearSet)

        @property
        def gear_set(self: "HypoidGearSet._Cast_HypoidGearSet") -> "_2534.GearSet":
            from mastapy.system_model.part_model.gears import _2534

            return self._parent._cast(_2534.GearSet)

        @property
        def specialised_assembly(
            self: "HypoidGearSet._Cast_HypoidGearSet",
        ) -> "_2478.SpecialisedAssembly":
            from mastapy.system_model.part_model import _2478

            return self._parent._cast(_2478.SpecialisedAssembly)

        @property
        def abstract_assembly(
            self: "HypoidGearSet._Cast_HypoidGearSet",
        ) -> "_2436.AbstractAssembly":
            from mastapy.system_model.part_model import _2436

            return self._parent._cast(_2436.AbstractAssembly)

        @property
        def part(self: "HypoidGearSet._Cast_HypoidGearSet") -> "_2470.Part":
            from mastapy.system_model.part_model import _2470

            return self._parent._cast(_2470.Part)

        @property
        def design_entity(
            self: "HypoidGearSet._Cast_HypoidGearSet",
        ) -> "_2205.DesignEntity":
            from mastapy.system_model import _2205

            return self._parent._cast(_2205.DesignEntity)

        @property
        def hypoid_gear_set(
            self: "HypoidGearSet._Cast_HypoidGearSet",
        ) -> "HypoidGearSet":
            return self._parent

        def __getattr__(self: "HypoidGearSet._Cast_HypoidGearSet", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearSet.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_gear_set_design(self: Self) -> "_988.HypoidGearSetDesign":
        """mastapy.gears.gear_designs.hypoid.HypoidGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def hypoid_gear_set_design(self: Self) -> "_988.HypoidGearSetDesign":
        """mastapy.gears.gear_designs.hypoid.HypoidGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def hypoid_gears(self: Self) -> "List[_2536.HypoidGear]":
        """List[mastapy.system_model.part_model.gears.HypoidGear]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_meshes(self: Self) -> "List[_2317.HypoidGearMesh]":
        """List[mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "HypoidGearSet._Cast_HypoidGearSet":
        return self._Cast_HypoidGearSet(self)
