"""KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4236
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_COMPOUND_POWER_FLOW = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
        "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2322
    from mastapy.system_model.analyses_and_results.power_flows import _4109
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4202,
        _4228,
        _4234,
        _4204,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow"
)


class KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow(
    _4236.KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow
):
    """KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_power_flow(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow",
        ) -> "_4236.KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow":
            return self._parent._cast(
                _4236.KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow
            )

        @property
        def conical_gear_mesh_compound_power_flow(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow",
        ) -> "_4202.ConicalGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4202,
            )

            return self._parent._cast(_4202.ConicalGearMeshCompoundPowerFlow)

        @property
        def gear_mesh_compound_power_flow(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow",
        ) -> "_4228.GearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4228,
            )

            return self._parent._cast(_4228.GearMeshCompoundPowerFlow)

        @property
        def inter_mountable_component_connection_compound_power_flow(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow",
        ) -> "_4234.InterMountableComponentConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4234,
            )

            return self._parent._cast(
                _4234.InterMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def connection_compound_power_flow(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow",
        ) -> "_4204.ConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4204,
            )

            return self._parent._cast(_4204.ConnectionCompoundPowerFlow)

        @property
        def connection_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow",
        ) -> "_7541.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_power_flow(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(
        self: Self,
    ) -> "_2322.KlingelnbergCycloPalloidSpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(
        self: Self,
    ) -> "_2322.KlingelnbergCycloPalloidSpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4109.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4109.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow]

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
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow(
            self
        )
