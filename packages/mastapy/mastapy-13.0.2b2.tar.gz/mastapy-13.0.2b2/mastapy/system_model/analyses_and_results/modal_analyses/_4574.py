"""AbstractAssemblyModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4664
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "AbstractAssemblyModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2436
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4637,
        _4599,
        _4580,
        _4581,
        _4584,
        _4587,
        _4592,
        _4593,
        _4597,
        _4602,
        _4605,
        _4608,
        _4614,
        _4616,
        _4618,
        _4624,
        _4633,
        _4635,
        _4639,
        _4643,
        _4647,
        _4650,
        _4653,
        _4667,
        _4669,
        _4676,
        _4679,
        _4684,
        _4687,
        _4690,
        _4693,
        _4696,
        _4700,
        _4704,
        _4714,
        _4717,
    )
    from mastapy.system_model.analyses_and_results.system_deflections import _2687
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyModalAnalysis",)


Self = TypeVar("Self", bound="AbstractAssemblyModalAnalysis")


class AbstractAssemblyModalAnalysis(_4664.PartModalAnalysis):
    """AbstractAssemblyModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractAssemblyModalAnalysis")

    class _Cast_AbstractAssemblyModalAnalysis:
        """Special nested class for casting AbstractAssemblyModalAnalysis to subclasses."""

        def __init__(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
            parent: "AbstractAssemblyModalAnalysis",
        ):
            self._parent = parent

        @property
        def part_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_4664.PartModalAnalysis":
            return self._parent._cast(_4664.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_4580.AGMAGleasonConicalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4580

            return self._parent._cast(_4580.AGMAGleasonConicalGearSetModalAnalysis)

        @property
        def assembly_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_4581.AssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4581

            return self._parent._cast(_4581.AssemblyModalAnalysis)

        @property
        def belt_drive_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_4584.BeltDriveModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4584

            return self._parent._cast(_4584.BeltDriveModalAnalysis)

        @property
        def bevel_differential_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_4587.BevelDifferentialGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4587

            return self._parent._cast(_4587.BevelDifferentialGearSetModalAnalysis)

        @property
        def bevel_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_4592.BevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4592

            return self._parent._cast(_4592.BevelGearSetModalAnalysis)

        @property
        def bolted_joint_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_4593.BoltedJointModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4593

            return self._parent._cast(_4593.BoltedJointModalAnalysis)

        @property
        def clutch_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_4597.ClutchModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4597

            return self._parent._cast(_4597.ClutchModalAnalysis)

        @property
        def concept_coupling_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_4602.ConceptCouplingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4602

            return self._parent._cast(_4602.ConceptCouplingModalAnalysis)

        @property
        def concept_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_4605.ConceptGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4605

            return self._parent._cast(_4605.ConceptGearSetModalAnalysis)

        @property
        def conical_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_4608.ConicalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4608

            return self._parent._cast(_4608.ConicalGearSetModalAnalysis)

        @property
        def coupling_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_4614.CouplingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4614

            return self._parent._cast(_4614.CouplingModalAnalysis)

        @property
        def cvt_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_4616.CVTModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4616

            return self._parent._cast(_4616.CVTModalAnalysis)

        @property
        def cycloidal_assembly_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_4618.CycloidalAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4618

            return self._parent._cast(_4618.CycloidalAssemblyModalAnalysis)

        @property
        def cylindrical_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_4624.CylindricalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4624

            return self._parent._cast(_4624.CylindricalGearSetModalAnalysis)

        @property
        def face_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_4633.FaceGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4633

            return self._parent._cast(_4633.FaceGearSetModalAnalysis)

        @property
        def flexible_pin_assembly_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_4635.FlexiblePinAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4635

            return self._parent._cast(_4635.FlexiblePinAssemblyModalAnalysis)

        @property
        def gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_4639.GearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4639

            return self._parent._cast(_4639.GearSetModalAnalysis)

        @property
        def hypoid_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_4643.HypoidGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4643

            return self._parent._cast(_4643.HypoidGearSetModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_4647.KlingelnbergCycloPalloidConicalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4647

            return self._parent._cast(
                _4647.KlingelnbergCycloPalloidConicalGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_4650.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4650

            return self._parent._cast(
                _4650.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_4653.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4653

            return self._parent._cast(
                _4653.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis
            )

        @property
        def part_to_part_shear_coupling_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_4667.PartToPartShearCouplingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4667

            return self._parent._cast(_4667.PartToPartShearCouplingModalAnalysis)

        @property
        def planetary_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_4669.PlanetaryGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4669

            return self._parent._cast(_4669.PlanetaryGearSetModalAnalysis)

        @property
        def rolling_ring_assembly_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_4676.RollingRingAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4676

            return self._parent._cast(_4676.RollingRingAssemblyModalAnalysis)

        @property
        def root_assembly_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_4679.RootAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4679

            return self._parent._cast(_4679.RootAssemblyModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_4684.SpecialisedAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4684

            return self._parent._cast(_4684.SpecialisedAssemblyModalAnalysis)

        @property
        def spiral_bevel_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_4687.SpiralBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4687

            return self._parent._cast(_4687.SpiralBevelGearSetModalAnalysis)

        @property
        def spring_damper_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_4690.SpringDamperModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4690

            return self._parent._cast(_4690.SpringDamperModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_4693.StraightBevelDiffGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4693

            return self._parent._cast(_4693.StraightBevelDiffGearSetModalAnalysis)

        @property
        def straight_bevel_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_4696.StraightBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4696

            return self._parent._cast(_4696.StraightBevelGearSetModalAnalysis)

        @property
        def synchroniser_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_4700.SynchroniserModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4700

            return self._parent._cast(_4700.SynchroniserModalAnalysis)

        @property
        def torque_converter_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_4704.TorqueConverterModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4704

            return self._parent._cast(_4704.TorqueConverterModalAnalysis)

        @property
        def worm_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_4714.WormGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4714

            return self._parent._cast(_4714.WormGearSetModalAnalysis)

        @property
        def zerol_bevel_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "_4717.ZerolBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4717

            return self._parent._cast(_4717.ZerolBevelGearSetModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "AbstractAssemblyModalAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractAssemblyModalAnalysis.TYPE"):
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
    def gear_meshes(self: Self) -> "List[_4637.GearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.GearMeshModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def rigidly_connected_groups(self: Self) -> "List[_4599.ComponentModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ComponentModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RigidlyConnectedGroups

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2687.AbstractAssemblySystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.AbstractAssemblySystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis":
        return self._Cast_AbstractAssemblyModalAnalysis(self)
