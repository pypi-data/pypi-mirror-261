"""LoadedBearingResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.bearings import _1877
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults", "LoadedBearingResults"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results import (
        _1962,
        _1953,
        _1954,
        _1955,
        _1956,
        _1957,
        _1959,
    )
    from mastapy.bearings.bearing_designs import _2132
    from mastapy.math_utility.measured_vectors import _1566
    from mastapy.bearings.bearing_results.rolling import (
        _2070,
        _1985,
        _1988,
        _1991,
        _1996,
        _1999,
        _2004,
        _2007,
        _2011,
        _2014,
        _2019,
        _2023,
        _2026,
        _2031,
        _2035,
        _2038,
        _2042,
        _2045,
        _2050,
        _2053,
        _2056,
        _2059,
    )
    from mastapy.bearings.bearing_results.fluid_film import (
        _2121,
        _2122,
        _2123,
        _2124,
        _2126,
        _2129,
        _2130,
    )


__docformat__ = "restructuredtext en"
__all__ = ("LoadedBearingResults",)


Self = TypeVar("Self", bound="LoadedBearingResults")


class LoadedBearingResults(_1877.BearingLoadCaseResultsLightweight):
    """LoadedBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_BEARING_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedBearingResults")

    class _Cast_LoadedBearingResults:
        """Special nested class for casting LoadedBearingResults to subclasses."""

        def __init__(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
            parent: "LoadedBearingResults",
        ):
            self._parent = parent

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_1877.BearingLoadCaseResultsLightweight":
            return self._parent._cast(_1877.BearingLoadCaseResultsLightweight)

        @property
        def loaded_concept_axial_clearance_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_1953.LoadedConceptAxialClearanceBearingResults":
            from mastapy.bearings.bearing_results import _1953

            return self._parent._cast(_1953.LoadedConceptAxialClearanceBearingResults)

        @property
        def loaded_concept_clearance_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_1954.LoadedConceptClearanceBearingResults":
            from mastapy.bearings.bearing_results import _1954

            return self._parent._cast(_1954.LoadedConceptClearanceBearingResults)

        @property
        def loaded_concept_radial_clearance_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_1955.LoadedConceptRadialClearanceBearingResults":
            from mastapy.bearings.bearing_results import _1955

            return self._parent._cast(_1955.LoadedConceptRadialClearanceBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_1956.LoadedDetailedBearingResults":
            from mastapy.bearings.bearing_results import _1956

            return self._parent._cast(_1956.LoadedDetailedBearingResults)

        @property
        def loaded_linear_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_1957.LoadedLinearBearingResults":
            from mastapy.bearings.bearing_results import _1957

            return self._parent._cast(_1957.LoadedLinearBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_1959.LoadedNonLinearBearingResults":
            from mastapy.bearings.bearing_results import _1959

            return self._parent._cast(_1959.LoadedNonLinearBearingResults)

        @property
        def loaded_angular_contact_ball_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_1985.LoadedAngularContactBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _1985

            return self._parent._cast(_1985.LoadedAngularContactBallBearingResults)

        @property
        def loaded_angular_contact_thrust_ball_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_1988.LoadedAngularContactThrustBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _1988

            return self._parent._cast(
                _1988.LoadedAngularContactThrustBallBearingResults
            )

        @property
        def loaded_asymmetric_spherical_roller_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_1991.LoadedAsymmetricSphericalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _1991

            return self._parent._cast(
                _1991.LoadedAsymmetricSphericalRollerBearingResults
            )

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_1996.LoadedAxialThrustCylindricalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _1996

            return self._parent._cast(
                _1996.LoadedAxialThrustCylindricalRollerBearingResults
            )

        @property
        def loaded_axial_thrust_needle_roller_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_1999.LoadedAxialThrustNeedleRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _1999

            return self._parent._cast(_1999.LoadedAxialThrustNeedleRollerBearingResults)

        @property
        def loaded_ball_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2004.LoadedBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2004

            return self._parent._cast(_2004.LoadedBallBearingResults)

        @property
        def loaded_crossed_roller_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2007.LoadedCrossedRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2007

            return self._parent._cast(_2007.LoadedCrossedRollerBearingResults)

        @property
        def loaded_cylindrical_roller_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2011.LoadedCylindricalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2011

            return self._parent._cast(_2011.LoadedCylindricalRollerBearingResults)

        @property
        def loaded_deep_groove_ball_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2014.LoadedDeepGrooveBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2014

            return self._parent._cast(_2014.LoadedDeepGrooveBallBearingResults)

        @property
        def loaded_four_point_contact_ball_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2019.LoadedFourPointContactBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2019

            return self._parent._cast(_2019.LoadedFourPointContactBallBearingResults)

        @property
        def loaded_needle_roller_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2023.LoadedNeedleRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2023

            return self._parent._cast(_2023.LoadedNeedleRollerBearingResults)

        @property
        def loaded_non_barrel_roller_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2026.LoadedNonBarrelRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2026

            return self._parent._cast(_2026.LoadedNonBarrelRollerBearingResults)

        @property
        def loaded_roller_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2031.LoadedRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2031

            return self._parent._cast(_2031.LoadedRollerBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2035.LoadedRollingBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2035

            return self._parent._cast(_2035.LoadedRollingBearingResults)

        @property
        def loaded_self_aligning_ball_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2038.LoadedSelfAligningBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2038

            return self._parent._cast(_2038.LoadedSelfAligningBallBearingResults)

        @property
        def loaded_spherical_roller_radial_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2042.LoadedSphericalRollerRadialBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2042

            return self._parent._cast(_2042.LoadedSphericalRollerRadialBearingResults)

        @property
        def loaded_spherical_roller_thrust_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2045.LoadedSphericalRollerThrustBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2045

            return self._parent._cast(_2045.LoadedSphericalRollerThrustBearingResults)

        @property
        def loaded_taper_roller_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2050.LoadedTaperRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2050

            return self._parent._cast(_2050.LoadedTaperRollerBearingResults)

        @property
        def loaded_three_point_contact_ball_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2053.LoadedThreePointContactBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2053

            return self._parent._cast(_2053.LoadedThreePointContactBallBearingResults)

        @property
        def loaded_thrust_ball_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2056.LoadedThrustBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2056

            return self._parent._cast(_2056.LoadedThrustBallBearingResults)

        @property
        def loaded_toroidal_roller_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2059.LoadedToroidalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2059

            return self._parent._cast(_2059.LoadedToroidalRollerBearingResults)

        @property
        def loaded_fluid_film_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2121.LoadedFluidFilmBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2121

            return self._parent._cast(_2121.LoadedFluidFilmBearingResults)

        @property
        def loaded_grease_filled_journal_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2122.LoadedGreaseFilledJournalBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2122

            return self._parent._cast(_2122.LoadedGreaseFilledJournalBearingResults)

        @property
        def loaded_pad_fluid_film_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2123.LoadedPadFluidFilmBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2123

            return self._parent._cast(_2123.LoadedPadFluidFilmBearingResults)

        @property
        def loaded_plain_journal_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2124.LoadedPlainJournalBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2124

            return self._parent._cast(_2124.LoadedPlainJournalBearingResults)

        @property
        def loaded_plain_oil_fed_journal_bearing(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2126.LoadedPlainOilFedJournalBearing":
            from mastapy.bearings.bearing_results.fluid_film import _2126

            return self._parent._cast(_2126.LoadedPlainOilFedJournalBearing)

        @property
        def loaded_tilting_pad_journal_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2129.LoadedTiltingPadJournalBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2129

            return self._parent._cast(_2129.LoadedTiltingPadJournalBearingResults)

        @property
        def loaded_tilting_pad_thrust_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2130.LoadedTiltingPadThrustBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2130

            return self._parent._cast(_2130.LoadedTiltingPadThrustBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "LoadedBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedBearingResults._Cast_LoadedBearingResults", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedBearingResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle_of_gravity_from_z_axis(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngleOfGravityFromZAxis

        if temp is None:
            return 0.0

        return temp

    @property
    def axial_displacement_preload(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AxialDisplacementPreload

        if temp is None:
            return 0.0

        return temp

    @axial_displacement_preload.setter
    @enforce_parameter_types
    def axial_displacement_preload(self: Self, value: "float"):
        self.wrapped.AxialDisplacementPreload = (
            float(value) if value is not None else 0.0
        )

    @property
    def duration(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Duration

        if temp is None:
            return 0.0

        return temp

    @duration.setter
    @enforce_parameter_types
    def duration(self: Self, value: "float"):
        self.wrapped.Duration = float(value) if value is not None else 0.0

    @property
    def force_results_are_overridden(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceResultsAreOverridden

        if temp is None:
            return False

        return temp

    @property
    def inner_ring_angular_velocity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.InnerRingAngularVelocity

        if temp is None:
            return 0.0

        return temp

    @inner_ring_angular_velocity.setter
    @enforce_parameter_types
    def inner_ring_angular_velocity(self: Self, value: "float"):
        self.wrapped.InnerRingAngularVelocity = (
            float(value) if value is not None else 0.0
        )

    @property
    def orientation(self: Self) -> "_1962.Orientations":
        """mastapy.bearings.bearing_results.Orientations"""
        temp = self.wrapped.Orientation

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Bearings.BearingResults.Orientations"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings.bearing_results._1962", "Orientations"
        )(value)

    @orientation.setter
    @enforce_parameter_types
    def orientation(self: Self, value: "_1962.Orientations"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Bearings.BearingResults.Orientations"
        )
        self.wrapped.Orientation = value

    @property
    def outer_ring_angular_velocity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OuterRingAngularVelocity

        if temp is None:
            return 0.0

        return temp

    @outer_ring_angular_velocity.setter
    @enforce_parameter_types
    def outer_ring_angular_velocity(self: Self, value: "float"):
        self.wrapped.OuterRingAngularVelocity = (
            float(value) if value is not None else 0.0
        )

    @property
    def relative_angular_velocity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeAngularVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_axial_displacement(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeAxialDisplacement

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_radial_displacement(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeRadialDisplacement

        if temp is None:
            return 0.0

        return temp

    @property
    def signed_relative_angular_velocity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SignedRelativeAngularVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def specified_axial_internal_clearance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SpecifiedAxialInternalClearance

        if temp is None:
            return 0.0

        return temp

    @specified_axial_internal_clearance.setter
    @enforce_parameter_types
    def specified_axial_internal_clearance(self: Self, value: "float"):
        self.wrapped.SpecifiedAxialInternalClearance = (
            float(value) if value is not None else 0.0
        )

    @property
    def specified_radial_internal_clearance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SpecifiedRadialInternalClearance

        if temp is None:
            return 0.0

        return temp

    @specified_radial_internal_clearance.setter
    @enforce_parameter_types
    def specified_radial_internal_clearance(self: Self, value: "float"):
        self.wrapped.SpecifiedRadialInternalClearance = (
            float(value) if value is not None else 0.0
        )

    @property
    def bearing(self: Self) -> "_2132.BearingDesign":
        """mastapy.bearings.bearing_designs.BearingDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Bearing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def force_on_inner_race(self: Self) -> "_1566.VectorWithLinearAndAngularComponents":
        """mastapy.math_utility.measured_vectors.VectorWithLinearAndAngularComponents

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceOnInnerRace

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def ring_results(self: Self) -> "List[_2070.RingForceAndDisplacement]":
        """List[mastapy.bearings.bearing_results.rolling.RingForceAndDisplacement]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RingResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "LoadedBearingResults._Cast_LoadedBearingResults":
        return self._Cast_LoadedBearingResults(self)
