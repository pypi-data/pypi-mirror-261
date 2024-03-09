"""SpecialisedAssemblyCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5249,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5218,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5255,
        _5259,
        _5262,
        _5267,
        _5269,
        _5270,
        _5275,
        _5280,
        _5283,
        _5286,
        _5290,
        _5292,
        _5298,
        _5304,
        _5306,
        _5309,
        _5313,
        _5317,
        _5320,
        _5323,
        _5329,
        _5333,
        _5340,
        _5350,
        _5351,
        _5356,
        _5359,
        _5362,
        _5366,
        _5374,
        _5377,
        _5328,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="SpecialisedAssemblyCompoundModalAnalysisAtASpeed")


class SpecialisedAssemblyCompoundModalAnalysisAtASpeed(
    _5249.AbstractAssemblyCompoundModalAnalysisAtASpeed
):
    """SpecialisedAssemblyCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed"
    )

    class _Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed:
        """Special nested class for casting SpecialisedAssemblyCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
            parent: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5249.AbstractAssemblyCompoundModalAnalysisAtASpeed":
            return self._parent._cast(
                _5249.AbstractAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5328.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5328,
            )

            return self._parent._cast(_5328.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5255.AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5255,
            )

            return self._parent._cast(
                _5255.AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def belt_drive_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5259.BeltDriveCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5259,
            )

            return self._parent._cast(_5259.BeltDriveCompoundModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5262.BevelDifferentialGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5262,
            )

            return self._parent._cast(
                _5262.BevelDifferentialGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5267.BevelGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5267,
            )

            return self._parent._cast(_5267.BevelGearSetCompoundModalAnalysisAtASpeed)

        @property
        def bolted_joint_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5269.BoltedJointCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5269,
            )

            return self._parent._cast(_5269.BoltedJointCompoundModalAnalysisAtASpeed)

        @property
        def clutch_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5270.ClutchCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5270,
            )

            return self._parent._cast(_5270.ClutchCompoundModalAnalysisAtASpeed)

        @property
        def concept_coupling_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5275.ConceptCouplingCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5275,
            )

            return self._parent._cast(
                _5275.ConceptCouplingCompoundModalAnalysisAtASpeed
            )

        @property
        def concept_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5280.ConceptGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5280,
            )

            return self._parent._cast(_5280.ConceptGearSetCompoundModalAnalysisAtASpeed)

        @property
        def conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5283.ConicalGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5283,
            )

            return self._parent._cast(_5283.ConicalGearSetCompoundModalAnalysisAtASpeed)

        @property
        def coupling_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5286.CouplingCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5286,
            )

            return self._parent._cast(_5286.CouplingCompoundModalAnalysisAtASpeed)

        @property
        def cvt_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5290.CVTCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5290,
            )

            return self._parent._cast(_5290.CVTCompoundModalAnalysisAtASpeed)

        @property
        def cycloidal_assembly_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5292.CycloidalAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5292,
            )

            return self._parent._cast(
                _5292.CycloidalAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def cylindrical_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5298.CylindricalGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5298,
            )

            return self._parent._cast(
                _5298.CylindricalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def face_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5304.FaceGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5304,
            )

            return self._parent._cast(_5304.FaceGearSetCompoundModalAnalysisAtASpeed)

        @property
        def flexible_pin_assembly_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5306.FlexiblePinAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5306,
            )

            return self._parent._cast(
                _5306.FlexiblePinAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5309.GearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5309,
            )

            return self._parent._cast(_5309.GearSetCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5313.HypoidGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5313,
            )

            return self._parent._cast(_5313.HypoidGearSetCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> (
            "_5317.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5317,
            )

            return self._parent._cast(
                _5317.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5320.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5320,
            )

            return self._parent._cast(
                _5320.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5323.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5323,
            )

            return self._parent._cast(
                _5323.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5329.PartToPartShearCouplingCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5329,
            )

            return self._parent._cast(
                _5329.PartToPartShearCouplingCompoundModalAnalysisAtASpeed
            )

        @property
        def planetary_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5333.PlanetaryGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5333,
            )

            return self._parent._cast(
                _5333.PlanetaryGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def rolling_ring_assembly_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5340.RollingRingAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5340,
            )

            return self._parent._cast(
                _5340.RollingRingAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5350.SpiralBevelGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5350,
            )

            return self._parent._cast(
                _5350.SpiralBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def spring_damper_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5351.SpringDamperCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5351,
            )

            return self._parent._cast(_5351.SpringDamperCompoundModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5356.StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5356,
            )

            return self._parent._cast(
                _5356.StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5359.StraightBevelGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5359,
            )

            return self._parent._cast(
                _5359.StraightBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5362.SynchroniserCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5362,
            )

            return self._parent._cast(_5362.SynchroniserCompoundModalAnalysisAtASpeed)

        @property
        def torque_converter_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5366.TorqueConverterCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5366,
            )

            return self._parent._cast(
                _5366.TorqueConverterCompoundModalAnalysisAtASpeed
            )

        @property
        def worm_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5374.WormGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5374,
            )

            return self._parent._cast(_5374.WormGearSetCompoundModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5377.ZerolBevelGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5377,
            )

            return self._parent._cast(
                _5377.ZerolBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "SpecialisedAssemblyCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5218.SpecialisedAssemblyModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.SpecialisedAssemblyModalAnalysisAtASpeed]

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
    ) -> "List[_5218.SpecialisedAssemblyModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.SpecialisedAssemblyModalAnalysisAtASpeed]

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
    ) -> "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed":
        return self._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed(self)
