"""KlingelnbergCycloPalloidConicalGearParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4331
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "KlingelnbergCycloPalloidConicalGearParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2538
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4375,
        _4378,
        _4364,
        _4383,
        _4323,
        _4395,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearParametricStudyTool",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearParametricStudyTool")


class KlingelnbergCycloPalloidConicalGearParametricStudyTool(
    _4331.ConicalGearParametricStudyTool
):
    """KlingelnbergCycloPalloidConicalGearParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearParametricStudyTool to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
            parent: "KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ):
            self._parent = parent

        @property
        def conical_gear_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ) -> "_4331.ConicalGearParametricStudyTool":
            return self._parent._cast(_4331.ConicalGearParametricStudyTool)

        @property
        def gear_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ) -> "_4364.GearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4364,
            )

            return self._parent._cast(_4364.GearParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ) -> "_4383.MountableComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4383,
            )

            return self._parent._cast(_4383.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ) -> "_4323.ComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4323,
            )

            return self._parent._cast(_4323.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ) -> "_4395.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4395,
            )

            return self._parent._cast(_4395.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ) -> "_4375.KlingelnbergCycloPalloidHypoidGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4375,
            )

            return self._parent._cast(
                _4375.KlingelnbergCycloPalloidHypoidGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ) -> "_4378.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4378,
            )

            return self._parent._cast(
                _4378.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ) -> "KlingelnbergCycloPalloidConicalGearParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2538.KlingelnbergCycloPalloidConicalGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool":
        return self._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool(self)
