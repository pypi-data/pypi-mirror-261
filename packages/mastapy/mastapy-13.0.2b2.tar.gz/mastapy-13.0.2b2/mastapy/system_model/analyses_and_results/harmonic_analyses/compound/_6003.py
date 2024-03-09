"""VirtualComponentCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5958
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "VirtualComponentCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5839
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5956,
        _5957,
        _5967,
        _5968,
        _6002,
        _5906,
        _5960,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="VirtualComponentCompoundHarmonicAnalysis")


class VirtualComponentCompoundHarmonicAnalysis(
    _5958.MountableComponentCompoundHarmonicAnalysis
):
    """VirtualComponentCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualComponentCompoundHarmonicAnalysis"
    )

    class _Cast_VirtualComponentCompoundHarmonicAnalysis:
        """Special nested class for casting VirtualComponentCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "VirtualComponentCompoundHarmonicAnalysis._Cast_VirtualComponentCompoundHarmonicAnalysis",
            parent: "VirtualComponentCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "VirtualComponentCompoundHarmonicAnalysis._Cast_VirtualComponentCompoundHarmonicAnalysis",
        ) -> "_5958.MountableComponentCompoundHarmonicAnalysis":
            return self._parent._cast(_5958.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "VirtualComponentCompoundHarmonicAnalysis._Cast_VirtualComponentCompoundHarmonicAnalysis",
        ) -> "_5906.ComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5906,
            )

            return self._parent._cast(_5906.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "VirtualComponentCompoundHarmonicAnalysis._Cast_VirtualComponentCompoundHarmonicAnalysis",
        ) -> "_5960.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5960,
            )

            return self._parent._cast(_5960.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "VirtualComponentCompoundHarmonicAnalysis._Cast_VirtualComponentCompoundHarmonicAnalysis",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "VirtualComponentCompoundHarmonicAnalysis._Cast_VirtualComponentCompoundHarmonicAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentCompoundHarmonicAnalysis._Cast_VirtualComponentCompoundHarmonicAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def mass_disc_compound_harmonic_analysis(
            self: "VirtualComponentCompoundHarmonicAnalysis._Cast_VirtualComponentCompoundHarmonicAnalysis",
        ) -> "_5956.MassDiscCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5956,
            )

            return self._parent._cast(_5956.MassDiscCompoundHarmonicAnalysis)

        @property
        def measurement_component_compound_harmonic_analysis(
            self: "VirtualComponentCompoundHarmonicAnalysis._Cast_VirtualComponentCompoundHarmonicAnalysis",
        ) -> "_5957.MeasurementComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5957,
            )

            return self._parent._cast(
                _5957.MeasurementComponentCompoundHarmonicAnalysis
            )

        @property
        def point_load_compound_harmonic_analysis(
            self: "VirtualComponentCompoundHarmonicAnalysis._Cast_VirtualComponentCompoundHarmonicAnalysis",
        ) -> "_5967.PointLoadCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5967,
            )

            return self._parent._cast(_5967.PointLoadCompoundHarmonicAnalysis)

        @property
        def power_load_compound_harmonic_analysis(
            self: "VirtualComponentCompoundHarmonicAnalysis._Cast_VirtualComponentCompoundHarmonicAnalysis",
        ) -> "_5968.PowerLoadCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5968,
            )

            return self._parent._cast(_5968.PowerLoadCompoundHarmonicAnalysis)

        @property
        def unbalanced_mass_compound_harmonic_analysis(
            self: "VirtualComponentCompoundHarmonicAnalysis._Cast_VirtualComponentCompoundHarmonicAnalysis",
        ) -> "_6002.UnbalancedMassCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6002,
            )

            return self._parent._cast(_6002.UnbalancedMassCompoundHarmonicAnalysis)

        @property
        def virtual_component_compound_harmonic_analysis(
            self: "VirtualComponentCompoundHarmonicAnalysis._Cast_VirtualComponentCompoundHarmonicAnalysis",
        ) -> "VirtualComponentCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "VirtualComponentCompoundHarmonicAnalysis._Cast_VirtualComponentCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "VirtualComponentCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5839.VirtualComponentHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.VirtualComponentHarmonicAnalysis]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5839.VirtualComponentHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.VirtualComponentHarmonicAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "VirtualComponentCompoundHarmonicAnalysis._Cast_VirtualComponentCompoundHarmonicAnalysis":
        return self._Cast_VirtualComponentCompoundHarmonicAnalysis(self)
