"""BevelDifferentialSunGearModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5131
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "BevelDifferentialSunGearModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2520
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5136,
        _5124,
        _5152,
        _5178,
        _5197,
        _5144,
        _5199,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialSunGearModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="BevelDifferentialSunGearModalAnalysisAtASpeed")


class BevelDifferentialSunGearModalAnalysisAtASpeed(
    _5131.BevelDifferentialGearModalAnalysisAtASpeed
):
    """BevelDifferentialSunGearModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialSunGearModalAnalysisAtASpeed"
    )

    class _Cast_BevelDifferentialSunGearModalAnalysisAtASpeed:
        """Special nested class for casting BevelDifferentialSunGearModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "BevelDifferentialSunGearModalAnalysisAtASpeed._Cast_BevelDifferentialSunGearModalAnalysisAtASpeed",
            parent: "BevelDifferentialSunGearModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_modal_analysis_at_a_speed(
            self: "BevelDifferentialSunGearModalAnalysisAtASpeed._Cast_BevelDifferentialSunGearModalAnalysisAtASpeed",
        ) -> "_5131.BevelDifferentialGearModalAnalysisAtASpeed":
            return self._parent._cast(_5131.BevelDifferentialGearModalAnalysisAtASpeed)

        @property
        def bevel_gear_modal_analysis_at_a_speed(
            self: "BevelDifferentialSunGearModalAnalysisAtASpeed._Cast_BevelDifferentialSunGearModalAnalysisAtASpeed",
        ) -> "_5136.BevelGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5136,
            )

            return self._parent._cast(_5136.BevelGearModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_speed(
            self: "BevelDifferentialSunGearModalAnalysisAtASpeed._Cast_BevelDifferentialSunGearModalAnalysisAtASpeed",
        ) -> "_5124.AGMAGleasonConicalGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5124,
            )

            return self._parent._cast(_5124.AGMAGleasonConicalGearModalAnalysisAtASpeed)

        @property
        def conical_gear_modal_analysis_at_a_speed(
            self: "BevelDifferentialSunGearModalAnalysisAtASpeed._Cast_BevelDifferentialSunGearModalAnalysisAtASpeed",
        ) -> "_5152.ConicalGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5152,
            )

            return self._parent._cast(_5152.ConicalGearModalAnalysisAtASpeed)

        @property
        def gear_modal_analysis_at_a_speed(
            self: "BevelDifferentialSunGearModalAnalysisAtASpeed._Cast_BevelDifferentialSunGearModalAnalysisAtASpeed",
        ) -> "_5178.GearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5178,
            )

            return self._parent._cast(_5178.GearModalAnalysisAtASpeed)

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "BevelDifferentialSunGearModalAnalysisAtASpeed._Cast_BevelDifferentialSunGearModalAnalysisAtASpeed",
        ) -> "_5197.MountableComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5197,
            )

            return self._parent._cast(_5197.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "BevelDifferentialSunGearModalAnalysisAtASpeed._Cast_BevelDifferentialSunGearModalAnalysisAtASpeed",
        ) -> "_5144.ComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5144,
            )

            return self._parent._cast(_5144.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "BevelDifferentialSunGearModalAnalysisAtASpeed._Cast_BevelDifferentialSunGearModalAnalysisAtASpeed",
        ) -> "_5199.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5199,
            )

            return self._parent._cast(_5199.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialSunGearModalAnalysisAtASpeed._Cast_BevelDifferentialSunGearModalAnalysisAtASpeed",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialSunGearModalAnalysisAtASpeed._Cast_BevelDifferentialSunGearModalAnalysisAtASpeed",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialSunGearModalAnalysisAtASpeed._Cast_BevelDifferentialSunGearModalAnalysisAtASpeed",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialSunGearModalAnalysisAtASpeed._Cast_BevelDifferentialSunGearModalAnalysisAtASpeed",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialSunGearModalAnalysisAtASpeed._Cast_BevelDifferentialSunGearModalAnalysisAtASpeed",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bevel_differential_sun_gear_modal_analysis_at_a_speed(
            self: "BevelDifferentialSunGearModalAnalysisAtASpeed._Cast_BevelDifferentialSunGearModalAnalysisAtASpeed",
        ) -> "BevelDifferentialSunGearModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialSunGearModalAnalysisAtASpeed._Cast_BevelDifferentialSunGearModalAnalysisAtASpeed",
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
        instance_to_wrap: "BevelDifferentialSunGearModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2520.BevelDifferentialSunGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialSunGear

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
    ) -> "BevelDifferentialSunGearModalAnalysisAtASpeed._Cast_BevelDifferentialSunGearModalAnalysisAtASpeed":
        return self._Cast_BevelDifferentialSunGearModalAnalysisAtASpeed(self)
