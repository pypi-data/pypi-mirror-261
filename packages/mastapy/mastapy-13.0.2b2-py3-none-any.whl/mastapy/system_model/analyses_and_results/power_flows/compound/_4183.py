"""BevelDifferentialPlanetGearCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4180
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "BevelDifferentialPlanetGearCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4048
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4185,
        _4173,
        _4201,
        _4227,
        _4246,
        _4194,
        _4248,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialPlanetGearCompoundPowerFlow",)


Self = TypeVar("Self", bound="BevelDifferentialPlanetGearCompoundPowerFlow")


class BevelDifferentialPlanetGearCompoundPowerFlow(
    _4180.BevelDifferentialGearCompoundPowerFlow
):
    """BevelDifferentialPlanetGearCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialPlanetGearCompoundPowerFlow"
    )

    class _Cast_BevelDifferentialPlanetGearCompoundPowerFlow:
        """Special nested class for casting BevelDifferentialPlanetGearCompoundPowerFlow to subclasses."""

        def __init__(
            self: "BevelDifferentialPlanetGearCompoundPowerFlow._Cast_BevelDifferentialPlanetGearCompoundPowerFlow",
            parent: "BevelDifferentialPlanetGearCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_compound_power_flow(
            self: "BevelDifferentialPlanetGearCompoundPowerFlow._Cast_BevelDifferentialPlanetGearCompoundPowerFlow",
        ) -> "_4180.BevelDifferentialGearCompoundPowerFlow":
            return self._parent._cast(_4180.BevelDifferentialGearCompoundPowerFlow)

        @property
        def bevel_gear_compound_power_flow(
            self: "BevelDifferentialPlanetGearCompoundPowerFlow._Cast_BevelDifferentialPlanetGearCompoundPowerFlow",
        ) -> "_4185.BevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4185,
            )

            return self._parent._cast(_4185.BevelGearCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_compound_power_flow(
            self: "BevelDifferentialPlanetGearCompoundPowerFlow._Cast_BevelDifferentialPlanetGearCompoundPowerFlow",
        ) -> "_4173.AGMAGleasonConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4173,
            )

            return self._parent._cast(_4173.AGMAGleasonConicalGearCompoundPowerFlow)

        @property
        def conical_gear_compound_power_flow(
            self: "BevelDifferentialPlanetGearCompoundPowerFlow._Cast_BevelDifferentialPlanetGearCompoundPowerFlow",
        ) -> "_4201.ConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4201,
            )

            return self._parent._cast(_4201.ConicalGearCompoundPowerFlow)

        @property
        def gear_compound_power_flow(
            self: "BevelDifferentialPlanetGearCompoundPowerFlow._Cast_BevelDifferentialPlanetGearCompoundPowerFlow",
        ) -> "_4227.GearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4227,
            )

            return self._parent._cast(_4227.GearCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "BevelDifferentialPlanetGearCompoundPowerFlow._Cast_BevelDifferentialPlanetGearCompoundPowerFlow",
        ) -> "_4246.MountableComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4246,
            )

            return self._parent._cast(_4246.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "BevelDifferentialPlanetGearCompoundPowerFlow._Cast_BevelDifferentialPlanetGearCompoundPowerFlow",
        ) -> "_4194.ComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4194,
            )

            return self._parent._cast(_4194.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "BevelDifferentialPlanetGearCompoundPowerFlow._Cast_BevelDifferentialPlanetGearCompoundPowerFlow",
        ) -> "_4248.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4248,
            )

            return self._parent._cast(_4248.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialPlanetGearCompoundPowerFlow._Cast_BevelDifferentialPlanetGearCompoundPowerFlow",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialPlanetGearCompoundPowerFlow._Cast_BevelDifferentialPlanetGearCompoundPowerFlow",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialPlanetGearCompoundPowerFlow._Cast_BevelDifferentialPlanetGearCompoundPowerFlow",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_compound_power_flow(
            self: "BevelDifferentialPlanetGearCompoundPowerFlow._Cast_BevelDifferentialPlanetGearCompoundPowerFlow",
        ) -> "BevelDifferentialPlanetGearCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialPlanetGearCompoundPowerFlow._Cast_BevelDifferentialPlanetGearCompoundPowerFlow",
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
        self: Self,
        instance_to_wrap: "BevelDifferentialPlanetGearCompoundPowerFlow.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4048.BevelDifferentialPlanetGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.BevelDifferentialPlanetGearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4048.BevelDifferentialPlanetGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.BevelDifferentialPlanetGearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialPlanetGearCompoundPowerFlow._Cast_BevelDifferentialPlanetGearCompoundPowerFlow":
        return self._Cast_BevelDifferentialPlanetGearCompoundPowerFlow(self)
