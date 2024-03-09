"""CVTPulleyCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6636
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "CVTPulleyCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2589
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6584,
        _6625,
        _6570,
        _6627,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="CVTPulleyCriticalSpeedAnalysis")


class CVTPulleyCriticalSpeedAnalysis(_6636.PulleyCriticalSpeedAnalysis):
    """CVTPulleyCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTPulleyCriticalSpeedAnalysis")

    class _Cast_CVTPulleyCriticalSpeedAnalysis:
        """Special nested class for casting CVTPulleyCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
            parent: "CVTPulleyCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def pulley_critical_speed_analysis(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
        ) -> "_6636.PulleyCriticalSpeedAnalysis":
            return self._parent._cast(_6636.PulleyCriticalSpeedAnalysis)

        @property
        def coupling_half_critical_speed_analysis(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
        ) -> "_6584.CouplingHalfCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6584,
            )

            return self._parent._cast(_6584.CouplingHalfCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
        ) -> "_6625.MountableComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6625,
            )

            return self._parent._cast(_6625.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
        ) -> "_6570.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6570,
            )

            return self._parent._cast(_6570.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
        ) -> "_6627.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6627,
            )

            return self._parent._cast(_6627.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cvt_pulley_critical_speed_analysis(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
        ) -> "CVTPulleyCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTPulleyCriticalSpeedAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2589.CVTPulley":
        """mastapy.system_model.part_model.couplings.CVTPulley

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis":
        return self._Cast_CVTPulleyCriticalSpeedAnalysis(self)
