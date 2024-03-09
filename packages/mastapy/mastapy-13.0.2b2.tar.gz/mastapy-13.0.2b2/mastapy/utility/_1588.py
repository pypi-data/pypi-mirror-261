"""IndependentReportablePropertiesBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Generic

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INDEPENDENT_REPORTABLE_PROPERTIES_BASE = python_net_import(
    "SMT.MastaAPI.Utility", "IndependentReportablePropertiesBase"
)

if TYPE_CHECKING:
    from mastapy.materials.efficiency import _298
    from mastapy.geometry import _309
    from mastapy.gears import _346
    from mastapy.gears.gear_designs.cylindrical import (
        _1021,
        _1052,
        _1060,
        _1061,
        _1064,
        _1071,
        _1079,
        _1081,
        _1085,
        _1089,
    )
    from mastapy.electric_machines import _1262
    from mastapy.electric_machines.load_cases_and_analyses import _1379
    from mastapy.math_utility.measured_data import _1568, _1569, _1570
    from mastapy.bearings.tolerances import _1920
    from mastapy.bearings.bearing_results import _1947
    from mastapy.bearings.bearing_results.rolling import _1978, _2072
    from mastapy.system_model.analyses_and_results.static_loads import _6813


__docformat__ = "restructuredtext en"
__all__ = ("IndependentReportablePropertiesBase",)


Self = TypeVar("Self", bound="IndependentReportablePropertiesBase")
T = TypeVar("T", bound="IndependentReportablePropertiesBase")


class IndependentReportablePropertiesBase(_0.APIBase, Generic[T]):
    """IndependentReportablePropertiesBase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _INDEPENDENT_REPORTABLE_PROPERTIES_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_IndependentReportablePropertiesBase")

    class _Cast_IndependentReportablePropertiesBase:
        """Special nested class for casting IndependentReportablePropertiesBase to subclasses."""

        def __init__(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
            parent: "IndependentReportablePropertiesBase",
        ):
            self._parent = parent

        @property
        def oil_pump_detail(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_298.OilPumpDetail":
            from mastapy.materials.efficiency import _298

            return self._parent._cast(_298.OilPumpDetail)

        @property
        def packaging_limits(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_309.PackagingLimits":
            from mastapy.geometry import _309

            return self._parent._cast(_309.PackagingLimits)

        @property
        def specification_for_the_effect_of_oil_kinematic_viscosity(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_346.SpecificationForTheEffectOfOilKinematicViscosity":
            from mastapy.gears import _346

            return self._parent._cast(
                _346.SpecificationForTheEffectOfOilKinematicViscosity
            )

        @property
        def cylindrical_gear_micro_geometry_settings(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1021.CylindricalGearMicroGeometrySettings":
            from mastapy.gears.gear_designs.cylindrical import _1021

            return self._parent._cast(_1021.CylindricalGearMicroGeometrySettings)

        @property
        def hardened_material_properties(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1052.HardenedMaterialProperties":
            from mastapy.gears.gear_designs.cylindrical import _1052

            return self._parent._cast(_1052.HardenedMaterialProperties)

        @property
        def ltca_load_case_modifiable_settings(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1060.LTCALoadCaseModifiableSettings":
            from mastapy.gears.gear_designs.cylindrical import _1060

            return self._parent._cast(_1060.LTCALoadCaseModifiableSettings)

        @property
        def ltca_settings(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1061.LTCASettings":
            from mastapy.gears.gear_designs.cylindrical import _1061

            return self._parent._cast(_1061.LTCASettings)

        @property
        def micropitting(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1064.Micropitting":
            from mastapy.gears.gear_designs.cylindrical import _1064

            return self._parent._cast(_1064.Micropitting)

        @property
        def scuffing(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1071.Scuffing":
            from mastapy.gears.gear_designs.cylindrical import _1071

            return self._parent._cast(_1071.Scuffing)

        @property
        def surface_roughness(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1079.SurfaceRoughness":
            from mastapy.gears.gear_designs.cylindrical import _1079

            return self._parent._cast(_1079.SurfaceRoughness)

        @property
        def tiff_analysis_settings(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1081.TiffAnalysisSettings":
            from mastapy.gears.gear_designs.cylindrical import _1081

            return self._parent._cast(_1081.TiffAnalysisSettings)

        @property
        def tooth_flank_fracture_analysis_settings(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1085.ToothFlankFractureAnalysisSettings":
            from mastapy.gears.gear_designs.cylindrical import _1085

            return self._parent._cast(_1085.ToothFlankFractureAnalysisSettings)

        @property
        def usage(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1089.Usage":
            from mastapy.gears.gear_designs.cylindrical import _1089

            return self._parent._cast(_1089.Usage)

        @property
        def eccentricity(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1262.Eccentricity":
            from mastapy.electric_machines import _1262

            return self._parent._cast(_1262.Eccentricity)

        @property
        def temperatures(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1379.Temperatures":
            from mastapy.electric_machines.load_cases_and_analyses import _1379

            return self._parent._cast(_1379.Temperatures)

        @property
        def lookup_table_base(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1568.LookupTableBase":
            from mastapy.math_utility.measured_data import _1568

            return self._parent._cast(_1568.LookupTableBase)

        @property
        def onedimensional_function_lookup_table(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1569.OnedimensionalFunctionLookupTable":
            from mastapy.math_utility.measured_data import _1569

            return self._parent._cast(_1569.OnedimensionalFunctionLookupTable)

        @property
        def twodimensional_function_lookup_table(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1570.TwodimensionalFunctionLookupTable":
            from mastapy.math_utility.measured_data import _1570

            return self._parent._cast(_1570.TwodimensionalFunctionLookupTable)

        @property
        def roundness_specification(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1920.RoundnessSpecification":
            from mastapy.bearings.tolerances import _1920

            return self._parent._cast(_1920.RoundnessSpecification)

        @property
        def equivalent_load_factors(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1947.EquivalentLoadFactors":
            from mastapy.bearings.bearing_results import _1947

            return self._parent._cast(_1947.EquivalentLoadFactors)

        @property
        def iso14179_settings_per_bearing_type(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1978.ISO14179SettingsPerBearingType":
            from mastapy.bearings.bearing_results.rolling import _1978

            return self._parent._cast(_1978.ISO14179SettingsPerBearingType)

        @property
        def rolling_bearing_friction_coefficients(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_2072.RollingBearingFrictionCoefficients":
            from mastapy.bearings.bearing_results.rolling import _2072

            return self._parent._cast(_2072.RollingBearingFrictionCoefficients)

        @property
        def additional_acceleration_options(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_6813.AdditionalAccelerationOptions":
            from mastapy.system_model.analyses_and_results.static_loads import _6813

            return self._parent._cast(_6813.AdditionalAccelerationOptions)

        @property
        def independent_reportable_properties_base(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "IndependentReportablePropertiesBase":
            return self._parent

        def __getattr__(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
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
        self: Self, instance_to_wrap: "IndependentReportablePropertiesBase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> (
        "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase"
    ):
        return self._Cast_IndependentReportablePropertiesBase(self)
