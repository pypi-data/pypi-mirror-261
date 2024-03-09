"""LoadedRollingBearingResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.bearings.bearing_results import _1956
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ROLLING_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedRollingBearingResults"
)

if TYPE_CHECKING:
    from mastapy.bearings import _1886, _1877
    from mastapy.bearings.bearing_results.rolling.abma import _2119
    from mastapy.bearings.bearing_results.rolling import (
        _1971,
        _1980,
        _1982,
        _1975,
        _2062,
        _2036,
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
        _2038,
        _2042,
        _2045,
        _2050,
        _2053,
        _2056,
        _2059,
    )
    from mastapy.bearings.bearing_results.rolling.iso_rating_results import (
        _2105,
        _2106,
        _2108,
    )
    from mastapy.bearings.bearing_results.rolling.fitting import _2112, _2114, _2115
    from mastapy.bearings.bearing_results.rolling.skf_module import _2100
    from mastapy.bearings.bearing_results import _1959, _1951


__docformat__ = "restructuredtext en"
__all__ = ("LoadedRollingBearingResults",)


Self = TypeVar("Self", bound="LoadedRollingBearingResults")


class LoadedRollingBearingResults(_1956.LoadedDetailedBearingResults):
    """LoadedRollingBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_ROLLING_BEARING_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedRollingBearingResults")

    class _Cast_LoadedRollingBearingResults:
        """Special nested class for casting LoadedRollingBearingResults to subclasses."""

        def __init__(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
            parent: "LoadedRollingBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_1956.LoadedDetailedBearingResults":
            return self._parent._cast(_1956.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_1959.LoadedNonLinearBearingResults":
            from mastapy.bearings.bearing_results import _1959

            return self._parent._cast(_1959.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_1951.LoadedBearingResults":
            from mastapy.bearings.bearing_results import _1951

            return self._parent._cast(_1951.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_1877.BearingLoadCaseResultsLightweight":
            from mastapy.bearings import _1877

            return self._parent._cast(_1877.BearingLoadCaseResultsLightweight)

        @property
        def loaded_angular_contact_ball_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_1985.LoadedAngularContactBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _1985

            return self._parent._cast(_1985.LoadedAngularContactBallBearingResults)

        @property
        def loaded_angular_contact_thrust_ball_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_1988.LoadedAngularContactThrustBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _1988

            return self._parent._cast(
                _1988.LoadedAngularContactThrustBallBearingResults
            )

        @property
        def loaded_asymmetric_spherical_roller_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_1991.LoadedAsymmetricSphericalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _1991

            return self._parent._cast(
                _1991.LoadedAsymmetricSphericalRollerBearingResults
            )

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_1996.LoadedAxialThrustCylindricalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _1996

            return self._parent._cast(
                _1996.LoadedAxialThrustCylindricalRollerBearingResults
            )

        @property
        def loaded_axial_thrust_needle_roller_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_1999.LoadedAxialThrustNeedleRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _1999

            return self._parent._cast(_1999.LoadedAxialThrustNeedleRollerBearingResults)

        @property
        def loaded_ball_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_2004.LoadedBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2004

            return self._parent._cast(_2004.LoadedBallBearingResults)

        @property
        def loaded_crossed_roller_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_2007.LoadedCrossedRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2007

            return self._parent._cast(_2007.LoadedCrossedRollerBearingResults)

        @property
        def loaded_cylindrical_roller_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_2011.LoadedCylindricalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2011

            return self._parent._cast(_2011.LoadedCylindricalRollerBearingResults)

        @property
        def loaded_deep_groove_ball_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_2014.LoadedDeepGrooveBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2014

            return self._parent._cast(_2014.LoadedDeepGrooveBallBearingResults)

        @property
        def loaded_four_point_contact_ball_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_2019.LoadedFourPointContactBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2019

            return self._parent._cast(_2019.LoadedFourPointContactBallBearingResults)

        @property
        def loaded_needle_roller_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_2023.LoadedNeedleRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2023

            return self._parent._cast(_2023.LoadedNeedleRollerBearingResults)

        @property
        def loaded_non_barrel_roller_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_2026.LoadedNonBarrelRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2026

            return self._parent._cast(_2026.LoadedNonBarrelRollerBearingResults)

        @property
        def loaded_roller_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_2031.LoadedRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2031

            return self._parent._cast(_2031.LoadedRollerBearingResults)

        @property
        def loaded_self_aligning_ball_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_2038.LoadedSelfAligningBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2038

            return self._parent._cast(_2038.LoadedSelfAligningBallBearingResults)

        @property
        def loaded_spherical_roller_radial_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_2042.LoadedSphericalRollerRadialBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2042

            return self._parent._cast(_2042.LoadedSphericalRollerRadialBearingResults)

        @property
        def loaded_spherical_roller_thrust_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_2045.LoadedSphericalRollerThrustBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2045

            return self._parent._cast(_2045.LoadedSphericalRollerThrustBearingResults)

        @property
        def loaded_taper_roller_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_2050.LoadedTaperRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2050

            return self._parent._cast(_2050.LoadedTaperRollerBearingResults)

        @property
        def loaded_three_point_contact_ball_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_2053.LoadedThreePointContactBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2053

            return self._parent._cast(_2053.LoadedThreePointContactBallBearingResults)

        @property
        def loaded_thrust_ball_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_2056.LoadedThrustBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2056

            return self._parent._cast(_2056.LoadedThrustBallBearingResults)

        @property
        def loaded_toroidal_roller_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "_2059.LoadedToroidalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2059

            return self._parent._cast(_2059.LoadedToroidalRollerBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
        ) -> "LoadedRollingBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedRollingBearingResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_to_radial_load_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialToRadialLoadRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def cage_angular_velocity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CageAngularVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def change_in_element_diameter_due_to_thermal_expansion(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ChangeInElementDiameterDueToThermalExpansion

        if temp is None:
            return 0.0

        return temp

    @property
    def change_in_operating_radial_internal_clearance_due_to_element_thermal_expansion(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.ChangeInOperatingRadialInternalClearanceDueToElementThermalExpansion
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def drag_loss_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DragLossFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_viscosity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicViscosity

        if temp is None:
            return 0.0

        return temp

    @property
    def element_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ElementTemperature

        if temp is None:
            return 0.0

        return temp

    @element_temperature.setter
    @enforce_parameter_types
    def element_temperature(self: Self, value: "float"):
        self.wrapped.ElementTemperature = float(value) if value is not None else 0.0

    @property
    def fluid_film_density(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FluidFilmDensity

        if temp is None:
            return 0.0

        return temp

    @property
    def fluid_film_temperature_source(
        self: Self,
    ) -> "_1886.FluidFilmTemperatureOptions":
        """mastapy.bearings.FluidFilmTemperatureOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FluidFilmTemperatureSource

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Bearings.FluidFilmTemperatureOptions"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings._1886", "FluidFilmTemperatureOptions"
        )(value)

    @property
    def frequency_of_over_rolling_on_inner_ring(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FrequencyOfOverRollingOnInnerRing

        if temp is None:
            return 0.0

        return temp

    @property
    def frequency_of_over_rolling_on_outer_ring(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FrequencyOfOverRollingOnOuterRing

        if temp is None:
            return 0.0

        return temp

    @property
    def frequency_of_over_rolling_on_rolling_element(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FrequencyOfOverRollingOnRollingElement

        if temp is None:
            return 0.0

        return temp

    @property
    def frictional_moment_of_drag_losses(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FrictionalMomentOfDragLosses

        if temp is None:
            return 0.0

        return temp

    @property
    def frictional_moment_of_seals(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FrictionalMomentOfSeals

        if temp is None:
            return 0.0

        return temp

    @property
    def include_centrifugal_effects(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IncludeCentrifugalEffects

        if temp is None:
            return False

        return temp

    @property
    def include_centrifugal_ring_expansion(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IncludeCentrifugalRingExpansion

        if temp is None:
            return False

        return temp

    @property
    def include_fitting_effects(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IncludeFittingEffects

        if temp is None:
            return False

        return temp

    @property
    def include_gear_blank_elastic_distortion(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IncludeGearBlankElasticDistortion

        if temp is None:
            return False

        return temp

    @property
    def include_inner_race_deflections(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IncludeInnerRaceDeflections

        if temp is None:
            return False

        return temp

    @property
    def include_thermal_expansion_effects(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IncludeThermalExpansionEffects

        if temp is None:
            return False

        return temp

    @property
    def is_inner_ring_rotating_relative_to_load(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsInnerRingRotatingRelativeToLoad

        if temp is None:
            return False

        return temp

    @property
    def is_outer_ring_rotating_relative_to_load(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsOuterRingRotatingRelativeToLoad

        if temp is None:
            return False

        return temp

    @property
    def kinematic_viscosity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KinematicViscosity

        if temp is None:
            return 0.0

        return temp

    @property
    def kinematic_viscosity_of_oil_for_efficiency_calculations(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KinematicViscosityOfOilForEfficiencyCalculations

        if temp is None:
            return 0.0

        return temp

    @property
    def lambda_ratio_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LambdaRatioInner

        if temp is None:
            return 0.0

        return temp

    @property
    def lambda_ratio_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LambdaRatioOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def lubricant_film_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LubricantFilmTemperature

        if temp is None:
            return 0.0

        return temp

    @lubricant_film_temperature.setter
    @enforce_parameter_types
    def lubricant_film_temperature(self: Self, value: "float"):
        self.wrapped.LubricantFilmTemperature = (
            float(value) if value is not None else 0.0
        )

    @property
    def lubricant_windage_and_churning_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LubricantWindageAndChurningTemperature

        if temp is None:
            return 0.0

        return temp

    @lubricant_windage_and_churning_temperature.setter
    @enforce_parameter_types
    def lubricant_windage_and_churning_temperature(self: Self, value: "float"):
        self.wrapped.LubricantWindageAndChurningTemperature = (
            float(value) if value is not None else 0.0
        )

    @property
    def maximum_normal_load_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalLoadInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_load_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalLoadOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalStress

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_stress_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalStressInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_stress_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalStressOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_lubricating_film_thickness_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumLubricatingFilmThicknessInner

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_lubricating_film_thickness_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumLubricatingFilmThicknessOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def number_of_elements_in_contact(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfElementsInContact

        if temp is None:
            return 0

        return temp

    @property
    def oil_dip_coefficient(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OilDipCoefficient

        if temp is None:
            return 0.0

        return temp

    @property
    def ratio_of_operating_element_diameter_to_element_pcd(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatioOfOperatingElementDiameterToElementPCD

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_misalignment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def rolling_frictional_moment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RollingFrictionalMoment

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_friction_coefficient(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingFrictionCoefficient

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_frictional_moment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingFrictionalMoment

        if temp is None:
            return 0.0

        return temp

    @property
    def speed_factor_dmn(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpeedFactorDmn

        if temp is None:
            return 0.0

        return temp

    @property
    def speed_factor_dn(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpeedFactorDn

        if temp is None:
            return 0.0

        return temp

    @property
    def static_equivalent_load_capacity_ratio_limit(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StaticEquivalentLoadCapacityRatioLimit

        if temp is None:
            return 0.0

        return temp

    @property
    def surrounding_lubricant_density(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SurroundingLubricantDensity

        if temp is None:
            return 0.0

        return temp

    @property
    def total_element_raceway_contact_area_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalElementRacewayContactAreaInner

        if temp is None:
            return 0.0

        return temp

    @property
    def total_element_raceway_contact_area_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalElementRacewayContactAreaLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def total_element_raceway_contact_area_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalElementRacewayContactAreaOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def total_element_raceway_contact_area_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalElementRacewayContactAreaRight

        if temp is None:
            return 0.0

        return temp

    @property
    def total_frictional_moment_from_skf_loss_method(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalFrictionalMomentFromSKFLossMethod

        if temp is None:
            return 0.0

        return temp

    @property
    def ansiabma(self: Self) -> "_2119.ANSIABMAResults":
        """mastapy.bearings.bearing_results.rolling.abma.ANSIABMAResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ANSIABMA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def din7322010(self: Self) -> "_1971.DIN7322010Results":
        """mastapy.bearings.bearing_results.rolling.DIN7322010Results

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DIN7322010

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def iso2812007(self: Self) -> "_2105.ISO2812007Results":
        """mastapy.bearings.bearing_results.rolling.iso_rating_results.ISO2812007Results

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO2812007

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def iso762006(self: Self) -> "_2106.ISO762006Results":
        """mastapy.bearings.bearing_results.rolling.iso_rating_results.ISO762006Results

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO762006

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def isotr1417912001(self: Self) -> "_1980.ISOTR1417912001Results":
        """mastapy.bearings.bearing_results.rolling.ISOTR1417912001Results

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISOTR1417912001

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def isotr1417922001(self: Self) -> "_1982.ISOTR1417922001Results":
        """mastapy.bearings.bearing_results.rolling.ISOTR1417922001Results

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISOTR1417922001

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def isots162812008(self: Self) -> "_2108.ISOTS162812008Results":
        """mastapy.bearings.bearing_results.rolling.iso_rating_results.ISOTS162812008Results

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISOTS162812008

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_ring_fitting_at_assembly(
        self: Self,
    ) -> "_2112.InnerRingFittingThermalResults":
        """mastapy.bearings.bearing_results.rolling.fitting.InnerRingFittingThermalResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerRingFittingAtAssembly

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_ring_fitting_at_operating_conditions(
        self: Self,
    ) -> "_2112.InnerRingFittingThermalResults":
        """mastapy.bearings.bearing_results.rolling.fitting.InnerRingFittingThermalResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerRingFittingAtOperatingConditions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def maximum_operating_internal_clearance(self: Self) -> "_1975.InternalClearance":
        """mastapy.bearings.bearing_results.rolling.InternalClearance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumOperatingInternalClearance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def maximum_static_contact_stress(self: Self) -> "_2062.MaximumStaticContactStress":
        """mastapy.bearings.bearing_results.rolling.MaximumStaticContactStress

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumStaticContactStress

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def minimum_operating_internal_clearance(self: Self) -> "_1975.InternalClearance":
        """mastapy.bearings.bearing_results.rolling.InternalClearance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumOperatingInternalClearance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def outer_ring_fitting_at_assembly(
        self: Self,
    ) -> "_2114.OuterRingFittingThermalResults":
        """mastapy.bearings.bearing_results.rolling.fitting.OuterRingFittingThermalResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterRingFittingAtAssembly

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def outer_ring_fitting_at_operating_conditions(
        self: Self,
    ) -> "_2114.OuterRingFittingThermalResults":
        """mastapy.bearings.bearing_results.rolling.fitting.OuterRingFittingThermalResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterRingFittingAtOperatingConditions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def skf_module_results(self: Self) -> "_2100.SKFModuleResults":
        """mastapy.bearings.bearing_results.rolling.skf_module.SKFModuleResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SKFModuleResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def all_mounting_results(self: Self) -> "List[_2115.RingFittingThermalResults]":
        """List[mastapy.bearings.bearing_results.rolling.fitting.RingFittingThermalResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllMountingResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def rows(self: Self) -> "List[_2036.LoadedRollingBearingRow]":
        """List[mastapy.bearings.bearing_results.rolling.LoadedRollingBearingRow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rows

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedRollingBearingResults._Cast_LoadedRollingBearingResults":
        return self._Cast_LoadedRollingBearingResults(self)
