"""AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7222,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7008,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7149,
        _7150,
        _7153,
        _7156,
        _7161,
        _7163,
        _7164,
        _7169,
        _7174,
        _7177,
        _7180,
        _7184,
        _7186,
        _7192,
        _7198,
        _7200,
        _7203,
        _7207,
        _7211,
        _7214,
        _7217,
        _7223,
        _7227,
        _7234,
        _7237,
        _7241,
        _7244,
        _7245,
        _7250,
        _7253,
        _7256,
        _7260,
        _7268,
        _7271,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
)


class AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7222.PartCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7222.PartCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7222.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7149.AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7149,
            )

            return self._parent._cast(
                _7149.AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7150.AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7150,
            )

            return self._parent._cast(
                _7150.AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def belt_drive_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7153.BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7153,
            )

            return self._parent._cast(
                _7153.BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7156.BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7156,
            )

            return self._parent._cast(
                _7156.BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7161.BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7161,
            )

            return self._parent._cast(
                _7161.BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bolted_joint_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7163.BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7163,
            )

            return self._parent._cast(
                _7163.BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7164.ClutchCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7164,
            )

            return self._parent._cast(
                _7164.ClutchCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7169.ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7169,
            )

            return self._parent._cast(
                _7169.ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7174.ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7174,
            )

            return self._parent._cast(
                _7174.ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7177.ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7177,
            )

            return self._parent._cast(
                _7177.ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7180.CouplingCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7180,
            )

            return self._parent._cast(
                _7180.CouplingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7184.CVTCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7184,
            )

            return self._parent._cast(
                _7184.CVTCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7186.CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7186,
            )

            return self._parent._cast(
                _7186.CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7192.CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7192,
            )

            return self._parent._cast(
                _7192.CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7198.FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7198,
            )

            return self._parent._cast(
                _7198.FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def flexible_pin_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7200.FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7200,
            )

            return self._parent._cast(
                _7200.FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7203.GearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7203,
            )

            return self._parent._cast(
                _7203.GearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7207.HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7207,
            )

            return self._parent._cast(
                _7207.HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7211.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7211,
            )

            return self._parent._cast(
                _7211.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7214.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7214,
            )

            return self._parent._cast(
                _7214.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7217.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7217,
            )

            return self._parent._cast(
                _7217.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7223.PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7223,
            )

            return self._parent._cast(
                _7223.PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planetary_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7227.PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7227,
            )

            return self._parent._cast(
                _7227.PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7234.RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7234,
            )

            return self._parent._cast(
                _7234.RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def root_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7237.RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7237,
            )

            return self._parent._cast(
                _7237.RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def specialised_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7241.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7241,
            )

            return self._parent._cast(
                _7241.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7244.SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7244,
            )

            return self._parent._cast(
                _7244.SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7245.SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7245,
            )

            return self._parent._cast(
                _7245.SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7250.StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7250,
            )

            return self._parent._cast(
                _7250.StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7253.StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7253,
            )

            return self._parent._cast(
                _7253.StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7256.SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7256,
            )

            return self._parent._cast(
                _7256.SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7260.TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7260,
            )

            return self._parent._cast(
                _7260.TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7268.WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7268,
            )

            return self._parent._cast(
                _7268.WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7271.ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7271,
            )

            return self._parent._cast(
                _7271.ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7008.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "List[_7008.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
