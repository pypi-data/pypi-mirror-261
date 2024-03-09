"""ConicalGearMeshHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5757
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ConicalGearMeshHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2309
    from mastapy.system_model.analyses_and_results.system_deflections import _2726
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5686,
        _5693,
        _5698,
        _5774,
        _5778,
        _5781,
        _5784,
        _5815,
        _5822,
        _5825,
        _5844,
        _5776,
        _5717,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543, _7540
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshHarmonicAnalysis",)


Self = TypeVar("Self", bound="ConicalGearMeshHarmonicAnalysis")


class ConicalGearMeshHarmonicAnalysis(_5757.GearMeshHarmonicAnalysis):
    """ConicalGearMeshHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearMeshHarmonicAnalysis")

    class _Cast_ConicalGearMeshHarmonicAnalysis:
        """Special nested class for casting ConicalGearMeshHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
            parent: "ConicalGearMeshHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_5757.GearMeshHarmonicAnalysis":
            return self._parent._cast(_5757.GearMeshHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_5776.InterMountableComponentConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5776,
            )

            return self._parent._cast(
                _5776.InterMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def connection_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_5717.ConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5717,
            )

            return self._parent._cast(_5717.ConnectionHarmonicAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_7543.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_5686.AGMAGleasonConicalGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5686,
            )

            return self._parent._cast(_5686.AGMAGleasonConicalGearMeshHarmonicAnalysis)

        @property
        def bevel_differential_gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_5693.BevelDifferentialGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5693,
            )

            return self._parent._cast(_5693.BevelDifferentialGearMeshHarmonicAnalysis)

        @property
        def bevel_gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_5698.BevelGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5698,
            )

            return self._parent._cast(_5698.BevelGearMeshHarmonicAnalysis)

        @property
        def hypoid_gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_5774.HypoidGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5774,
            )

            return self._parent._cast(_5774.HypoidGearMeshHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_5778.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5778,
            )

            return self._parent._cast(
                _5778.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_5781.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5781,
            )

            return self._parent._cast(
                _5781.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_5784.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5784,
            )

            return self._parent._cast(
                _5784.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_5815.SpiralBevelGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5815,
            )

            return self._parent._cast(_5815.SpiralBevelGearMeshHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_5822.StraightBevelDiffGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5822,
            )

            return self._parent._cast(_5822.StraightBevelDiffGearMeshHarmonicAnalysis)

        @property
        def straight_bevel_gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_5825.StraightBevelGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5825,
            )

            return self._parent._cast(_5825.StraightBevelGearMeshHarmonicAnalysis)

        @property
        def zerol_bevel_gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "_5844.ZerolBevelGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5844,
            )

            return self._parent._cast(_5844.ZerolBevelGearMeshHarmonicAnalysis)

        @property
        def conical_gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "ConicalGearMeshHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearMeshHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2309.ConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ConicalGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ConicalGearMeshHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2726.ConicalGearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConicalGearMeshSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis":
        return self._Cast_ConicalGearMeshHarmonicAnalysis(self)
