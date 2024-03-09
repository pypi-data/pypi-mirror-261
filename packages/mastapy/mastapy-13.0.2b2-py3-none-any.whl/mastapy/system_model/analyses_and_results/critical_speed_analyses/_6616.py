"""KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6579
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_CRITICAL_SPEED_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
        "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2539
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6619,
        _6622,
        _6608,
        _6646,
        _6545,
        _6627,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis"
)


class KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis(
    _6579.ConicalGearSetCriticalSpeedAnalysis
):
    """KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6579.ConicalGearSetCriticalSpeedAnalysis":
            return self._parent._cast(_6579.ConicalGearSetCriticalSpeedAnalysis)

        @property
        def gear_set_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6608.GearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6608,
            )

            return self._parent._cast(_6608.GearSetCriticalSpeedAnalysis)

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6646.SpecialisedAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6646,
            )

            return self._parent._cast(_6646.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6545.AbstractAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6545,
            )

            return self._parent._cast(_6545.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6627.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6627,
            )

            return self._parent._cast(_6627.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6619.KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6619,
            )

            return self._parent._cast(
                _6619.KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6622.KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6622,
            )

            return self._parent._cast(
                _6622.KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2539.KlingelnbergCycloPalloidConicalGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet

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
    ) -> "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis":
        return self._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis(
            self
        )
