"""OilSealCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6581
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "OilSealCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2468
    from mastapy.system_model.analyses_and_results.static_loads import _6929
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6625,
        _6570,
        _6627,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("OilSealCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="OilSealCriticalSpeedAnalysis")


class OilSealCriticalSpeedAnalysis(_6581.ConnectorCriticalSpeedAnalysis):
    """OilSealCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _OIL_SEAL_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OilSealCriticalSpeedAnalysis")

    class _Cast_OilSealCriticalSpeedAnalysis:
        """Special nested class for casting OilSealCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "OilSealCriticalSpeedAnalysis._Cast_OilSealCriticalSpeedAnalysis",
            parent: "OilSealCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def connector_critical_speed_analysis(
            self: "OilSealCriticalSpeedAnalysis._Cast_OilSealCriticalSpeedAnalysis",
        ) -> "_6581.ConnectorCriticalSpeedAnalysis":
            return self._parent._cast(_6581.ConnectorCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "OilSealCriticalSpeedAnalysis._Cast_OilSealCriticalSpeedAnalysis",
        ) -> "_6625.MountableComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6625,
            )

            return self._parent._cast(_6625.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "OilSealCriticalSpeedAnalysis._Cast_OilSealCriticalSpeedAnalysis",
        ) -> "_6570.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6570,
            )

            return self._parent._cast(_6570.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "OilSealCriticalSpeedAnalysis._Cast_OilSealCriticalSpeedAnalysis",
        ) -> "_6627.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6627,
            )

            return self._parent._cast(_6627.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "OilSealCriticalSpeedAnalysis._Cast_OilSealCriticalSpeedAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "OilSealCriticalSpeedAnalysis._Cast_OilSealCriticalSpeedAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "OilSealCriticalSpeedAnalysis._Cast_OilSealCriticalSpeedAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "OilSealCriticalSpeedAnalysis._Cast_OilSealCriticalSpeedAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "OilSealCriticalSpeedAnalysis._Cast_OilSealCriticalSpeedAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def oil_seal_critical_speed_analysis(
            self: "OilSealCriticalSpeedAnalysis._Cast_OilSealCriticalSpeedAnalysis",
        ) -> "OilSealCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "OilSealCriticalSpeedAnalysis._Cast_OilSealCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OilSealCriticalSpeedAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2468.OilSeal":
        """mastapy.system_model.part_model.OilSeal

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6929.OilSealLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.OilSealLoadCase

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
    ) -> "OilSealCriticalSpeedAnalysis._Cast_OilSealCriticalSpeedAnalysis":
        return self._Cast_OilSealCriticalSpeedAnalysis(self)
