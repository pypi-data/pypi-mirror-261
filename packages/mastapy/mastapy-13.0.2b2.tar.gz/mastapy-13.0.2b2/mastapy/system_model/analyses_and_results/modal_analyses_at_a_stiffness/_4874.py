"""BevelDifferentialSunGearModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4871,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "BevelDifferentialSunGearModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2520
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4876,
        _4864,
        _4892,
        _4919,
        _4938,
        _4884,
        _4940,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialSunGearModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="BevelDifferentialSunGearModalAnalysisAtAStiffness")


class BevelDifferentialSunGearModalAnalysisAtAStiffness(
    _4871.BevelDifferentialGearModalAnalysisAtAStiffness
):
    """BevelDifferentialSunGearModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness"
    )

    class _Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness:
        """Special nested class for casting BevelDifferentialSunGearModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "BevelDifferentialSunGearModalAnalysisAtAStiffness._Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness",
            parent: "BevelDifferentialSunGearModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialSunGearModalAnalysisAtAStiffness._Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness",
        ) -> "_4871.BevelDifferentialGearModalAnalysisAtAStiffness":
            return self._parent._cast(
                _4871.BevelDifferentialGearModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialSunGearModalAnalysisAtAStiffness._Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness",
        ) -> "_4876.BevelGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4876,
            )

            return self._parent._cast(_4876.BevelGearModalAnalysisAtAStiffness)

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialSunGearModalAnalysisAtAStiffness._Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness",
        ) -> "_4864.AGMAGleasonConicalGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4864,
            )

            return self._parent._cast(
                _4864.AGMAGleasonConicalGearModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialSunGearModalAnalysisAtAStiffness._Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness",
        ) -> "_4892.ConicalGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4892,
            )

            return self._parent._cast(_4892.ConicalGearModalAnalysisAtAStiffness)

        @property
        def gear_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialSunGearModalAnalysisAtAStiffness._Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness",
        ) -> "_4919.GearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4919,
            )

            return self._parent._cast(_4919.GearModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialSunGearModalAnalysisAtAStiffness._Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness",
        ) -> "_4938.MountableComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4938,
            )

            return self._parent._cast(_4938.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialSunGearModalAnalysisAtAStiffness._Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness",
        ) -> "_4884.ComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4884,
            )

            return self._parent._cast(_4884.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialSunGearModalAnalysisAtAStiffness._Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness",
        ) -> "_4940.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4940,
            )

            return self._parent._cast(_4940.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialSunGearModalAnalysisAtAStiffness._Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialSunGearModalAnalysisAtAStiffness._Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialSunGearModalAnalysisAtAStiffness._Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialSunGearModalAnalysisAtAStiffness._Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialSunGearModalAnalysisAtAStiffness._Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bevel_differential_sun_gear_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialSunGearModalAnalysisAtAStiffness._Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness",
        ) -> "BevelDifferentialSunGearModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialSunGearModalAnalysisAtAStiffness._Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness",
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
        instance_to_wrap: "BevelDifferentialSunGearModalAnalysisAtAStiffness.TYPE",
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
    ) -> "BevelDifferentialSunGearModalAnalysisAtAStiffness._Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness":
        return self._Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness(self)
