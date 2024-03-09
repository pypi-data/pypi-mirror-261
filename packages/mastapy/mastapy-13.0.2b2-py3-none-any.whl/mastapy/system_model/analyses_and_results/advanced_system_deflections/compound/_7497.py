"""RingPinsCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7485,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "RingPinsCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2572
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7367,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7433,
        _7487,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="RingPinsCompoundAdvancedSystemDeflection")


class RingPinsCompoundAdvancedSystemDeflection(
    _7485.MountableComponentCompoundAdvancedSystemDeflection
):
    """RingPinsCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _RING_PINS_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RingPinsCompoundAdvancedSystemDeflection"
    )

    class _Cast_RingPinsCompoundAdvancedSystemDeflection:
        """Special nested class for casting RingPinsCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "RingPinsCompoundAdvancedSystemDeflection._Cast_RingPinsCompoundAdvancedSystemDeflection",
            parent: "RingPinsCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "RingPinsCompoundAdvancedSystemDeflection._Cast_RingPinsCompoundAdvancedSystemDeflection",
        ) -> "_7485.MountableComponentCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7485.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "RingPinsCompoundAdvancedSystemDeflection._Cast_RingPinsCompoundAdvancedSystemDeflection",
        ) -> "_7433.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7433,
            )

            return self._parent._cast(_7433.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "RingPinsCompoundAdvancedSystemDeflection._Cast_RingPinsCompoundAdvancedSystemDeflection",
        ) -> "_7487.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7487,
            )

            return self._parent._cast(_7487.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "RingPinsCompoundAdvancedSystemDeflection._Cast_RingPinsCompoundAdvancedSystemDeflection",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RingPinsCompoundAdvancedSystemDeflection._Cast_RingPinsCompoundAdvancedSystemDeflection",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsCompoundAdvancedSystemDeflection._Cast_RingPinsCompoundAdvancedSystemDeflection",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def ring_pins_compound_advanced_system_deflection(
            self: "RingPinsCompoundAdvancedSystemDeflection._Cast_RingPinsCompoundAdvancedSystemDeflection",
        ) -> "RingPinsCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "RingPinsCompoundAdvancedSystemDeflection._Cast_RingPinsCompoundAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "RingPinsCompoundAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2572.RingPins":
        """mastapy.system_model.part_model.cycloidal.RingPins

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
    ) -> "List[_7367.RingPinsAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.RingPinsAdvancedSystemDeflection]

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
    ) -> "List[_7367.RingPinsAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.RingPinsAdvancedSystemDeflection]

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
    ) -> "RingPinsCompoundAdvancedSystemDeflection._Cast_RingPinsCompoundAdvancedSystemDeflection":
        return self._Cast_RingPinsCompoundAdvancedSystemDeflection(self)
