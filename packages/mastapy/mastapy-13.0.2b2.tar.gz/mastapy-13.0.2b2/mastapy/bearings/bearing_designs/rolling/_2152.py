"""DeepGrooveBallBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_designs.rolling import _2142
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DEEP_GROOVE_BALL_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "DeepGrooveBallBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.rolling import _2167
    from mastapy.bearings.bearing_designs import _2133, _2136, _2132


__docformat__ = "restructuredtext en"
__all__ = ("DeepGrooveBallBearing",)


Self = TypeVar("Self", bound="DeepGrooveBallBearing")


class DeepGrooveBallBearing(_2142.BallBearing):
    """DeepGrooveBallBearing

    This is a mastapy class.
    """

    TYPE = _DEEP_GROOVE_BALL_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DeepGrooveBallBearing")

    class _Cast_DeepGrooveBallBearing:
        """Special nested class for casting DeepGrooveBallBearing to subclasses."""

        def __init__(
            self: "DeepGrooveBallBearing._Cast_DeepGrooveBallBearing",
            parent: "DeepGrooveBallBearing",
        ):
            self._parent = parent

        @property
        def ball_bearing(
            self: "DeepGrooveBallBearing._Cast_DeepGrooveBallBearing",
        ) -> "_2142.BallBearing":
            return self._parent._cast(_2142.BallBearing)

        @property
        def rolling_bearing(
            self: "DeepGrooveBallBearing._Cast_DeepGrooveBallBearing",
        ) -> "_2167.RollingBearing":
            from mastapy.bearings.bearing_designs.rolling import _2167

            return self._parent._cast(_2167.RollingBearing)

        @property
        def detailed_bearing(
            self: "DeepGrooveBallBearing._Cast_DeepGrooveBallBearing",
        ) -> "_2133.DetailedBearing":
            from mastapy.bearings.bearing_designs import _2133

            return self._parent._cast(_2133.DetailedBearing)

        @property
        def non_linear_bearing(
            self: "DeepGrooveBallBearing._Cast_DeepGrooveBallBearing",
        ) -> "_2136.NonLinearBearing":
            from mastapy.bearings.bearing_designs import _2136

            return self._parent._cast(_2136.NonLinearBearing)

        @property
        def bearing_design(
            self: "DeepGrooveBallBearing._Cast_DeepGrooveBallBearing",
        ) -> "_2132.BearingDesign":
            from mastapy.bearings.bearing_designs import _2132

            return self._parent._cast(_2132.BearingDesign)

        @property
        def deep_groove_ball_bearing(
            self: "DeepGrooveBallBearing._Cast_DeepGrooveBallBearing",
        ) -> "DeepGrooveBallBearing":
            return self._parent

        def __getattr__(
            self: "DeepGrooveBallBearing._Cast_DeepGrooveBallBearing", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DeepGrooveBallBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "DeepGrooveBallBearing._Cast_DeepGrooveBallBearing":
        return self._Cast_DeepGrooveBallBearing(self)
