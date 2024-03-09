"""ConnectorStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3844
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "ConnectorStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2449
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3773,
        _3845,
        _3862,
        _3790,
        _3846,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorStabilityAnalysis",)


Self = TypeVar("Self", bound="ConnectorStabilityAnalysis")


class ConnectorStabilityAnalysis(_3844.MountableComponentStabilityAnalysis):
    """ConnectorStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorStabilityAnalysis")

    class _Cast_ConnectorStabilityAnalysis:
        """Special nested class for casting ConnectorStabilityAnalysis to subclasses."""

        def __init__(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
            parent: "ConnectorStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_stability_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_3844.MountableComponentStabilityAnalysis":
            return self._parent._cast(_3844.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_3790.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3790,
            )

            return self._parent._cast(_3790.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_3846.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3846,
            )

            return self._parent._cast(_3846.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bearing_stability_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_3773.BearingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3773,
            )

            return self._parent._cast(_3773.BearingStabilityAnalysis)

        @property
        def oil_seal_stability_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_3845.OilSealStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3845,
            )

            return self._parent._cast(_3845.OilSealStabilityAnalysis)

        @property
        def shaft_hub_connection_stability_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_3862.ShaftHubConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3862,
            )

            return self._parent._cast(_3862.ShaftHubConnectionStabilityAnalysis)

        @property
        def connector_stability_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "ConnectorStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectorStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2449.Connector":
        """mastapy.system_model.part_model.Connector

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
    ) -> "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis":
        return self._Cast_ConnectorStabilityAnalysis(self)
