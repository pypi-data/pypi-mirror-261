"""GearSetAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7112,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "GearSetAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2534
    from mastapy.math_utility import _1510
    from mastapy.system_model.analyses_and_results.system_deflections import _2762
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7018,
        _7026,
        _7031,
        _7044,
        _7047,
        _7062,
        _7068,
        _7078,
        _7082,
        _7085,
        _7088,
        _7098,
        _7115,
        _7121,
        _7124,
        _7139,
        _7142,
        _7008,
        _7093,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("GearSetAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="GearSetAdvancedTimeSteppingAnalysisForModulation")


class GearSetAdvancedTimeSteppingAnalysisForModulation(
    _7112.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
):
    """GearSetAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearSetAdvancedTimeSteppingAnalysisForModulation"
    )

    class _Cast_GearSetAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting GearSetAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "GearSetAdvancedTimeSteppingAnalysisForModulation._Cast_GearSetAdvancedTimeSteppingAnalysisForModulation",
            parent: "GearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "GearSetAdvancedTimeSteppingAnalysisForModulation._Cast_GearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7112.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7112.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "GearSetAdvancedTimeSteppingAnalysisForModulation._Cast_GearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7008.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7008,
            )

            return self._parent._cast(
                _7008.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "GearSetAdvancedTimeSteppingAnalysisForModulation._Cast_GearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7093.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7093,
            )

            return self._parent._cast(
                _7093.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "GearSetAdvancedTimeSteppingAnalysisForModulation._Cast_GearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearSetAdvancedTimeSteppingAnalysisForModulation._Cast_GearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearSetAdvancedTimeSteppingAnalysisForModulation._Cast_GearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearSetAdvancedTimeSteppingAnalysisForModulation._Cast_GearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetAdvancedTimeSteppingAnalysisForModulation._Cast_GearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "GearSetAdvancedTimeSteppingAnalysisForModulation._Cast_GearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7018.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7018,
            )

            return self._parent._cast(
                _7018.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "GearSetAdvancedTimeSteppingAnalysisForModulation._Cast_GearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7026.BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7026,
            )

            return self._parent._cast(
                _7026.BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "GearSetAdvancedTimeSteppingAnalysisForModulation._Cast_GearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7031.BevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7031,
            )

            return self._parent._cast(
                _7031.BevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "GearSetAdvancedTimeSteppingAnalysisForModulation._Cast_GearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7044.ConceptGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7044,
            )

            return self._parent._cast(
                _7044.ConceptGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "GearSetAdvancedTimeSteppingAnalysisForModulation._Cast_GearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7047.ConicalGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7047,
            )

            return self._parent._cast(
                _7047.ConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "GearSetAdvancedTimeSteppingAnalysisForModulation._Cast_GearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7062.CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7062,
            )

            return self._parent._cast(
                _7062.CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "GearSetAdvancedTimeSteppingAnalysisForModulation._Cast_GearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7068.FaceGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7068,
            )

            return self._parent._cast(
                _7068.FaceGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "GearSetAdvancedTimeSteppingAnalysisForModulation._Cast_GearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7078.HypoidGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7078,
            )

            return self._parent._cast(
                _7078.HypoidGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "GearSetAdvancedTimeSteppingAnalysisForModulation._Cast_GearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7082.KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7082,
            )

            return self._parent._cast(
                _7082.KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "GearSetAdvancedTimeSteppingAnalysisForModulation._Cast_GearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7085.KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7085,
            )

            return self._parent._cast(
                _7085.KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "GearSetAdvancedTimeSteppingAnalysisForModulation._Cast_GearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7088.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7088,
            )

            return self._parent._cast(
                _7088.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planetary_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "GearSetAdvancedTimeSteppingAnalysisForModulation._Cast_GearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7098.PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7098,
            )

            return self._parent._cast(
                _7098.PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "GearSetAdvancedTimeSteppingAnalysisForModulation._Cast_GearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7115.SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7115,
            )

            return self._parent._cast(
                _7115.SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "GearSetAdvancedTimeSteppingAnalysisForModulation._Cast_GearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7121.StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7121,
            )

            return self._parent._cast(
                _7121.StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "GearSetAdvancedTimeSteppingAnalysisForModulation._Cast_GearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7124.StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7124,
            )

            return self._parent._cast(
                _7124.StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "GearSetAdvancedTimeSteppingAnalysisForModulation._Cast_GearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7139.WormGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7139,
            )

            return self._parent._cast(
                _7139.WormGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "GearSetAdvancedTimeSteppingAnalysisForModulation._Cast_GearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7142.ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7142,
            )

            return self._parent._cast(
                _7142.ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "GearSetAdvancedTimeSteppingAnalysisForModulation._Cast_GearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "GearSetAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "GearSetAdvancedTimeSteppingAnalysisForModulation._Cast_GearSetAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "GearSetAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2534.GearSet":
        """mastapy.system_model.part_model.gears.GearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def eignenmodes_indexed_by_mode_id(self: Self) -> "List[_1510.Eigenmodes]":
        """List[mastapy.math_utility.Eigenmodes]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EignenmodesIndexedByModeId

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def system_deflection_results(self: Self) -> "_2762.GearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.GearSetSystemDeflection

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
    ) -> "GearSetAdvancedTimeSteppingAnalysisForModulation._Cast_GearSetAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_GearSetAdvancedTimeSteppingAnalysisForModulation(self)
