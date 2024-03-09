"""ZerolBevelGearCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6693,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "ZerolBevelGearCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2555
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6674
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6681,
        _6709,
        _6735,
        _6754,
        _6702,
        _6756,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ZerolBevelGearCompoundCriticalSpeedAnalysis")


class ZerolBevelGearCompoundCriticalSpeedAnalysis(
    _6693.BevelGearCompoundCriticalSpeedAnalysis
):
    """ZerolBevelGearCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ZerolBevelGearCompoundCriticalSpeedAnalysis"
    )

    class _Cast_ZerolBevelGearCompoundCriticalSpeedAnalysis:
        """Special nested class for casting ZerolBevelGearCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ZerolBevelGearCompoundCriticalSpeedAnalysis._Cast_ZerolBevelGearCompoundCriticalSpeedAnalysis",
            parent: "ZerolBevelGearCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_critical_speed_analysis(
            self: "ZerolBevelGearCompoundCriticalSpeedAnalysis._Cast_ZerolBevelGearCompoundCriticalSpeedAnalysis",
        ) -> "_6693.BevelGearCompoundCriticalSpeedAnalysis":
            return self._parent._cast(_6693.BevelGearCompoundCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_compound_critical_speed_analysis(
            self: "ZerolBevelGearCompoundCriticalSpeedAnalysis._Cast_ZerolBevelGearCompoundCriticalSpeedAnalysis",
        ) -> "_6681.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6681,
            )

            return self._parent._cast(
                _6681.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_compound_critical_speed_analysis(
            self: "ZerolBevelGearCompoundCriticalSpeedAnalysis._Cast_ZerolBevelGearCompoundCriticalSpeedAnalysis",
        ) -> "_6709.ConicalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6709,
            )

            return self._parent._cast(_6709.ConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def gear_compound_critical_speed_analysis(
            self: "ZerolBevelGearCompoundCriticalSpeedAnalysis._Cast_ZerolBevelGearCompoundCriticalSpeedAnalysis",
        ) -> "_6735.GearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6735,
            )

            return self._parent._cast(_6735.GearCompoundCriticalSpeedAnalysis)

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "ZerolBevelGearCompoundCriticalSpeedAnalysis._Cast_ZerolBevelGearCompoundCriticalSpeedAnalysis",
        ) -> "_6754.MountableComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6754,
            )

            return self._parent._cast(
                _6754.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "ZerolBevelGearCompoundCriticalSpeedAnalysis._Cast_ZerolBevelGearCompoundCriticalSpeedAnalysis",
        ) -> "_6702.ComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6702,
            )

            return self._parent._cast(_6702.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "ZerolBevelGearCompoundCriticalSpeedAnalysis._Cast_ZerolBevelGearCompoundCriticalSpeedAnalysis",
        ) -> "_6756.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6756,
            )

            return self._parent._cast(_6756.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "ZerolBevelGearCompoundCriticalSpeedAnalysis._Cast_ZerolBevelGearCompoundCriticalSpeedAnalysis",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ZerolBevelGearCompoundCriticalSpeedAnalysis._Cast_ZerolBevelGearCompoundCriticalSpeedAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearCompoundCriticalSpeedAnalysis._Cast_ZerolBevelGearCompoundCriticalSpeedAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_compound_critical_speed_analysis(
            self: "ZerolBevelGearCompoundCriticalSpeedAnalysis._Cast_ZerolBevelGearCompoundCriticalSpeedAnalysis",
        ) -> "ZerolBevelGearCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearCompoundCriticalSpeedAnalysis._Cast_ZerolBevelGearCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "ZerolBevelGearCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2555.ZerolBevelGear":
        """mastapy.system_model.part_model.gears.ZerolBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6674.ZerolBevelGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ZerolBevelGearCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6674.ZerolBevelGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ZerolBevelGearCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ZerolBevelGearCompoundCriticalSpeedAnalysis._Cast_ZerolBevelGearCompoundCriticalSpeedAnalysis":
        return self._Cast_ZerolBevelGearCompoundCriticalSpeedAnalysis(self)
