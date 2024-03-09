"""NonBarrelRollerBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy.bearings.bearing_designs.rolling import _2164
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NON_BARREL_ROLLER_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "NonBarrelRollerBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.rolling import (
        _2165,
        _2166,
        _2140,
        _2141,
        _2151,
        _2162,
        _2173,
        _2167,
    )
    from mastapy.bearings.bearing_designs import _2133, _2136, _2132


__docformat__ = "restructuredtext en"
__all__ = ("NonBarrelRollerBearing",)


Self = TypeVar("Self", bound="NonBarrelRollerBearing")


class NonBarrelRollerBearing(_2164.RollerBearing):
    """NonBarrelRollerBearing

    This is a mastapy class.
    """

    TYPE = _NON_BARREL_ROLLER_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NonBarrelRollerBearing")

    class _Cast_NonBarrelRollerBearing:
        """Special nested class for casting NonBarrelRollerBearing to subclasses."""

        def __init__(
            self: "NonBarrelRollerBearing._Cast_NonBarrelRollerBearing",
            parent: "NonBarrelRollerBearing",
        ):
            self._parent = parent

        @property
        def roller_bearing(
            self: "NonBarrelRollerBearing._Cast_NonBarrelRollerBearing",
        ) -> "_2164.RollerBearing":
            return self._parent._cast(_2164.RollerBearing)

        @property
        def rolling_bearing(
            self: "NonBarrelRollerBearing._Cast_NonBarrelRollerBearing",
        ) -> "_2167.RollingBearing":
            from mastapy.bearings.bearing_designs.rolling import _2167

            return self._parent._cast(_2167.RollingBearing)

        @property
        def detailed_bearing(
            self: "NonBarrelRollerBearing._Cast_NonBarrelRollerBearing",
        ) -> "_2133.DetailedBearing":
            from mastapy.bearings.bearing_designs import _2133

            return self._parent._cast(_2133.DetailedBearing)

        @property
        def non_linear_bearing(
            self: "NonBarrelRollerBearing._Cast_NonBarrelRollerBearing",
        ) -> "_2136.NonLinearBearing":
            from mastapy.bearings.bearing_designs import _2136

            return self._parent._cast(_2136.NonLinearBearing)

        @property
        def bearing_design(
            self: "NonBarrelRollerBearing._Cast_NonBarrelRollerBearing",
        ) -> "_2132.BearingDesign":
            from mastapy.bearings.bearing_designs import _2132

            return self._parent._cast(_2132.BearingDesign)

        @property
        def axial_thrust_cylindrical_roller_bearing(
            self: "NonBarrelRollerBearing._Cast_NonBarrelRollerBearing",
        ) -> "_2140.AxialThrustCylindricalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2140

            return self._parent._cast(_2140.AxialThrustCylindricalRollerBearing)

        @property
        def axial_thrust_needle_roller_bearing(
            self: "NonBarrelRollerBearing._Cast_NonBarrelRollerBearing",
        ) -> "_2141.AxialThrustNeedleRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2141

            return self._parent._cast(_2141.AxialThrustNeedleRollerBearing)

        @property
        def cylindrical_roller_bearing(
            self: "NonBarrelRollerBearing._Cast_NonBarrelRollerBearing",
        ) -> "_2151.CylindricalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2151

            return self._parent._cast(_2151.CylindricalRollerBearing)

        @property
        def needle_roller_bearing(
            self: "NonBarrelRollerBearing._Cast_NonBarrelRollerBearing",
        ) -> "_2162.NeedleRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2162

            return self._parent._cast(_2162.NeedleRollerBearing)

        @property
        def taper_roller_bearing(
            self: "NonBarrelRollerBearing._Cast_NonBarrelRollerBearing",
        ) -> "_2173.TaperRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2173

            return self._parent._cast(_2173.TaperRollerBearing)

        @property
        def non_barrel_roller_bearing(
            self: "NonBarrelRollerBearing._Cast_NonBarrelRollerBearing",
        ) -> "NonBarrelRollerBearing":
            return self._parent

        def __getattr__(
            self: "NonBarrelRollerBearing._Cast_NonBarrelRollerBearing", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NonBarrelRollerBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def roller_end_radius(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RollerEndRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @roller_end_radius.setter
    @enforce_parameter_types
    def roller_end_radius(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RollerEndRadius = value

    @property
    def roller_end_shape(self: Self) -> "_2165.RollerEndShape":
        """mastapy.bearings.bearing_designs.rolling.RollerEndShape"""
        temp = self.wrapped.RollerEndShape

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Bearings.BearingDesigns.Rolling.RollerEndShape"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings.bearing_designs.rolling._2165", "RollerEndShape"
        )(value)

    @roller_end_shape.setter
    @enforce_parameter_types
    def roller_end_shape(self: Self, value: "_2165.RollerEndShape"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Bearings.BearingDesigns.Rolling.RollerEndShape"
        )
        self.wrapped.RollerEndShape = value

    @property
    def ribs(self: Self) -> "List[_2166.RollerRibDetail]":
        """List[mastapy.bearings.bearing_designs.rolling.RollerRibDetail]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Ribs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "NonBarrelRollerBearing._Cast_NonBarrelRollerBearing":
        return self._Cast_NonBarrelRollerBearing(self)
