"""MeasurementComponentCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5371,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "MeasurementComponentCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2465
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5195,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5326,
        _5274,
        _5328,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("MeasurementComponentCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="MeasurementComponentCompoundModalAnalysisAtASpeed")


class MeasurementComponentCompoundModalAnalysisAtASpeed(
    _5371.VirtualComponentCompoundModalAnalysisAtASpeed
):
    """MeasurementComponentCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_COMPONENT_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MeasurementComponentCompoundModalAnalysisAtASpeed"
    )

    class _Cast_MeasurementComponentCompoundModalAnalysisAtASpeed:
        """Special nested class for casting MeasurementComponentCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "MeasurementComponentCompoundModalAnalysisAtASpeed._Cast_MeasurementComponentCompoundModalAnalysisAtASpeed",
            parent: "MeasurementComponentCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_modal_analysis_at_a_speed(
            self: "MeasurementComponentCompoundModalAnalysisAtASpeed._Cast_MeasurementComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5371.VirtualComponentCompoundModalAnalysisAtASpeed":
            return self._parent._cast(
                _5371.VirtualComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(
            self: "MeasurementComponentCompoundModalAnalysisAtASpeed._Cast_MeasurementComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5326.MountableComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5326,
            )

            return self._parent._cast(
                _5326.MountableComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "MeasurementComponentCompoundModalAnalysisAtASpeed._Cast_MeasurementComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5274.ComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5274,
            )

            return self._parent._cast(_5274.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "MeasurementComponentCompoundModalAnalysisAtASpeed._Cast_MeasurementComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5328.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5328,
            )

            return self._parent._cast(_5328.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "MeasurementComponentCompoundModalAnalysisAtASpeed._Cast_MeasurementComponentCompoundModalAnalysisAtASpeed",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MeasurementComponentCompoundModalAnalysisAtASpeed._Cast_MeasurementComponentCompoundModalAnalysisAtASpeed",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MeasurementComponentCompoundModalAnalysisAtASpeed._Cast_MeasurementComponentCompoundModalAnalysisAtASpeed",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def measurement_component_compound_modal_analysis_at_a_speed(
            self: "MeasurementComponentCompoundModalAnalysisAtASpeed._Cast_MeasurementComponentCompoundModalAnalysisAtASpeed",
        ) -> "MeasurementComponentCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "MeasurementComponentCompoundModalAnalysisAtASpeed._Cast_MeasurementComponentCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "MeasurementComponentCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2465.MeasurementComponent":
        """mastapy.system_model.part_model.MeasurementComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5195.MeasurementComponentModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.MeasurementComponentModalAnalysisAtASpeed]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5195.MeasurementComponentModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.MeasurementComponentModalAnalysisAtASpeed]

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
    def cast_to(
        self: Self,
    ) -> "MeasurementComponentCompoundModalAnalysisAtASpeed._Cast_MeasurementComponentCompoundModalAnalysisAtASpeed":
        return self._Cast_MeasurementComponentCompoundModalAnalysisAtASpeed(self)
