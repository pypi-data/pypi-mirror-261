"""StraightBevelGearMeshDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.bevel import _1182
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_MESH_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.StraightBevel", "StraightBevelGearMeshDesign"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.straight_bevel import _964, _962, _965
    from mastapy.gears.gear_designs.agma_gleason_conical import _1195
    from mastapy.gears.gear_designs.conical import _1156
    from mastapy.gears.gear_designs import _950, _949


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearMeshDesign",)


Self = TypeVar("Self", bound="StraightBevelGearMeshDesign")


class StraightBevelGearMeshDesign(_1182.BevelGearMeshDesign):
    """StraightBevelGearMeshDesign

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_MESH_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelGearMeshDesign")

    class _Cast_StraightBevelGearMeshDesign:
        """Special nested class for casting StraightBevelGearMeshDesign to subclasses."""

        def __init__(
            self: "StraightBevelGearMeshDesign._Cast_StraightBevelGearMeshDesign",
            parent: "StraightBevelGearMeshDesign",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_design(
            self: "StraightBevelGearMeshDesign._Cast_StraightBevelGearMeshDesign",
        ) -> "_1182.BevelGearMeshDesign":
            return self._parent._cast(_1182.BevelGearMeshDesign)

        @property
        def agma_gleason_conical_gear_mesh_design(
            self: "StraightBevelGearMeshDesign._Cast_StraightBevelGearMeshDesign",
        ) -> "_1195.AGMAGleasonConicalGearMeshDesign":
            from mastapy.gears.gear_designs.agma_gleason_conical import _1195

            return self._parent._cast(_1195.AGMAGleasonConicalGearMeshDesign)

        @property
        def conical_gear_mesh_design(
            self: "StraightBevelGearMeshDesign._Cast_StraightBevelGearMeshDesign",
        ) -> "_1156.ConicalGearMeshDesign":
            from mastapy.gears.gear_designs.conical import _1156

            return self._parent._cast(_1156.ConicalGearMeshDesign)

        @property
        def gear_mesh_design(
            self: "StraightBevelGearMeshDesign._Cast_StraightBevelGearMeshDesign",
        ) -> "_950.GearMeshDesign":
            from mastapy.gears.gear_designs import _950

            return self._parent._cast(_950.GearMeshDesign)

        @property
        def gear_design_component(
            self: "StraightBevelGearMeshDesign._Cast_StraightBevelGearMeshDesign",
        ) -> "_949.GearDesignComponent":
            from mastapy.gears.gear_designs import _949

            return self._parent._cast(_949.GearDesignComponent)

        @property
        def straight_bevel_gear_mesh_design(
            self: "StraightBevelGearMeshDesign._Cast_StraightBevelGearMeshDesign",
        ) -> "StraightBevelGearMeshDesign":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearMeshDesign._Cast_StraightBevelGearMeshDesign",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelGearMeshDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def straight_bevel_gear_set(self: Self) -> "_964.StraightBevelGearSetDesign":
        """mastapy.gears.gear_designs.straight_bevel.StraightBevelGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def straight_bevel_gears(self: Self) -> "List[_962.StraightBevelGearDesign]":
        """List[mastapy.gears.gear_designs.straight_bevel.StraightBevelGearDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_meshed_gears(
        self: Self,
    ) -> "List[_965.StraightBevelMeshedGearDesign]":
        """List[mastapy.gears.gear_designs.straight_bevel.StraightBevelMeshedGearDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelMeshedGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelGearMeshDesign._Cast_StraightBevelGearMeshDesign":
        return self._Cast_StraightBevelGearMeshDesign(self)
