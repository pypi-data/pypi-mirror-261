"""VirtualComponentCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6625
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "VirtualComponentCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2481
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6623,
        _6624,
        _6634,
        _6635,
        _6669,
        _6570,
        _6627,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="VirtualComponentCriticalSpeedAnalysis")


class VirtualComponentCriticalSpeedAnalysis(
    _6625.MountableComponentCriticalSpeedAnalysis
):
    """VirtualComponentCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualComponentCriticalSpeedAnalysis"
    )

    class _Cast_VirtualComponentCriticalSpeedAnalysis:
        """Special nested class for casting VirtualComponentCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
            parent: "VirtualComponentCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_critical_speed_analysis(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_6625.MountableComponentCriticalSpeedAnalysis":
            return self._parent._cast(_6625.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_6570.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6570,
            )

            return self._parent._cast(_6570.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_6627.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6627,
            )

            return self._parent._cast(_6627.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def mass_disc_critical_speed_analysis(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_6623.MassDiscCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6623,
            )

            return self._parent._cast(_6623.MassDiscCriticalSpeedAnalysis)

        @property
        def measurement_component_critical_speed_analysis(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_6624.MeasurementComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6624,
            )

            return self._parent._cast(_6624.MeasurementComponentCriticalSpeedAnalysis)

        @property
        def point_load_critical_speed_analysis(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_6634.PointLoadCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6634,
            )

            return self._parent._cast(_6634.PointLoadCriticalSpeedAnalysis)

        @property
        def power_load_critical_speed_analysis(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_6635.PowerLoadCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6635,
            )

            return self._parent._cast(_6635.PowerLoadCriticalSpeedAnalysis)

        @property
        def unbalanced_mass_critical_speed_analysis(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_6669.UnbalancedMassCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6669,
            )

            return self._parent._cast(_6669.UnbalancedMassCriticalSpeedAnalysis)

        @property
        def virtual_component_critical_speed_analysis(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "VirtualComponentCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "VirtualComponentCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2481.VirtualComponent":
        """mastapy.system_model.part_model.VirtualComponent

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
    ) -> "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis":
        return self._Cast_VirtualComponentCriticalSpeedAnalysis(self)
