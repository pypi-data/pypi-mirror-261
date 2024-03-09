"""BearingDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_DESIGN = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns", "BearingDesign"
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1520
    from mastapy.bearings.bearing_designs import _2133, _2134, _2135, _2136
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
    from mastapy.bearings.bearing_designs.concept import _2199, _2200, _2201


__docformat__ = "restructuredtext en"
__all__ = ("BearingDesign",)


Self = TypeVar("Self", bound="BearingDesign")


class BearingDesign(_0.APIBase):
    """BearingDesign

    This is a mastapy class.
    """

    TYPE = _BEARING_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BearingDesign")

    class _Cast_BearingDesign:
        """Special nested class for casting BearingDesign to subclasses."""

        def __init__(
            self: "BearingDesign._Cast_BearingDesign", parent: "BearingDesign"
        ):
            self._parent = parent

        @property
        def detailed_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2133.DetailedBearing":
            from mastapy.bearings.bearing_designs import _2133

            return self._parent._cast(_2133.DetailedBearing)

        @property
        def dummy_rolling_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2134.DummyRollingBearing":
            from mastapy.bearings.bearing_designs import _2134

            return self._parent._cast(_2134.DummyRollingBearing)

        @property
        def linear_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2135.LinearBearing":
            from mastapy.bearings.bearing_designs import _2135

            return self._parent._cast(_2135.LinearBearing)

        @property
        def non_linear_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2136.NonLinearBearing":
            from mastapy.bearings.bearing_designs import _2136

            return self._parent._cast(_2136.NonLinearBearing)

        @property
        def angular_contact_ball_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2137.AngularContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2137

            return self._parent._cast(_2137.AngularContactBallBearing)

        @property
        def angular_contact_thrust_ball_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2138.AngularContactThrustBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2138

            return self._parent._cast(_2138.AngularContactThrustBallBearing)

        @property
        def asymmetric_spherical_roller_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2139.AsymmetricSphericalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2139

            return self._parent._cast(_2139.AsymmetricSphericalRollerBearing)

        @property
        def axial_thrust_cylindrical_roller_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2140.AxialThrustCylindricalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2140

            return self._parent._cast(_2140.AxialThrustCylindricalRollerBearing)

        @property
        def axial_thrust_needle_roller_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2141.AxialThrustNeedleRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2141

            return self._parent._cast(_2141.AxialThrustNeedleRollerBearing)

        @property
        def ball_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2142.BallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2142

            return self._parent._cast(_2142.BallBearing)

        @property
        def barrel_roller_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2144.BarrelRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2144

            return self._parent._cast(_2144.BarrelRollerBearing)

        @property
        def crossed_roller_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2150.CrossedRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2150

            return self._parent._cast(_2150.CrossedRollerBearing)

        @property
        def cylindrical_roller_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2151.CylindricalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2151

            return self._parent._cast(_2151.CylindricalRollerBearing)

        @property
        def deep_groove_ball_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2152.DeepGrooveBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2152

            return self._parent._cast(_2152.DeepGrooveBallBearing)

        @property
        def four_point_contact_ball_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2156.FourPointContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2156

            return self._parent._cast(_2156.FourPointContactBallBearing)

        @property
        def multi_point_contact_ball_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2161.MultiPointContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2161

            return self._parent._cast(_2161.MultiPointContactBallBearing)

        @property
        def needle_roller_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2162.NeedleRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2162

            return self._parent._cast(_2162.NeedleRollerBearing)

        @property
        def non_barrel_roller_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2163.NonBarrelRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2163

            return self._parent._cast(_2163.NonBarrelRollerBearing)

        @property
        def roller_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2164.RollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2164

            return self._parent._cast(_2164.RollerBearing)

        @property
        def rolling_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2167.RollingBearing":
            from mastapy.bearings.bearing_designs.rolling import _2167

            return self._parent._cast(_2167.RollingBearing)

        @property
        def self_aligning_ball_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2168.SelfAligningBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2168

            return self._parent._cast(_2168.SelfAligningBallBearing)

        @property
        def spherical_roller_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2171.SphericalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2171

            return self._parent._cast(_2171.SphericalRollerBearing)

        @property
        def spherical_roller_thrust_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2172.SphericalRollerThrustBearing":
            from mastapy.bearings.bearing_designs.rolling import _2172

            return self._parent._cast(_2172.SphericalRollerThrustBearing)

        @property
        def taper_roller_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2173.TaperRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2173

            return self._parent._cast(_2173.TaperRollerBearing)

        @property
        def three_point_contact_ball_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2174.ThreePointContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2174

            return self._parent._cast(_2174.ThreePointContactBallBearing)

        @property
        def thrust_ball_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2175.ThrustBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2175

            return self._parent._cast(_2175.ThrustBallBearing)

        @property
        def toroidal_roller_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2176.ToroidalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2176

            return self._parent._cast(_2176.ToroidalRollerBearing)

        @property
        def pad_fluid_film_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2189.PadFluidFilmBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2189

            return self._parent._cast(_2189.PadFluidFilmBearing)

        @property
        def plain_grease_filled_journal_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2191.PlainGreaseFilledJournalBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2191

            return self._parent._cast(_2191.PlainGreaseFilledJournalBearing)

        @property
        def plain_journal_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2193.PlainJournalBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2193

            return self._parent._cast(_2193.PlainJournalBearing)

        @property
        def plain_oil_fed_journal_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2195.PlainOilFedJournalBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2195

            return self._parent._cast(_2195.PlainOilFedJournalBearing)

        @property
        def tilting_pad_journal_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2196.TiltingPadJournalBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2196

            return self._parent._cast(_2196.TiltingPadJournalBearing)

        @property
        def tilting_pad_thrust_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2197.TiltingPadThrustBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2197

            return self._parent._cast(_2197.TiltingPadThrustBearing)

        @property
        def concept_axial_clearance_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2199.ConceptAxialClearanceBearing":
            from mastapy.bearings.bearing_designs.concept import _2199

            return self._parent._cast(_2199.ConceptAxialClearanceBearing)

        @property
        def concept_clearance_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2200.ConceptClearanceBearing":
            from mastapy.bearings.bearing_designs.concept import _2200

            return self._parent._cast(_2200.ConceptClearanceBearing)

        @property
        def concept_radial_clearance_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2201.ConceptRadialClearanceBearing":
            from mastapy.bearings.bearing_designs.concept import _2201

            return self._parent._cast(_2201.ConceptRadialClearanceBearing)

        @property
        def bearing_design(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "BearingDesign":
            return self._parent

        def __getattr__(self: "BearingDesign._Cast_BearingDesign", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BearingDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bore(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Bore

        if temp is None:
            return 0.0

        return temp

    @bore.setter
    @enforce_parameter_types
    def bore(self: Self, value: "float"):
        self.wrapped.Bore = float(value) if value is not None else 0.0

    @property
    def mass(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Mass

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @mass.setter
    @enforce_parameter_types
    def mass(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Mass = value

    @property
    def outer_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OuterDiameter

        if temp is None:
            return 0.0

        return temp

    @outer_diameter.setter
    @enforce_parameter_types
    def outer_diameter(self: Self, value: "float"):
        self.wrapped.OuterDiameter = float(value) if value is not None else 0.0

    @property
    def type_(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Type

        if temp is None:
            return ""

        return temp

    @property
    def width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Width

        if temp is None:
            return 0.0

        return temp

    @width.setter
    @enforce_parameter_types
    def width(self: Self, value: "float"):
        self.wrapped.Width = float(value) if value is not None else 0.0

    @property
    def mass_properties_of_elements_from_geometry(self: Self) -> "_1520.MassProperties":
        """mastapy.math_utility.MassProperties

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassPropertiesOfElementsFromGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mass_properties_of_inner_ring_from_geometry(
        self: Self,
    ) -> "_1520.MassProperties":
        """mastapy.math_utility.MassProperties

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassPropertiesOfInnerRingFromGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mass_properties_of_outer_ring_from_geometry(
        self: Self,
    ) -> "_1520.MassProperties":
        """mastapy.math_utility.MassProperties

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassPropertiesOfOuterRingFromGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def total_mass_properties(self: Self) -> "_1520.MassProperties":
        """mastapy.math_utility.MassProperties

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalMassProperties

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(self: Self) -> "BearingDesign._Cast_BearingDesign":
        return self._Cast_BearingDesign(self)
