"""FlexiblePinAssemblyCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2953
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "FlexiblePinAssemblyCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2456
    from mastapy.system_model.analyses_and_results.system_deflections import _2760
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2853,
        _2933,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("FlexiblePinAssemblyCompoundSystemDeflection",)


Self = TypeVar("Self", bound="FlexiblePinAssemblyCompoundSystemDeflection")


class FlexiblePinAssemblyCompoundSystemDeflection(
    _2953.SpecialisedAssemblyCompoundSystemDeflection
):
    """FlexiblePinAssemblyCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FlexiblePinAssemblyCompoundSystemDeflection"
    )

    class _Cast_FlexiblePinAssemblyCompoundSystemDeflection:
        """Special nested class for casting FlexiblePinAssemblyCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "FlexiblePinAssemblyCompoundSystemDeflection._Cast_FlexiblePinAssemblyCompoundSystemDeflection",
            parent: "FlexiblePinAssemblyCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_system_deflection(
            self: "FlexiblePinAssemblyCompoundSystemDeflection._Cast_FlexiblePinAssemblyCompoundSystemDeflection",
        ) -> "_2953.SpecialisedAssemblyCompoundSystemDeflection":
            return self._parent._cast(_2953.SpecialisedAssemblyCompoundSystemDeflection)

        @property
        def abstract_assembly_compound_system_deflection(
            self: "FlexiblePinAssemblyCompoundSystemDeflection._Cast_FlexiblePinAssemblyCompoundSystemDeflection",
        ) -> "_2853.AbstractAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2853,
            )

            return self._parent._cast(_2853.AbstractAssemblyCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "FlexiblePinAssemblyCompoundSystemDeflection._Cast_FlexiblePinAssemblyCompoundSystemDeflection",
        ) -> "_2933.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2933,
            )

            return self._parent._cast(_2933.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "FlexiblePinAssemblyCompoundSystemDeflection._Cast_FlexiblePinAssemblyCompoundSystemDeflection",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "FlexiblePinAssemblyCompoundSystemDeflection._Cast_FlexiblePinAssemblyCompoundSystemDeflection",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "FlexiblePinAssemblyCompoundSystemDeflection._Cast_FlexiblePinAssemblyCompoundSystemDeflection",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def flexible_pin_assembly_compound_system_deflection(
            self: "FlexiblePinAssemblyCompoundSystemDeflection._Cast_FlexiblePinAssemblyCompoundSystemDeflection",
        ) -> "FlexiblePinAssemblyCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "FlexiblePinAssemblyCompoundSystemDeflection._Cast_FlexiblePinAssemblyCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "FlexiblePinAssemblyCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2456.FlexiblePinAssembly":
        """mastapy.system_model.part_model.FlexiblePinAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2456.FlexiblePinAssembly":
        """mastapy.system_model.part_model.FlexiblePinAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_2760.FlexiblePinAssemblySystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.FlexiblePinAssemblySystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_2760.FlexiblePinAssemblySystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.FlexiblePinAssemblySystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "FlexiblePinAssemblyCompoundSystemDeflection._Cast_FlexiblePinAssemblyCompoundSystemDeflection":
        return self._Cast_FlexiblePinAssemblyCompoundSystemDeflection(self)
