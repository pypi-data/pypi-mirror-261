"""BeltConnectionSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2769
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "BeltConnectionSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2270
    from mastapy.system_model.analyses_and_results.static_loads import _6823
    from mastapy.system_model.analyses_and_results.power_flows import _4043
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2734,
        _2729,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7542,
        _7543,
        _7540,
    )
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("BeltConnectionSystemDeflection",)


Self = TypeVar("Self", bound="BeltConnectionSystemDeflection")


class BeltConnectionSystemDeflection(
    _2769.InterMountableComponentConnectionSystemDeflection
):
    """BeltConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BeltConnectionSystemDeflection")

    class _Cast_BeltConnectionSystemDeflection:
        """Special nested class for casting BeltConnectionSystemDeflection to subclasses."""

        def __init__(
            self: "BeltConnectionSystemDeflection._Cast_BeltConnectionSystemDeflection",
            parent: "BeltConnectionSystemDeflection",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "BeltConnectionSystemDeflection._Cast_BeltConnectionSystemDeflection",
        ) -> "_2769.InterMountableComponentConnectionSystemDeflection":
            return self._parent._cast(
                _2769.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "BeltConnectionSystemDeflection._Cast_BeltConnectionSystemDeflection",
        ) -> "_2729.ConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2729,
            )

            return self._parent._cast(_2729.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "BeltConnectionSystemDeflection._Cast_BeltConnectionSystemDeflection",
        ) -> "_7542.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "BeltConnectionSystemDeflection._Cast_BeltConnectionSystemDeflection",
        ) -> "_7543.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BeltConnectionSystemDeflection._Cast_BeltConnectionSystemDeflection",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BeltConnectionSystemDeflection._Cast_BeltConnectionSystemDeflection",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BeltConnectionSystemDeflection._Cast_BeltConnectionSystemDeflection",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltConnectionSystemDeflection._Cast_BeltConnectionSystemDeflection",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_system_deflection(
            self: "BeltConnectionSystemDeflection._Cast_BeltConnectionSystemDeflection",
        ) -> "_2734.CVTBeltConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2734,
            )

            return self._parent._cast(_2734.CVTBeltConnectionSystemDeflection)

        @property
        def belt_connection_system_deflection(
            self: "BeltConnectionSystemDeflection._Cast_BeltConnectionSystemDeflection",
        ) -> "BeltConnectionSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BeltConnectionSystemDeflection._Cast_BeltConnectionSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BeltConnectionSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def extension(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Extension

        if temp is None:
            return 0.0

        return temp

    @property
    def extension_including_pre_tension(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExtensionIncludingPreTension

        if temp is None:
            return 0.0

        return temp

    @property
    def force_in_loa(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceInLOA

        if temp is None:
            return 0.0

        return temp

    @property
    def connection_design(self: Self) -> "_2270.BeltConnection":
        """mastapy.system_model.connections_and_sockets.BeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6823.BeltConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BeltConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4043.BeltConnectionPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.BeltConnectionPowerFlow

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
    ) -> "BeltConnectionSystemDeflection._Cast_BeltConnectionSystemDeflection":
        return self._Cast_BeltConnectionSystemDeflection(self)
