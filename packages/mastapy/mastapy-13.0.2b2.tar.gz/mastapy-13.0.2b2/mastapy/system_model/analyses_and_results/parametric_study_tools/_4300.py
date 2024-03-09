"""AbstractShaftParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4299
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "AbstractShaftParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2437
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4343,
        _4412,
        _4323,
        _4395,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftParametricStudyTool",)


Self = TypeVar("Self", bound="AbstractShaftParametricStudyTool")


class AbstractShaftParametricStudyTool(_4299.AbstractShaftOrHousingParametricStudyTool):
    """AbstractShaftParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractShaftParametricStudyTool")

    class _Cast_AbstractShaftParametricStudyTool:
        """Special nested class for casting AbstractShaftParametricStudyTool to subclasses."""

        def __init__(
            self: "AbstractShaftParametricStudyTool._Cast_AbstractShaftParametricStudyTool",
            parent: "AbstractShaftParametricStudyTool",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_parametric_study_tool(
            self: "AbstractShaftParametricStudyTool._Cast_AbstractShaftParametricStudyTool",
        ) -> "_4299.AbstractShaftOrHousingParametricStudyTool":
            return self._parent._cast(_4299.AbstractShaftOrHousingParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "AbstractShaftParametricStudyTool._Cast_AbstractShaftParametricStudyTool",
        ) -> "_4323.ComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4323,
            )

            return self._parent._cast(_4323.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "AbstractShaftParametricStudyTool._Cast_AbstractShaftParametricStudyTool",
        ) -> "_4395.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4395,
            )

            return self._parent._cast(_4395.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "AbstractShaftParametricStudyTool._Cast_AbstractShaftParametricStudyTool",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftParametricStudyTool._Cast_AbstractShaftParametricStudyTool",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftParametricStudyTool._Cast_AbstractShaftParametricStudyTool",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftParametricStudyTool._Cast_AbstractShaftParametricStudyTool",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cycloidal_disc_parametric_study_tool(
            self: "AbstractShaftParametricStudyTool._Cast_AbstractShaftParametricStudyTool",
        ) -> "_4343.CycloidalDiscParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4343,
            )

            return self._parent._cast(_4343.CycloidalDiscParametricStudyTool)

        @property
        def shaft_parametric_study_tool(
            self: "AbstractShaftParametricStudyTool._Cast_AbstractShaftParametricStudyTool",
        ) -> "_4412.ShaftParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4412,
            )

            return self._parent._cast(_4412.ShaftParametricStudyTool)

        @property
        def abstract_shaft_parametric_study_tool(
            self: "AbstractShaftParametricStudyTool._Cast_AbstractShaftParametricStudyTool",
        ) -> "AbstractShaftParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "AbstractShaftParametricStudyTool._Cast_AbstractShaftParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractShaftParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2437.AbstractShaft":
        """mastapy.system_model.part_model.AbstractShaft

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
    ) -> "AbstractShaftParametricStudyTool._Cast_AbstractShaftParametricStudyTool":
        return self._Cast_AbstractShaftParametricStudyTool(self)
