"""InterMountableComponentConnectionCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6712,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
        "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6613
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6682,
        _6686,
        _6689,
        _6694,
        _6699,
        _6704,
        _6707,
        _6710,
        _6715,
        _6717,
        _6725,
        _6731,
        _6736,
        _6740,
        _6744,
        _6747,
        _6750,
        _6758,
        _6767,
        _6770,
        _6777,
        _6780,
        _6783,
        _6786,
        _6795,
        _6801,
        _6804,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",)


Self = TypeVar(
    "Self", bound="InterMountableComponentConnectionCompoundCriticalSpeedAnalysis"
)


class InterMountableComponentConnectionCompoundCriticalSpeedAnalysis(
    _6712.ConnectionCompoundCriticalSpeedAnalysis
):
    """InterMountableComponentConnectionCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
    )

    class _Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis:
        """Special nested class for casting InterMountableComponentConnectionCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
            parent: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def connection_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6712.ConnectionCompoundCriticalSpeedAnalysis":
            return self._parent._cast(_6712.ConnectionCompoundCriticalSpeedAnalysis)

        @property
        def connection_compound_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_7541.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6682.AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6682,
            )

            return self._parent._cast(
                _6682.AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def belt_connection_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6686.BeltConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6686,
            )

            return self._parent._cast(_6686.BeltConnectionCompoundCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6689.BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6689,
            )

            return self._parent._cast(
                _6689.BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6694.BevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6694,
            )

            return self._parent._cast(_6694.BevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def clutch_connection_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6699.ClutchConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6699,
            )

            return self._parent._cast(
                _6699.ClutchConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def concept_coupling_connection_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6704.ConceptCouplingConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6704,
            )

            return self._parent._cast(
                _6704.ConceptCouplingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def concept_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6707.ConceptGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6707,
            )

            return self._parent._cast(
                _6707.ConceptGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6710.ConicalGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6710,
            )

            return self._parent._cast(
                _6710.ConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def coupling_connection_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6715.CouplingConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6715,
            )

            return self._parent._cast(
                _6715.CouplingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def cvt_belt_connection_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6717.CVTBeltConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6717,
            )

            return self._parent._cast(
                _6717.CVTBeltConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def cylindrical_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6725.CylindricalGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6725,
            )

            return self._parent._cast(
                _6725.CylindricalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def face_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6731.FaceGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6731,
            )

            return self._parent._cast(_6731.FaceGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6736.GearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6736,
            )

            return self._parent._cast(_6736.GearMeshCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6740.HypoidGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6740,
            )

            return self._parent._cast(_6740.HypoidGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
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
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
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
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6750.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6750,
            )

            return self._parent._cast(
                _6750.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6758.PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6758,
            )

            return self._parent._cast(
                _6758.PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def ring_pins_to_disc_connection_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6767.RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6767,
            )

            return self._parent._cast(
                _6767.RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def rolling_ring_connection_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6770.RollingRingConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6770,
            )

            return self._parent._cast(
                _6770.RollingRingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6777.SpiralBevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6777,
            )

            return self._parent._cast(
                _6777.SpiralBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def spring_damper_connection_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6780.SpringDamperConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6780,
            )

            return self._parent._cast(
                _6780.SpringDamperConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6783.StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6783,
            )

            return self._parent._cast(
                _6783.StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6786.StraightBevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6786,
            )

            return self._parent._cast(
                _6786.StraightBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def torque_converter_connection_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6795.TorqueConverterConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6795,
            )

            return self._parent._cast(
                _6795.TorqueConverterConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def worm_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6801.WormGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6801,
            )

            return self._parent._cast(_6801.WormGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6804.ZerolBevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6804,
            )

            return self._parent._cast(
                _6804.ZerolBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def inter_mountable_component_connection_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6613.InterMountableComponentConnectionCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.InterMountableComponentConnectionCriticalSpeedAnalysis]

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
    ) -> "List[_6613.InterMountableComponentConnectionCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.InterMountableComponentConnectionCriticalSpeedAnalysis]

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
    ) -> "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis":
        return (
            self._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis(
                self
            )
        )
