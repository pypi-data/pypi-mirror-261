"""StraightBevelDiffGearSetModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5137
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "StraightBevelDiffGearSetModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2548
    from mastapy.system_model.analyses_and_results.static_loads import _6964
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5226,
        _5225,
        _5125,
        _5153,
        _5179,
        _5218,
        _5119,
        _5199,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSetModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="StraightBevelDiffGearSetModalAnalysisAtASpeed")


class StraightBevelDiffGearSetModalAnalysisAtASpeed(
    _5137.BevelGearSetModalAnalysisAtASpeed
):
    """StraightBevelDiffGearSetModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed"
    )

    class _Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed:
        """Special nested class for casting StraightBevelDiffGearSetModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearSetModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed",
            parent: "StraightBevelDiffGearSetModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_modal_analysis_at_a_speed(
            self: "StraightBevelDiffGearSetModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed",
        ) -> "_5137.BevelGearSetModalAnalysisAtASpeed":
            return self._parent._cast(_5137.BevelGearSetModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_set_modal_analysis_at_a_speed(
            self: "StraightBevelDiffGearSetModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed",
        ) -> "_5125.AGMAGleasonConicalGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5125,
            )

            return self._parent._cast(
                _5125.AGMAGleasonConicalGearSetModalAnalysisAtASpeed
            )

        @property
        def conical_gear_set_modal_analysis_at_a_speed(
            self: "StraightBevelDiffGearSetModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed",
        ) -> "_5153.ConicalGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5153,
            )

            return self._parent._cast(_5153.ConicalGearSetModalAnalysisAtASpeed)

        @property
        def gear_set_modal_analysis_at_a_speed(
            self: "StraightBevelDiffGearSetModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed",
        ) -> "_5179.GearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5179,
            )

            return self._parent._cast(_5179.GearSetModalAnalysisAtASpeed)

        @property
        def specialised_assembly_modal_analysis_at_a_speed(
            self: "StraightBevelDiffGearSetModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed",
        ) -> "_5218.SpecialisedAssemblyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5218,
            )

            return self._parent._cast(_5218.SpecialisedAssemblyModalAnalysisAtASpeed)

        @property
        def abstract_assembly_modal_analysis_at_a_speed(
            self: "StraightBevelDiffGearSetModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed",
        ) -> "_5119.AbstractAssemblyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5119,
            )

            return self._parent._cast(_5119.AbstractAssemblyModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "StraightBevelDiffGearSetModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed",
        ) -> "_5199.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5199,
            )

            return self._parent._cast(_5199.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelDiffGearSetModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelDiffGearSetModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelDiffGearSetModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearSetModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearSetModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_set_modal_analysis_at_a_speed(
            self: "StraightBevelDiffGearSetModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed",
        ) -> "StraightBevelDiffGearSetModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearSetModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed",
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
        instance_to_wrap: "StraightBevelDiffGearSetModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2548.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6964.StraightBevelDiffGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def straight_bevel_diff_gears_modal_analysis_at_a_speed(
        self: Self,
    ) -> "List[_5226.StraightBevelDiffGearModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.StraightBevelDiffGearModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearsModalAnalysisAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_meshes_modal_analysis_at_a_speed(
        self: Self,
    ) -> "List[_5225.StraightBevelDiffGearMeshModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.StraightBevelDiffGearMeshModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffMeshesModalAnalysisAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearSetModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed":
        return self._Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed(self)
