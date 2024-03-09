"""RingPinsMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5466
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "RingPinsMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2572
    from mastapy.system_model.analyses_and_results.static_loads import _6946
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5406, _5469
    from mastapy.system_model.analyses_and_results.analysis_cases import _7551, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="RingPinsMultibodyDynamicsAnalysis")


class RingPinsMultibodyDynamicsAnalysis(
    _5466.MountableComponentMultibodyDynamicsAnalysis
):
    """RingPinsMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _RING_PINS_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RingPinsMultibodyDynamicsAnalysis")

    class _Cast_RingPinsMultibodyDynamicsAnalysis:
        """Special nested class for casting RingPinsMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "RingPinsMultibodyDynamicsAnalysis._Cast_RingPinsMultibodyDynamicsAnalysis",
            parent: "RingPinsMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "RingPinsMultibodyDynamicsAnalysis._Cast_RingPinsMultibodyDynamicsAnalysis",
        ) -> "_5466.MountableComponentMultibodyDynamicsAnalysis":
            return self._parent._cast(_5466.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "RingPinsMultibodyDynamicsAnalysis._Cast_RingPinsMultibodyDynamicsAnalysis",
        ) -> "_5406.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5406

            return self._parent._cast(_5406.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "RingPinsMultibodyDynamicsAnalysis._Cast_RingPinsMultibodyDynamicsAnalysis",
        ) -> "_5469.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5469

            return self._parent._cast(_5469.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "RingPinsMultibodyDynamicsAnalysis._Cast_RingPinsMultibodyDynamicsAnalysis",
        ) -> "_7551.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RingPinsMultibodyDynamicsAnalysis._Cast_RingPinsMultibodyDynamicsAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RingPinsMultibodyDynamicsAnalysis._Cast_RingPinsMultibodyDynamicsAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RingPinsMultibodyDynamicsAnalysis._Cast_RingPinsMultibodyDynamicsAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsMultibodyDynamicsAnalysis._Cast_RingPinsMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def ring_pins_multibody_dynamics_analysis(
            self: "RingPinsMultibodyDynamicsAnalysis._Cast_RingPinsMultibodyDynamicsAnalysis",
        ) -> "RingPinsMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "RingPinsMultibodyDynamicsAnalysis._Cast_RingPinsMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "RingPinsMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2572.RingPins":
        """mastapy.system_model.part_model.cycloidal.RingPins

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6946.RingPinsLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RingPinsLoadCase

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
    ) -> "RingPinsMultibodyDynamicsAnalysis._Cast_RingPinsMultibodyDynamicsAnalysis":
        return self._Cast_RingPinsMultibodyDynamicsAnalysis(self)
