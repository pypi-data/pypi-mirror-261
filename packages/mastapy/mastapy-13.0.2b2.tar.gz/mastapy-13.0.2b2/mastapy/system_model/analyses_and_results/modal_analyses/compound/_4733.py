"""AbstractShaftToMountableComponentConnectionCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4765
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
        "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4577
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4754,
        _4774,
        _4776,
        _4813,
        _4827,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",)


Self = TypeVar(
    "Self", bound="AbstractShaftToMountableComponentConnectionCompoundModalAnalysis"
)


class AbstractShaftToMountableComponentConnectionCompoundModalAnalysis(
    _4765.ConnectionCompoundModalAnalysis
):
    """AbstractShaftToMountableComponentConnectionCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysis:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",
            parent: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def connection_compound_modal_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4765.ConnectionCompoundModalAnalysis":
            return self._parent._cast(_4765.ConnectionCompoundModalAnalysis)

        @property
        def connection_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_7541.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_modal_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4754.CoaxialConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4754,
            )

            return self._parent._cast(_4754.CoaxialConnectionCompoundModalAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4774.CycloidalDiscCentralBearingConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4774,
            )

            return self._parent._cast(
                _4774.CycloidalDiscCentralBearingConnectionCompoundModalAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_modal_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4776.CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4776,
            )

            return self._parent._cast(
                _4776.CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis
            )

        @property
        def planetary_connection_compound_modal_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4813.PlanetaryConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4813,
            )

            return self._parent._cast(_4813.PlanetaryConnectionCompoundModalAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4827.ShaftToMountableComponentConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4827,
            )

            return self._parent._cast(
                _4827.ShaftToMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",
        ) -> "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",
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
        self: Self,
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4577.AbstractShaftToMountableComponentConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.AbstractShaftToMountableComponentConnectionModalAnalysis]

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4577.AbstractShaftToMountableComponentConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.AbstractShaftToMountableComponentConnectionModalAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysis":
        return (
            self._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysis(
                self
            )
        )
