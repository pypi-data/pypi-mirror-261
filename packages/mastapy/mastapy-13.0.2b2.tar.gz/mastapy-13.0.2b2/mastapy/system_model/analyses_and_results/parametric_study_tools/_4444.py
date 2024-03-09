"""ZerolBevelGearSetParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4316
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "ZerolBevelGearSetParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2556
    from mastapy.system_model.analyses_and_results.static_loads import _6990
    from mastapy.system_model.analyses_and_results.system_deflections import _2842
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4443,
        _4442,
        _4304,
        _4332,
        _4365,
        _4414,
        _4298,
        _4395,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearSetParametricStudyTool",)


Self = TypeVar("Self", bound="ZerolBevelGearSetParametricStudyTool")


class ZerolBevelGearSetParametricStudyTool(_4316.BevelGearSetParametricStudyTool):
    """ZerolBevelGearSetParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ZerolBevelGearSetParametricStudyTool")

    class _Cast_ZerolBevelGearSetParametricStudyTool:
        """Special nested class for casting ZerolBevelGearSetParametricStudyTool to subclasses."""

        def __init__(
            self: "ZerolBevelGearSetParametricStudyTool._Cast_ZerolBevelGearSetParametricStudyTool",
            parent: "ZerolBevelGearSetParametricStudyTool",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_parametric_study_tool(
            self: "ZerolBevelGearSetParametricStudyTool._Cast_ZerolBevelGearSetParametricStudyTool",
        ) -> "_4316.BevelGearSetParametricStudyTool":
            return self._parent._cast(_4316.BevelGearSetParametricStudyTool)

        @property
        def agma_gleason_conical_gear_set_parametric_study_tool(
            self: "ZerolBevelGearSetParametricStudyTool._Cast_ZerolBevelGearSetParametricStudyTool",
        ) -> "_4304.AGMAGleasonConicalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4304,
            )

            return self._parent._cast(
                _4304.AGMAGleasonConicalGearSetParametricStudyTool
            )

        @property
        def conical_gear_set_parametric_study_tool(
            self: "ZerolBevelGearSetParametricStudyTool._Cast_ZerolBevelGearSetParametricStudyTool",
        ) -> "_4332.ConicalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4332,
            )

            return self._parent._cast(_4332.ConicalGearSetParametricStudyTool)

        @property
        def gear_set_parametric_study_tool(
            self: "ZerolBevelGearSetParametricStudyTool._Cast_ZerolBevelGearSetParametricStudyTool",
        ) -> "_4365.GearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4365,
            )

            return self._parent._cast(_4365.GearSetParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(
            self: "ZerolBevelGearSetParametricStudyTool._Cast_ZerolBevelGearSetParametricStudyTool",
        ) -> "_4414.SpecialisedAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4414,
            )

            return self._parent._cast(_4414.SpecialisedAssemblyParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "ZerolBevelGearSetParametricStudyTool._Cast_ZerolBevelGearSetParametricStudyTool",
        ) -> "_4298.AbstractAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4298,
            )

            return self._parent._cast(_4298.AbstractAssemblyParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "ZerolBevelGearSetParametricStudyTool._Cast_ZerolBevelGearSetParametricStudyTool",
        ) -> "_4395.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4395,
            )

            return self._parent._cast(_4395.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "ZerolBevelGearSetParametricStudyTool._Cast_ZerolBevelGearSetParametricStudyTool",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ZerolBevelGearSetParametricStudyTool._Cast_ZerolBevelGearSetParametricStudyTool",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ZerolBevelGearSetParametricStudyTool._Cast_ZerolBevelGearSetParametricStudyTool",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearSetParametricStudyTool._Cast_ZerolBevelGearSetParametricStudyTool",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_set_parametric_study_tool(
            self: "ZerolBevelGearSetParametricStudyTool._Cast_ZerolBevelGearSetParametricStudyTool",
        ) -> "ZerolBevelGearSetParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearSetParametricStudyTool._Cast_ZerolBevelGearSetParametricStudyTool",
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
        self: Self, instance_to_wrap: "ZerolBevelGearSetParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2556.ZerolBevelGearSet":
        """mastapy.system_model.part_model.gears.ZerolBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6990.ZerolBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearSetLoadCase

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
    ) -> "List[_2842.ZerolBevelGearSetSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearSetSystemDeflection]

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
    def zerol_bevel_gears_parametric_study_tool(
        self: Self,
    ) -> "List[_4443.ZerolBevelGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ZerolBevelGearParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearsParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_meshes_parametric_study_tool(
        self: Self,
    ) -> "List[_4442.ZerolBevelGearMeshParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ZerolBevelGearMeshParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelMeshesParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ZerolBevelGearSetParametricStudyTool._Cast_ZerolBevelGearSetParametricStudyTool":
        return self._Cast_ZerolBevelGearSetParametricStudyTool(self)
