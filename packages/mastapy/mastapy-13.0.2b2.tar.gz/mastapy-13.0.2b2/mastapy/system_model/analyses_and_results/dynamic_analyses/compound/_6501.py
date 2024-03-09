"""RollingRingAssemblyCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6508
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "RollingRingAssemblyCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2599
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6372
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6410,
        _6489,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingAssemblyCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="RollingRingAssemblyCompoundDynamicAnalysis")


class RollingRingAssemblyCompoundDynamicAnalysis(
    _6508.SpecialisedAssemblyCompoundDynamicAnalysis
):
    """RollingRingAssemblyCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_ASSEMBLY_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RollingRingAssemblyCompoundDynamicAnalysis"
    )

    class _Cast_RollingRingAssemblyCompoundDynamicAnalysis:
        """Special nested class for casting RollingRingAssemblyCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "RollingRingAssemblyCompoundDynamicAnalysis._Cast_RollingRingAssemblyCompoundDynamicAnalysis",
            parent: "RollingRingAssemblyCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_dynamic_analysis(
            self: "RollingRingAssemblyCompoundDynamicAnalysis._Cast_RollingRingAssemblyCompoundDynamicAnalysis",
        ) -> "_6508.SpecialisedAssemblyCompoundDynamicAnalysis":
            return self._parent._cast(_6508.SpecialisedAssemblyCompoundDynamicAnalysis)

        @property
        def abstract_assembly_compound_dynamic_analysis(
            self: "RollingRingAssemblyCompoundDynamicAnalysis._Cast_RollingRingAssemblyCompoundDynamicAnalysis",
        ) -> "_6410.AbstractAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6410,
            )

            return self._parent._cast(_6410.AbstractAssemblyCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "RollingRingAssemblyCompoundDynamicAnalysis._Cast_RollingRingAssemblyCompoundDynamicAnalysis",
        ) -> "_6489.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6489,
            )

            return self._parent._cast(_6489.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "RollingRingAssemblyCompoundDynamicAnalysis._Cast_RollingRingAssemblyCompoundDynamicAnalysis",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RollingRingAssemblyCompoundDynamicAnalysis._Cast_RollingRingAssemblyCompoundDynamicAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingAssemblyCompoundDynamicAnalysis._Cast_RollingRingAssemblyCompoundDynamicAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def rolling_ring_assembly_compound_dynamic_analysis(
            self: "RollingRingAssemblyCompoundDynamicAnalysis._Cast_RollingRingAssemblyCompoundDynamicAnalysis",
        ) -> "RollingRingAssemblyCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "RollingRingAssemblyCompoundDynamicAnalysis._Cast_RollingRingAssemblyCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "RollingRingAssemblyCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2599.RollingRingAssembly":
        """mastapy.system_model.part_model.couplings.RollingRingAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2599.RollingRingAssembly":
        """mastapy.system_model.part_model.couplings.RollingRingAssembly

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
    ) -> "List[_6372.RollingRingAssemblyDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.RollingRingAssemblyDynamicAnalysis]

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
    ) -> "List[_6372.RollingRingAssemblyDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.RollingRingAssemblyDynamicAnalysis]

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
    ) -> "RollingRingAssemblyCompoundDynamicAnalysis._Cast_RollingRingAssemblyCompoundDynamicAnalysis":
        return self._Cast_RollingRingAssemblyCompoundDynamicAnalysis(self)
