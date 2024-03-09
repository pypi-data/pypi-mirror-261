"""ConicalGearMeshCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6736,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "ConicalGearMeshCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6578
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6682,
        _6689,
        _6694,
        _6740,
        _6744,
        _6747,
        _6750,
        _6777,
        _6783,
        _6786,
        _6804,
        _6742,
        _6712,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ConicalGearMeshCompoundCriticalSpeedAnalysis")


class ConicalGearMeshCompoundCriticalSpeedAnalysis(
    _6736.GearMeshCompoundCriticalSpeedAnalysis
):
    """ConicalGearMeshCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearMeshCompoundCriticalSpeedAnalysis"
    )

    class _Cast_ConicalGearMeshCompoundCriticalSpeedAnalysis:
        """Special nested class for casting ConicalGearMeshCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_ConicalGearMeshCompoundCriticalSpeedAnalysis",
            parent: "ConicalGearMeshCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_critical_speed_analysis(
            self: "ConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_ConicalGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6736.GearMeshCompoundCriticalSpeedAnalysis":
            return self._parent._cast(_6736.GearMeshCompoundCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_compound_critical_speed_analysis(
            self: "ConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_ConicalGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6742.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6742,
            )

            return self._parent._cast(
                _6742.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def connection_compound_critical_speed_analysis(
            self: "ConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_ConicalGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6712.ConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6712,
            )

            return self._parent._cast(_6712.ConnectionCompoundCriticalSpeedAnalysis)

        @property
        def connection_compound_analysis(
            self: "ConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_ConicalGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_7541.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_ConicalGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_ConicalGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_critical_speed_analysis(
            self: "ConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_ConicalGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6682.AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6682,
            )

            return self._parent._cast(
                _6682.AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_gear_mesh_compound_critical_speed_analysis(
            self: "ConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_ConicalGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6689.BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6689,
            )

            return self._parent._cast(
                _6689.BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_mesh_compound_critical_speed_analysis(
            self: "ConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_ConicalGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6694.BevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6694,
            )

            return self._parent._cast(_6694.BevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_mesh_compound_critical_speed_analysis(
            self: "ConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_ConicalGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6740.HypoidGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6740,
            )

            return self._parent._cast(_6740.HypoidGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_critical_speed_analysis(
            self: "ConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_ConicalGearMeshCompoundCriticalSpeedAnalysis",
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
            self: "ConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_ConicalGearMeshCompoundCriticalSpeedAnalysis",
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
            self: "ConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_ConicalGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6750.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6750,
            )

            return self._parent._cast(
                _6750.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "ConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_ConicalGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6777.SpiralBevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6777,
            )

            return self._parent._cast(
                _6777.SpiralBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_critical_speed_analysis(
            self: "ConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_ConicalGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6783.StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6783,
            )

            return self._parent._cast(
                _6783.StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "ConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_ConicalGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6786.StraightBevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6786,
            )

            return self._parent._cast(
                _6786.StraightBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def zerol_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "ConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_ConicalGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6804.ZerolBevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6804,
            )

            return self._parent._cast(
                _6804.ZerolBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_mesh_compound_critical_speed_analysis(
            self: "ConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_ConicalGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "ConicalGearMeshCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_ConicalGearMeshCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "ConicalGearMeshCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetaries(self: Self) -> "List[ConicalGearMeshCompoundCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.compound.ConicalGearMeshCompoundCriticalSpeedAnalysis]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6578.ConicalGearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ConicalGearMeshCriticalSpeedAnalysis]

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
    ) -> "List[_6578.ConicalGearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ConicalGearMeshCriticalSpeedAnalysis]

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
    ) -> "ConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_ConicalGearMeshCompoundCriticalSpeedAnalysis":
        return self._Cast_ConicalGearMeshCompoundCriticalSpeedAnalysis(self)
