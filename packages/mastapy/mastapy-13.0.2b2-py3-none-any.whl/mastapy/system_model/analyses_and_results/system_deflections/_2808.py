"""SpecialisedAssemblySystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2687
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "SpecialisedAssemblySystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2478
    from mastapy.system_model.analyses_and_results.power_flows import _4137
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2692,
        _2702,
        _2704,
        _2709,
        _2711,
        _2715,
        _2721,
        _2723,
        _2727,
        _2733,
        _2736,
        _2737,
        _2744,
        _2745,
        _2746,
        _2757,
        _2760,
        _2762,
        _2766,
        _2771,
        _2774,
        _2777,
        _2790,
        _2799,
        _2810,
        _2814,
        _2816,
        _2819,
        _2826,
        _2832,
        _2839,
        _2842,
        _2787,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7549,
        _7550,
        _7547,
    )
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblySystemDeflection",)


Self = TypeVar("Self", bound="SpecialisedAssemblySystemDeflection")


class SpecialisedAssemblySystemDeflection(_2687.AbstractAssemblySystemDeflection):
    """SpecialisedAssemblySystemDeflection

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpecialisedAssemblySystemDeflection")

    class _Cast_SpecialisedAssemblySystemDeflection:
        """Special nested class for casting SpecialisedAssemblySystemDeflection to subclasses."""

        def __init__(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
            parent: "SpecialisedAssemblySystemDeflection",
        ):
            self._parent = parent

        @property
        def abstract_assembly_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2687.AbstractAssemblySystemDeflection":
            return self._parent._cast(_2687.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2787.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2787,
            )

            return self._parent._cast(_2787.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_7549.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2692.AGMAGleasonConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2692,
            )

            return self._parent._cast(_2692.AGMAGleasonConicalGearSetSystemDeflection)

        @property
        def belt_drive_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2702.BeltDriveSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2702,
            )

            return self._parent._cast(_2702.BeltDriveSystemDeflection)

        @property
        def bevel_differential_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2704.BevelDifferentialGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2704,
            )

            return self._parent._cast(_2704.BevelDifferentialGearSetSystemDeflection)

        @property
        def bevel_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2709.BevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2709,
            )

            return self._parent._cast(_2709.BevelGearSetSystemDeflection)

        @property
        def bolted_joint_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2711.BoltedJointSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2711,
            )

            return self._parent._cast(_2711.BoltedJointSystemDeflection)

        @property
        def clutch_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2715.ClutchSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2715,
            )

            return self._parent._cast(_2715.ClutchSystemDeflection)

        @property
        def concept_coupling_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2721.ConceptCouplingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2721,
            )

            return self._parent._cast(_2721.ConceptCouplingSystemDeflection)

        @property
        def concept_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2723.ConceptGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2723,
            )

            return self._parent._cast(_2723.ConceptGearSetSystemDeflection)

        @property
        def conical_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2727.ConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2727,
            )

            return self._parent._cast(_2727.ConicalGearSetSystemDeflection)

        @property
        def coupling_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2733.CouplingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2733,
            )

            return self._parent._cast(_2733.CouplingSystemDeflection)

        @property
        def cvt_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2736.CVTSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2736,
            )

            return self._parent._cast(_2736.CVTSystemDeflection)

        @property
        def cycloidal_assembly_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2737.CycloidalAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2737,
            )

            return self._parent._cast(_2737.CycloidalAssemblySystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2744.CylindricalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2744,
            )

            return self._parent._cast(_2744.CylindricalGearSetSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection_timestep(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2745.CylindricalGearSetSystemDeflectionTimestep":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2745,
            )

            return self._parent._cast(_2745.CylindricalGearSetSystemDeflectionTimestep)

        @property
        def cylindrical_gear_set_system_deflection_with_ltca_results(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2746.CylindricalGearSetSystemDeflectionWithLTCAResults":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2746,
            )

            return self._parent._cast(
                _2746.CylindricalGearSetSystemDeflectionWithLTCAResults
            )

        @property
        def face_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2757.FaceGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2757,
            )

            return self._parent._cast(_2757.FaceGearSetSystemDeflection)

        @property
        def flexible_pin_assembly_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2760.FlexiblePinAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2760,
            )

            return self._parent._cast(_2760.FlexiblePinAssemblySystemDeflection)

        @property
        def gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2762.GearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2762,
            )

            return self._parent._cast(_2762.GearSetSystemDeflection)

        @property
        def hypoid_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2766.HypoidGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2766,
            )

            return self._parent._cast(_2766.HypoidGearSetSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2771.KlingelnbergCycloPalloidConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2771,
            )

            return self._parent._cast(
                _2771.KlingelnbergCycloPalloidConicalGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2774.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2774,
            )

            return self._parent._cast(
                _2774.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2777.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2777,
            )

            return self._parent._cast(
                _2777.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2790.PartToPartShearCouplingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2790,
            )

            return self._parent._cast(_2790.PartToPartShearCouplingSystemDeflection)

        @property
        def rolling_ring_assembly_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2799.RollingRingAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2799,
            )

            return self._parent._cast(_2799.RollingRingAssemblySystemDeflection)

        @property
        def spiral_bevel_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2810.SpiralBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2810,
            )

            return self._parent._cast(_2810.SpiralBevelGearSetSystemDeflection)

        @property
        def spring_damper_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2814.SpringDamperSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2814,
            )

            return self._parent._cast(_2814.SpringDamperSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2816.StraightBevelDiffGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2816,
            )

            return self._parent._cast(_2816.StraightBevelDiffGearSetSystemDeflection)

        @property
        def straight_bevel_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2819.StraightBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2819,
            )

            return self._parent._cast(_2819.StraightBevelGearSetSystemDeflection)

        @property
        def synchroniser_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2826.SynchroniserSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2826,
            )

            return self._parent._cast(_2826.SynchroniserSystemDeflection)

        @property
        def torque_converter_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2832.TorqueConverterSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2832,
            )

            return self._parent._cast(_2832.TorqueConverterSystemDeflection)

        @property
        def worm_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2839.WormGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2839,
            )

            return self._parent._cast(_2839.WormGearSetSystemDeflection)

        @property
        def zerol_bevel_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2842.ZerolBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2842,
            )

            return self._parent._cast(_2842.ZerolBevelGearSetSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "SpecialisedAssemblySystemDeflection":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
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
        self: Self, instance_to_wrap: "SpecialisedAssemblySystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2478.SpecialisedAssembly":
        """mastapy.system_model.part_model.SpecialisedAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4137.SpecialisedAssemblyPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.SpecialisedAssemblyPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> (
        "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection"
    ):
        return self._Cast_SpecialisedAssemblySystemDeflection(self)
