"""PointLoadCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7530,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "PointLoadCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2473
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7364,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7485,
        _7433,
        _7487,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("PointLoadCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="PointLoadCompoundAdvancedSystemDeflection")


class PointLoadCompoundAdvancedSystemDeflection(
    _7530.VirtualComponentCompoundAdvancedSystemDeflection
):
    """PointLoadCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _POINT_LOAD_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PointLoadCompoundAdvancedSystemDeflection"
    )

    class _Cast_PointLoadCompoundAdvancedSystemDeflection:
        """Special nested class for casting PointLoadCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "PointLoadCompoundAdvancedSystemDeflection._Cast_PointLoadCompoundAdvancedSystemDeflection",
            parent: "PointLoadCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_advanced_system_deflection(
            self: "PointLoadCompoundAdvancedSystemDeflection._Cast_PointLoadCompoundAdvancedSystemDeflection",
        ) -> "_7530.VirtualComponentCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7530.VirtualComponentCompoundAdvancedSystemDeflection
            )

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "PointLoadCompoundAdvancedSystemDeflection._Cast_PointLoadCompoundAdvancedSystemDeflection",
        ) -> "_7485.MountableComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7485,
            )

            return self._parent._cast(
                _7485.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "PointLoadCompoundAdvancedSystemDeflection._Cast_PointLoadCompoundAdvancedSystemDeflection",
        ) -> "_7433.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7433,
            )

            return self._parent._cast(_7433.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "PointLoadCompoundAdvancedSystemDeflection._Cast_PointLoadCompoundAdvancedSystemDeflection",
        ) -> "_7487.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7487,
            )

            return self._parent._cast(_7487.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "PointLoadCompoundAdvancedSystemDeflection._Cast_PointLoadCompoundAdvancedSystemDeflection",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PointLoadCompoundAdvancedSystemDeflection._Cast_PointLoadCompoundAdvancedSystemDeflection",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PointLoadCompoundAdvancedSystemDeflection._Cast_PointLoadCompoundAdvancedSystemDeflection",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def point_load_compound_advanced_system_deflection(
            self: "PointLoadCompoundAdvancedSystemDeflection._Cast_PointLoadCompoundAdvancedSystemDeflection",
        ) -> "PointLoadCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "PointLoadCompoundAdvancedSystemDeflection._Cast_PointLoadCompoundAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "PointLoadCompoundAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2473.PointLoad":
        """mastapy.system_model.part_model.PointLoad

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7364.PointLoadAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.PointLoadAdvancedSystemDeflection]

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
    ) -> "List[_7364.PointLoadAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.PointLoadAdvancedSystemDeflection]

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
    ) -> "PointLoadCompoundAdvancedSystemDeflection._Cast_PointLoadCompoundAdvancedSystemDeflection":
        return self._Cast_PointLoadCompoundAdvancedSystemDeflection(self)
