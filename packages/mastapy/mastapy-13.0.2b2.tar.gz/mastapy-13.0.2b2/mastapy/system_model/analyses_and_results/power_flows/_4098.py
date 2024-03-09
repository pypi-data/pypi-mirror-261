"""GuideDxfModelPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4059
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "GuideDxfModelPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2457
    from mastapy.system_model.analyses_and_results.static_loads import _6899
    from mastapy.system_model.analyses_and_results.power_flows import _4116
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("GuideDxfModelPowerFlow",)


Self = TypeVar("Self", bound="GuideDxfModelPowerFlow")


class GuideDxfModelPowerFlow(_4059.ComponentPowerFlow):
    """GuideDxfModelPowerFlow

    This is a mastapy class.
    """

    TYPE = _GUIDE_DXF_MODEL_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GuideDxfModelPowerFlow")

    class _Cast_GuideDxfModelPowerFlow:
        """Special nested class for casting GuideDxfModelPowerFlow to subclasses."""

        def __init__(
            self: "GuideDxfModelPowerFlow._Cast_GuideDxfModelPowerFlow",
            parent: "GuideDxfModelPowerFlow",
        ):
            self._parent = parent

        @property
        def component_power_flow(
            self: "GuideDxfModelPowerFlow._Cast_GuideDxfModelPowerFlow",
        ) -> "_4059.ComponentPowerFlow":
            return self._parent._cast(_4059.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "GuideDxfModelPowerFlow._Cast_GuideDxfModelPowerFlow",
        ) -> "_4116.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4116

            return self._parent._cast(_4116.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "GuideDxfModelPowerFlow._Cast_GuideDxfModelPowerFlow",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GuideDxfModelPowerFlow._Cast_GuideDxfModelPowerFlow",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GuideDxfModelPowerFlow._Cast_GuideDxfModelPowerFlow",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GuideDxfModelPowerFlow._Cast_GuideDxfModelPowerFlow",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GuideDxfModelPowerFlow._Cast_GuideDxfModelPowerFlow",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def guide_dxf_model_power_flow(
            self: "GuideDxfModelPowerFlow._Cast_GuideDxfModelPowerFlow",
        ) -> "GuideDxfModelPowerFlow":
            return self._parent

        def __getattr__(
            self: "GuideDxfModelPowerFlow._Cast_GuideDxfModelPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GuideDxfModelPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2457.GuideDxfModel":
        """mastapy.system_model.part_model.GuideDxfModel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6899.GuideDxfModelLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.GuideDxfModelLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "GuideDxfModelPowerFlow._Cast_GuideDxfModelPowerFlow":
        return self._Cast_GuideDxfModelPowerFlow(self)
