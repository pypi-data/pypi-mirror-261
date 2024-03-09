"""StraightBevelDiffGearSetPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4052
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "StraightBevelDiffGearSetPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2548
    from mastapy.system_model.analyses_and_results.static_loads import _6964
    from mastapy.gears.rating.straight_bevel_diff import _400
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4145,
        _4144,
        _4040,
        _4068,
        _4097,
        _4137,
        _4034,
        _4116,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSetPowerFlow",)


Self = TypeVar("Self", bound="StraightBevelDiffGearSetPowerFlow")


class StraightBevelDiffGearSetPowerFlow(_4052.BevelGearSetPowerFlow):
    """StraightBevelDiffGearSetPowerFlow

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelDiffGearSetPowerFlow")

    class _Cast_StraightBevelDiffGearSetPowerFlow:
        """Special nested class for casting StraightBevelDiffGearSetPowerFlow to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearSetPowerFlow._Cast_StraightBevelDiffGearSetPowerFlow",
            parent: "StraightBevelDiffGearSetPowerFlow",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_power_flow(
            self: "StraightBevelDiffGearSetPowerFlow._Cast_StraightBevelDiffGearSetPowerFlow",
        ) -> "_4052.BevelGearSetPowerFlow":
            return self._parent._cast(_4052.BevelGearSetPowerFlow)

        @property
        def agma_gleason_conical_gear_set_power_flow(
            self: "StraightBevelDiffGearSetPowerFlow._Cast_StraightBevelDiffGearSetPowerFlow",
        ) -> "_4040.AGMAGleasonConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4040

            return self._parent._cast(_4040.AGMAGleasonConicalGearSetPowerFlow)

        @property
        def conical_gear_set_power_flow(
            self: "StraightBevelDiffGearSetPowerFlow._Cast_StraightBevelDiffGearSetPowerFlow",
        ) -> "_4068.ConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4068

            return self._parent._cast(_4068.ConicalGearSetPowerFlow)

        @property
        def gear_set_power_flow(
            self: "StraightBevelDiffGearSetPowerFlow._Cast_StraightBevelDiffGearSetPowerFlow",
        ) -> "_4097.GearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4097

            return self._parent._cast(_4097.GearSetPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "StraightBevelDiffGearSetPowerFlow._Cast_StraightBevelDiffGearSetPowerFlow",
        ) -> "_4137.SpecialisedAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "StraightBevelDiffGearSetPowerFlow._Cast_StraightBevelDiffGearSetPowerFlow",
        ) -> "_4034.AbstractAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4034

            return self._parent._cast(_4034.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "StraightBevelDiffGearSetPowerFlow._Cast_StraightBevelDiffGearSetPowerFlow",
        ) -> "_4116.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4116

            return self._parent._cast(_4116.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelDiffGearSetPowerFlow._Cast_StraightBevelDiffGearSetPowerFlow",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelDiffGearSetPowerFlow._Cast_StraightBevelDiffGearSetPowerFlow",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelDiffGearSetPowerFlow._Cast_StraightBevelDiffGearSetPowerFlow",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearSetPowerFlow._Cast_StraightBevelDiffGearSetPowerFlow",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearSetPowerFlow._Cast_StraightBevelDiffGearSetPowerFlow",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_set_power_flow(
            self: "StraightBevelDiffGearSetPowerFlow._Cast_StraightBevelDiffGearSetPowerFlow",
        ) -> "StraightBevelDiffGearSetPowerFlow":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearSetPowerFlow._Cast_StraightBevelDiffGearSetPowerFlow",
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
        self: Self, instance_to_wrap: "StraightBevelDiffGearSetPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2548.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6964.StraightBevelDiffGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: Self) -> "_400.StraightBevelDiffGearSetRating":
        """mastapy.gears.rating.straight_bevel_diff.StraightBevelDiffGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(
        self: Self,
    ) -> "_400.StraightBevelDiffGearSetRating":
        """mastapy.gears.rating.straight_bevel_diff.StraightBevelDiffGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_power_flow(self: Self) -> "List[_4145.StraightBevelDiffGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.StraightBevelDiffGearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_gears_power_flow(
        self: Self,
    ) -> "List[_4145.StraightBevelDiffGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.StraightBevelDiffGearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearsPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_power_flow(
        self: Self,
    ) -> "List[_4144.StraightBevelDiffGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.StraightBevelDiffGearMeshPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_meshes_power_flow(
        self: Self,
    ) -> "List[_4144.StraightBevelDiffGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.StraightBevelDiffGearMeshPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffMeshesPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearSetPowerFlow._Cast_StraightBevelDiffGearSetPowerFlow":
        return self._Cast_StraightBevelDiffGearSetPowerFlow(self)
