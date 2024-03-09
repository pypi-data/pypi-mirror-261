"""BevelDifferentialGearMeshPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4050
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MESH_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "BevelDifferentialGearMeshPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.bevel import _554
    from mastapy.system_model.connections_and_sockets.gears import _2303
    from mastapy.system_model.analyses_and_results.static_loads import _6826
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4038,
        _4066,
        _4095,
        _4102,
        _4069,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543, _7540
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearMeshPowerFlow",)


Self = TypeVar("Self", bound="BevelDifferentialGearMeshPowerFlow")


class BevelDifferentialGearMeshPowerFlow(_4050.BevelGearMeshPowerFlow):
    """BevelDifferentialGearMeshPowerFlow

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MESH_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelDifferentialGearMeshPowerFlow")

    class _Cast_BevelDifferentialGearMeshPowerFlow:
        """Special nested class for casting BevelDifferentialGearMeshPowerFlow to subclasses."""

        def __init__(
            self: "BevelDifferentialGearMeshPowerFlow._Cast_BevelDifferentialGearMeshPowerFlow",
            parent: "BevelDifferentialGearMeshPowerFlow",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_power_flow(
            self: "BevelDifferentialGearMeshPowerFlow._Cast_BevelDifferentialGearMeshPowerFlow",
        ) -> "_4050.BevelGearMeshPowerFlow":
            return self._parent._cast(_4050.BevelGearMeshPowerFlow)

        @property
        def agma_gleason_conical_gear_mesh_power_flow(
            self: "BevelDifferentialGearMeshPowerFlow._Cast_BevelDifferentialGearMeshPowerFlow",
        ) -> "_4038.AGMAGleasonConicalGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4038

            return self._parent._cast(_4038.AGMAGleasonConicalGearMeshPowerFlow)

        @property
        def conical_gear_mesh_power_flow(
            self: "BevelDifferentialGearMeshPowerFlow._Cast_BevelDifferentialGearMeshPowerFlow",
        ) -> "_4066.ConicalGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4066

            return self._parent._cast(_4066.ConicalGearMeshPowerFlow)

        @property
        def gear_mesh_power_flow(
            self: "BevelDifferentialGearMeshPowerFlow._Cast_BevelDifferentialGearMeshPowerFlow",
        ) -> "_4095.GearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4095

            return self._parent._cast(_4095.GearMeshPowerFlow)

        @property
        def inter_mountable_component_connection_power_flow(
            self: "BevelDifferentialGearMeshPowerFlow._Cast_BevelDifferentialGearMeshPowerFlow",
        ) -> "_4102.InterMountableComponentConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4102

            return self._parent._cast(_4102.InterMountableComponentConnectionPowerFlow)

        @property
        def connection_power_flow(
            self: "BevelDifferentialGearMeshPowerFlow._Cast_BevelDifferentialGearMeshPowerFlow",
        ) -> "_4069.ConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4069

            return self._parent._cast(_4069.ConnectionPowerFlow)

        @property
        def connection_static_load_analysis_case(
            self: "BevelDifferentialGearMeshPowerFlow._Cast_BevelDifferentialGearMeshPowerFlow",
        ) -> "_7543.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelDifferentialGearMeshPowerFlow._Cast_BevelDifferentialGearMeshPowerFlow",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelDifferentialGearMeshPowerFlow._Cast_BevelDifferentialGearMeshPowerFlow",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearMeshPowerFlow._Cast_BevelDifferentialGearMeshPowerFlow",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearMeshPowerFlow._Cast_BevelDifferentialGearMeshPowerFlow",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_power_flow(
            self: "BevelDifferentialGearMeshPowerFlow._Cast_BevelDifferentialGearMeshPowerFlow",
        ) -> "BevelDifferentialGearMeshPowerFlow":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearMeshPowerFlow._Cast_BevelDifferentialGearMeshPowerFlow",
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
        self: Self, instance_to_wrap: "BevelDifferentialGearMeshPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self: Self) -> "_554.BevelGearMeshRating":
        """mastapy.gears.rating.bevel.BevelGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_554.BevelGearMeshRating":
        """mastapy.gears.rating.bevel.BevelGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2303.BevelDifferentialGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6826.BevelDifferentialGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialGearMeshPowerFlow._Cast_BevelDifferentialGearMeshPowerFlow":
        return self._Cast_BevelDifferentialGearMeshPowerFlow(self)
