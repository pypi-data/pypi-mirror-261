"""AGMAGleasonConicalGearSetModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5153
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2516
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5132,
        _5137,
        _5183,
        _5221,
        _5227,
        _5230,
        _5248,
        _5179,
        _5218,
        _5119,
        _5199,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetModalAnalysisAtASpeed")


class AGMAGleasonConicalGearSetModalAnalysisAtASpeed(
    _5153.ConicalGearSetModalAnalysisAtASpeed
):
    """AGMAGleasonConicalGearSetModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed"
    )

    class _Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed:
        """Special nested class for casting AGMAGleasonConicalGearSetModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
            parent: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def conical_gear_set_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ) -> "_5153.ConicalGearSetModalAnalysisAtASpeed":
            return self._parent._cast(_5153.ConicalGearSetModalAnalysisAtASpeed)

        @property
        def gear_set_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ) -> "_5179.GearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5179,
            )

            return self._parent._cast(_5179.GearSetModalAnalysisAtASpeed)

        @property
        def specialised_assembly_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ) -> "_5218.SpecialisedAssemblyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5218,
            )

            return self._parent._cast(_5218.SpecialisedAssemblyModalAnalysisAtASpeed)

        @property
        def abstract_assembly_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ) -> "_5119.AbstractAssemblyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5119,
            )

            return self._parent._cast(_5119.AbstractAssemblyModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ) -> "_5199.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5199,
            )

            return self._parent._cast(_5199.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ) -> "_5132.BevelDifferentialGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5132,
            )

            return self._parent._cast(
                _5132.BevelDifferentialGearSetModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_set_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ) -> "_5137.BevelGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5137,
            )

            return self._parent._cast(_5137.BevelGearSetModalAnalysisAtASpeed)

        @property
        def hypoid_gear_set_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ) -> "_5183.HypoidGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5183,
            )

            return self._parent._cast(_5183.HypoidGearSetModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_set_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ) -> "_5221.SpiralBevelGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5221,
            )

            return self._parent._cast(_5221.SpiralBevelGearSetModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_set_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ) -> "_5227.StraightBevelDiffGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5227,
            )

            return self._parent._cast(
                _5227.StraightBevelDiffGearSetModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_set_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ) -> "_5230.StraightBevelGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5230,
            )

            return self._parent._cast(_5230.StraightBevelGearSetModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_set_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ) -> "_5248.ZerolBevelGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5248,
            )

            return self._parent._cast(_5248.ZerolBevelGearSetModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_set_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ) -> "AGMAGleasonConicalGearSetModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
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
        instance_to_wrap: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2516.AGMAGleasonConicalGearSet":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet

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
    ) -> "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed":
        return self._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed(self)
