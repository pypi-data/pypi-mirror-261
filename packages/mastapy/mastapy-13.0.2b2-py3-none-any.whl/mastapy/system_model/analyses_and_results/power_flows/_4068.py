"""ConicalGearSetPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4097
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "ConicalGearSetPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2526
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4040,
        _4047,
        _4052,
        _4101,
        _4105,
        _4108,
        _4111,
        _4140,
        _4146,
        _4149,
        _4168,
        _4137,
        _4034,
        _4116,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetPowerFlow",)


Self = TypeVar("Self", bound="ConicalGearSetPowerFlow")


class ConicalGearSetPowerFlow(_4097.GearSetPowerFlow):
    """ConicalGearSetPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearSetPowerFlow")

    class _Cast_ConicalGearSetPowerFlow:
        """Special nested class for casting ConicalGearSetPowerFlow to subclasses."""

        def __init__(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
            parent: "ConicalGearSetPowerFlow",
        ):
            self._parent = parent

        @property
        def gear_set_power_flow(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ) -> "_4097.GearSetPowerFlow":
            return self._parent._cast(_4097.GearSetPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ) -> "_4137.SpecialisedAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ) -> "_4034.AbstractAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4034

            return self._parent._cast(_4034.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ) -> "_4116.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4116

            return self._parent._cast(_4116.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_power_flow(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ) -> "_4040.AGMAGleasonConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4040

            return self._parent._cast(_4040.AGMAGleasonConicalGearSetPowerFlow)

        @property
        def bevel_differential_gear_set_power_flow(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ) -> "_4047.BevelDifferentialGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4047

            return self._parent._cast(_4047.BevelDifferentialGearSetPowerFlow)

        @property
        def bevel_gear_set_power_flow(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ) -> "_4052.BevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4052

            return self._parent._cast(_4052.BevelGearSetPowerFlow)

        @property
        def hypoid_gear_set_power_flow(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ) -> "_4101.HypoidGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4101

            return self._parent._cast(_4101.HypoidGearSetPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_power_flow(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ) -> "_4105.KlingelnbergCycloPalloidConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4105

            return self._parent._cast(
                _4105.KlingelnbergCycloPalloidConicalGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_power_flow(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ) -> "_4108.KlingelnbergCycloPalloidHypoidGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4108

            return self._parent._cast(
                _4108.KlingelnbergCycloPalloidHypoidGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_power_flow(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ) -> "_4111.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4111

            return self._parent._cast(
                _4111.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow
            )

        @property
        def spiral_bevel_gear_set_power_flow(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ) -> "_4140.SpiralBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4140

            return self._parent._cast(_4140.SpiralBevelGearSetPowerFlow)

        @property
        def straight_bevel_diff_gear_set_power_flow(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ) -> "_4146.StraightBevelDiffGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4146

            return self._parent._cast(_4146.StraightBevelDiffGearSetPowerFlow)

        @property
        def straight_bevel_gear_set_power_flow(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ) -> "_4149.StraightBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4149

            return self._parent._cast(_4149.StraightBevelGearSetPowerFlow)

        @property
        def zerol_bevel_gear_set_power_flow(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ) -> "_4168.ZerolBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4168

            return self._parent._cast(_4168.ZerolBevelGearSetPowerFlow)

        @property
        def conical_gear_set_power_flow(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ) -> "ConicalGearSetPowerFlow":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearSetPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2526.ConicalGearSet":
        """mastapy.system_model.part_model.gears.ConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow":
        return self._Cast_ConicalGearSetPowerFlow(self)
