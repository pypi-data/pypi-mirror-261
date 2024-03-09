"""AbstractAssemblySteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3585,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2436
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3511,
        _3513,
        _3516,
        _3518,
        _3523,
        _3525,
        _3529,
        _3534,
        _3536,
        _3539,
        _3545,
        _3548,
        _3549,
        _3554,
        _3560,
        _3563,
        _3565,
        _3569,
        _3573,
        _3576,
        _3579,
        _3588,
        _3590,
        _3597,
        _3600,
        _3604,
        _3606,
        _3610,
        _3613,
        _3616,
        _3623,
        _3626,
        _3631,
        _3634,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblySteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="AbstractAssemblySteadyStateSynchronousResponseAtASpeed")


class AbstractAssemblySteadyStateSynchronousResponseAtASpeed(
    _3585.PartSteadyStateSynchronousResponseAtASpeed
):
    """AbstractAssemblySteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting AbstractAssemblySteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
            parent: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3585.PartSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(_3585.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3511.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3511,
            )

            return self._parent._cast(
                _3511.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def assembly_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3513.AssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3513,
            )

            return self._parent._cast(
                _3513.AssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def belt_drive_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3516.BeltDriveSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3516,
            )

            return self._parent._cast(
                _3516.BeltDriveSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3518.BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3518,
            )

            return self._parent._cast(
                _3518.BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3523.BevelGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3523,
            )

            return self._parent._cast(
                _3523.BevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bolted_joint_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3525.BoltedJointSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3525,
            )

            return self._parent._cast(
                _3525.BoltedJointSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def clutch_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3529.ClutchSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3529,
            )

            return self._parent._cast(
                _3529.ClutchSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3534.ConceptCouplingSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3534,
            )

            return self._parent._cast(
                _3534.ConceptCouplingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3536.ConceptGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3536,
            )

            return self._parent._cast(
                _3536.ConceptGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3539.ConicalGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3539,
            )

            return self._parent._cast(
                _3539.ConicalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3545.CouplingSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3545,
            )

            return self._parent._cast(
                _3545.CouplingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3548.CVTSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3548,
            )

            return self._parent._cast(_3548.CVTSteadyStateSynchronousResponseAtASpeed)

        @property
        def cycloidal_assembly_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3549.CycloidalAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3549,
            )

            return self._parent._cast(
                _3549.CycloidalAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3554.CylindricalGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3554,
            )

            return self._parent._cast(
                _3554.CylindricalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3560.FaceGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3560,
            )

            return self._parent._cast(
                _3560.FaceGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def flexible_pin_assembly_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3563.FlexiblePinAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3563,
            )

            return self._parent._cast(
                _3563.FlexiblePinAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3565.GearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3565,
            )

            return self._parent._cast(
                _3565.GearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3569.HypoidGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3569,
            )

            return self._parent._cast(
                _3569.HypoidGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3573.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3573,
            )

            return self._parent._cast(
                _3573.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3576.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3576,
            )

            return self._parent._cast(
                _3576.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3579.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3579,
            )

            return self._parent._cast(
                _3579.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3588.PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3588,
            )

            return self._parent._cast(
                _3588.PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planetary_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3590.PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3590,
            )

            return self._parent._cast(
                _3590.PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_assembly_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3597.RollingRingAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3597,
            )

            return self._parent._cast(
                _3597.RollingRingAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def root_assembly_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3600.RootAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3600,
            )

            return self._parent._cast(
                _3600.RootAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3604.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3604,
            )

            return self._parent._cast(
                _3604.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3606.SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3606,
            )

            return self._parent._cast(
                _3606.SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3610.SpringDamperSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3610,
            )

            return self._parent._cast(
                _3610.SpringDamperSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3613.StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3613,
            )

            return self._parent._cast(
                _3613.StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3616.StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3616,
            )

            return self._parent._cast(
                _3616.StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3623.SynchroniserSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3623,
            )

            return self._parent._cast(
                _3623.SynchroniserSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3626.TorqueConverterSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3626,
            )

            return self._parent._cast(
                _3626.TorqueConverterSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3631.WormGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3631,
            )

            return self._parent._cast(
                _3631.WormGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3634.ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3634,
            )

            return self._parent._cast(
                _3634.ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "AbstractAssemblySteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed.TYPE",
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
    ) -> "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed":
        return self._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed(self)
