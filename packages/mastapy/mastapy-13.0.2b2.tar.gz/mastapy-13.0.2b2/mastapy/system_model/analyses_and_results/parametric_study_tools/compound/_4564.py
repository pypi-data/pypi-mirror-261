"""TorqueConverterPumpCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4484,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "TorqueConverterPumpCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2610
    from mastapy.system_model.analyses_and_results.static_loads import _6977
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4435
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4522,
        _4470,
        _4524,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterPumpCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="TorqueConverterPumpCompoundParametricStudyTool")


class TorqueConverterPumpCompoundParametricStudyTool(
    _4484.CouplingHalfCompoundParametricStudyTool
):
    """TorqueConverterPumpCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_PUMP_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterPumpCompoundParametricStudyTool"
    )

    class _Cast_TorqueConverterPumpCompoundParametricStudyTool:
        """Special nested class for casting TorqueConverterPumpCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "TorqueConverterPumpCompoundParametricStudyTool._Cast_TorqueConverterPumpCompoundParametricStudyTool",
            parent: "TorqueConverterPumpCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_parametric_study_tool(
            self: "TorqueConverterPumpCompoundParametricStudyTool._Cast_TorqueConverterPumpCompoundParametricStudyTool",
        ) -> "_4484.CouplingHalfCompoundParametricStudyTool":
            return self._parent._cast(_4484.CouplingHalfCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "TorqueConverterPumpCompoundParametricStudyTool._Cast_TorqueConverterPumpCompoundParametricStudyTool",
        ) -> "_4522.MountableComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4522,
            )

            return self._parent._cast(
                _4522.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "TorqueConverterPumpCompoundParametricStudyTool._Cast_TorqueConverterPumpCompoundParametricStudyTool",
        ) -> "_4470.ComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4470,
            )

            return self._parent._cast(_4470.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "TorqueConverterPumpCompoundParametricStudyTool._Cast_TorqueConverterPumpCompoundParametricStudyTool",
        ) -> "_4524.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4524,
            )

            return self._parent._cast(_4524.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "TorqueConverterPumpCompoundParametricStudyTool._Cast_TorqueConverterPumpCompoundParametricStudyTool",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterPumpCompoundParametricStudyTool._Cast_TorqueConverterPumpCompoundParametricStudyTool",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterPumpCompoundParametricStudyTool._Cast_TorqueConverterPumpCompoundParametricStudyTool",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def torque_converter_pump_compound_parametric_study_tool(
            self: "TorqueConverterPumpCompoundParametricStudyTool._Cast_TorqueConverterPumpCompoundParametricStudyTool",
        ) -> "TorqueConverterPumpCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "TorqueConverterPumpCompoundParametricStudyTool._Cast_TorqueConverterPumpCompoundParametricStudyTool",
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
        self: Self,
        instance_to_wrap: "TorqueConverterPumpCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2610.TorqueConverterPump":
        """mastapy.system_model.part_model.couplings.TorqueConverterPump

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def properties_changing_all_load_cases(
        self: Self,
    ) -> "_6977.TorqueConverterPumpLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterPumpLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PropertiesChangingAllLoadCases

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4435.TorqueConverterPumpParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.TorqueConverterPumpParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4435.TorqueConverterPumpParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.TorqueConverterPumpParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "TorqueConverterPumpCompoundParametricStudyTool._Cast_TorqueConverterPumpCompoundParametricStudyTool":
        return self._Cast_TorqueConverterPumpCompoundParametricStudyTool(self)
