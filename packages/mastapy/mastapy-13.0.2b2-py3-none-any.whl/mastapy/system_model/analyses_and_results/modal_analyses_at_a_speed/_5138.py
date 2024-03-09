"""BoltedJointModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5218
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "BoltedJointModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2445
    from mastapy.system_model.analyses_and_results.static_loads import _6833
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5119,
        _5199,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("BoltedJointModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="BoltedJointModalAnalysisAtASpeed")


class BoltedJointModalAnalysisAtASpeed(_5218.SpecialisedAssemblyModalAnalysisAtASpeed):
    """BoltedJointModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _BOLTED_JOINT_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BoltedJointModalAnalysisAtASpeed")

    class _Cast_BoltedJointModalAnalysisAtASpeed:
        """Special nested class for casting BoltedJointModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "BoltedJointModalAnalysisAtASpeed._Cast_BoltedJointModalAnalysisAtASpeed",
            parent: "BoltedJointModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def specialised_assembly_modal_analysis_at_a_speed(
            self: "BoltedJointModalAnalysisAtASpeed._Cast_BoltedJointModalAnalysisAtASpeed",
        ) -> "_5218.SpecialisedAssemblyModalAnalysisAtASpeed":
            return self._parent._cast(_5218.SpecialisedAssemblyModalAnalysisAtASpeed)

        @property
        def abstract_assembly_modal_analysis_at_a_speed(
            self: "BoltedJointModalAnalysisAtASpeed._Cast_BoltedJointModalAnalysisAtASpeed",
        ) -> "_5119.AbstractAssemblyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5119,
            )

            return self._parent._cast(_5119.AbstractAssemblyModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "BoltedJointModalAnalysisAtASpeed._Cast_BoltedJointModalAnalysisAtASpeed",
        ) -> "_5199.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5199,
            )

            return self._parent._cast(_5199.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "BoltedJointModalAnalysisAtASpeed._Cast_BoltedJointModalAnalysisAtASpeed",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BoltedJointModalAnalysisAtASpeed._Cast_BoltedJointModalAnalysisAtASpeed",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BoltedJointModalAnalysisAtASpeed._Cast_BoltedJointModalAnalysisAtASpeed",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BoltedJointModalAnalysisAtASpeed._Cast_BoltedJointModalAnalysisAtASpeed",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltedJointModalAnalysisAtASpeed._Cast_BoltedJointModalAnalysisAtASpeed",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bolted_joint_modal_analysis_at_a_speed(
            self: "BoltedJointModalAnalysisAtASpeed._Cast_BoltedJointModalAnalysisAtASpeed",
        ) -> "BoltedJointModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "BoltedJointModalAnalysisAtASpeed._Cast_BoltedJointModalAnalysisAtASpeed",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BoltedJointModalAnalysisAtASpeed.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2445.BoltedJoint":
        """mastapy.system_model.part_model.BoltedJoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6833.BoltedJointLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BoltedJointLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BoltedJointModalAnalysisAtASpeed._Cast_BoltedJointModalAnalysisAtASpeed":
        return self._Cast_BoltedJointModalAnalysisAtASpeed(self)
