"""HypoidGearMeshSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2691
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "HypoidGearMeshSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.hypoid import _438
    from mastapy.system_model.connections_and_sockets.gears import _2317
    from mastapy.system_model.analyses_and_results.static_loads import _6909
    from mastapy.system_model.analyses_and_results.power_flows import _4099
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2726,
        _2761,
        _2769,
        _2729,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7542,
        _7543,
        _7540,
    )
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearMeshSystemDeflection",)


Self = TypeVar("Self", bound="HypoidGearMeshSystemDeflection")


class HypoidGearMeshSystemDeflection(_2691.AGMAGleasonConicalGearMeshSystemDeflection):
    """HypoidGearMeshSystemDeflection

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearMeshSystemDeflection")

    class _Cast_HypoidGearMeshSystemDeflection:
        """Special nested class for casting HypoidGearMeshSystemDeflection to subclasses."""

        def __init__(
            self: "HypoidGearMeshSystemDeflection._Cast_HypoidGearMeshSystemDeflection",
            parent: "HypoidGearMeshSystemDeflection",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_system_deflection(
            self: "HypoidGearMeshSystemDeflection._Cast_HypoidGearMeshSystemDeflection",
        ) -> "_2691.AGMAGleasonConicalGearMeshSystemDeflection":
            return self._parent._cast(_2691.AGMAGleasonConicalGearMeshSystemDeflection)

        @property
        def conical_gear_mesh_system_deflection(
            self: "HypoidGearMeshSystemDeflection._Cast_HypoidGearMeshSystemDeflection",
        ) -> "_2726.ConicalGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2726,
            )

            return self._parent._cast(_2726.ConicalGearMeshSystemDeflection)

        @property
        def gear_mesh_system_deflection(
            self: "HypoidGearMeshSystemDeflection._Cast_HypoidGearMeshSystemDeflection",
        ) -> "_2761.GearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2761,
            )

            return self._parent._cast(_2761.GearMeshSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "HypoidGearMeshSystemDeflection._Cast_HypoidGearMeshSystemDeflection",
        ) -> "_2769.InterMountableComponentConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2769,
            )

            return self._parent._cast(
                _2769.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "HypoidGearMeshSystemDeflection._Cast_HypoidGearMeshSystemDeflection",
        ) -> "_2729.ConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2729,
            )

            return self._parent._cast(_2729.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "HypoidGearMeshSystemDeflection._Cast_HypoidGearMeshSystemDeflection",
        ) -> "_7542.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "HypoidGearMeshSystemDeflection._Cast_HypoidGearMeshSystemDeflection",
        ) -> "_7543.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "HypoidGearMeshSystemDeflection._Cast_HypoidGearMeshSystemDeflection",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "HypoidGearMeshSystemDeflection._Cast_HypoidGearMeshSystemDeflection",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearMeshSystemDeflection._Cast_HypoidGearMeshSystemDeflection",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearMeshSystemDeflection._Cast_HypoidGearMeshSystemDeflection",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def hypoid_gear_mesh_system_deflection(
            self: "HypoidGearMeshSystemDeflection._Cast_HypoidGearMeshSystemDeflection",
        ) -> "HypoidGearMeshSystemDeflection":
            return self._parent

        def __getattr__(
            self: "HypoidGearMeshSystemDeflection._Cast_HypoidGearMeshSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearMeshSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self: Self) -> "_438.HypoidGearMeshRating":
        """mastapy.gears.rating.hypoid.HypoidGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_438.HypoidGearMeshRating":
        """mastapy.gears.rating.hypoid.HypoidGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2317.HypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6909.HypoidGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4099.HypoidGearMeshPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.HypoidGearMeshPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "HypoidGearMeshSystemDeflection._Cast_HypoidGearMeshSystemDeflection":
        return self._Cast_HypoidGearMeshSystemDeflection(self)
