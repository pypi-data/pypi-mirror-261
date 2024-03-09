"""CrossedRollerBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_designs.rolling import _2164
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CROSSED_ROLLER_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "CrossedRollerBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.rolling import _2167
    from mastapy.bearings.bearing_designs import _2133, _2136, _2132


__docformat__ = "restructuredtext en"
__all__ = ("CrossedRollerBearing",)


Self = TypeVar("Self", bound="CrossedRollerBearing")


class CrossedRollerBearing(_2164.RollerBearing):
    """CrossedRollerBearing

    This is a mastapy class.
    """

    TYPE = _CROSSED_ROLLER_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CrossedRollerBearing")

    class _Cast_CrossedRollerBearing:
        """Special nested class for casting CrossedRollerBearing to subclasses."""

        def __init__(
            self: "CrossedRollerBearing._Cast_CrossedRollerBearing",
            parent: "CrossedRollerBearing",
        ):
            self._parent = parent

        @property
        def roller_bearing(
            self: "CrossedRollerBearing._Cast_CrossedRollerBearing",
        ) -> "_2164.RollerBearing":
            return self._parent._cast(_2164.RollerBearing)

        @property
        def rolling_bearing(
            self: "CrossedRollerBearing._Cast_CrossedRollerBearing",
        ) -> "_2167.RollingBearing":
            from mastapy.bearings.bearing_designs.rolling import _2167

            return self._parent._cast(_2167.RollingBearing)

        @property
        def detailed_bearing(
            self: "CrossedRollerBearing._Cast_CrossedRollerBearing",
        ) -> "_2133.DetailedBearing":
            from mastapy.bearings.bearing_designs import _2133

            return self._parent._cast(_2133.DetailedBearing)

        @property
        def non_linear_bearing(
            self: "CrossedRollerBearing._Cast_CrossedRollerBearing",
        ) -> "_2136.NonLinearBearing":
            from mastapy.bearings.bearing_designs import _2136

            return self._parent._cast(_2136.NonLinearBearing)

        @property
        def bearing_design(
            self: "CrossedRollerBearing._Cast_CrossedRollerBearing",
        ) -> "_2132.BearingDesign":
            from mastapy.bearings.bearing_designs import _2132

            return self._parent._cast(_2132.BearingDesign)

        @property
        def crossed_roller_bearing(
            self: "CrossedRollerBearing._Cast_CrossedRollerBearing",
        ) -> "CrossedRollerBearing":
            return self._parent

        def __getattr__(
            self: "CrossedRollerBearing._Cast_CrossedRollerBearing", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CrossedRollerBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CrossedRollerBearing._Cast_CrossedRollerBearing":
        return self._Cast_CrossedRollerBearing(self)
