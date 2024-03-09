"""CouplingConnectionStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3832
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "CouplingConnectionStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2348
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3786,
        _3791,
        _3847,
        _3869,
        _3887,
        _3800,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543, _7540
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionStabilityAnalysis",)


Self = TypeVar("Self", bound="CouplingConnectionStabilityAnalysis")


class CouplingConnectionStabilityAnalysis(
    _3832.InterMountableComponentConnectionStabilityAnalysis
):
    """CouplingConnectionStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingConnectionStabilityAnalysis")

    class _Cast_CouplingConnectionStabilityAnalysis:
        """Special nested class for casting CouplingConnectionStabilityAnalysis to subclasses."""

        def __init__(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
            parent: "CouplingConnectionStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_stability_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_3832.InterMountableComponentConnectionStabilityAnalysis":
            return self._parent._cast(
                _3832.InterMountableComponentConnectionStabilityAnalysis
            )

        @property
        def connection_stability_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_3800.ConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3800,
            )

            return self._parent._cast(_3800.ConnectionStabilityAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_7543.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def clutch_connection_stability_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_3786.ClutchConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3786,
            )

            return self._parent._cast(_3786.ClutchConnectionStabilityAnalysis)

        @property
        def concept_coupling_connection_stability_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_3791.ConceptCouplingConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3791,
            )

            return self._parent._cast(_3791.ConceptCouplingConnectionStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_stability_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_3847.PartToPartShearCouplingConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3847,
            )

            return self._parent._cast(
                _3847.PartToPartShearCouplingConnectionStabilityAnalysis
            )

        @property
        def spring_damper_connection_stability_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_3869.SpringDamperConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3869,
            )

            return self._parent._cast(_3869.SpringDamperConnectionStabilityAnalysis)

        @property
        def torque_converter_connection_stability_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_3887.TorqueConverterConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3887,
            )

            return self._parent._cast(_3887.TorqueConverterConnectionStabilityAnalysis)

        @property
        def coupling_connection_stability_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "CouplingConnectionStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
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
        self: Self, instance_to_wrap: "CouplingConnectionStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2348.CouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.CouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> (
        "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis"
    ):
        return self._Cast_CouplingConnectionStabilityAnalysis(self)
