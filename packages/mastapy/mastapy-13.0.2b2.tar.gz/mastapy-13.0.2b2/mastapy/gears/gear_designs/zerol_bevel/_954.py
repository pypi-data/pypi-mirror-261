"""ZerolBevelGearMeshDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.bevel import _1182
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MESH_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.ZerolBevel", "ZerolBevelGearMeshDesign"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.zerol_bevel import _955, _953, _956
    from mastapy.gears.gear_designs.agma_gleason_conical import _1195
    from mastapy.gears.gear_designs.conical import _1156
    from mastapy.gears.gear_designs import _950, _949


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearMeshDesign",)


Self = TypeVar("Self", bound="ZerolBevelGearMeshDesign")


class ZerolBevelGearMeshDesign(_1182.BevelGearMeshDesign):
    """ZerolBevelGearMeshDesign

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MESH_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ZerolBevelGearMeshDesign")

    class _Cast_ZerolBevelGearMeshDesign:
        """Special nested class for casting ZerolBevelGearMeshDesign to subclasses."""

        def __init__(
            self: "ZerolBevelGearMeshDesign._Cast_ZerolBevelGearMeshDesign",
            parent: "ZerolBevelGearMeshDesign",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_design(
            self: "ZerolBevelGearMeshDesign._Cast_ZerolBevelGearMeshDesign",
        ) -> "_1182.BevelGearMeshDesign":
            return self._parent._cast(_1182.BevelGearMeshDesign)

        @property
        def agma_gleason_conical_gear_mesh_design(
            self: "ZerolBevelGearMeshDesign._Cast_ZerolBevelGearMeshDesign",
        ) -> "_1195.AGMAGleasonConicalGearMeshDesign":
            from mastapy.gears.gear_designs.agma_gleason_conical import _1195

            return self._parent._cast(_1195.AGMAGleasonConicalGearMeshDesign)

        @property
        def conical_gear_mesh_design(
            self: "ZerolBevelGearMeshDesign._Cast_ZerolBevelGearMeshDesign",
        ) -> "_1156.ConicalGearMeshDesign":
            from mastapy.gears.gear_designs.conical import _1156

            return self._parent._cast(_1156.ConicalGearMeshDesign)

        @property
        def gear_mesh_design(
            self: "ZerolBevelGearMeshDesign._Cast_ZerolBevelGearMeshDesign",
        ) -> "_950.GearMeshDesign":
            from mastapy.gears.gear_designs import _950

            return self._parent._cast(_950.GearMeshDesign)

        @property
        def gear_design_component(
            self: "ZerolBevelGearMeshDesign._Cast_ZerolBevelGearMeshDesign",
        ) -> "_949.GearDesignComponent":
            from mastapy.gears.gear_designs import _949

            return self._parent._cast(_949.GearDesignComponent)

        @property
        def zerol_bevel_gear_mesh_design(
            self: "ZerolBevelGearMeshDesign._Cast_ZerolBevelGearMeshDesign",
        ) -> "ZerolBevelGearMeshDesign":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearMeshDesign._Cast_ZerolBevelGearMeshDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ZerolBevelGearMeshDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def zerol_bevel_gear_set(self: Self) -> "_955.ZerolBevelGearSetDesign":
        """mastapy.gears.gear_designs.zerol_bevel.ZerolBevelGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def zerol_bevel_gears(self: Self) -> "List[_953.ZerolBevelGearDesign]":
        """List[mastapy.gears.gear_designs.zerol_bevel.ZerolBevelGearDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_meshed_gears(self: Self) -> "List[_956.ZerolBevelMeshedGearDesign]":
        """List[mastapy.gears.gear_designs.zerol_bevel.ZerolBevelMeshedGearDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelMeshedGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ZerolBevelGearMeshDesign._Cast_ZerolBevelGearMeshDesign":
        return self._Cast_ZerolBevelGearMeshDesign(self)
