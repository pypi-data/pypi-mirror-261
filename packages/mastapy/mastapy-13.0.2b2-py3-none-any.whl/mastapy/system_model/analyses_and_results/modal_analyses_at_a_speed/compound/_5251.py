"""AbstractShaftOrHousingCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5274,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5121,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5250,
        _5294,
        _5305,
        _5344,
        _5328,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingCompoundModalAnalysisAtASpeed")


class AbstractShaftOrHousingCompoundModalAnalysisAtASpeed(
    _5274.ComponentCompoundModalAnalysisAtASpeed
):
    """AbstractShaftOrHousingCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed"
    )

    class _Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed:
        """Special nested class for casting AbstractShaftOrHousingCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
            parent: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
        ) -> "_5274.ComponentCompoundModalAnalysisAtASpeed":
            return self._parent._cast(_5274.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
        ) -> "_5328.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5328,
            )

            return self._parent._cast(_5328.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
        ) -> "_5250.AbstractShaftCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5250,
            )

            return self._parent._cast(_5250.AbstractShaftCompoundModalAnalysisAtASpeed)

        @property
        def cycloidal_disc_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
        ) -> "_5294.CycloidalDiscCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5294,
            )

            return self._parent._cast(_5294.CycloidalDiscCompoundModalAnalysisAtASpeed)

        @property
        def fe_part_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
        ) -> "_5305.FEPartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5305,
            )

            return self._parent._cast(_5305.FEPartCompoundModalAnalysisAtASpeed)

        @property
        def shaft_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
        ) -> "_5344.ShaftCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5344,
            )

            return self._parent._cast(_5344.ShaftCompoundModalAnalysisAtASpeed)

        @property
        def abstract_shaft_or_housing_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
        ) -> "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5121.AbstractShaftOrHousingModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.AbstractShaftOrHousingModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5121.AbstractShaftOrHousingModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.AbstractShaftOrHousingModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed":
        return self._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed(self)
