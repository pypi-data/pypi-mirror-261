"""TorqueConverterTurbineModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4897,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "TorqueConverterTurbineModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2612
    from mastapy.system_model.analyses_and_results.static_loads import _6978
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4938,
        _4884,
        _4940,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterTurbineModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="TorqueConverterTurbineModalAnalysisAtAStiffness")


class TorqueConverterTurbineModalAnalysisAtAStiffness(
    _4897.CouplingHalfModalAnalysisAtAStiffness
):
    """TorqueConverterTurbineModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterTurbineModalAnalysisAtAStiffness"
    )

    class _Cast_TorqueConverterTurbineModalAnalysisAtAStiffness:
        """Special nested class for casting TorqueConverterTurbineModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "TorqueConverterTurbineModalAnalysisAtAStiffness._Cast_TorqueConverterTurbineModalAnalysisAtAStiffness",
            parent: "TorqueConverterTurbineModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def coupling_half_modal_analysis_at_a_stiffness(
            self: "TorqueConverterTurbineModalAnalysisAtAStiffness._Cast_TorqueConverterTurbineModalAnalysisAtAStiffness",
        ) -> "_4897.CouplingHalfModalAnalysisAtAStiffness":
            return self._parent._cast(_4897.CouplingHalfModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "TorqueConverterTurbineModalAnalysisAtAStiffness._Cast_TorqueConverterTurbineModalAnalysisAtAStiffness",
        ) -> "_4938.MountableComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4938,
            )

            return self._parent._cast(_4938.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "TorqueConverterTurbineModalAnalysisAtAStiffness._Cast_TorqueConverterTurbineModalAnalysisAtAStiffness",
        ) -> "_4884.ComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4884,
            )

            return self._parent._cast(_4884.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "TorqueConverterTurbineModalAnalysisAtAStiffness._Cast_TorqueConverterTurbineModalAnalysisAtAStiffness",
        ) -> "_4940.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4940,
            )

            return self._parent._cast(_4940.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "TorqueConverterTurbineModalAnalysisAtAStiffness._Cast_TorqueConverterTurbineModalAnalysisAtAStiffness",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterTurbineModalAnalysisAtAStiffness._Cast_TorqueConverterTurbineModalAnalysisAtAStiffness",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterTurbineModalAnalysisAtAStiffness._Cast_TorqueConverterTurbineModalAnalysisAtAStiffness",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterTurbineModalAnalysisAtAStiffness._Cast_TorqueConverterTurbineModalAnalysisAtAStiffness",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterTurbineModalAnalysisAtAStiffness._Cast_TorqueConverterTurbineModalAnalysisAtAStiffness",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def torque_converter_turbine_modal_analysis_at_a_stiffness(
            self: "TorqueConverterTurbineModalAnalysisAtAStiffness._Cast_TorqueConverterTurbineModalAnalysisAtAStiffness",
        ) -> "TorqueConverterTurbineModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "TorqueConverterTurbineModalAnalysisAtAStiffness._Cast_TorqueConverterTurbineModalAnalysisAtAStiffness",
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
        instance_to_wrap: "TorqueConverterTurbineModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2612.TorqueConverterTurbine":
        """mastapy.system_model.part_model.couplings.TorqueConverterTurbine

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6978.TorqueConverterTurbineLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "TorqueConverterTurbineModalAnalysisAtAStiffness._Cast_TorqueConverterTurbineModalAnalysisAtAStiffness":
        return self._Cast_TorqueConverterTurbineModalAnalysisAtAStiffness(self)
