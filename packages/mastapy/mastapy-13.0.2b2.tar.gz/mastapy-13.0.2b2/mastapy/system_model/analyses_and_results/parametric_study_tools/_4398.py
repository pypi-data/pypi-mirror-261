"""PartToPartShearCouplingParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4337
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "PartToPartShearCouplingParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2590
    from mastapy.system_model.analyses_and_results.static_loads import _6934
    from mastapy.system_model.analyses_and_results.system_deflections import _2790
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4414,
        _4298,
        _4395,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingParametricStudyTool",)


Self = TypeVar("Self", bound="PartToPartShearCouplingParametricStudyTool")


class PartToPartShearCouplingParametricStudyTool(_4337.CouplingParametricStudyTool):
    """PartToPartShearCouplingParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingParametricStudyTool"
    )

    class _Cast_PartToPartShearCouplingParametricStudyTool:
        """Special nested class for casting PartToPartShearCouplingParametricStudyTool to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingParametricStudyTool._Cast_PartToPartShearCouplingParametricStudyTool",
            parent: "PartToPartShearCouplingParametricStudyTool",
        ):
            self._parent = parent

        @property
        def coupling_parametric_study_tool(
            self: "PartToPartShearCouplingParametricStudyTool._Cast_PartToPartShearCouplingParametricStudyTool",
        ) -> "_4337.CouplingParametricStudyTool":
            return self._parent._cast(_4337.CouplingParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(
            self: "PartToPartShearCouplingParametricStudyTool._Cast_PartToPartShearCouplingParametricStudyTool",
        ) -> "_4414.SpecialisedAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4414,
            )

            return self._parent._cast(_4414.SpecialisedAssemblyParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "PartToPartShearCouplingParametricStudyTool._Cast_PartToPartShearCouplingParametricStudyTool",
        ) -> "_4298.AbstractAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4298,
            )

            return self._parent._cast(_4298.AbstractAssemblyParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "PartToPartShearCouplingParametricStudyTool._Cast_PartToPartShearCouplingParametricStudyTool",
        ) -> "_4395.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4395,
            )

            return self._parent._cast(_4395.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "PartToPartShearCouplingParametricStudyTool._Cast_PartToPartShearCouplingParametricStudyTool",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartToPartShearCouplingParametricStudyTool._Cast_PartToPartShearCouplingParametricStudyTool",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingParametricStudyTool._Cast_PartToPartShearCouplingParametricStudyTool",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingParametricStudyTool._Cast_PartToPartShearCouplingParametricStudyTool",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_parametric_study_tool(
            self: "PartToPartShearCouplingParametricStudyTool._Cast_PartToPartShearCouplingParametricStudyTool",
        ) -> "PartToPartShearCouplingParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingParametricStudyTool._Cast_PartToPartShearCouplingParametricStudyTool",
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
        self: Self, instance_to_wrap: "PartToPartShearCouplingParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2590.PartToPartShearCoupling":
        """mastapy.system_model.part_model.couplings.PartToPartShearCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6934.PartToPartShearCouplingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_system_deflection_results(
        self: Self,
    ) -> "List[_2790.PartToPartShearCouplingSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.PartToPartShearCouplingSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblySystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PartToPartShearCouplingParametricStudyTool._Cast_PartToPartShearCouplingParametricStudyTool":
        return self._Cast_PartToPartShearCouplingParametricStudyTool(self)
