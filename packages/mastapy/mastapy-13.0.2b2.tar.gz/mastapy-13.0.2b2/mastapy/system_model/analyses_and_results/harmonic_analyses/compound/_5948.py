"""KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5914
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
        "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5778
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5951,
        _5954,
        _5940,
        _5946,
        _5916,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis"
)


class KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis(
    _5914.ConicalGearMeshCompoundHarmonicAnalysis
):
    """KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_5914.ConicalGearMeshCompoundHarmonicAnalysis":
            return self._parent._cast(_5914.ConicalGearMeshCompoundHarmonicAnalysis)

        @property
        def gear_mesh_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_5940.GearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5940,
            )

            return self._parent._cast(_5940.GearMeshCompoundHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_5946.InterMountableComponentConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5946,
            )

            return self._parent._cast(
                _5946.InterMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def connection_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_5916.ConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5916,
            )

            return self._parent._cast(_5916.ConnectionCompoundHarmonicAnalysis)

        @property
        def connection_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_7541.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_5951.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5951,
            )

            return self._parent._cast(
                _5951.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",
        ) -> (
            "_5954.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5954,
            )

            return self._parent._cast(
                _5954.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5778.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis]

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5778.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis":
        return (
            self._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis(
                self
            )
        )
