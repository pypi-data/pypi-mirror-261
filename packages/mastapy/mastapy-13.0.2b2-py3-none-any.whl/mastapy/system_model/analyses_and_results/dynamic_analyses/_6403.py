"""VirtualComponentDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "VirtualComponentDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2481
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6356,
        _6357,
        _6367,
        _6368,
        _6402,
        _6304,
        _6360,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7549,
        _7550,
        _7547,
    )
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentDynamicAnalysis",)


Self = TypeVar("Self", bound="VirtualComponentDynamicAnalysis")


class VirtualComponentDynamicAnalysis(_6358.MountableComponentDynamicAnalysis):
    """VirtualComponentDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VirtualComponentDynamicAnalysis")

    class _Cast_VirtualComponentDynamicAnalysis:
        """Special nested class for casting VirtualComponentDynamicAnalysis to subclasses."""

        def __init__(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
            parent: "VirtualComponentDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_dynamic_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_6358.MountableComponentDynamicAnalysis":
            return self._parent._cast(_6358.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_6304.ComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6304

            return self._parent._cast(_6304.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_6360.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6360

            return self._parent._cast(_6360.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_7549.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def mass_disc_dynamic_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_6356.MassDiscDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6356

            return self._parent._cast(_6356.MassDiscDynamicAnalysis)

        @property
        def measurement_component_dynamic_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_6357.MeasurementComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6357

            return self._parent._cast(_6357.MeasurementComponentDynamicAnalysis)

        @property
        def point_load_dynamic_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_6367.PointLoadDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6367

            return self._parent._cast(_6367.PointLoadDynamicAnalysis)

        @property
        def power_load_dynamic_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_6368.PowerLoadDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6368

            return self._parent._cast(_6368.PowerLoadDynamicAnalysis)

        @property
        def unbalanced_mass_dynamic_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_6402.UnbalancedMassDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6402

            return self._parent._cast(_6402.UnbalancedMassDynamicAnalysis)

        @property
        def virtual_component_dynamic_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "VirtualComponentDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "VirtualComponentDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2481.VirtualComponent":
        """mastapy.system_model.part_model.VirtualComponent

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
    ) -> "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis":
        return self._Cast_VirtualComponentDynamicAnalysis(self)
