"""HypoidGearMeshDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.agma_gleason_conical import _1195
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Hypoid", "HypoidGearMeshDesign"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.hypoid import _988, _986, _989
    from mastapy.gears.gear_designs.conical import _1156
    from mastapy.gears.gear_designs import _950, _949


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearMeshDesign",)


Self = TypeVar("Self", bound="HypoidGearMeshDesign")


class HypoidGearMeshDesign(_1195.AGMAGleasonConicalGearMeshDesign):
    """HypoidGearMeshDesign

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearMeshDesign")

    class _Cast_HypoidGearMeshDesign:
        """Special nested class for casting HypoidGearMeshDesign to subclasses."""

        def __init__(
            self: "HypoidGearMeshDesign._Cast_HypoidGearMeshDesign",
            parent: "HypoidGearMeshDesign",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_design(
            self: "HypoidGearMeshDesign._Cast_HypoidGearMeshDesign",
        ) -> "_1195.AGMAGleasonConicalGearMeshDesign":
            return self._parent._cast(_1195.AGMAGleasonConicalGearMeshDesign)

        @property
        def conical_gear_mesh_design(
            self: "HypoidGearMeshDesign._Cast_HypoidGearMeshDesign",
        ) -> "_1156.ConicalGearMeshDesign":
            from mastapy.gears.gear_designs.conical import _1156

            return self._parent._cast(_1156.ConicalGearMeshDesign)

        @property
        def gear_mesh_design(
            self: "HypoidGearMeshDesign._Cast_HypoidGearMeshDesign",
        ) -> "_950.GearMeshDesign":
            from mastapy.gears.gear_designs import _950

            return self._parent._cast(_950.GearMeshDesign)

        @property
        def gear_design_component(
            self: "HypoidGearMeshDesign._Cast_HypoidGearMeshDesign",
        ) -> "_949.GearDesignComponent":
            from mastapy.gears.gear_designs import _949

            return self._parent._cast(_949.GearDesignComponent)

        @property
        def hypoid_gear_mesh_design(
            self: "HypoidGearMeshDesign._Cast_HypoidGearMeshDesign",
        ) -> "HypoidGearMeshDesign":
            return self._parent

        def __getattr__(
            self: "HypoidGearMeshDesign._Cast_HypoidGearMeshDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearMeshDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def hypoid_gear_set(self: Self) -> "_988.HypoidGearSetDesign":
        """mastapy.gears.gear_designs.hypoid.HypoidGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def hypoid_gears(self: Self) -> "List[_986.HypoidGearDesign]":
        """List[mastapy.gears.gear_designs.hypoid.HypoidGearDesign]

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
    def hypoid_meshed_gears(self: Self) -> "List[_989.HypoidMeshedGearDesign]":
        """List[mastapy.gears.gear_designs.hypoid.HypoidMeshedGearDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidMeshedGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "HypoidGearMeshDesign._Cast_HypoidGearMeshDesign":
        return self._Cast_HypoidGearMeshDesign(self)
