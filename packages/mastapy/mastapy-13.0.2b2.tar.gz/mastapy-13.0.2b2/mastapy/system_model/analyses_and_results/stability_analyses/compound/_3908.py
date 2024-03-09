"""BeltConnectionCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3964
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "BeltConnectionCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2270
    from mastapy.system_model.analyses_and_results.stability_analyses import _3774
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3939,
        _3934,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("BeltConnectionCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="BeltConnectionCompoundStabilityAnalysis")


class BeltConnectionCompoundStabilityAnalysis(
    _3964.InterMountableComponentConnectionCompoundStabilityAnalysis
):
    """BeltConnectionCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BeltConnectionCompoundStabilityAnalysis"
    )

    class _Cast_BeltConnectionCompoundStabilityAnalysis:
        """Special nested class for casting BeltConnectionCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "BeltConnectionCompoundStabilityAnalysis._Cast_BeltConnectionCompoundStabilityAnalysis",
            parent: "BeltConnectionCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_stability_analysis(
            self: "BeltConnectionCompoundStabilityAnalysis._Cast_BeltConnectionCompoundStabilityAnalysis",
        ) -> "_3964.InterMountableComponentConnectionCompoundStabilityAnalysis":
            return self._parent._cast(
                _3964.InterMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def connection_compound_stability_analysis(
            self: "BeltConnectionCompoundStabilityAnalysis._Cast_BeltConnectionCompoundStabilityAnalysis",
        ) -> "_3934.ConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3934,
            )

            return self._parent._cast(_3934.ConnectionCompoundStabilityAnalysis)

        @property
        def connection_compound_analysis(
            self: "BeltConnectionCompoundStabilityAnalysis._Cast_BeltConnectionCompoundStabilityAnalysis",
        ) -> "_7541.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BeltConnectionCompoundStabilityAnalysis._Cast_BeltConnectionCompoundStabilityAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltConnectionCompoundStabilityAnalysis._Cast_BeltConnectionCompoundStabilityAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_compound_stability_analysis(
            self: "BeltConnectionCompoundStabilityAnalysis._Cast_BeltConnectionCompoundStabilityAnalysis",
        ) -> "_3939.CVTBeltConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3939,
            )

            return self._parent._cast(_3939.CVTBeltConnectionCompoundStabilityAnalysis)

        @property
        def belt_connection_compound_stability_analysis(
            self: "BeltConnectionCompoundStabilityAnalysis._Cast_BeltConnectionCompoundStabilityAnalysis",
        ) -> "BeltConnectionCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "BeltConnectionCompoundStabilityAnalysis._Cast_BeltConnectionCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "BeltConnectionCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2270.BeltConnection":
        """mastapy.system_model.connections_and_sockets.BeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2270.BeltConnection":
        """mastapy.system_model.connections_and_sockets.BeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3774.BeltConnectionStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.BeltConnectionStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3774.BeltConnectionStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.BeltConnectionStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BeltConnectionCompoundStabilityAnalysis._Cast_BeltConnectionCompoundStabilityAnalysis":
        return self._Cast_BeltConnectionCompoundStabilityAnalysis(self)
