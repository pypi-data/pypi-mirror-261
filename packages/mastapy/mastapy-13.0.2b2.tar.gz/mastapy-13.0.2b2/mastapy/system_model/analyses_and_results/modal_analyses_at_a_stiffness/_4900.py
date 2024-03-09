"""CVTModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4869,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "CVTModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2588
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4959,
        _4859,
        _4940,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("CVTModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="CVTModalAnalysisAtAStiffness")


class CVTModalAnalysisAtAStiffness(_4869.BeltDriveModalAnalysisAtAStiffness):
    """CVTModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CVT_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTModalAnalysisAtAStiffness")

    class _Cast_CVTModalAnalysisAtAStiffness:
        """Special nested class for casting CVTModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness",
            parent: "CVTModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def belt_drive_modal_analysis_at_a_stiffness(
            self: "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness",
        ) -> "_4869.BeltDriveModalAnalysisAtAStiffness":
            return self._parent._cast(_4869.BeltDriveModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(
            self: "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness",
        ) -> "_4959.SpecialisedAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4959,
            )

            return self._parent._cast(
                _4959.SpecialisedAssemblyModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness",
        ) -> "_4859.AbstractAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4859,
            )

            return self._parent._cast(_4859.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness",
        ) -> "_4940.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4940,
            )

            return self._parent._cast(_4940.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cvt_modal_analysis_at_a_stiffness(
            self: "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness",
        ) -> "CVTModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTModalAnalysisAtAStiffness.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2588.CVT":
        """mastapy.system_model.part_model.couplings.CVT

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness":
        return self._Cast_CVTModalAnalysisAtAStiffness(self)
