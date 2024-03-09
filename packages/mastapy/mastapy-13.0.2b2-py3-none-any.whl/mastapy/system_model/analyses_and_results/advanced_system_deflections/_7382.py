"""SpringDamperHalfAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7315
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "SpringDamperHalfAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2603
    from mastapy.system_model.analyses_and_results.static_loads import _6960
    from mastapy.system_model.analyses_and_results.system_deflections import _2813
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7355,
        _7300,
        _7357,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperHalfAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="SpringDamperHalfAdvancedSystemDeflection")


class SpringDamperHalfAdvancedSystemDeflection(
    _7315.CouplingHalfAdvancedSystemDeflection
):
    """SpringDamperHalfAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_HALF_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpringDamperHalfAdvancedSystemDeflection"
    )

    class _Cast_SpringDamperHalfAdvancedSystemDeflection:
        """Special nested class for casting SpringDamperHalfAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "SpringDamperHalfAdvancedSystemDeflection._Cast_SpringDamperHalfAdvancedSystemDeflection",
            parent: "SpringDamperHalfAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_half_advanced_system_deflection(
            self: "SpringDamperHalfAdvancedSystemDeflection._Cast_SpringDamperHalfAdvancedSystemDeflection",
        ) -> "_7315.CouplingHalfAdvancedSystemDeflection":
            return self._parent._cast(_7315.CouplingHalfAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "SpringDamperHalfAdvancedSystemDeflection._Cast_SpringDamperHalfAdvancedSystemDeflection",
        ) -> "_7355.MountableComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7355,
            )

            return self._parent._cast(_7355.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "SpringDamperHalfAdvancedSystemDeflection._Cast_SpringDamperHalfAdvancedSystemDeflection",
        ) -> "_7300.ComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7300,
            )

            return self._parent._cast(_7300.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "SpringDamperHalfAdvancedSystemDeflection._Cast_SpringDamperHalfAdvancedSystemDeflection",
        ) -> "_7357.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7357,
            )

            return self._parent._cast(_7357.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "SpringDamperHalfAdvancedSystemDeflection._Cast_SpringDamperHalfAdvancedSystemDeflection",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpringDamperHalfAdvancedSystemDeflection._Cast_SpringDamperHalfAdvancedSystemDeflection",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpringDamperHalfAdvancedSystemDeflection._Cast_SpringDamperHalfAdvancedSystemDeflection",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperHalfAdvancedSystemDeflection._Cast_SpringDamperHalfAdvancedSystemDeflection",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperHalfAdvancedSystemDeflection._Cast_SpringDamperHalfAdvancedSystemDeflection",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def spring_damper_half_advanced_system_deflection(
            self: "SpringDamperHalfAdvancedSystemDeflection._Cast_SpringDamperHalfAdvancedSystemDeflection",
        ) -> "SpringDamperHalfAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SpringDamperHalfAdvancedSystemDeflection._Cast_SpringDamperHalfAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "SpringDamperHalfAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2603.SpringDamperHalf":
        """mastapy.system_model.part_model.couplings.SpringDamperHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6960.SpringDamperHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperHalfLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_system_deflection_results(
        self: Self,
    ) -> "List[_2813.SpringDamperHalfSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.SpringDamperHalfSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpringDamperHalfAdvancedSystemDeflection._Cast_SpringDamperHalfAdvancedSystemDeflection":
        return self._Cast_SpringDamperHalfAdvancedSystemDeflection(self)
