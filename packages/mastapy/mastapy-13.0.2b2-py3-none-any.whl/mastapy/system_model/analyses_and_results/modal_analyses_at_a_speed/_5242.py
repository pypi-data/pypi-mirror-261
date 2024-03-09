"""VirtualComponentModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5197
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "VirtualComponentModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2481
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5194,
        _5195,
        _5206,
        _5207,
        _5241,
        _5144,
        _5199,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="VirtualComponentModalAnalysisAtASpeed")


class VirtualComponentModalAnalysisAtASpeed(
    _5197.MountableComponentModalAnalysisAtASpeed
):
    """VirtualComponentModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualComponentModalAnalysisAtASpeed"
    )

    class _Cast_VirtualComponentModalAnalysisAtASpeed:
        """Special nested class for casting VirtualComponentModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
            parent: "VirtualComponentModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_5197.MountableComponentModalAnalysisAtASpeed":
            return self._parent._cast(_5197.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_5144.ComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5144,
            )

            return self._parent._cast(_5144.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_5199.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5199,
            )

            return self._parent._cast(_5199.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def mass_disc_modal_analysis_at_a_speed(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_5194.MassDiscModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5194,
            )

            return self._parent._cast(_5194.MassDiscModalAnalysisAtASpeed)

        @property
        def measurement_component_modal_analysis_at_a_speed(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_5195.MeasurementComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5195,
            )

            return self._parent._cast(_5195.MeasurementComponentModalAnalysisAtASpeed)

        @property
        def point_load_modal_analysis_at_a_speed(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_5206.PointLoadModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5206,
            )

            return self._parent._cast(_5206.PointLoadModalAnalysisAtASpeed)

        @property
        def power_load_modal_analysis_at_a_speed(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_5207.PowerLoadModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5207,
            )

            return self._parent._cast(_5207.PowerLoadModalAnalysisAtASpeed)

        @property
        def unbalanced_mass_modal_analysis_at_a_speed(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_5241.UnbalancedMassModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5241,
            )

            return self._parent._cast(_5241.UnbalancedMassModalAnalysisAtASpeed)

        @property
        def virtual_component_modal_analysis_at_a_speed(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "VirtualComponentModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "VirtualComponentModalAnalysisAtASpeed.TYPE"
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
    ) -> "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed":
        return self._Cast_VirtualComponentModalAnalysisAtASpeed(self)
