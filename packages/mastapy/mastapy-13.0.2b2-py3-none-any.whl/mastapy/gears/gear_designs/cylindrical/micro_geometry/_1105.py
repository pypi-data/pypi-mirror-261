"""CylindricalGearMicroGeometryPerTooth"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1102
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MICRO_GEOMETRY_PER_TOOTH = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "CylindricalGearMicroGeometryPerTooth",
)

if TYPE_CHECKING:
    from mastapy.gears.analysis import _1222, _1219, _1216


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMicroGeometryPerTooth",)


Self = TypeVar("Self", bound="CylindricalGearMicroGeometryPerTooth")


class CylindricalGearMicroGeometryPerTooth(_1102.CylindricalGearMicroGeometryBase):
    """CylindricalGearMicroGeometryPerTooth

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MICRO_GEOMETRY_PER_TOOTH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearMicroGeometryPerTooth")

    class _Cast_CylindricalGearMicroGeometryPerTooth:
        """Special nested class for casting CylindricalGearMicroGeometryPerTooth to subclasses."""

        def __init__(
            self: "CylindricalGearMicroGeometryPerTooth._Cast_CylindricalGearMicroGeometryPerTooth",
            parent: "CylindricalGearMicroGeometryPerTooth",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_micro_geometry_base(
            self: "CylindricalGearMicroGeometryPerTooth._Cast_CylindricalGearMicroGeometryPerTooth",
        ) -> "_1102.CylindricalGearMicroGeometryBase":
            return self._parent._cast(_1102.CylindricalGearMicroGeometryBase)

        @property
        def gear_implementation_detail(
            self: "CylindricalGearMicroGeometryPerTooth._Cast_CylindricalGearMicroGeometryPerTooth",
        ) -> "_1222.GearImplementationDetail":
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.GearImplementationDetail)

        @property
        def gear_design_analysis(
            self: "CylindricalGearMicroGeometryPerTooth._Cast_CylindricalGearMicroGeometryPerTooth",
        ) -> "_1219.GearDesignAnalysis":
            from mastapy.gears.analysis import _1219

            return self._parent._cast(_1219.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "CylindricalGearMicroGeometryPerTooth._Cast_CylindricalGearMicroGeometryPerTooth",
        ) -> "_1216.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1216

            return self._parent._cast(_1216.AbstractGearAnalysis)

        @property
        def cylindrical_gear_micro_geometry_per_tooth(
            self: "CylindricalGearMicroGeometryPerTooth._Cast_CylindricalGearMicroGeometryPerTooth",
        ) -> "CylindricalGearMicroGeometryPerTooth":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMicroGeometryPerTooth._Cast_CylindricalGearMicroGeometryPerTooth",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "CylindricalGearMicroGeometryPerTooth.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearMicroGeometryPerTooth._Cast_CylindricalGearMicroGeometryPerTooth":
        return self._Cast_CylindricalGearMicroGeometryPerTooth(self)
