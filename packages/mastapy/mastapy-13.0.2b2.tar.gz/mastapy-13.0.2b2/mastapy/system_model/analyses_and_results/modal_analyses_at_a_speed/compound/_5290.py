"""CVTCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5259,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "CVTCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5160,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5347,
        _5249,
        _5328,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("CVTCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="CVTCompoundModalAnalysisAtASpeed")


class CVTCompoundModalAnalysisAtASpeed(_5259.BeltDriveCompoundModalAnalysisAtASpeed):
    """CVTCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CVT_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTCompoundModalAnalysisAtASpeed")

    class _Cast_CVTCompoundModalAnalysisAtASpeed:
        """Special nested class for casting CVTCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "CVTCompoundModalAnalysisAtASpeed._Cast_CVTCompoundModalAnalysisAtASpeed",
            parent: "CVTCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def belt_drive_compound_modal_analysis_at_a_speed(
            self: "CVTCompoundModalAnalysisAtASpeed._Cast_CVTCompoundModalAnalysisAtASpeed",
        ) -> "_5259.BeltDriveCompoundModalAnalysisAtASpeed":
            return self._parent._cast(_5259.BeltDriveCompoundModalAnalysisAtASpeed)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(
            self: "CVTCompoundModalAnalysisAtASpeed._Cast_CVTCompoundModalAnalysisAtASpeed",
        ) -> "_5347.SpecialisedAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5347,
            )

            return self._parent._cast(
                _5347.SpecialisedAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(
            self: "CVTCompoundModalAnalysisAtASpeed._Cast_CVTCompoundModalAnalysisAtASpeed",
        ) -> "_5249.AbstractAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5249,
            )

            return self._parent._cast(
                _5249.AbstractAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "CVTCompoundModalAnalysisAtASpeed._Cast_CVTCompoundModalAnalysisAtASpeed",
        ) -> "_5328.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5328,
            )

            return self._parent._cast(_5328.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "CVTCompoundModalAnalysisAtASpeed._Cast_CVTCompoundModalAnalysisAtASpeed",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTCompoundModalAnalysisAtASpeed._Cast_CVTCompoundModalAnalysisAtASpeed",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTCompoundModalAnalysisAtASpeed._Cast_CVTCompoundModalAnalysisAtASpeed",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cvt_compound_modal_analysis_at_a_speed(
            self: "CVTCompoundModalAnalysisAtASpeed._Cast_CVTCompoundModalAnalysisAtASpeed",
        ) -> "CVTCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "CVTCompoundModalAnalysisAtASpeed._Cast_CVTCompoundModalAnalysisAtASpeed",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTCompoundModalAnalysisAtASpeed.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5160.CVTModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.CVTModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(self: Self) -> "List[_5160.CVTModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.CVTModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CVTCompoundModalAnalysisAtASpeed._Cast_CVTCompoundModalAnalysisAtASpeed":
        return self._Cast_CVTCompoundModalAnalysisAtASpeed(self)
