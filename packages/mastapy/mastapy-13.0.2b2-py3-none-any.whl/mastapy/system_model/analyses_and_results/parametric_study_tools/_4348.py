"""CylindricalPlanetGearParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4346
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "CylindricalPlanetGearParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2529
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4364,
        _4383,
        _4323,
        _4395,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearParametricStudyTool",)


Self = TypeVar("Self", bound="CylindricalPlanetGearParametricStudyTool")


class CylindricalPlanetGearParametricStudyTool(
    _4346.CylindricalGearParametricStudyTool
):
    """CylindricalPlanetGearParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalPlanetGearParametricStudyTool"
    )

    class _Cast_CylindricalPlanetGearParametricStudyTool:
        """Special nested class for casting CylindricalPlanetGearParametricStudyTool to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool",
            parent: "CylindricalPlanetGearParametricStudyTool",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_parametric_study_tool(
            self: "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool",
        ) -> "_4346.CylindricalGearParametricStudyTool":
            return self._parent._cast(_4346.CylindricalGearParametricStudyTool)

        @property
        def gear_parametric_study_tool(
            self: "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool",
        ) -> "_4364.GearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4364,
            )

            return self._parent._cast(_4364.GearParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool",
        ) -> "_4383.MountableComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4383,
            )

            return self._parent._cast(_4383.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool",
        ) -> "_4323.ComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4323,
            )

            return self._parent._cast(_4323.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool",
        ) -> "_4395.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4395,
            )

            return self._parent._cast(_4395.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_parametric_study_tool(
            self: "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool",
        ) -> "CylindricalPlanetGearParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool",
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
        self: Self, instance_to_wrap: "CylindricalPlanetGearParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2529.CylindricalPlanetGear":
        """mastapy.system_model.part_model.gears.CylindricalPlanetGear

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
    ) -> "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool":
        return self._Cast_CylindricalPlanetGearParametricStudyTool(self)
