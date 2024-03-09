"""ConicalGearSetStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3826
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "ConicalGearSetStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2526
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3770,
        _3777,
        _3782,
        _3830,
        _3834,
        _3837,
        _3840,
        _3867,
        _3876,
        _3879,
        _3897,
        _3865,
        _3765,
        _3846,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetStabilityAnalysis",)


Self = TypeVar("Self", bound="ConicalGearSetStabilityAnalysis")


class ConicalGearSetStabilityAnalysis(_3826.GearSetStabilityAnalysis):
    """ConicalGearSetStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearSetStabilityAnalysis")

    class _Cast_ConicalGearSetStabilityAnalysis:
        """Special nested class for casting ConicalGearSetStabilityAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearSetStabilityAnalysis._Cast_ConicalGearSetStabilityAnalysis",
            parent: "ConicalGearSetStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_stability_analysis(
            self: "ConicalGearSetStabilityAnalysis._Cast_ConicalGearSetStabilityAnalysis",
        ) -> "_3826.GearSetStabilityAnalysis":
            return self._parent._cast(_3826.GearSetStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "ConicalGearSetStabilityAnalysis._Cast_ConicalGearSetStabilityAnalysis",
        ) -> "_3865.SpecialisedAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3865,
            )

            return self._parent._cast(_3865.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "ConicalGearSetStabilityAnalysis._Cast_ConicalGearSetStabilityAnalysis",
        ) -> "_3765.AbstractAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3765,
            )

            return self._parent._cast(_3765.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "ConicalGearSetStabilityAnalysis._Cast_ConicalGearSetStabilityAnalysis",
        ) -> "_3846.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3846,
            )

            return self._parent._cast(_3846.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearSetStabilityAnalysis._Cast_ConicalGearSetStabilityAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearSetStabilityAnalysis._Cast_ConicalGearSetStabilityAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearSetStabilityAnalysis._Cast_ConicalGearSetStabilityAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearSetStabilityAnalysis._Cast_ConicalGearSetStabilityAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetStabilityAnalysis._Cast_ConicalGearSetStabilityAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_stability_analysis(
            self: "ConicalGearSetStabilityAnalysis._Cast_ConicalGearSetStabilityAnalysis",
        ) -> "_3770.AGMAGleasonConicalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3770,
            )

            return self._parent._cast(_3770.AGMAGleasonConicalGearSetStabilityAnalysis)

        @property
        def bevel_differential_gear_set_stability_analysis(
            self: "ConicalGearSetStabilityAnalysis._Cast_ConicalGearSetStabilityAnalysis",
        ) -> "_3777.BevelDifferentialGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3777,
            )

            return self._parent._cast(_3777.BevelDifferentialGearSetStabilityAnalysis)

        @property
        def bevel_gear_set_stability_analysis(
            self: "ConicalGearSetStabilityAnalysis._Cast_ConicalGearSetStabilityAnalysis",
        ) -> "_3782.BevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3782,
            )

            return self._parent._cast(_3782.BevelGearSetStabilityAnalysis)

        @property
        def hypoid_gear_set_stability_analysis(
            self: "ConicalGearSetStabilityAnalysis._Cast_ConicalGearSetStabilityAnalysis",
        ) -> "_3830.HypoidGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3830,
            )

            return self._parent._cast(_3830.HypoidGearSetStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_stability_analysis(
            self: "ConicalGearSetStabilityAnalysis._Cast_ConicalGearSetStabilityAnalysis",
        ) -> "_3834.KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3834,
            )

            return self._parent._cast(
                _3834.KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_stability_analysis(
            self: "ConicalGearSetStabilityAnalysis._Cast_ConicalGearSetStabilityAnalysis",
        ) -> "_3837.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3837,
            )

            return self._parent._cast(
                _3837.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_stability_analysis(
            self: "ConicalGearSetStabilityAnalysis._Cast_ConicalGearSetStabilityAnalysis",
        ) -> "_3840.KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3840,
            )

            return self._parent._cast(
                _3840.KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_set_stability_analysis(
            self: "ConicalGearSetStabilityAnalysis._Cast_ConicalGearSetStabilityAnalysis",
        ) -> "_3867.SpiralBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3867,
            )

            return self._parent._cast(_3867.SpiralBevelGearSetStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_set_stability_analysis(
            self: "ConicalGearSetStabilityAnalysis._Cast_ConicalGearSetStabilityAnalysis",
        ) -> "_3876.StraightBevelDiffGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3876,
            )

            return self._parent._cast(_3876.StraightBevelDiffGearSetStabilityAnalysis)

        @property
        def straight_bevel_gear_set_stability_analysis(
            self: "ConicalGearSetStabilityAnalysis._Cast_ConicalGearSetStabilityAnalysis",
        ) -> "_3879.StraightBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3879,
            )

            return self._parent._cast(_3879.StraightBevelGearSetStabilityAnalysis)

        @property
        def zerol_bevel_gear_set_stability_analysis(
            self: "ConicalGearSetStabilityAnalysis._Cast_ConicalGearSetStabilityAnalysis",
        ) -> "_3897.ZerolBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3897,
            )

            return self._parent._cast(_3897.ZerolBevelGearSetStabilityAnalysis)

        @property
        def conical_gear_set_stability_analysis(
            self: "ConicalGearSetStabilityAnalysis._Cast_ConicalGearSetStabilityAnalysis",
        ) -> "ConicalGearSetStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetStabilityAnalysis._Cast_ConicalGearSetStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearSetStabilityAnalysis.TYPE"):
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
    ) -> "ConicalGearSetStabilityAnalysis._Cast_ConicalGearSetStabilityAnalysis":
        return self._Cast_ConicalGearSetStabilityAnalysis(self)
