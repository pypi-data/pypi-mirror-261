"""BevelGearMeshCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4174
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "BevelGearMeshCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4050
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4181,
        _4269,
        _4275,
        _4278,
        _4296,
        _4202,
        _4228,
        _4234,
        _4204,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshCompoundPowerFlow",)


Self = TypeVar("Self", bound="BevelGearMeshCompoundPowerFlow")


class BevelGearMeshCompoundPowerFlow(_4174.AGMAGleasonConicalGearMeshCompoundPowerFlow):
    """BevelGearMeshCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearMeshCompoundPowerFlow")

    class _Cast_BevelGearMeshCompoundPowerFlow:
        """Special nested class for casting BevelGearMeshCompoundPowerFlow to subclasses."""

        def __init__(
            self: "BevelGearMeshCompoundPowerFlow._Cast_BevelGearMeshCompoundPowerFlow",
            parent: "BevelGearMeshCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_compound_power_flow(
            self: "BevelGearMeshCompoundPowerFlow._Cast_BevelGearMeshCompoundPowerFlow",
        ) -> "_4174.AGMAGleasonConicalGearMeshCompoundPowerFlow":
            return self._parent._cast(_4174.AGMAGleasonConicalGearMeshCompoundPowerFlow)

        @property
        def conical_gear_mesh_compound_power_flow(
            self: "BevelGearMeshCompoundPowerFlow._Cast_BevelGearMeshCompoundPowerFlow",
        ) -> "_4202.ConicalGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4202,
            )

            return self._parent._cast(_4202.ConicalGearMeshCompoundPowerFlow)

        @property
        def gear_mesh_compound_power_flow(
            self: "BevelGearMeshCompoundPowerFlow._Cast_BevelGearMeshCompoundPowerFlow",
        ) -> "_4228.GearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4228,
            )

            return self._parent._cast(_4228.GearMeshCompoundPowerFlow)

        @property
        def inter_mountable_component_connection_compound_power_flow(
            self: "BevelGearMeshCompoundPowerFlow._Cast_BevelGearMeshCompoundPowerFlow",
        ) -> "_4234.InterMountableComponentConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4234,
            )

            return self._parent._cast(
                _4234.InterMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def connection_compound_power_flow(
            self: "BevelGearMeshCompoundPowerFlow._Cast_BevelGearMeshCompoundPowerFlow",
        ) -> "_4204.ConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4204,
            )

            return self._parent._cast(_4204.ConnectionCompoundPowerFlow)

        @property
        def connection_compound_analysis(
            self: "BevelGearMeshCompoundPowerFlow._Cast_BevelGearMeshCompoundPowerFlow",
        ) -> "_7541.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearMeshCompoundPowerFlow._Cast_BevelGearMeshCompoundPowerFlow",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshCompoundPowerFlow._Cast_BevelGearMeshCompoundPowerFlow",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_power_flow(
            self: "BevelGearMeshCompoundPowerFlow._Cast_BevelGearMeshCompoundPowerFlow",
        ) -> "_4181.BevelDifferentialGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4181,
            )

            return self._parent._cast(_4181.BevelDifferentialGearMeshCompoundPowerFlow)

        @property
        def spiral_bevel_gear_mesh_compound_power_flow(
            self: "BevelGearMeshCompoundPowerFlow._Cast_BevelGearMeshCompoundPowerFlow",
        ) -> "_4269.SpiralBevelGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4269,
            )

            return self._parent._cast(_4269.SpiralBevelGearMeshCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_mesh_compound_power_flow(
            self: "BevelGearMeshCompoundPowerFlow._Cast_BevelGearMeshCompoundPowerFlow",
        ) -> "_4275.StraightBevelDiffGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4275,
            )

            return self._parent._cast(_4275.StraightBevelDiffGearMeshCompoundPowerFlow)

        @property
        def straight_bevel_gear_mesh_compound_power_flow(
            self: "BevelGearMeshCompoundPowerFlow._Cast_BevelGearMeshCompoundPowerFlow",
        ) -> "_4278.StraightBevelGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4278,
            )

            return self._parent._cast(_4278.StraightBevelGearMeshCompoundPowerFlow)

        @property
        def zerol_bevel_gear_mesh_compound_power_flow(
            self: "BevelGearMeshCompoundPowerFlow._Cast_BevelGearMeshCompoundPowerFlow",
        ) -> "_4296.ZerolBevelGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4296,
            )

            return self._parent._cast(_4296.ZerolBevelGearMeshCompoundPowerFlow)

        @property
        def bevel_gear_mesh_compound_power_flow(
            self: "BevelGearMeshCompoundPowerFlow._Cast_BevelGearMeshCompoundPowerFlow",
        ) -> "BevelGearMeshCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshCompoundPowerFlow._Cast_BevelGearMeshCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearMeshCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self: Self) -> "List[_4050.BevelGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.BevelGearMeshPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4050.BevelGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.BevelGearMeshPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearMeshCompoundPowerFlow._Cast_BevelGearMeshCompoundPowerFlow":
        return self._Cast_BevelGearMeshCompoundPowerFlow(self)
