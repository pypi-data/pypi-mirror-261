"""GearMeshCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6742,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "GearMeshCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6607
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6682,
        _6689,
        _6694,
        _6707,
        _6710,
        _6725,
        _6731,
        _6740,
        _6744,
        _6747,
        _6750,
        _6777,
        _6783,
        _6786,
        _6801,
        _6804,
        _6712,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="GearMeshCompoundCriticalSpeedAnalysis")


class GearMeshCompoundCriticalSpeedAnalysis(
    _6742.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
):
    """GearMeshCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearMeshCompoundCriticalSpeedAnalysis"
    )

    class _Cast_GearMeshCompoundCriticalSpeedAnalysis:
        """Special nested class for casting GearMeshCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
            parent: "GearMeshCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6742.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis":
            return self._parent._cast(
                _6742.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def connection_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6712.ConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6712,
            )

            return self._parent._cast(_6712.ConnectionCompoundCriticalSpeedAnalysis)

        @property
        def connection_compound_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_7541.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6682.AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6682,
            )

            return self._parent._cast(
                _6682.AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6689.BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6689,
            )

            return self._parent._cast(
                _6689.BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6694.BevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6694,
            )

            return self._parent._cast(_6694.BevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def concept_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6707.ConceptGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6707,
            )

            return self._parent._cast(
                _6707.ConceptGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6710.ConicalGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6710,
            )

            return self._parent._cast(
                _6710.ConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def cylindrical_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6725.CylindricalGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6725,
            )

            return self._parent._cast(
                _6725.CylindricalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def face_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6731.FaceGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6731,
            )

            return self._parent._cast(_6731.FaceGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6740.HypoidGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6740,
            )

            return self._parent._cast(_6740.HypoidGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> (
            "_6744.KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6744,
            )

            return self._parent._cast(
                _6744.KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> (
            "_6747.KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6747,
            )

            return self._parent._cast(
                _6747.KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6750.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6750,
            )

            return self._parent._cast(
                _6750.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6777.SpiralBevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6777,
            )

            return self._parent._cast(
                _6777.SpiralBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6783.StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6783,
            )

            return self._parent._cast(
                _6783.StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6786.StraightBevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6786,
            )

            return self._parent._cast(
                _6786.StraightBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def worm_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6801.WormGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6801,
            )

            return self._parent._cast(_6801.WormGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6804.ZerolBevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6804,
            )

            return self._parent._cast(
                _6804.ZerolBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "GearMeshCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "GearMeshCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6607.GearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.GearMeshCriticalSpeedAnalysis]

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
    ) -> "List[_6607.GearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.GearMeshCriticalSpeedAnalysis]

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
    ) -> "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis":
        return self._Cast_GearMeshCompoundCriticalSpeedAnalysis(self)
