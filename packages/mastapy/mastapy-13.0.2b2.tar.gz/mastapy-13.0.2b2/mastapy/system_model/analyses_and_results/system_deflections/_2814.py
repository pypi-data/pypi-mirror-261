"""SpringDamperSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2733
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "SpringDamperSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2602
    from mastapy.system_model.analyses_and_results.static_loads import _6961
    from mastapy.system_model.analyses_and_results.power_flows import _4143
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2808,
        _2687,
        _2787,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7549,
        _7550,
        _7547,
    )
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperSystemDeflection",)


Self = TypeVar("Self", bound="SpringDamperSystemDeflection")


class SpringDamperSystemDeflection(_2733.CouplingSystemDeflection):
    """SpringDamperSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpringDamperSystemDeflection")

    class _Cast_SpringDamperSystemDeflection:
        """Special nested class for casting SpringDamperSystemDeflection to subclasses."""

        def __init__(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
            parent: "SpringDamperSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_system_deflection(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ) -> "_2733.CouplingSystemDeflection":
            return self._parent._cast(_2733.CouplingSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ) -> "_2808.SpecialisedAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ) -> "_2687.AbstractAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2687,
            )

            return self._parent._cast(_2687.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ) -> "_2787.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2787,
            )

            return self._parent._cast(_2787.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ) -> "_7549.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def spring_damper_system_deflection(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ) -> "SpringDamperSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpringDamperSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2602.SpringDamper":
        """mastapy.system_model.part_model.couplings.SpringDamper

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6961.SpringDamperLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4143.SpringDamperPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.SpringDamperPowerFlow

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
    ) -> "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection":
        return self._Cast_SpringDamperSystemDeflection(self)
