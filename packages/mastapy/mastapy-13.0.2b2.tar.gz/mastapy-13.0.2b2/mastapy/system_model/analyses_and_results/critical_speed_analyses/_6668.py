"""TorqueConverterTurbineCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6584
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "TorqueConverterTurbineCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2612
    from mastapy.system_model.analyses_and_results.static_loads import _6978
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6625,
        _6570,
        _6627,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterTurbineCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="TorqueConverterTurbineCriticalSpeedAnalysis")


class TorqueConverterTurbineCriticalSpeedAnalysis(
    _6584.CouplingHalfCriticalSpeedAnalysis
):
    """TorqueConverterTurbineCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterTurbineCriticalSpeedAnalysis"
    )

    class _Cast_TorqueConverterTurbineCriticalSpeedAnalysis:
        """Special nested class for casting TorqueConverterTurbineCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "TorqueConverterTurbineCriticalSpeedAnalysis._Cast_TorqueConverterTurbineCriticalSpeedAnalysis",
            parent: "TorqueConverterTurbineCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_critical_speed_analysis(
            self: "TorqueConverterTurbineCriticalSpeedAnalysis._Cast_TorqueConverterTurbineCriticalSpeedAnalysis",
        ) -> "_6584.CouplingHalfCriticalSpeedAnalysis":
            return self._parent._cast(_6584.CouplingHalfCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "TorqueConverterTurbineCriticalSpeedAnalysis._Cast_TorqueConverterTurbineCriticalSpeedAnalysis",
        ) -> "_6625.MountableComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6625,
            )

            return self._parent._cast(_6625.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "TorqueConverterTurbineCriticalSpeedAnalysis._Cast_TorqueConverterTurbineCriticalSpeedAnalysis",
        ) -> "_6570.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6570,
            )

            return self._parent._cast(_6570.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "TorqueConverterTurbineCriticalSpeedAnalysis._Cast_TorqueConverterTurbineCriticalSpeedAnalysis",
        ) -> "_6627.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6627,
            )

            return self._parent._cast(_6627.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "TorqueConverterTurbineCriticalSpeedAnalysis._Cast_TorqueConverterTurbineCriticalSpeedAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterTurbineCriticalSpeedAnalysis._Cast_TorqueConverterTurbineCriticalSpeedAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterTurbineCriticalSpeedAnalysis._Cast_TorqueConverterTurbineCriticalSpeedAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterTurbineCriticalSpeedAnalysis._Cast_TorqueConverterTurbineCriticalSpeedAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterTurbineCriticalSpeedAnalysis._Cast_TorqueConverterTurbineCriticalSpeedAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def torque_converter_turbine_critical_speed_analysis(
            self: "TorqueConverterTurbineCriticalSpeedAnalysis._Cast_TorqueConverterTurbineCriticalSpeedAnalysis",
        ) -> "TorqueConverterTurbineCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "TorqueConverterTurbineCriticalSpeedAnalysis._Cast_TorqueConverterTurbineCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "TorqueConverterTurbineCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2612.TorqueConverterTurbine":
        """mastapy.system_model.part_model.couplings.TorqueConverterTurbine

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6978.TorqueConverterTurbineLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase

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
    ) -> "TorqueConverterTurbineCriticalSpeedAnalysis._Cast_TorqueConverterTurbineCriticalSpeedAnalysis":
        return self._Cast_TorqueConverterTurbineCriticalSpeedAnalysis(self)
