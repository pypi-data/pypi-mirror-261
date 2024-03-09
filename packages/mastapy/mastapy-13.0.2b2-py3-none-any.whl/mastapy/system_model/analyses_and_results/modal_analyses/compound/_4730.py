"""AbstractAssemblyCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4809
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "AbstractAssemblyCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4574
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4736,
        _4737,
        _4740,
        _4743,
        _4748,
        _4750,
        _4751,
        _4756,
        _4761,
        _4764,
        _4767,
        _4771,
        _4773,
        _4779,
        _4785,
        _4787,
        _4790,
        _4794,
        _4798,
        _4801,
        _4804,
        _4810,
        _4814,
        _4821,
        _4824,
        _4828,
        _4831,
        _4832,
        _4837,
        _4840,
        _4843,
        _4847,
        _4855,
        _4858,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyCompoundModalAnalysis",)


Self = TypeVar("Self", bound="AbstractAssemblyCompoundModalAnalysis")


class AbstractAssemblyCompoundModalAnalysis(_4809.PartCompoundModalAnalysis):
    """AbstractAssemblyCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractAssemblyCompoundModalAnalysis"
    )

    class _Cast_AbstractAssemblyCompoundModalAnalysis:
        """Special nested class for casting AbstractAssemblyCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
            parent: "AbstractAssemblyCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def part_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_4809.PartCompoundModalAnalysis":
            return self._parent._cast(_4809.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_4736.AGMAGleasonConicalGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4736,
            )

            return self._parent._cast(
                _4736.AGMAGleasonConicalGearSetCompoundModalAnalysis
            )

        @property
        def assembly_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_4737.AssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4737,
            )

            return self._parent._cast(_4737.AssemblyCompoundModalAnalysis)

        @property
        def belt_drive_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_4740.BeltDriveCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4740,
            )

            return self._parent._cast(_4740.BeltDriveCompoundModalAnalysis)

        @property
        def bevel_differential_gear_set_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_4743.BevelDifferentialGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4743,
            )

            return self._parent._cast(
                _4743.BevelDifferentialGearSetCompoundModalAnalysis
            )

        @property
        def bevel_gear_set_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_4748.BevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4748,
            )

            return self._parent._cast(_4748.BevelGearSetCompoundModalAnalysis)

        @property
        def bolted_joint_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_4750.BoltedJointCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4750,
            )

            return self._parent._cast(_4750.BoltedJointCompoundModalAnalysis)

        @property
        def clutch_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_4751.ClutchCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4751,
            )

            return self._parent._cast(_4751.ClutchCompoundModalAnalysis)

        @property
        def concept_coupling_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_4756.ConceptCouplingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4756,
            )

            return self._parent._cast(_4756.ConceptCouplingCompoundModalAnalysis)

        @property
        def concept_gear_set_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_4761.ConceptGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4761,
            )

            return self._parent._cast(_4761.ConceptGearSetCompoundModalAnalysis)

        @property
        def conical_gear_set_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_4764.ConicalGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4764,
            )

            return self._parent._cast(_4764.ConicalGearSetCompoundModalAnalysis)

        @property
        def coupling_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_4767.CouplingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4767,
            )

            return self._parent._cast(_4767.CouplingCompoundModalAnalysis)

        @property
        def cvt_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_4771.CVTCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4771,
            )

            return self._parent._cast(_4771.CVTCompoundModalAnalysis)

        @property
        def cycloidal_assembly_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_4773.CycloidalAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4773,
            )

            return self._parent._cast(_4773.CycloidalAssemblyCompoundModalAnalysis)

        @property
        def cylindrical_gear_set_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_4779.CylindricalGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4779,
            )

            return self._parent._cast(_4779.CylindricalGearSetCompoundModalAnalysis)

        @property
        def face_gear_set_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_4785.FaceGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4785,
            )

            return self._parent._cast(_4785.FaceGearSetCompoundModalAnalysis)

        @property
        def flexible_pin_assembly_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_4787.FlexiblePinAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4787,
            )

            return self._parent._cast(_4787.FlexiblePinAssemblyCompoundModalAnalysis)

        @property
        def gear_set_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_4790.GearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4790,
            )

            return self._parent._cast(_4790.GearSetCompoundModalAnalysis)

        @property
        def hypoid_gear_set_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_4794.HypoidGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4794,
            )

            return self._parent._cast(_4794.HypoidGearSetCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_4798.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4798,
            )

            return self._parent._cast(
                _4798.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_4801.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4801,
            )

            return self._parent._cast(
                _4801.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_4804.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4804,
            )

            return self._parent._cast(
                _4804.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis
            )

        @property
        def part_to_part_shear_coupling_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_4810.PartToPartShearCouplingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4810,
            )

            return self._parent._cast(
                _4810.PartToPartShearCouplingCompoundModalAnalysis
            )

        @property
        def planetary_gear_set_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_4814.PlanetaryGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4814,
            )

            return self._parent._cast(_4814.PlanetaryGearSetCompoundModalAnalysis)

        @property
        def rolling_ring_assembly_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_4821.RollingRingAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4821,
            )

            return self._parent._cast(_4821.RollingRingAssemblyCompoundModalAnalysis)

        @property
        def root_assembly_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_4824.RootAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4824,
            )

            return self._parent._cast(_4824.RootAssemblyCompoundModalAnalysis)

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_4828.SpecialisedAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4828,
            )

            return self._parent._cast(_4828.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_set_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_4831.SpiralBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4831,
            )

            return self._parent._cast(_4831.SpiralBevelGearSetCompoundModalAnalysis)

        @property
        def spring_damper_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_4832.SpringDamperCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4832,
            )

            return self._parent._cast(_4832.SpringDamperCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_4837.StraightBevelDiffGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4837,
            )

            return self._parent._cast(
                _4837.StraightBevelDiffGearSetCompoundModalAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_4840.StraightBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4840,
            )

            return self._parent._cast(_4840.StraightBevelGearSetCompoundModalAnalysis)

        @property
        def synchroniser_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_4843.SynchroniserCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4843,
            )

            return self._parent._cast(_4843.SynchroniserCompoundModalAnalysis)

        @property
        def torque_converter_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_4847.TorqueConverterCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4847,
            )

            return self._parent._cast(_4847.TorqueConverterCompoundModalAnalysis)

        @property
        def worm_gear_set_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_4855.WormGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4855,
            )

            return self._parent._cast(_4855.WormGearSetCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "_4858.ZerolBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4858,
            )

            return self._parent._cast(_4858.ZerolBevelGearSetCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "AbstractAssemblyCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "AbstractAssemblyCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4574.AbstractAssemblyModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.AbstractAssemblyModalAnalysis]

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
    ) -> "List[_4574.AbstractAssemblyModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.AbstractAssemblyModalAnalysis]

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
    ) -> "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis":
        return self._Cast_AbstractAssemblyCompoundModalAnalysis(self)
