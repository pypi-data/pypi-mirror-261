"""TorqueConverterConnectionCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7446,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "TorqueConverterConnectionCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2354
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7396,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7473,
        _7443,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterConnectionCompoundAdvancedSystemDeflection",)


Self = TypeVar(
    "Self", bound="TorqueConverterConnectionCompoundAdvancedSystemDeflection"
)


class TorqueConverterConnectionCompoundAdvancedSystemDeflection(
    _7446.CouplingConnectionCompoundAdvancedSystemDeflection
):
    """TorqueConverterConnectionCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_TorqueConverterConnectionCompoundAdvancedSystemDeflection",
    )

    class _Cast_TorqueConverterConnectionCompoundAdvancedSystemDeflection:
        """Special nested class for casting TorqueConverterConnectionCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "TorqueConverterConnectionCompoundAdvancedSystemDeflection._Cast_TorqueConverterConnectionCompoundAdvancedSystemDeflection",
            parent: "TorqueConverterConnectionCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_advanced_system_deflection(
            self: "TorqueConverterConnectionCompoundAdvancedSystemDeflection._Cast_TorqueConverterConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7446.CouplingConnectionCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7446.CouplingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def inter_mountable_component_connection_compound_advanced_system_deflection(
            self: "TorqueConverterConnectionCompoundAdvancedSystemDeflection._Cast_TorqueConverterConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7473.InterMountableComponentConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7473,
            )

            return self._parent._cast(
                _7473.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def connection_compound_advanced_system_deflection(
            self: "TorqueConverterConnectionCompoundAdvancedSystemDeflection._Cast_TorqueConverterConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7443.ConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7443,
            )

            return self._parent._cast(_7443.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "TorqueConverterConnectionCompoundAdvancedSystemDeflection._Cast_TorqueConverterConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7541.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterConnectionCompoundAdvancedSystemDeflection._Cast_TorqueConverterConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterConnectionCompoundAdvancedSystemDeflection._Cast_TorqueConverterConnectionCompoundAdvancedSystemDeflection",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def torque_converter_connection_compound_advanced_system_deflection(
            self: "TorqueConverterConnectionCompoundAdvancedSystemDeflection._Cast_TorqueConverterConnectionCompoundAdvancedSystemDeflection",
        ) -> "TorqueConverterConnectionCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "TorqueConverterConnectionCompoundAdvancedSystemDeflection._Cast_TorqueConverterConnectionCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "TorqueConverterConnectionCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2354.TorqueConverterConnection":
        """mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2354.TorqueConverterConnection":
        """mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection

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
    ) -> "List[_7396.TorqueConverterConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.TorqueConverterConnectionAdvancedSystemDeflection]

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
    ) -> "List[_7396.TorqueConverterConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.TorqueConverterConnectionAdvancedSystemDeflection]

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
    ) -> "TorqueConverterConnectionCompoundAdvancedSystemDeflection._Cast_TorqueConverterConnectionCompoundAdvancedSystemDeflection":
        return self._Cast_TorqueConverterConnectionCompoundAdvancedSystemDeflection(
            self
        )
