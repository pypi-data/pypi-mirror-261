"""ColumnInputOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import list_with_selected_item
from mastapy.utility.file_access_helpers import _1819
from mastapy._internal import constructor, conversion
from mastapy.utility.units_and_measurements import _1612
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COLUMN_INPUT_OPTIONS = python_net_import(
    "SMT.MastaAPI.UtilityGUI", "ColumnInputOptions"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears.supercharger_rotor_set import (
        _2557,
        _2558,
        _2559,
        _2562,
    )
    from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
        _6992,
        _6993,
        _6995,
        _6996,
        _6997,
        _6998,
        _7000,
        _7001,
        _7002,
        _7003,
        _7005,
        _7006,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ColumnInputOptions",)


Self = TypeVar("Self", bound="ColumnInputOptions")


class ColumnInputOptions(_0.APIBase):
    """ColumnInputOptions

    This is a mastapy class.
    """

    TYPE = _COLUMN_INPUT_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ColumnInputOptions")

    class _Cast_ColumnInputOptions:
        """Special nested class for casting ColumnInputOptions to subclasses."""

        def __init__(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
            parent: "ColumnInputOptions",
        ):
            self._parent = parent

        @property
        def boost_pressure_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ) -> "_2557.BoostPressureInputOptions":
            from mastapy.system_model.part_model.gears.supercharger_rotor_set import (
                _2557,
            )

            return self._parent._cast(_2557.BoostPressureInputOptions)

        @property
        def input_power_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ) -> "_2558.InputPowerInputOptions":
            from mastapy.system_model.part_model.gears.supercharger_rotor_set import (
                _2558,
            )

            return self._parent._cast(_2558.InputPowerInputOptions)

        @property
        def pressure_ratio_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ) -> "_2559.PressureRatioInputOptions":
            from mastapy.system_model.part_model.gears.supercharger_rotor_set import (
                _2559,
            )

            return self._parent._cast(_2559.PressureRatioInputOptions)

        @property
        def rotor_speed_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ) -> "_2562.RotorSpeedInputOptions":
            from mastapy.system_model.part_model.gears.supercharger_rotor_set import (
                _2562,
            )

            return self._parent._cast(_2562.RotorSpeedInputOptions)

        @property
        def boost_pressure_load_case_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ) -> "_6992.BoostPressureLoadCaseInputOptions":
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _6992,
            )

            return self._parent._cast(_6992.BoostPressureLoadCaseInputOptions)

        @property
        def design_state_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ) -> "_6993.DesignStateOptions":
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _6993,
            )

            return self._parent._cast(_6993.DesignStateOptions)

        @property
        def force_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ) -> "_6995.ForceInputOptions":
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _6995,
            )

            return self._parent._cast(_6995.ForceInputOptions)

        @property
        def gear_ratio_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ) -> "_6996.GearRatioInputOptions":
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _6996,
            )

            return self._parent._cast(_6996.GearRatioInputOptions)

        @property
        def load_case_name_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ) -> "_6997.LoadCaseNameOptions":
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _6997,
            )

            return self._parent._cast(_6997.LoadCaseNameOptions)

        @property
        def moment_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ) -> "_6998.MomentInputOptions":
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _6998,
            )

            return self._parent._cast(_6998.MomentInputOptions)

        @property
        def point_load_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ) -> "_7000.PointLoadInputOptions":
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _7000,
            )

            return self._parent._cast(_7000.PointLoadInputOptions)

        @property
        def power_load_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ) -> "_7001.PowerLoadInputOptions":
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _7001,
            )

            return self._parent._cast(_7001.PowerLoadInputOptions)

        @property
        def ramp_or_steady_state_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ) -> "_7002.RampOrSteadyStateInputOptions":
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _7002,
            )

            return self._parent._cast(_7002.RampOrSteadyStateInputOptions)

        @property
        def speed_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ) -> "_7003.SpeedInputOptions":
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _7003,
            )

            return self._parent._cast(_7003.SpeedInputOptions)

        @property
        def time_step_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ) -> "_7005.TimeStepInputOptions":
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _7005,
            )

            return self._parent._cast(_7005.TimeStepInputOptions)

        @property
        def torque_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ) -> "_7006.TorqueInputOptions":
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _7006,
            )

            return self._parent._cast(_7006.TorqueInputOptions)

        @property
        def column_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ) -> "ColumnInputOptions":
            return self._parent

        def __getattr__(self: "ColumnInputOptions._Cast_ColumnInputOptions", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ColumnInputOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def column(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_ColumnTitle":
        """ListWithSelectedItem[mastapy.utility.file_access_helpers.ColumnTitle]"""
        temp = self.wrapped.Column

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_ColumnTitle",
        )(temp)

    @column.setter
    @enforce_parameter_types
    def column(self: Self, value: "_1819.ColumnTitle"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_ColumnTitle.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_ColumnTitle.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.Column = value

    @property
    def unit(self: Self) -> "list_with_selected_item.ListWithSelectedItem_Unit":
        """ListWithSelectedItem[mastapy.utility.units_and_measurements.Unit]"""
        temp = self.wrapped.Unit

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_Unit",
        )(temp)

    @unit.setter
    @enforce_parameter_types
    def unit(self: Self, value: "_1612.Unit"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_Unit.wrapper_type()
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.Unit = value

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
    def cast_to(self: Self) -> "ColumnInputOptions._Cast_ColumnInputOptions":
        return self._Cast_ColumnInputOptions(self)
