"""TorqueConverterTurbineParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4336
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "TorqueConverterTurbineParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2612
    from mastapy.system_model.analyses_and_results.static_loads import _6978
    from mastapy.system_model.analyses_and_results.system_deflections import _2833
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4383,
        _4323,
        _4395,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterTurbineParametricStudyTool",)


Self = TypeVar("Self", bound="TorqueConverterTurbineParametricStudyTool")


class TorqueConverterTurbineParametricStudyTool(_4336.CouplingHalfParametricStudyTool):
    """TorqueConverterTurbineParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterTurbineParametricStudyTool"
    )

    class _Cast_TorqueConverterTurbineParametricStudyTool:
        """Special nested class for casting TorqueConverterTurbineParametricStudyTool to subclasses."""

        def __init__(
            self: "TorqueConverterTurbineParametricStudyTool._Cast_TorqueConverterTurbineParametricStudyTool",
            parent: "TorqueConverterTurbineParametricStudyTool",
        ):
            self._parent = parent

        @property
        def coupling_half_parametric_study_tool(
            self: "TorqueConverterTurbineParametricStudyTool._Cast_TorqueConverterTurbineParametricStudyTool",
        ) -> "_4336.CouplingHalfParametricStudyTool":
            return self._parent._cast(_4336.CouplingHalfParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "TorqueConverterTurbineParametricStudyTool._Cast_TorqueConverterTurbineParametricStudyTool",
        ) -> "_4383.MountableComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4383,
            )

            return self._parent._cast(_4383.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "TorqueConverterTurbineParametricStudyTool._Cast_TorqueConverterTurbineParametricStudyTool",
        ) -> "_4323.ComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4323,
            )

            return self._parent._cast(_4323.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "TorqueConverterTurbineParametricStudyTool._Cast_TorqueConverterTurbineParametricStudyTool",
        ) -> "_4395.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4395,
            )

            return self._parent._cast(_4395.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "TorqueConverterTurbineParametricStudyTool._Cast_TorqueConverterTurbineParametricStudyTool",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterTurbineParametricStudyTool._Cast_TorqueConverterTurbineParametricStudyTool",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterTurbineParametricStudyTool._Cast_TorqueConverterTurbineParametricStudyTool",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterTurbineParametricStudyTool._Cast_TorqueConverterTurbineParametricStudyTool",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def torque_converter_turbine_parametric_study_tool(
            self: "TorqueConverterTurbineParametricStudyTool._Cast_TorqueConverterTurbineParametricStudyTool",
        ) -> "TorqueConverterTurbineParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "TorqueConverterTurbineParametricStudyTool._Cast_TorqueConverterTurbineParametricStudyTool",
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
        self: Self, instance_to_wrap: "TorqueConverterTurbineParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2612.TorqueConverterTurbine":
        """mastapy.system_model.part_model.couplings.TorqueConverterTurbine

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6978.TorqueConverterTurbineLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase

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
    ) -> "List[_2833.TorqueConverterTurbineSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterTurbineSystemDeflection]

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
    ) -> "TorqueConverterTurbineParametricStudyTool._Cast_TorqueConverterTurbineParametricStudyTool":
        return self._Cast_TorqueConverterTurbineParametricStudyTool(self)
