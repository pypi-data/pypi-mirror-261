"""AbstractAssemblyCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5610
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5378
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5537,
        _5538,
        _5541,
        _5544,
        _5549,
        _5551,
        _5552,
        _5557,
        _5562,
        _5565,
        _5568,
        _5572,
        _5574,
        _5580,
        _5586,
        _5588,
        _5591,
        _5595,
        _5599,
        _5602,
        _5605,
        _5611,
        _5615,
        _5622,
        _5625,
        _5629,
        _5632,
        _5633,
        _5638,
        _5641,
        _5644,
        _5648,
        _5656,
        _5659,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="AbstractAssemblyCompoundMultibodyDynamicsAnalysis")


class AbstractAssemblyCompoundMultibodyDynamicsAnalysis(
    _5610.PartCompoundMultibodyDynamicsAnalysis
):
    """AbstractAssemblyCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting AbstractAssemblyCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
            parent: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5610.PartCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(_5610.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5537.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5537,
            )

            return self._parent._cast(
                _5537.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def assembly_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5538.AssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5538,
            )

            return self._parent._cast(_5538.AssemblyCompoundMultibodyDynamicsAnalysis)

        @property
        def belt_drive_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5541.BeltDriveCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5541,
            )

            return self._parent._cast(_5541.BeltDriveCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5544.BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5544,
            )

            return self._parent._cast(
                _5544.BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5549.BevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5549,
            )

            return self._parent._cast(
                _5549.BevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bolted_joint_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5551.BoltedJointCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5551,
            )

            return self._parent._cast(
                _5551.BoltedJointCompoundMultibodyDynamicsAnalysis
            )

        @property
        def clutch_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5552.ClutchCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5552,
            )

            return self._parent._cast(_5552.ClutchCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5557.ConceptCouplingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5557,
            )

            return self._parent._cast(
                _5557.ConceptCouplingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5562.ConceptGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5562,
            )

            return self._parent._cast(
                _5562.ConceptGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5565.ConicalGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5565,
            )

            return self._parent._cast(
                _5565.ConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def coupling_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5568.CouplingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5568,
            )

            return self._parent._cast(_5568.CouplingCompoundMultibodyDynamicsAnalysis)

        @property
        def cvt_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5572.CVTCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5572,
            )

            return self._parent._cast(_5572.CVTCompoundMultibodyDynamicsAnalysis)

        @property
        def cycloidal_assembly_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5574.CycloidalAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5574,
            )

            return self._parent._cast(
                _5574.CycloidalAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5580.CylindricalGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5580,
            )

            return self._parent._cast(
                _5580.CylindricalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def face_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5586.FaceGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5586,
            )

            return self._parent._cast(
                _5586.FaceGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def flexible_pin_assembly_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5588.FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5588,
            )

            return self._parent._cast(
                _5588.FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5591.GearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5591,
            )

            return self._parent._cast(_5591.GearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5595.HypoidGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5595,
            )

            return self._parent._cast(
                _5595.HypoidGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5599.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5599,
            )

            return self._parent._cast(
                _5599.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5602.KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5602,
            )

            return self._parent._cast(
                _5602.KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5605.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5605,
            )

            return self._parent._cast(
                _5605.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5611.PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5611,
            )

            return self._parent._cast(
                _5611.PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def planetary_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5615.PlanetaryGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5615,
            )

            return self._parent._cast(
                _5615.PlanetaryGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def rolling_ring_assembly_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5622.RollingRingAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5622,
            )

            return self._parent._cast(
                _5622.RollingRingAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def root_assembly_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5625.RootAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5625,
            )

            return self._parent._cast(
                _5625.RootAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5629.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5629,
            )

            return self._parent._cast(
                _5629.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5632.SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5632,
            )

            return self._parent._cast(
                _5632.SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5633.SpringDamperCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5633,
            )

            return self._parent._cast(
                _5633.SpringDamperCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5638.StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5638,
            )

            return self._parent._cast(
                _5638.StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5641.StraightBevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5641,
            )

            return self._parent._cast(
                _5641.StraightBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5644.SynchroniserCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5644,
            )

            return self._parent._cast(
                _5644.SynchroniserCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5648.TorqueConverterCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5648,
            )

            return self._parent._cast(
                _5648.TorqueConverterCompoundMultibodyDynamicsAnalysis
            )

        @property
        def worm_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5656.WormGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5656,
            )

            return self._parent._cast(
                _5656.WormGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5659.ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5659,
            )

            return self._parent._cast(
                _5659.ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "AbstractAssemblyCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5378.AbstractAssemblyMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.AbstractAssemblyMultibodyDynamicsAnalysis]

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
    ) -> "List[_5378.AbstractAssemblyMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.AbstractAssemblyMultibodyDynamicsAnalysis]

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
    ) -> "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis":
        return self._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis(self)
