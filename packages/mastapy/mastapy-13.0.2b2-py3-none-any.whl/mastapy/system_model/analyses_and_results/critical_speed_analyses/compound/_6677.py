"""AbstractAssemblyCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6756,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "AbstractAssemblyCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6545
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6683,
        _6684,
        _6687,
        _6690,
        _6695,
        _6697,
        _6698,
        _6703,
        _6708,
        _6711,
        _6714,
        _6718,
        _6720,
        _6726,
        _6732,
        _6734,
        _6737,
        _6741,
        _6745,
        _6748,
        _6751,
        _6757,
        _6761,
        _6768,
        _6771,
        _6775,
        _6778,
        _6779,
        _6784,
        _6787,
        _6790,
        _6794,
        _6802,
        _6805,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="AbstractAssemblyCompoundCriticalSpeedAnalysis")


class AbstractAssemblyCompoundCriticalSpeedAnalysis(
    _6756.PartCompoundCriticalSpeedAnalysis
):
    """AbstractAssemblyCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis"
    )

    class _Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis:
        """Special nested class for casting AbstractAssemblyCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
            parent: "AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def part_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6756.PartCompoundCriticalSpeedAnalysis":
            return self._parent._cast(_6756.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6683.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6683,
            )

            return self._parent._cast(
                _6683.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def assembly_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6684.AssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6684,
            )

            return self._parent._cast(_6684.AssemblyCompoundCriticalSpeedAnalysis)

        @property
        def belt_drive_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6687.BeltDriveCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6687,
            )

            return self._parent._cast(_6687.BeltDriveCompoundCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6690.BevelDifferentialGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6690,
            )

            return self._parent._cast(
                _6690.BevelDifferentialGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6695.BevelGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6695,
            )

            return self._parent._cast(_6695.BevelGearSetCompoundCriticalSpeedAnalysis)

        @property
        def bolted_joint_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6697.BoltedJointCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6697,
            )

            return self._parent._cast(_6697.BoltedJointCompoundCriticalSpeedAnalysis)

        @property
        def clutch_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6698.ClutchCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6698,
            )

            return self._parent._cast(_6698.ClutchCompoundCriticalSpeedAnalysis)

        @property
        def concept_coupling_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6703.ConceptCouplingCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6703,
            )

            return self._parent._cast(
                _6703.ConceptCouplingCompoundCriticalSpeedAnalysis
            )

        @property
        def concept_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6708.ConceptGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6708,
            )

            return self._parent._cast(_6708.ConceptGearSetCompoundCriticalSpeedAnalysis)

        @property
        def conical_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6711.ConicalGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6711,
            )

            return self._parent._cast(_6711.ConicalGearSetCompoundCriticalSpeedAnalysis)

        @property
        def coupling_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6714.CouplingCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6714,
            )

            return self._parent._cast(_6714.CouplingCompoundCriticalSpeedAnalysis)

        @property
        def cvt_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6718.CVTCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6718,
            )

            return self._parent._cast(_6718.CVTCompoundCriticalSpeedAnalysis)

        @property
        def cycloidal_assembly_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6720.CycloidalAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6720,
            )

            return self._parent._cast(
                _6720.CycloidalAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def cylindrical_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6726.CylindricalGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6726,
            )

            return self._parent._cast(
                _6726.CylindricalGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def face_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6732.FaceGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6732,
            )

            return self._parent._cast(_6732.FaceGearSetCompoundCriticalSpeedAnalysis)

        @property
        def flexible_pin_assembly_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6734.FlexiblePinAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6734,
            )

            return self._parent._cast(
                _6734.FlexiblePinAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6737.GearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6737,
            )

            return self._parent._cast(_6737.GearSetCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6741.HypoidGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6741,
            )

            return self._parent._cast(_6741.HypoidGearSetCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> (
            "_6745.KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6745,
            )

            return self._parent._cast(
                _6745.KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6748.KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6748,
            )

            return self._parent._cast(
                _6748.KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6751.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6751,
            )

            return self._parent._cast(
                _6751.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def part_to_part_shear_coupling_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6757.PartToPartShearCouplingCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6757,
            )

            return self._parent._cast(
                _6757.PartToPartShearCouplingCompoundCriticalSpeedAnalysis
            )

        @property
        def planetary_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6761.PlanetaryGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6761,
            )

            return self._parent._cast(
                _6761.PlanetaryGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def rolling_ring_assembly_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6768.RollingRingAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6768,
            )

            return self._parent._cast(
                _6768.RollingRingAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def root_assembly_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6771.RootAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6771,
            )

            return self._parent._cast(_6771.RootAssemblyCompoundCriticalSpeedAnalysis)

        @property
        def specialised_assembly_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6775.SpecialisedAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6775,
            )

            return self._parent._cast(
                _6775.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6778.SpiralBevelGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6778,
            )

            return self._parent._cast(
                _6778.SpiralBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def spring_damper_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6779.SpringDamperCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6779,
            )

            return self._parent._cast(_6779.SpringDamperCompoundCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6784.StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6784,
            )

            return self._parent._cast(
                _6784.StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6787.StraightBevelGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6787,
            )

            return self._parent._cast(
                _6787.StraightBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def synchroniser_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6790.SynchroniserCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6790,
            )

            return self._parent._cast(_6790.SynchroniserCompoundCriticalSpeedAnalysis)

        @property
        def torque_converter_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6794.TorqueConverterCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6794,
            )

            return self._parent._cast(
                _6794.TorqueConverterCompoundCriticalSpeedAnalysis
            )

        @property
        def worm_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6802.WormGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6802,
            )

            return self._parent._cast(_6802.WormGearSetCompoundCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6805.ZerolBevelGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6805,
            )

            return self._parent._cast(
                _6805.ZerolBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_assembly_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "AbstractAssemblyCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "AbstractAssemblyCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6545.AbstractAssemblyCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.AbstractAssemblyCriticalSpeedAnalysis]

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
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_6545.AbstractAssemblyCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.AbstractAssemblyCriticalSpeedAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis":
        return self._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis(self)
