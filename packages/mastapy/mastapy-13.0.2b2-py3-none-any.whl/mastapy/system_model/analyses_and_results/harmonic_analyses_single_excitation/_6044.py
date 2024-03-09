"""ConicalGearSetHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6070,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "ConicalGearSetHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2526
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6016,
        _6023,
        _6028,
        _6075,
        _6079,
        _6082,
        _6085,
        _6113,
        _6119,
        _6122,
        _6140,
        _6110,
        _6010,
        _6091,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="ConicalGearSetHarmonicAnalysisOfSingleExcitation")


class ConicalGearSetHarmonicAnalysisOfSingleExcitation(
    _6070.GearSetHarmonicAnalysisOfSingleExcitation
):
    """ConicalGearSetHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting ConicalGearSetHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
            parent: "ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def gear_set_harmonic_analysis_of_single_excitation(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6070.GearSetHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(_6070.GearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6110.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6110,
            )

            return self._parent._cast(
                _6110.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6010.AbstractAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6010,
            )

            return self._parent._cast(
                _6010.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6091.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6091,
            )

            return self._parent._cast(_6091.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6016.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6016,
            )

            return self._parent._cast(
                _6016.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_set_harmonic_analysis_of_single_excitation(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6023.BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6023,
            )

            return self._parent._cast(
                _6023.BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6028.BevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6028,
            )

            return self._parent._cast(
                _6028.BevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_set_harmonic_analysis_of_single_excitation(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6075.HypoidGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6075,
            )

            return self._parent._cast(
                _6075.HypoidGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6079.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6079,
            )

            return self._parent._cast(
                _6079.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis_of_single_excitation(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6082.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6082,
            )

            return self._parent._cast(
                _6082.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6085.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6085,
            )

            return self._parent._cast(
                _6085.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6113.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6113,
            )

            return self._parent._cast(
                _6113.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis_of_single_excitation(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6119.StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6119,
            )

            return self._parent._cast(
                _6119.StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6122.StraightBevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6122,
            )

            return self._parent._cast(
                _6122.StraightBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6140.ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6140,
            )

            return self._parent._cast(
                _6140.ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "ConicalGearSetHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "ConicalGearSetHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2526.ConicalGearSet":
        """mastapy.system_model.part_model.gears.ConicalGearSet

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
    ) -> "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation":
        return self._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation(self)
