"""TorqueConverterPumpParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4336
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "TorqueConverterPumpParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2610
    from mastapy.system_model.analyses_and_results.static_loads import _6977
    from mastapy.system_model.analyses_and_results.system_deflections import _2831
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4383,
        _4323,
        _4395,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterPumpParametricStudyTool",)


Self = TypeVar("Self", bound="TorqueConverterPumpParametricStudyTool")


class TorqueConverterPumpParametricStudyTool(_4336.CouplingHalfParametricStudyTool):
    """TorqueConverterPumpParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_PUMP_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterPumpParametricStudyTool"
    )

    class _Cast_TorqueConverterPumpParametricStudyTool:
        """Special nested class for casting TorqueConverterPumpParametricStudyTool to subclasses."""

        def __init__(
            self: "TorqueConverterPumpParametricStudyTool._Cast_TorqueConverterPumpParametricStudyTool",
            parent: "TorqueConverterPumpParametricStudyTool",
        ):
            self._parent = parent

        @property
        def coupling_half_parametric_study_tool(
            self: "TorqueConverterPumpParametricStudyTool._Cast_TorqueConverterPumpParametricStudyTool",
        ) -> "_4336.CouplingHalfParametricStudyTool":
            return self._parent._cast(_4336.CouplingHalfParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "TorqueConverterPumpParametricStudyTool._Cast_TorqueConverterPumpParametricStudyTool",
        ) -> "_4383.MountableComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4383,
            )

            return self._parent._cast(_4383.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "TorqueConverterPumpParametricStudyTool._Cast_TorqueConverterPumpParametricStudyTool",
        ) -> "_4323.ComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4323,
            )

            return self._parent._cast(_4323.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "TorqueConverterPumpParametricStudyTool._Cast_TorqueConverterPumpParametricStudyTool",
        ) -> "_4395.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4395,
            )

            return self._parent._cast(_4395.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "TorqueConverterPumpParametricStudyTool._Cast_TorqueConverterPumpParametricStudyTool",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterPumpParametricStudyTool._Cast_TorqueConverterPumpParametricStudyTool",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterPumpParametricStudyTool._Cast_TorqueConverterPumpParametricStudyTool",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterPumpParametricStudyTool._Cast_TorqueConverterPumpParametricStudyTool",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def torque_converter_pump_parametric_study_tool(
            self: "TorqueConverterPumpParametricStudyTool._Cast_TorqueConverterPumpParametricStudyTool",
        ) -> "TorqueConverterPumpParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "TorqueConverterPumpParametricStudyTool._Cast_TorqueConverterPumpParametricStudyTool",
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
        self: Self, instance_to_wrap: "TorqueConverterPumpParametricStudyTool.TYPE"
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
    def component_load_case(self: Self) -> "_6977.TorqueConverterPumpLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterPumpLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_system_deflection_results(
        self: Self,
    ) -> "List[_2831.TorqueConverterPumpSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterPumpSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "TorqueConverterPumpParametricStudyTool._Cast_TorqueConverterPumpParametricStudyTool":
        return self._Cast_TorqueConverterPumpParametricStudyTool(self)
