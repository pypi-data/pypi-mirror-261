"""ConceptCouplingSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2733
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "ConceptCouplingSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2583
    from mastapy.system_model.analyses_and_results.static_loads import _6843
    from mastapy.system_model.analyses_and_results.power_flows import _4062
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
__all__ = ("ConceptCouplingSystemDeflection",)


Self = TypeVar("Self", bound="ConceptCouplingSystemDeflection")


class ConceptCouplingSystemDeflection(_2733.CouplingSystemDeflection):
    """ConceptCouplingSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptCouplingSystemDeflection")

    class _Cast_ConceptCouplingSystemDeflection:
        """Special nested class for casting ConceptCouplingSystemDeflection to subclasses."""

        def __init__(
            self: "ConceptCouplingSystemDeflection._Cast_ConceptCouplingSystemDeflection",
            parent: "ConceptCouplingSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_system_deflection(
            self: "ConceptCouplingSystemDeflection._Cast_ConceptCouplingSystemDeflection",
        ) -> "_2733.CouplingSystemDeflection":
            return self._parent._cast(_2733.CouplingSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "ConceptCouplingSystemDeflection._Cast_ConceptCouplingSystemDeflection",
        ) -> "_2808.SpecialisedAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "ConceptCouplingSystemDeflection._Cast_ConceptCouplingSystemDeflection",
        ) -> "_2687.AbstractAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2687,
            )

            return self._parent._cast(_2687.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "ConceptCouplingSystemDeflection._Cast_ConceptCouplingSystemDeflection",
        ) -> "_2787.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2787,
            )

            return self._parent._cast(_2787.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "ConceptCouplingSystemDeflection._Cast_ConceptCouplingSystemDeflection",
        ) -> "_7549.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConceptCouplingSystemDeflection._Cast_ConceptCouplingSystemDeflection",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptCouplingSystemDeflection._Cast_ConceptCouplingSystemDeflection",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptCouplingSystemDeflection._Cast_ConceptCouplingSystemDeflection",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingSystemDeflection._Cast_ConceptCouplingSystemDeflection",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingSystemDeflection._Cast_ConceptCouplingSystemDeflection",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def concept_coupling_system_deflection(
            self: "ConceptCouplingSystemDeflection._Cast_ConceptCouplingSystemDeflection",
        ) -> "ConceptCouplingSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingSystemDeflection._Cast_ConceptCouplingSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptCouplingSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2583.ConceptCoupling":
        """mastapy.system_model.part_model.couplings.ConceptCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6843.ConceptCouplingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4062.ConceptCouplingPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.ConceptCouplingPowerFlow

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
    ) -> "ConceptCouplingSystemDeflection._Cast_ConceptCouplingSystemDeflection":
        return self._Cast_ConceptCouplingSystemDeflection(self)
