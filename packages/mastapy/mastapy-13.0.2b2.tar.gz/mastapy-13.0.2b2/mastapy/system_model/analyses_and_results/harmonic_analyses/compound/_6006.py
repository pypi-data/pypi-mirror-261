"""WormGearSetCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5941
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "WormGearSetCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2554
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5842
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _6004,
        _6005,
        _5979,
        _5881,
        _5960,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("WormGearSetCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="WormGearSetCompoundHarmonicAnalysis")


class WormGearSetCompoundHarmonicAnalysis(_5941.GearSetCompoundHarmonicAnalysis):
    """WormGearSetCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearSetCompoundHarmonicAnalysis")

    class _Cast_WormGearSetCompoundHarmonicAnalysis:
        """Special nested class for casting WormGearSetCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "WormGearSetCompoundHarmonicAnalysis._Cast_WormGearSetCompoundHarmonicAnalysis",
            parent: "WormGearSetCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_compound_harmonic_analysis(
            self: "WormGearSetCompoundHarmonicAnalysis._Cast_WormGearSetCompoundHarmonicAnalysis",
        ) -> "_5941.GearSetCompoundHarmonicAnalysis":
            return self._parent._cast(_5941.GearSetCompoundHarmonicAnalysis)

        @property
        def specialised_assembly_compound_harmonic_analysis(
            self: "WormGearSetCompoundHarmonicAnalysis._Cast_WormGearSetCompoundHarmonicAnalysis",
        ) -> "_5979.SpecialisedAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5979,
            )

            return self._parent._cast(_5979.SpecialisedAssemblyCompoundHarmonicAnalysis)

        @property
        def abstract_assembly_compound_harmonic_analysis(
            self: "WormGearSetCompoundHarmonicAnalysis._Cast_WormGearSetCompoundHarmonicAnalysis",
        ) -> "_5881.AbstractAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5881,
            )

            return self._parent._cast(_5881.AbstractAssemblyCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "WormGearSetCompoundHarmonicAnalysis._Cast_WormGearSetCompoundHarmonicAnalysis",
        ) -> "_5960.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5960,
            )

            return self._parent._cast(_5960.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "WormGearSetCompoundHarmonicAnalysis._Cast_WormGearSetCompoundHarmonicAnalysis",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "WormGearSetCompoundHarmonicAnalysis._Cast_WormGearSetCompoundHarmonicAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearSetCompoundHarmonicAnalysis._Cast_WormGearSetCompoundHarmonicAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def worm_gear_set_compound_harmonic_analysis(
            self: "WormGearSetCompoundHarmonicAnalysis._Cast_WormGearSetCompoundHarmonicAnalysis",
        ) -> "WormGearSetCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "WormGearSetCompoundHarmonicAnalysis._Cast_WormGearSetCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "WormGearSetCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2554.WormGearSet":
        """mastapy.system_model.part_model.gears.WormGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2554.WormGearSet":
        """mastapy.system_model.part_model.gears.WormGearSet

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
    ) -> "List[_5842.WormGearSetHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.WormGearSetHarmonicAnalysis]

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
    def worm_gears_compound_harmonic_analysis(
        self: Self,
    ) -> "List[_6004.WormGearCompoundHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.compound.WormGearCompoundHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGearsCompoundHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def worm_meshes_compound_harmonic_analysis(
        self: Self,
    ) -> "List[_6005.WormGearMeshCompoundHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.compound.WormGearMeshCompoundHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormMeshesCompoundHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5842.WormGearSetHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.WormGearSetHarmonicAnalysis]

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
    ) -> (
        "WormGearSetCompoundHarmonicAnalysis._Cast_WormGearSetCompoundHarmonicAnalysis"
    ):
        return self._Cast_WormGearSetCompoundHarmonicAnalysis(self)
