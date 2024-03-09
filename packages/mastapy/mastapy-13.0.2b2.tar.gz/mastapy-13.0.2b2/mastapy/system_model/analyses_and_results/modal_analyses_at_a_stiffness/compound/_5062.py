"""KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5056,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2542
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4933,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5022,
        _5048,
        _5067,
        _5015,
        _5069,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness",)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness",
)


class KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness(
    _5056.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness
):
    """KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness",
        ) -> (
            "_5056.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness"
        ):
            return self._parent._cast(
                _5056.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5022.ConicalGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5022,
            )

            return self._parent._cast(
                _5022.ConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_compound_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5048.GearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5048,
            )

            return self._parent._cast(_5048.GearCompoundModalAnalysisAtAStiffness)

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5067.MountableComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5067,
            )

            return self._parent._cast(
                _5067.MountableComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5015.ComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5015,
            )

            return self._parent._cast(_5015.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5069.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5069,
            )

            return self._parent._cast(_5069.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2542.KlingelnbergCycloPalloidSpiralBevelGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4933.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4933.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness(
            self
        )
