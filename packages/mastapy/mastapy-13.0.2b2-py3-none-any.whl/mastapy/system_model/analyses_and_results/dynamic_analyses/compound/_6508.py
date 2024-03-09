"""SpecialisedAssemblyCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6410
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "SpecialisedAssemblyCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6379
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6416,
        _6420,
        _6423,
        _6428,
        _6430,
        _6431,
        _6436,
        _6441,
        _6444,
        _6447,
        _6451,
        _6453,
        _6459,
        _6465,
        _6467,
        _6470,
        _6474,
        _6478,
        _6481,
        _6484,
        _6490,
        _6494,
        _6501,
        _6511,
        _6512,
        _6517,
        _6520,
        _6523,
        _6527,
        _6535,
        _6538,
        _6489,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="SpecialisedAssemblyCompoundDynamicAnalysis")


class SpecialisedAssemblyCompoundDynamicAnalysis(
    _6410.AbstractAssemblyCompoundDynamicAnalysis
):
    """SpecialisedAssemblyCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyCompoundDynamicAnalysis"
    )

    class _Cast_SpecialisedAssemblyCompoundDynamicAnalysis:
        """Special nested class for casting SpecialisedAssemblyCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
            parent: "SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_assembly_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6410.AbstractAssemblyCompoundDynamicAnalysis":
            return self._parent._cast(_6410.AbstractAssemblyCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6489.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6489,
            )

            return self._parent._cast(_6489.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6416.AGMAGleasonConicalGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6416,
            )

            return self._parent._cast(
                _6416.AGMAGleasonConicalGearSetCompoundDynamicAnalysis
            )

        @property
        def belt_drive_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6420.BeltDriveCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6420,
            )

            return self._parent._cast(_6420.BeltDriveCompoundDynamicAnalysis)

        @property
        def bevel_differential_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6423.BevelDifferentialGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6423,
            )

            return self._parent._cast(
                _6423.BevelDifferentialGearSetCompoundDynamicAnalysis
            )

        @property
        def bevel_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6428.BevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6428,
            )

            return self._parent._cast(_6428.BevelGearSetCompoundDynamicAnalysis)

        @property
        def bolted_joint_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6430.BoltedJointCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6430,
            )

            return self._parent._cast(_6430.BoltedJointCompoundDynamicAnalysis)

        @property
        def clutch_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6431.ClutchCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6431,
            )

            return self._parent._cast(_6431.ClutchCompoundDynamicAnalysis)

        @property
        def concept_coupling_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6436.ConceptCouplingCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6436,
            )

            return self._parent._cast(_6436.ConceptCouplingCompoundDynamicAnalysis)

        @property
        def concept_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6441.ConceptGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6441,
            )

            return self._parent._cast(_6441.ConceptGearSetCompoundDynamicAnalysis)

        @property
        def conical_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6444.ConicalGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6444,
            )

            return self._parent._cast(_6444.ConicalGearSetCompoundDynamicAnalysis)

        @property
        def coupling_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6447.CouplingCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6447,
            )

            return self._parent._cast(_6447.CouplingCompoundDynamicAnalysis)

        @property
        def cvt_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6451.CVTCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6451,
            )

            return self._parent._cast(_6451.CVTCompoundDynamicAnalysis)

        @property
        def cycloidal_assembly_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6453.CycloidalAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6453,
            )

            return self._parent._cast(_6453.CycloidalAssemblyCompoundDynamicAnalysis)

        @property
        def cylindrical_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6459.CylindricalGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6459,
            )

            return self._parent._cast(_6459.CylindricalGearSetCompoundDynamicAnalysis)

        @property
        def face_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6465.FaceGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6465,
            )

            return self._parent._cast(_6465.FaceGearSetCompoundDynamicAnalysis)

        @property
        def flexible_pin_assembly_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6467.FlexiblePinAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6467,
            )

            return self._parent._cast(_6467.FlexiblePinAssemblyCompoundDynamicAnalysis)

        @property
        def gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6470.GearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6470,
            )

            return self._parent._cast(_6470.GearSetCompoundDynamicAnalysis)

        @property
        def hypoid_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6474.HypoidGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6474,
            )

            return self._parent._cast(_6474.HypoidGearSetCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6478.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6478,
            )

            return self._parent._cast(
                _6478.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6481.KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6481,
            )

            return self._parent._cast(
                _6481.KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6484.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6484,
            )

            return self._parent._cast(
                _6484.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis
            )

        @property
        def part_to_part_shear_coupling_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6490.PartToPartShearCouplingCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6490,
            )

            return self._parent._cast(
                _6490.PartToPartShearCouplingCompoundDynamicAnalysis
            )

        @property
        def planetary_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6494.PlanetaryGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6494,
            )

            return self._parent._cast(_6494.PlanetaryGearSetCompoundDynamicAnalysis)

        @property
        def rolling_ring_assembly_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6501.RollingRingAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6501,
            )

            return self._parent._cast(_6501.RollingRingAssemblyCompoundDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6511.SpiralBevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6511,
            )

            return self._parent._cast(_6511.SpiralBevelGearSetCompoundDynamicAnalysis)

        @property
        def spring_damper_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6512.SpringDamperCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6512,
            )

            return self._parent._cast(_6512.SpringDamperCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6517.StraightBevelDiffGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6517,
            )

            return self._parent._cast(
                _6517.StraightBevelDiffGearSetCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6520.StraightBevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6520,
            )

            return self._parent._cast(_6520.StraightBevelGearSetCompoundDynamicAnalysis)

        @property
        def synchroniser_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6523.SynchroniserCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6523,
            )

            return self._parent._cast(_6523.SynchroniserCompoundDynamicAnalysis)

        @property
        def torque_converter_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6527.TorqueConverterCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6527,
            )

            return self._parent._cast(_6527.TorqueConverterCompoundDynamicAnalysis)

        @property
        def worm_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6535.WormGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6535,
            )

            return self._parent._cast(_6535.WormGearSetCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6538.ZerolBevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6538,
            )

            return self._parent._cast(_6538.ZerolBevelGearSetCompoundDynamicAnalysis)

        @property
        def specialised_assembly_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "SpecialisedAssemblyCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "SpecialisedAssemblyCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6379.SpecialisedAssemblyDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.SpecialisedAssemblyDynamicAnalysis]

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
    ) -> "List[_6379.SpecialisedAssemblyDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.SpecialisedAssemblyDynamicAnalysis]

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
    ) -> "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis":
        return self._Cast_SpecialisedAssemblyCompoundDynamicAnalysis(self)
