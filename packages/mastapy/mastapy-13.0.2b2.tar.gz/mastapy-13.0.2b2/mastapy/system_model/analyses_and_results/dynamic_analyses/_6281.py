"""AbstractShaftOrHousingDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6304
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "AbstractShaftOrHousingDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2438
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6280,
        _6324,
        _6337,
        _6376,
        _6360,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7549,
        _7550,
        _7547,
    )
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingDynamicAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingDynamicAnalysis")


class AbstractShaftOrHousingDynamicAnalysis(_6304.ComponentDynamicAnalysis):
    """AbstractShaftOrHousingDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftOrHousingDynamicAnalysis"
    )

    class _Cast_AbstractShaftOrHousingDynamicAnalysis:
        """Special nested class for casting AbstractShaftOrHousingDynamicAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingDynamicAnalysis._Cast_AbstractShaftOrHousingDynamicAnalysis",
            parent: "AbstractShaftOrHousingDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def component_dynamic_analysis(
            self: "AbstractShaftOrHousingDynamicAnalysis._Cast_AbstractShaftOrHousingDynamicAnalysis",
        ) -> "_6304.ComponentDynamicAnalysis":
            return self._parent._cast(_6304.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "AbstractShaftOrHousingDynamicAnalysis._Cast_AbstractShaftOrHousingDynamicAnalysis",
        ) -> "_6360.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6360

            return self._parent._cast(_6360.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "AbstractShaftOrHousingDynamicAnalysis._Cast_AbstractShaftOrHousingDynamicAnalysis",
        ) -> "_7549.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftOrHousingDynamicAnalysis._Cast_AbstractShaftOrHousingDynamicAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftOrHousingDynamicAnalysis._Cast_AbstractShaftOrHousingDynamicAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftOrHousingDynamicAnalysis._Cast_AbstractShaftOrHousingDynamicAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftOrHousingDynamicAnalysis._Cast_AbstractShaftOrHousingDynamicAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingDynamicAnalysis._Cast_AbstractShaftOrHousingDynamicAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def abstract_shaft_dynamic_analysis(
            self: "AbstractShaftOrHousingDynamicAnalysis._Cast_AbstractShaftOrHousingDynamicAnalysis",
        ) -> "_6280.AbstractShaftDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6280

            return self._parent._cast(_6280.AbstractShaftDynamicAnalysis)

        @property
        def cycloidal_disc_dynamic_analysis(
            self: "AbstractShaftOrHousingDynamicAnalysis._Cast_AbstractShaftOrHousingDynamicAnalysis",
        ) -> "_6324.CycloidalDiscDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6324

            return self._parent._cast(_6324.CycloidalDiscDynamicAnalysis)

        @property
        def fe_part_dynamic_analysis(
            self: "AbstractShaftOrHousingDynamicAnalysis._Cast_AbstractShaftOrHousingDynamicAnalysis",
        ) -> "_6337.FEPartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6337

            return self._parent._cast(_6337.FEPartDynamicAnalysis)

        @property
        def shaft_dynamic_analysis(
            self: "AbstractShaftOrHousingDynamicAnalysis._Cast_AbstractShaftOrHousingDynamicAnalysis",
        ) -> "_6376.ShaftDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6376

            return self._parent._cast(_6376.ShaftDynamicAnalysis)

        @property
        def abstract_shaft_or_housing_dynamic_analysis(
            self: "AbstractShaftOrHousingDynamicAnalysis._Cast_AbstractShaftOrHousingDynamicAnalysis",
        ) -> "AbstractShaftOrHousingDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingDynamicAnalysis._Cast_AbstractShaftOrHousingDynamicAnalysis",
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
        self: Self, instance_to_wrap: "AbstractShaftOrHousingDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2438.AbstractShaftOrHousing":
        """mastapy.system_model.part_model.AbstractShaftOrHousing

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
    ) -> "AbstractShaftOrHousingDynamicAnalysis._Cast_AbstractShaftOrHousingDynamicAnalysis":
        return self._Cast_AbstractShaftOrHousingDynamicAnalysis(self)
