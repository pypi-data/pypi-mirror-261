"""PointLoadPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4162
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "PointLoadPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2473
    from mastapy.system_model.analyses_and_results.static_loads import _6941
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4114,
        _4059,
        _4116,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("PointLoadPowerFlow",)


Self = TypeVar("Self", bound="PointLoadPowerFlow")


class PointLoadPowerFlow(_4162.VirtualComponentPowerFlow):
    """PointLoadPowerFlow

    This is a mastapy class.
    """

    TYPE = _POINT_LOAD_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PointLoadPowerFlow")

    class _Cast_PointLoadPowerFlow:
        """Special nested class for casting PointLoadPowerFlow to subclasses."""

        def __init__(
            self: "PointLoadPowerFlow._Cast_PointLoadPowerFlow",
            parent: "PointLoadPowerFlow",
        ):
            self._parent = parent

        @property
        def virtual_component_power_flow(
            self: "PointLoadPowerFlow._Cast_PointLoadPowerFlow",
        ) -> "_4162.VirtualComponentPowerFlow":
            return self._parent._cast(_4162.VirtualComponentPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "PointLoadPowerFlow._Cast_PointLoadPowerFlow",
        ) -> "_4114.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4114

            return self._parent._cast(_4114.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "PointLoadPowerFlow._Cast_PointLoadPowerFlow",
        ) -> "_4059.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4059

            return self._parent._cast(_4059.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "PointLoadPowerFlow._Cast_PointLoadPowerFlow",
        ) -> "_4116.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4116

            return self._parent._cast(_4116.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "PointLoadPowerFlow._Cast_PointLoadPowerFlow",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PointLoadPowerFlow._Cast_PointLoadPowerFlow",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PointLoadPowerFlow._Cast_PointLoadPowerFlow",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PointLoadPowerFlow._Cast_PointLoadPowerFlow",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PointLoadPowerFlow._Cast_PointLoadPowerFlow",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def point_load_power_flow(
            self: "PointLoadPowerFlow._Cast_PointLoadPowerFlow",
        ) -> "PointLoadPowerFlow":
            return self._parent

        def __getattr__(self: "PointLoadPowerFlow._Cast_PointLoadPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PointLoadPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2473.PointLoad":
        """mastapy.system_model.part_model.PointLoad

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6941.PointLoadLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PointLoadLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "PointLoadPowerFlow._Cast_PointLoadPowerFlow":
        return self._Cast_PointLoadPowerFlow(self)
