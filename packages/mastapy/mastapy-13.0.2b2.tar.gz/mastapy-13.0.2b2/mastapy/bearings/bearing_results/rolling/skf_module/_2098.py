"""SKFCalculationResult"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SKF_CALCULATION_RESULT = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule", "SKFCalculationResult"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling.skf_module import (
        _2078,
        _2080,
        _2081,
        _2082,
        _2083,
        _2085,
        _2088,
        _2089,
        _2090,
        _2091,
        _2092,
        _2093,
        _2101,
        _2102,
    )


__docformat__ = "restructuredtext en"
__all__ = ("SKFCalculationResult",)


Self = TypeVar("Self", bound="SKFCalculationResult")


class SKFCalculationResult(_0.APIBase):
    """SKFCalculationResult

    This is a mastapy class.
    """

    TYPE = _SKF_CALCULATION_RESULT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SKFCalculationResult")

    class _Cast_SKFCalculationResult:
        """Special nested class for casting SKFCalculationResult to subclasses."""

        def __init__(
            self: "SKFCalculationResult._Cast_SKFCalculationResult",
            parent: "SKFCalculationResult",
        ):
            self._parent = parent

        @property
        def adjusted_speed(
            self: "SKFCalculationResult._Cast_SKFCalculationResult",
        ) -> "_2078.AdjustedSpeed":
            from mastapy.bearings.bearing_results.rolling.skf_module import _2078

            return self._parent._cast(_2078.AdjustedSpeed)

        @property
        def bearing_loads(
            self: "SKFCalculationResult._Cast_SKFCalculationResult",
        ) -> "_2080.BearingLoads":
            from mastapy.bearings.bearing_results.rolling.skf_module import _2080

            return self._parent._cast(_2080.BearingLoads)

        @property
        def bearing_rating_life(
            self: "SKFCalculationResult._Cast_SKFCalculationResult",
        ) -> "_2081.BearingRatingLife":
            from mastapy.bearings.bearing_results.rolling.skf_module import _2081

            return self._parent._cast(_2081.BearingRatingLife)

        @property
        def dynamic_axial_load_carrying_capacity(
            self: "SKFCalculationResult._Cast_SKFCalculationResult",
        ) -> "_2082.DynamicAxialLoadCarryingCapacity":
            from mastapy.bearings.bearing_results.rolling.skf_module import _2082

            return self._parent._cast(_2082.DynamicAxialLoadCarryingCapacity)

        @property
        def frequencies(
            self: "SKFCalculationResult._Cast_SKFCalculationResult",
        ) -> "_2083.Frequencies":
            from mastapy.bearings.bearing_results.rolling.skf_module import _2083

            return self._parent._cast(_2083.Frequencies)

        @property
        def friction(
            self: "SKFCalculationResult._Cast_SKFCalculationResult",
        ) -> "_2085.Friction":
            from mastapy.bearings.bearing_results.rolling.skf_module import _2085

            return self._parent._cast(_2085.Friction)

        @property
        def grease(
            self: "SKFCalculationResult._Cast_SKFCalculationResult",
        ) -> "_2088.Grease":
            from mastapy.bearings.bearing_results.rolling.skf_module import _2088

            return self._parent._cast(_2088.Grease)

        @property
        def grease_life_and_relubrication_interval(
            self: "SKFCalculationResult._Cast_SKFCalculationResult",
        ) -> "_2089.GreaseLifeAndRelubricationInterval":
            from mastapy.bearings.bearing_results.rolling.skf_module import _2089

            return self._parent._cast(_2089.GreaseLifeAndRelubricationInterval)

        @property
        def grease_quantity(
            self: "SKFCalculationResult._Cast_SKFCalculationResult",
        ) -> "_2090.GreaseQuantity":
            from mastapy.bearings.bearing_results.rolling.skf_module import _2090

            return self._parent._cast(_2090.GreaseQuantity)

        @property
        def initial_fill(
            self: "SKFCalculationResult._Cast_SKFCalculationResult",
        ) -> "_2091.InitialFill":
            from mastapy.bearings.bearing_results.rolling.skf_module import _2091

            return self._parent._cast(_2091.InitialFill)

        @property
        def life_model(
            self: "SKFCalculationResult._Cast_SKFCalculationResult",
        ) -> "_2092.LifeModel":
            from mastapy.bearings.bearing_results.rolling.skf_module import _2092

            return self._parent._cast(_2092.LifeModel)

        @property
        def minimum_load(
            self: "SKFCalculationResult._Cast_SKFCalculationResult",
        ) -> "_2093.MinimumLoad":
            from mastapy.bearings.bearing_results.rolling.skf_module import _2093

            return self._parent._cast(_2093.MinimumLoad)

        @property
        def static_safety_factors(
            self: "SKFCalculationResult._Cast_SKFCalculationResult",
        ) -> "_2101.StaticSafetyFactors":
            from mastapy.bearings.bearing_results.rolling.skf_module import _2101

            return self._parent._cast(_2101.StaticSafetyFactors)

        @property
        def viscosities(
            self: "SKFCalculationResult._Cast_SKFCalculationResult",
        ) -> "_2102.Viscosities":
            from mastapy.bearings.bearing_results.rolling.skf_module import _2102

            return self._parent._cast(_2102.Viscosities)

        @property
        def skf_calculation_result(
            self: "SKFCalculationResult._Cast_SKFCalculationResult",
        ) -> "SKFCalculationResult":
            return self._parent

        def __getattr__(
            self: "SKFCalculationResult._Cast_SKFCalculationResult", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SKFCalculationResult.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def cast_to(self: Self) -> "SKFCalculationResult._Cast_SKFCalculationResult":
        return self._Cast_SKFCalculationResult(self)
