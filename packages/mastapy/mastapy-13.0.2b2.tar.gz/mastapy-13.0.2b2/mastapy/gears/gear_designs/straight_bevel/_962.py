"""StraightBevelGearDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_designs.bevel import _1181
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.StraightBevel", "StraightBevelGearDesign"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.agma_gleason_conical import _1194
    from mastapy.gears.gear_designs.conical import _1155
    from mastapy.gears.gear_designs import _948, _949


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearDesign",)


Self = TypeVar("Self", bound="StraightBevelGearDesign")


class StraightBevelGearDesign(_1181.BevelGearDesign):
    """StraightBevelGearDesign

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelGearDesign")

    class _Cast_StraightBevelGearDesign:
        """Special nested class for casting StraightBevelGearDesign to subclasses."""

        def __init__(
            self: "StraightBevelGearDesign._Cast_StraightBevelGearDesign",
            parent: "StraightBevelGearDesign",
        ):
            self._parent = parent

        @property
        def bevel_gear_design(
            self: "StraightBevelGearDesign._Cast_StraightBevelGearDesign",
        ) -> "_1181.BevelGearDesign":
            return self._parent._cast(_1181.BevelGearDesign)

        @property
        def agma_gleason_conical_gear_design(
            self: "StraightBevelGearDesign._Cast_StraightBevelGearDesign",
        ) -> "_1194.AGMAGleasonConicalGearDesign":
            from mastapy.gears.gear_designs.agma_gleason_conical import _1194

            return self._parent._cast(_1194.AGMAGleasonConicalGearDesign)

        @property
        def conical_gear_design(
            self: "StraightBevelGearDesign._Cast_StraightBevelGearDesign",
        ) -> "_1155.ConicalGearDesign":
            from mastapy.gears.gear_designs.conical import _1155

            return self._parent._cast(_1155.ConicalGearDesign)

        @property
        def gear_design(
            self: "StraightBevelGearDesign._Cast_StraightBevelGearDesign",
        ) -> "_948.GearDesign":
            from mastapy.gears.gear_designs import _948

            return self._parent._cast(_948.GearDesign)

        @property
        def gear_design_component(
            self: "StraightBevelGearDesign._Cast_StraightBevelGearDesign",
        ) -> "_949.GearDesignComponent":
            from mastapy.gears.gear_designs import _949

            return self._parent._cast(_949.GearDesignComponent)

        @property
        def straight_bevel_gear_design(
            self: "StraightBevelGearDesign._Cast_StraightBevelGearDesign",
        ) -> "StraightBevelGearDesign":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearDesign._Cast_StraightBevelGearDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelGearDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "StraightBevelGearDesign._Cast_StraightBevelGearDesign":
        return self._Cast_StraightBevelGearDesign(self)
