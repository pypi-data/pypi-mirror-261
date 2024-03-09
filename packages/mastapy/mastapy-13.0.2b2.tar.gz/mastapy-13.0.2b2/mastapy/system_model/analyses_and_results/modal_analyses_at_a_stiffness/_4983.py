"""VirtualComponentModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4938,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "VirtualComponentModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2481
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4935,
        _4936,
        _4947,
        _4948,
        _4982,
        _4884,
        _4940,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="VirtualComponentModalAnalysisAtAStiffness")


class VirtualComponentModalAnalysisAtAStiffness(
    _4938.MountableComponentModalAnalysisAtAStiffness
):
    """VirtualComponentModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualComponentModalAnalysisAtAStiffness"
    )

    class _Cast_VirtualComponentModalAnalysisAtAStiffness:
        """Special nested class for casting VirtualComponentModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "VirtualComponentModalAnalysisAtAStiffness._Cast_VirtualComponentModalAnalysisAtAStiffness",
            parent: "VirtualComponentModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "VirtualComponentModalAnalysisAtAStiffness._Cast_VirtualComponentModalAnalysisAtAStiffness",
        ) -> "_4938.MountableComponentModalAnalysisAtAStiffness":
            return self._parent._cast(_4938.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "VirtualComponentModalAnalysisAtAStiffness._Cast_VirtualComponentModalAnalysisAtAStiffness",
        ) -> "_4884.ComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4884,
            )

            return self._parent._cast(_4884.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "VirtualComponentModalAnalysisAtAStiffness._Cast_VirtualComponentModalAnalysisAtAStiffness",
        ) -> "_4940.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4940,
            )

            return self._parent._cast(_4940.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "VirtualComponentModalAnalysisAtAStiffness._Cast_VirtualComponentModalAnalysisAtAStiffness",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentModalAnalysisAtAStiffness._Cast_VirtualComponentModalAnalysisAtAStiffness",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentModalAnalysisAtAStiffness._Cast_VirtualComponentModalAnalysisAtAStiffness",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentModalAnalysisAtAStiffness._Cast_VirtualComponentModalAnalysisAtAStiffness",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentModalAnalysisAtAStiffness._Cast_VirtualComponentModalAnalysisAtAStiffness",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def mass_disc_modal_analysis_at_a_stiffness(
            self: "VirtualComponentModalAnalysisAtAStiffness._Cast_VirtualComponentModalAnalysisAtAStiffness",
        ) -> "_4935.MassDiscModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4935,
            )

            return self._parent._cast(_4935.MassDiscModalAnalysisAtAStiffness)

        @property
        def measurement_component_modal_analysis_at_a_stiffness(
            self: "VirtualComponentModalAnalysisAtAStiffness._Cast_VirtualComponentModalAnalysisAtAStiffness",
        ) -> "_4936.MeasurementComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4936,
            )

            return self._parent._cast(
                _4936.MeasurementComponentModalAnalysisAtAStiffness
            )

        @property
        def point_load_modal_analysis_at_a_stiffness(
            self: "VirtualComponentModalAnalysisAtAStiffness._Cast_VirtualComponentModalAnalysisAtAStiffness",
        ) -> "_4947.PointLoadModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4947,
            )

            return self._parent._cast(_4947.PointLoadModalAnalysisAtAStiffness)

        @property
        def power_load_modal_analysis_at_a_stiffness(
            self: "VirtualComponentModalAnalysisAtAStiffness._Cast_VirtualComponentModalAnalysisAtAStiffness",
        ) -> "_4948.PowerLoadModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4948,
            )

            return self._parent._cast(_4948.PowerLoadModalAnalysisAtAStiffness)

        @property
        def unbalanced_mass_modal_analysis_at_a_stiffness(
            self: "VirtualComponentModalAnalysisAtAStiffness._Cast_VirtualComponentModalAnalysisAtAStiffness",
        ) -> "_4982.UnbalancedMassModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4982,
            )

            return self._parent._cast(_4982.UnbalancedMassModalAnalysisAtAStiffness)

        @property
        def virtual_component_modal_analysis_at_a_stiffness(
            self: "VirtualComponentModalAnalysisAtAStiffness._Cast_VirtualComponentModalAnalysisAtAStiffness",
        ) -> "VirtualComponentModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "VirtualComponentModalAnalysisAtAStiffness._Cast_VirtualComponentModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "VirtualComponentModalAnalysisAtAStiffness.TYPE"
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
    ) -> "VirtualComponentModalAnalysisAtAStiffness._Cast_VirtualComponentModalAnalysisAtAStiffness":
        return self._Cast_VirtualComponentModalAnalysisAtAStiffness(self)
