"""DetailedBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_designs import _2136
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DETAILED_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns", "DetailedBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.rolling import (
        _2137,
        _2138,
        _2139,
        _2140,
        _2141,
        _2142,
        _2144,
        _2150,
        _2151,
        _2152,
        _2156,
        _2161,
        _2162,
        _2163,
        _2164,
        _2167,
        _2168,
        _2171,
        _2172,
        _2173,
        _2174,
        _2175,
        _2176,
    )
    from mastapy.bearings.bearing_designs.fluid_film import (
        _2189,
        _2191,
        _2193,
        _2195,
        _2196,
        _2197,
    )
    from mastapy.bearings.bearing_designs import _2132


__docformat__ = "restructuredtext en"
__all__ = ("DetailedBearing",)


Self = TypeVar("Self", bound="DetailedBearing")


class DetailedBearing(_2136.NonLinearBearing):
    """DetailedBearing

    This is a mastapy class.
    """

    TYPE = _DETAILED_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DetailedBearing")

    class _Cast_DetailedBearing:
        """Special nested class for casting DetailedBearing to subclasses."""

        def __init__(
            self: "DetailedBearing._Cast_DetailedBearing", parent: "DetailedBearing"
        ):
            self._parent = parent

        @property
        def non_linear_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2136.NonLinearBearing":
            return self._parent._cast(_2136.NonLinearBearing)

        @property
        def bearing_design(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2132.BearingDesign":
            from mastapy.bearings.bearing_designs import _2132

            return self._parent._cast(_2132.BearingDesign)

        @property
        def angular_contact_ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2137.AngularContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2137

            return self._parent._cast(_2137.AngularContactBallBearing)

        @property
        def angular_contact_thrust_ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2138.AngularContactThrustBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2138

            return self._parent._cast(_2138.AngularContactThrustBallBearing)

        @property
        def asymmetric_spherical_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2139.AsymmetricSphericalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2139

            return self._parent._cast(_2139.AsymmetricSphericalRollerBearing)

        @property
        def axial_thrust_cylindrical_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2140.AxialThrustCylindricalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2140

            return self._parent._cast(_2140.AxialThrustCylindricalRollerBearing)

        @property
        def axial_thrust_needle_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2141.AxialThrustNeedleRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2141

            return self._parent._cast(_2141.AxialThrustNeedleRollerBearing)

        @property
        def ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2142.BallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2142

            return self._parent._cast(_2142.BallBearing)

        @property
        def barrel_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2144.BarrelRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2144

            return self._parent._cast(_2144.BarrelRollerBearing)

        @property
        def crossed_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2150.CrossedRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2150

            return self._parent._cast(_2150.CrossedRollerBearing)

        @property
        def cylindrical_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2151.CylindricalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2151

            return self._parent._cast(_2151.CylindricalRollerBearing)

        @property
        def deep_groove_ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2152.DeepGrooveBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2152

            return self._parent._cast(_2152.DeepGrooveBallBearing)

        @property
        def four_point_contact_ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2156.FourPointContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2156

            return self._parent._cast(_2156.FourPointContactBallBearing)

        @property
        def multi_point_contact_ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2161.MultiPointContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2161

            return self._parent._cast(_2161.MultiPointContactBallBearing)

        @property
        def needle_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2162.NeedleRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2162

            return self._parent._cast(_2162.NeedleRollerBearing)

        @property
        def non_barrel_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2163.NonBarrelRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2163

            return self._parent._cast(_2163.NonBarrelRollerBearing)

        @property
        def roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2164.RollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2164

            return self._parent._cast(_2164.RollerBearing)

        @property
        def rolling_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2167.RollingBearing":
            from mastapy.bearings.bearing_designs.rolling import _2167

            return self._parent._cast(_2167.RollingBearing)

        @property
        def self_aligning_ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2168.SelfAligningBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2168

            return self._parent._cast(_2168.SelfAligningBallBearing)

        @property
        def spherical_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2171.SphericalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2171

            return self._parent._cast(_2171.SphericalRollerBearing)

        @property
        def spherical_roller_thrust_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2172.SphericalRollerThrustBearing":
            from mastapy.bearings.bearing_designs.rolling import _2172

            return self._parent._cast(_2172.SphericalRollerThrustBearing)

        @property
        def taper_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2173.TaperRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2173

            return self._parent._cast(_2173.TaperRollerBearing)

        @property
        def three_point_contact_ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2174.ThreePointContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2174

            return self._parent._cast(_2174.ThreePointContactBallBearing)

        @property
        def thrust_ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2175.ThrustBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2175

            return self._parent._cast(_2175.ThrustBallBearing)

        @property
        def toroidal_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2176.ToroidalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2176

            return self._parent._cast(_2176.ToroidalRollerBearing)

        @property
        def pad_fluid_film_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2189.PadFluidFilmBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2189

            return self._parent._cast(_2189.PadFluidFilmBearing)

        @property
        def plain_grease_filled_journal_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2191.PlainGreaseFilledJournalBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2191

            return self._parent._cast(_2191.PlainGreaseFilledJournalBearing)

        @property
        def plain_journal_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2193.PlainJournalBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2193

            return self._parent._cast(_2193.PlainJournalBearing)

        @property
        def plain_oil_fed_journal_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2195.PlainOilFedJournalBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2195

            return self._parent._cast(_2195.PlainOilFedJournalBearing)

        @property
        def tilting_pad_journal_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2196.TiltingPadJournalBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2196

            return self._parent._cast(_2196.TiltingPadJournalBearing)

        @property
        def tilting_pad_thrust_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2197.TiltingPadThrustBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2197

            return self._parent._cast(_2197.TiltingPadThrustBearing)

        @property
        def detailed_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "DetailedBearing":
            return self._parent

        def __getattr__(self: "DetailedBearing._Cast_DetailedBearing", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DetailedBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "DetailedBearing._Cast_DetailedBearing":
        return self._Cast_DetailedBearing(self)
