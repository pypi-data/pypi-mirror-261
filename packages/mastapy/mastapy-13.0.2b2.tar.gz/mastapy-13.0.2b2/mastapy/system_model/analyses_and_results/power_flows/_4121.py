"""PlanetaryGearSetPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4084
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "PlanetaryGearSetPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2544
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4097,
        _4137,
        _4034,
        _4116,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetPowerFlow",)


Self = TypeVar("Self", bound="PlanetaryGearSetPowerFlow")


class PlanetaryGearSetPowerFlow(_4084.CylindricalGearSetPowerFlow):
    """PlanetaryGearSetPowerFlow

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetaryGearSetPowerFlow")

    class _Cast_PlanetaryGearSetPowerFlow:
        """Special nested class for casting PlanetaryGearSetPowerFlow to subclasses."""

        def __init__(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
            parent: "PlanetaryGearSetPowerFlow",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_power_flow(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ) -> "_4084.CylindricalGearSetPowerFlow":
            return self._parent._cast(_4084.CylindricalGearSetPowerFlow)

        @property
        def gear_set_power_flow(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ) -> "_4097.GearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4097

            return self._parent._cast(_4097.GearSetPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ) -> "_4137.SpecialisedAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ) -> "_4034.AbstractAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4034

            return self._parent._cast(_4034.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ) -> "_4116.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4116

            return self._parent._cast(_4116.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def planetary_gear_set_power_flow(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ) -> "PlanetaryGearSetPowerFlow":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlanetaryGearSetPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2544.PlanetaryGearSet":
        """mastapy.system_model.part_model.gears.PlanetaryGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow":
        return self._Cast_PlanetaryGearSetPowerFlow(self)
