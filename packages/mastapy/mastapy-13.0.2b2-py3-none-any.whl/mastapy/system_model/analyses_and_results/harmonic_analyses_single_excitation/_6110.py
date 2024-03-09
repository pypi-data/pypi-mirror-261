"""SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6010,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2478
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6016,
        _6020,
        _6023,
        _6028,
        _6029,
        _6033,
        _6038,
        _6041,
        _6044,
        _6049,
        _6051,
        _6053,
        _6059,
        _6065,
        _6067,
        _6070,
        _6075,
        _6079,
        _6082,
        _6085,
        _6094,
        _6096,
        _6103,
        _6113,
        _6116,
        _6119,
        _6122,
        _6126,
        _6130,
        _6137,
        _6140,
        _6091,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation")


class SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation(
    _6010.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
):
    """SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
            parent: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6010.AbstractAssemblyHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6010.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6091.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6091,
            )

            return self._parent._cast(_6091.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6016.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6016,
            )

            return self._parent._cast(
                _6016.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def belt_drive_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6020.BeltDriveHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6020,
            )

            return self._parent._cast(_6020.BeltDriveHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_gear_set_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6023.BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6023,
            )

            return self._parent._cast(
                _6023.BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6028.BevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6028,
            )

            return self._parent._cast(
                _6028.BevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bolted_joint_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6029.BoltedJointHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6029,
            )

            return self._parent._cast(
                _6029.BoltedJointHarmonicAnalysisOfSingleExcitation
            )

        @property
        def clutch_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6033.ClutchHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6033,
            )

            return self._parent._cast(_6033.ClutchHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_coupling_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6038.ConceptCouplingHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6038,
            )

            return self._parent._cast(
                _6038.ConceptCouplingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_set_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6041.ConceptGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6041,
            )

            return self._parent._cast(
                _6041.ConceptGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6044.ConicalGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6044,
            )

            return self._parent._cast(
                _6044.ConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6049.CouplingHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6049,
            )

            return self._parent._cast(_6049.CouplingHarmonicAnalysisOfSingleExcitation)

        @property
        def cvt_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6051.CVTHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6051,
            )

            return self._parent._cast(_6051.CVTHarmonicAnalysisOfSingleExcitation)

        @property
        def cycloidal_assembly_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6053.CycloidalAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6053,
            )

            return self._parent._cast(
                _6053.CycloidalAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_set_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6059.CylindricalGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6059,
            )

            return self._parent._cast(
                _6059.CylindricalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_set_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6065.FaceGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6065,
            )

            return self._parent._cast(
                _6065.FaceGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def flexible_pin_assembly_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6067.FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6067,
            )

            return self._parent._cast(
                _6067.FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_set_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6070.GearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6070,
            )

            return self._parent._cast(_6070.GearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def hypoid_gear_set_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6075.HypoidGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6075,
            )

            return self._parent._cast(
                _6075.HypoidGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6079.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6079,
            )

            return self._parent._cast(
                _6079.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6082.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6082,
            )

            return self._parent._cast(
                _6082.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6085.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6085,
            )

            return self._parent._cast(
                _6085.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6094.PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6094,
            )

            return self._parent._cast(
                _6094.PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planetary_gear_set_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6096.PlanetaryGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6096,
            )

            return self._parent._cast(
                _6096.PlanetaryGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_assembly_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6103.RollingRingAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6103,
            )

            return self._parent._cast(
                _6103.RollingRingAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6113.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6113,
            )

            return self._parent._cast(
                _6113.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6116.SpringDamperHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6116,
            )

            return self._parent._cast(
                _6116.SpringDamperHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6119.StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6119,
            )

            return self._parent._cast(
                _6119.StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6122.StraightBevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6122,
            )

            return self._parent._cast(
                _6122.StraightBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6126.SynchroniserHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6126,
            )

            return self._parent._cast(
                _6126.SynchroniserHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6130.TorqueConverterHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6130,
            )

            return self._parent._cast(
                _6130.TorqueConverterHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_set_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6137.WormGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6137,
            )

            return self._parent._cast(
                _6137.WormGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6140.ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6140,
            )

            return self._parent._cast(
                _6140.ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation.TYPE",
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
    def cast_to(
        self: Self,
    ) -> "SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation":
        return self._Cast_SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation(self)
