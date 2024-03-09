"""AbstractAssemblyCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3978
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "AbstractAssemblyCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3765
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3905,
        _3906,
        _3909,
        _3912,
        _3917,
        _3919,
        _3920,
        _3925,
        _3930,
        _3933,
        _3936,
        _3940,
        _3942,
        _3948,
        _3954,
        _3956,
        _3959,
        _3963,
        _3967,
        _3970,
        _3973,
        _3979,
        _3983,
        _3990,
        _3993,
        _3997,
        _4000,
        _4001,
        _4006,
        _4009,
        _4012,
        _4016,
        _4024,
        _4027,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="AbstractAssemblyCompoundStabilityAnalysis")


class AbstractAssemblyCompoundStabilityAnalysis(_3978.PartCompoundStabilityAnalysis):
    """AbstractAssemblyCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractAssemblyCompoundStabilityAnalysis"
    )

    class _Cast_AbstractAssemblyCompoundStabilityAnalysis:
        """Special nested class for casting AbstractAssemblyCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
            parent: "AbstractAssemblyCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def part_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3978.PartCompoundStabilityAnalysis":
            return self._parent._cast(_3978.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3905.AGMAGleasonConicalGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3905,
            )

            return self._parent._cast(
                _3905.AGMAGleasonConicalGearSetCompoundStabilityAnalysis
            )

        @property
        def assembly_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3906.AssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3906,
            )

            return self._parent._cast(_3906.AssemblyCompoundStabilityAnalysis)

        @property
        def belt_drive_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3909.BeltDriveCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3909,
            )

            return self._parent._cast(_3909.BeltDriveCompoundStabilityAnalysis)

        @property
        def bevel_differential_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3912.BevelDifferentialGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3912,
            )

            return self._parent._cast(
                _3912.BevelDifferentialGearSetCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3917.BevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3917,
            )

            return self._parent._cast(_3917.BevelGearSetCompoundStabilityAnalysis)

        @property
        def bolted_joint_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3919.BoltedJointCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3919,
            )

            return self._parent._cast(_3919.BoltedJointCompoundStabilityAnalysis)

        @property
        def clutch_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3920.ClutchCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3920,
            )

            return self._parent._cast(_3920.ClutchCompoundStabilityAnalysis)

        @property
        def concept_coupling_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3925.ConceptCouplingCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3925,
            )

            return self._parent._cast(_3925.ConceptCouplingCompoundStabilityAnalysis)

        @property
        def concept_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3930.ConceptGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3930,
            )

            return self._parent._cast(_3930.ConceptGearSetCompoundStabilityAnalysis)

        @property
        def conical_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3933.ConicalGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3933,
            )

            return self._parent._cast(_3933.ConicalGearSetCompoundStabilityAnalysis)

        @property
        def coupling_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3936.CouplingCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3936,
            )

            return self._parent._cast(_3936.CouplingCompoundStabilityAnalysis)

        @property
        def cvt_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3940.CVTCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3940,
            )

            return self._parent._cast(_3940.CVTCompoundStabilityAnalysis)

        @property
        def cycloidal_assembly_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3942.CycloidalAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3942,
            )

            return self._parent._cast(_3942.CycloidalAssemblyCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3948.CylindricalGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3948,
            )

            return self._parent._cast(_3948.CylindricalGearSetCompoundStabilityAnalysis)

        @property
        def face_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3954.FaceGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3954,
            )

            return self._parent._cast(_3954.FaceGearSetCompoundStabilityAnalysis)

        @property
        def flexible_pin_assembly_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3956.FlexiblePinAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3956,
            )

            return self._parent._cast(
                _3956.FlexiblePinAssemblyCompoundStabilityAnalysis
            )

        @property
        def gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3959.GearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3959,
            )

            return self._parent._cast(_3959.GearSetCompoundStabilityAnalysis)

        @property
        def hypoid_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3963.HypoidGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3963,
            )

            return self._parent._cast(_3963.HypoidGearSetCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3967.KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3967,
            )

            return self._parent._cast(
                _3967.KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3970.KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3970,
            )

            return self._parent._cast(
                _3970.KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> (
            "_3973.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3973,
            )

            return self._parent._cast(
                _3973.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis
            )

        @property
        def part_to_part_shear_coupling_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3979.PartToPartShearCouplingCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3979,
            )

            return self._parent._cast(
                _3979.PartToPartShearCouplingCompoundStabilityAnalysis
            )

        @property
        def planetary_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3983.PlanetaryGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3983,
            )

            return self._parent._cast(_3983.PlanetaryGearSetCompoundStabilityAnalysis)

        @property
        def rolling_ring_assembly_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3990.RollingRingAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3990,
            )

            return self._parent._cast(
                _3990.RollingRingAssemblyCompoundStabilityAnalysis
            )

        @property
        def root_assembly_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3993.RootAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3993,
            )

            return self._parent._cast(_3993.RootAssemblyCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3997.SpecialisedAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3997,
            )

            return self._parent._cast(
                _3997.SpecialisedAssemblyCompoundStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_4000.SpiralBevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4000,
            )

            return self._parent._cast(_4000.SpiralBevelGearSetCompoundStabilityAnalysis)

        @property
        def spring_damper_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_4001.SpringDamperCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4001,
            )

            return self._parent._cast(_4001.SpringDamperCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_4006.StraightBevelDiffGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4006,
            )

            return self._parent._cast(
                _4006.StraightBevelDiffGearSetCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_4009.StraightBevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4009,
            )

            return self._parent._cast(
                _4009.StraightBevelGearSetCompoundStabilityAnalysis
            )

        @property
        def synchroniser_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_4012.SynchroniserCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4012,
            )

            return self._parent._cast(_4012.SynchroniserCompoundStabilityAnalysis)

        @property
        def torque_converter_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_4016.TorqueConverterCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4016,
            )

            return self._parent._cast(_4016.TorqueConverterCompoundStabilityAnalysis)

        @property
        def worm_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_4024.WormGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4024,
            )

            return self._parent._cast(_4024.WormGearSetCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_4027.ZerolBevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4027,
            )

            return self._parent._cast(_4027.ZerolBevelGearSetCompoundStabilityAnalysis)

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "AbstractAssemblyCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "AbstractAssemblyCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3765.AbstractAssemblyStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.AbstractAssemblyStabilityAnalysis]

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
    ) -> "List[_3765.AbstractAssemblyStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.AbstractAssemblyStabilityAnalysis]

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
    ) -> "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis":
        return self._Cast_AbstractAssemblyCompoundStabilityAnalysis(self)
