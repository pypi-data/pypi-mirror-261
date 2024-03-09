"""FlexiblePinAssemblyPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4137
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "FlexiblePinAssemblyPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2456
    from mastapy.system_model.analyses_and_results.static_loads import _6891
    from mastapy.system_model.analyses_and_results.power_flows import _4034, _4116
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("FlexiblePinAssemblyPowerFlow",)


Self = TypeVar("Self", bound="FlexiblePinAssemblyPowerFlow")


class FlexiblePinAssemblyPowerFlow(_4137.SpecialisedAssemblyPowerFlow):
    """FlexiblePinAssemblyPowerFlow

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FlexiblePinAssemblyPowerFlow")

    class _Cast_FlexiblePinAssemblyPowerFlow:
        """Special nested class for casting FlexiblePinAssemblyPowerFlow to subclasses."""

        def __init__(
            self: "FlexiblePinAssemblyPowerFlow._Cast_FlexiblePinAssemblyPowerFlow",
            parent: "FlexiblePinAssemblyPowerFlow",
        ):
            self._parent = parent

        @property
        def specialised_assembly_power_flow(
            self: "FlexiblePinAssemblyPowerFlow._Cast_FlexiblePinAssemblyPowerFlow",
        ) -> "_4137.SpecialisedAssemblyPowerFlow":
            return self._parent._cast(_4137.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "FlexiblePinAssemblyPowerFlow._Cast_FlexiblePinAssemblyPowerFlow",
        ) -> "_4034.AbstractAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4034

            return self._parent._cast(_4034.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "FlexiblePinAssemblyPowerFlow._Cast_FlexiblePinAssemblyPowerFlow",
        ) -> "_4116.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4116

            return self._parent._cast(_4116.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "FlexiblePinAssemblyPowerFlow._Cast_FlexiblePinAssemblyPowerFlow",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FlexiblePinAssemblyPowerFlow._Cast_FlexiblePinAssemblyPowerFlow",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FlexiblePinAssemblyPowerFlow._Cast_FlexiblePinAssemblyPowerFlow",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FlexiblePinAssemblyPowerFlow._Cast_FlexiblePinAssemblyPowerFlow",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FlexiblePinAssemblyPowerFlow._Cast_FlexiblePinAssemblyPowerFlow",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def flexible_pin_assembly_power_flow(
            self: "FlexiblePinAssemblyPowerFlow._Cast_FlexiblePinAssemblyPowerFlow",
        ) -> "FlexiblePinAssemblyPowerFlow":
            return self._parent

        def __getattr__(
            self: "FlexiblePinAssemblyPowerFlow._Cast_FlexiblePinAssemblyPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FlexiblePinAssemblyPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2456.FlexiblePinAssembly":
        """mastapy.system_model.part_model.FlexiblePinAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6891.FlexiblePinAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FlexiblePinAssemblyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "FlexiblePinAssemblyPowerFlow._Cast_FlexiblePinAssemblyPowerFlow":
        return self._Cast_FlexiblePinAssemblyPowerFlow(self)
