"""KlingelnbergCycloPalloidHypoidGearParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4372
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "KlingelnbergCycloPalloidHypoidGearParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2540
    from mastapy.system_model.analyses_and_results.static_loads import _6918
    from mastapy.system_model.analyses_and_results.system_deflections import _2775
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4331,
        _4364,
        _4383,
        _4323,
        _4395,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearParametricStudyTool",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearParametricStudyTool")


class KlingelnbergCycloPalloidHypoidGearParametricStudyTool(
    _4372.KlingelnbergCycloPalloidConicalGearParametricStudyTool
):
    """KlingelnbergCycloPalloidHypoidGearParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidGearParametricStudyTool"
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearParametricStudyTool:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearParametricStudyTool to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearParametricStudyTool",
            parent: "KlingelnbergCycloPalloidHypoidGearParametricStudyTool",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearParametricStudyTool",
        ) -> "_4372.KlingelnbergCycloPalloidConicalGearParametricStudyTool":
            return self._parent._cast(
                _4372.KlingelnbergCycloPalloidConicalGearParametricStudyTool
            )

        @property
        def conical_gear_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearParametricStudyTool",
        ) -> "_4331.ConicalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4331,
            )

            return self._parent._cast(_4331.ConicalGearParametricStudyTool)

        @property
        def gear_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearParametricStudyTool",
        ) -> "_4364.GearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4364,
            )

            return self._parent._cast(_4364.GearParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearParametricStudyTool",
        ) -> "_4383.MountableComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4383,
            )

            return self._parent._cast(_4383.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearParametricStudyTool",
        ) -> "_4323.ComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4323,
            )

            return self._parent._cast(_4323.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearParametricStudyTool",
        ) -> "_4395.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4395,
            )

            return self._parent._cast(_4395.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearParametricStudyTool",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearParametricStudyTool",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearParametricStudyTool",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearParametricStudyTool",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearParametricStudyTool",
        ) -> "KlingelnbergCycloPalloidHypoidGearParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearParametricStudyTool",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2540.KlingelnbergCycloPalloidHypoidGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(
        self: Self,
    ) -> "_6918.KlingelnbergCycloPalloidHypoidGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase

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
    ) -> "List[_2775.KlingelnbergCycloPalloidHypoidGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidHypoidGearSystemDeflection]

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
    ) -> "KlingelnbergCycloPalloidHypoidGearParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearParametricStudyTool":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearParametricStudyTool(self)
