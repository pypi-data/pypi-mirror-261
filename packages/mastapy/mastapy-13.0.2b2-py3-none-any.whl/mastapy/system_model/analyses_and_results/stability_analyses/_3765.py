"""AbstractAssemblyStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3846
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "AbstractAssemblyStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2436
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3770,
        _3772,
        _3775,
        _3777,
        _3782,
        _3784,
        _3788,
        _3793,
        _3795,
        _3798,
        _3804,
        _3808,
        _3809,
        _3814,
        _3821,
        _3824,
        _3826,
        _3830,
        _3834,
        _3837,
        _3840,
        _3849,
        _3851,
        _3858,
        _3861,
        _3865,
        _3867,
        _3871,
        _3876,
        _3879,
        _3886,
        _3889,
        _3894,
        _3897,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyStabilityAnalysis",)


Self = TypeVar("Self", bound="AbstractAssemblyStabilityAnalysis")


class AbstractAssemblyStabilityAnalysis(_3846.PartStabilityAnalysis):
    """AbstractAssemblyStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractAssemblyStabilityAnalysis")

    class _Cast_AbstractAssemblyStabilityAnalysis:
        """Special nested class for casting AbstractAssemblyStabilityAnalysis to subclasses."""

        def __init__(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
            parent: "AbstractAssemblyStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def part_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3846.PartStabilityAnalysis":
            return self._parent._cast(_3846.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3770.AGMAGleasonConicalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3770,
            )

            return self._parent._cast(_3770.AGMAGleasonConicalGearSetStabilityAnalysis)

        @property
        def assembly_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3772.AssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3772,
            )

            return self._parent._cast(_3772.AssemblyStabilityAnalysis)

        @property
        def belt_drive_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3775.BeltDriveStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3775,
            )

            return self._parent._cast(_3775.BeltDriveStabilityAnalysis)

        @property
        def bevel_differential_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3777.BevelDifferentialGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3777,
            )

            return self._parent._cast(_3777.BevelDifferentialGearSetStabilityAnalysis)

        @property
        def bevel_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3782.BevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3782,
            )

            return self._parent._cast(_3782.BevelGearSetStabilityAnalysis)

        @property
        def bolted_joint_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3784.BoltedJointStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3784,
            )

            return self._parent._cast(_3784.BoltedJointStabilityAnalysis)

        @property
        def clutch_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3788.ClutchStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3788,
            )

            return self._parent._cast(_3788.ClutchStabilityAnalysis)

        @property
        def concept_coupling_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3793.ConceptCouplingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3793,
            )

            return self._parent._cast(_3793.ConceptCouplingStabilityAnalysis)

        @property
        def concept_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3795.ConceptGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3795,
            )

            return self._parent._cast(_3795.ConceptGearSetStabilityAnalysis)

        @property
        def conical_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3798.ConicalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3798,
            )

            return self._parent._cast(_3798.ConicalGearSetStabilityAnalysis)

        @property
        def coupling_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3804.CouplingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3804,
            )

            return self._parent._cast(_3804.CouplingStabilityAnalysis)

        @property
        def cvt_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3808.CVTStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3808,
            )

            return self._parent._cast(_3808.CVTStabilityAnalysis)

        @property
        def cycloidal_assembly_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3809.CycloidalAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3809,
            )

            return self._parent._cast(_3809.CycloidalAssemblyStabilityAnalysis)

        @property
        def cylindrical_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3814.CylindricalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3814,
            )

            return self._parent._cast(_3814.CylindricalGearSetStabilityAnalysis)

        @property
        def face_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3821.FaceGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3821,
            )

            return self._parent._cast(_3821.FaceGearSetStabilityAnalysis)

        @property
        def flexible_pin_assembly_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3824.FlexiblePinAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3824,
            )

            return self._parent._cast(_3824.FlexiblePinAssemblyStabilityAnalysis)

        @property
        def gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3826.GearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3826,
            )

            return self._parent._cast(_3826.GearSetStabilityAnalysis)

        @property
        def hypoid_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3830.HypoidGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3830,
            )

            return self._parent._cast(_3830.HypoidGearSetStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3834.KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3834,
            )

            return self._parent._cast(
                _3834.KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3837.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3837,
            )

            return self._parent._cast(
                _3837.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3840.KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3840,
            )

            return self._parent._cast(
                _3840.KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis
            )

        @property
        def part_to_part_shear_coupling_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3849.PartToPartShearCouplingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3849,
            )

            return self._parent._cast(_3849.PartToPartShearCouplingStabilityAnalysis)

        @property
        def planetary_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3851.PlanetaryGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3851,
            )

            return self._parent._cast(_3851.PlanetaryGearSetStabilityAnalysis)

        @property
        def rolling_ring_assembly_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3858.RollingRingAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3858,
            )

            return self._parent._cast(_3858.RollingRingAssemblyStabilityAnalysis)

        @property
        def root_assembly_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3861.RootAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3861,
            )

            return self._parent._cast(_3861.RootAssemblyStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3865.SpecialisedAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3865,
            )

            return self._parent._cast(_3865.SpecialisedAssemblyStabilityAnalysis)

        @property
        def spiral_bevel_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3867.SpiralBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3867,
            )

            return self._parent._cast(_3867.SpiralBevelGearSetStabilityAnalysis)

        @property
        def spring_damper_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3871.SpringDamperStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3871,
            )

            return self._parent._cast(_3871.SpringDamperStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3876.StraightBevelDiffGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3876,
            )

            return self._parent._cast(_3876.StraightBevelDiffGearSetStabilityAnalysis)

        @property
        def straight_bevel_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3879.StraightBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3879,
            )

            return self._parent._cast(_3879.StraightBevelGearSetStabilityAnalysis)

        @property
        def synchroniser_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3886.SynchroniserStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3886,
            )

            return self._parent._cast(_3886.SynchroniserStabilityAnalysis)

        @property
        def torque_converter_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3889.TorqueConverterStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3889,
            )

            return self._parent._cast(_3889.TorqueConverterStabilityAnalysis)

        @property
        def worm_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3894.WormGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3894,
            )

            return self._parent._cast(_3894.WormGearSetStabilityAnalysis)

        @property
        def zerol_bevel_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3897.ZerolBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3897,
            )

            return self._parent._cast(_3897.ZerolBevelGearSetStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "AbstractAssemblyStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
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
        self: Self, instance_to_wrap: "AbstractAssemblyStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2436.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2436.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis":
        return self._Cast_AbstractAssemblyStabilityAnalysis(self)
