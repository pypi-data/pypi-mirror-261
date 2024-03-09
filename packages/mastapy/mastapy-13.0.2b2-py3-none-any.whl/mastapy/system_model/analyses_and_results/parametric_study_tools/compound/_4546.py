"""SpiralBevelGearSetCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4463,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "SpiralBevelGearSetCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2546
    from mastapy.system_model.analyses_and_results.static_loads import _6958
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4417
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4544,
        _4545,
        _4451,
        _4479,
        _4505,
        _4543,
        _4445,
        _4524,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearSetCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="SpiralBevelGearSetCompoundParametricStudyTool")


class SpiralBevelGearSetCompoundParametricStudyTool(
    _4463.BevelGearSetCompoundParametricStudyTool
):
    """SpiralBevelGearSetCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearSetCompoundParametricStudyTool"
    )

    class _Cast_SpiralBevelGearSetCompoundParametricStudyTool:
        """Special nested class for casting SpiralBevelGearSetCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "SpiralBevelGearSetCompoundParametricStudyTool._Cast_SpiralBevelGearSetCompoundParametricStudyTool",
            parent: "SpiralBevelGearSetCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_parametric_study_tool(
            self: "SpiralBevelGearSetCompoundParametricStudyTool._Cast_SpiralBevelGearSetCompoundParametricStudyTool",
        ) -> "_4463.BevelGearSetCompoundParametricStudyTool":
            return self._parent._cast(_4463.BevelGearSetCompoundParametricStudyTool)

        @property
        def agma_gleason_conical_gear_set_compound_parametric_study_tool(
            self: "SpiralBevelGearSetCompoundParametricStudyTool._Cast_SpiralBevelGearSetCompoundParametricStudyTool",
        ) -> "_4451.AGMAGleasonConicalGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4451,
            )

            return self._parent._cast(
                _4451.AGMAGleasonConicalGearSetCompoundParametricStudyTool
            )

        @property
        def conical_gear_set_compound_parametric_study_tool(
            self: "SpiralBevelGearSetCompoundParametricStudyTool._Cast_SpiralBevelGearSetCompoundParametricStudyTool",
        ) -> "_4479.ConicalGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4479,
            )

            return self._parent._cast(_4479.ConicalGearSetCompoundParametricStudyTool)

        @property
        def gear_set_compound_parametric_study_tool(
            self: "SpiralBevelGearSetCompoundParametricStudyTool._Cast_SpiralBevelGearSetCompoundParametricStudyTool",
        ) -> "_4505.GearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4505,
            )

            return self._parent._cast(_4505.GearSetCompoundParametricStudyTool)

        @property
        def specialised_assembly_compound_parametric_study_tool(
            self: "SpiralBevelGearSetCompoundParametricStudyTool._Cast_SpiralBevelGearSetCompoundParametricStudyTool",
        ) -> "_4543.SpecialisedAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4543,
            )

            return self._parent._cast(
                _4543.SpecialisedAssemblyCompoundParametricStudyTool
            )

        @property
        def abstract_assembly_compound_parametric_study_tool(
            self: "SpiralBevelGearSetCompoundParametricStudyTool._Cast_SpiralBevelGearSetCompoundParametricStudyTool",
        ) -> "_4445.AbstractAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4445,
            )

            return self._parent._cast(_4445.AbstractAssemblyCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "SpiralBevelGearSetCompoundParametricStudyTool._Cast_SpiralBevelGearSetCompoundParametricStudyTool",
        ) -> "_4524.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4524,
            )

            return self._parent._cast(_4524.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "SpiralBevelGearSetCompoundParametricStudyTool._Cast_SpiralBevelGearSetCompoundParametricStudyTool",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpiralBevelGearSetCompoundParametricStudyTool._Cast_SpiralBevelGearSetCompoundParametricStudyTool",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearSetCompoundParametricStudyTool._Cast_SpiralBevelGearSetCompoundParametricStudyTool",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_set_compound_parametric_study_tool(
            self: "SpiralBevelGearSetCompoundParametricStudyTool._Cast_SpiralBevelGearSetCompoundParametricStudyTool",
        ) -> "SpiralBevelGearSetCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearSetCompoundParametricStudyTool._Cast_SpiralBevelGearSetCompoundParametricStudyTool",
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
        instance_to_wrap: "SpiralBevelGearSetCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2546.SpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.SpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2546.SpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.SpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def properties_changing_all_load_cases(
        self: Self,
    ) -> "_6958.SpiralBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PropertiesChangingAllLoadCases

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4417.SpiralBevelGearSetParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.SpiralBevelGearSetParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_gears_compound_parametric_study_tool(
        self: Self,
    ) -> "List[_4544.SpiralBevelGearCompoundParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.compound.SpiralBevelGearCompoundParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelGearsCompoundParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_meshes_compound_parametric_study_tool(
        self: Self,
    ) -> "List[_4545.SpiralBevelGearMeshCompoundParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.compound.SpiralBevelGearMeshCompoundParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelMeshesCompoundParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4417.SpiralBevelGearSetParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.SpiralBevelGearSetParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearSetCompoundParametricStudyTool._Cast_SpiralBevelGearSetCompoundParametricStudyTool":
        return self._Cast_SpiralBevelGearSetCompoundParametricStudyTool(self)
