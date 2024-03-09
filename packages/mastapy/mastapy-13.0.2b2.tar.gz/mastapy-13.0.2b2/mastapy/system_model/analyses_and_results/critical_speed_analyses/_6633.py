"""PlanetCarrierCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6625
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "PlanetCarrierCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2471
    from mastapy.system_model.analyses_and_results.static_loads import _6938
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6570,
        _6627,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("PlanetCarrierCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="PlanetCarrierCriticalSpeedAnalysis")


class PlanetCarrierCriticalSpeedAnalysis(_6625.MountableComponentCriticalSpeedAnalysis):
    """PlanetCarrierCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANET_CARRIER_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetCarrierCriticalSpeedAnalysis")

    class _Cast_PlanetCarrierCriticalSpeedAnalysis:
        """Special nested class for casting PlanetCarrierCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "PlanetCarrierCriticalSpeedAnalysis._Cast_PlanetCarrierCriticalSpeedAnalysis",
            parent: "PlanetCarrierCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_critical_speed_analysis(
            self: "PlanetCarrierCriticalSpeedAnalysis._Cast_PlanetCarrierCriticalSpeedAnalysis",
        ) -> "_6625.MountableComponentCriticalSpeedAnalysis":
            return self._parent._cast(_6625.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "PlanetCarrierCriticalSpeedAnalysis._Cast_PlanetCarrierCriticalSpeedAnalysis",
        ) -> "_6570.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6570,
            )

            return self._parent._cast(_6570.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "PlanetCarrierCriticalSpeedAnalysis._Cast_PlanetCarrierCriticalSpeedAnalysis",
        ) -> "_6627.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6627,
            )

            return self._parent._cast(_6627.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PlanetCarrierCriticalSpeedAnalysis._Cast_PlanetCarrierCriticalSpeedAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetCarrierCriticalSpeedAnalysis._Cast_PlanetCarrierCriticalSpeedAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetCarrierCriticalSpeedAnalysis._Cast_PlanetCarrierCriticalSpeedAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetCarrierCriticalSpeedAnalysis._Cast_PlanetCarrierCriticalSpeedAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetCarrierCriticalSpeedAnalysis._Cast_PlanetCarrierCriticalSpeedAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def planet_carrier_critical_speed_analysis(
            self: "PlanetCarrierCriticalSpeedAnalysis._Cast_PlanetCarrierCriticalSpeedAnalysis",
        ) -> "PlanetCarrierCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetCarrierCriticalSpeedAnalysis._Cast_PlanetCarrierCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "PlanetCarrierCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2471.PlanetCarrier":
        """mastapy.system_model.part_model.PlanetCarrier

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6938.PlanetCarrierLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PlanetCarrierLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PlanetCarrierCriticalSpeedAnalysis._Cast_PlanetCarrierCriticalSpeedAnalysis":
        return self._Cast_PlanetCarrierCriticalSpeedAnalysis(self)
