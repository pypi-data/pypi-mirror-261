"""ZerolBevelGearSetCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5008,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "ZerolBevelGearSetCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2556
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4989,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5116,
        _5117,
        _4996,
        _5024,
        _5050,
        _5088,
        _4990,
        _5069,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearSetCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="ZerolBevelGearSetCompoundModalAnalysisAtAStiffness")


class ZerolBevelGearSetCompoundModalAnalysisAtAStiffness(
    _5008.BevelGearSetCompoundModalAnalysisAtAStiffness
):
    """ZerolBevelGearSetCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ZerolBevelGearSetCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_ZerolBevelGearSetCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting ZerolBevelGearSetCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "ZerolBevelGearSetCompoundModalAnalysisAtAStiffness._Cast_ZerolBevelGearSetCompoundModalAnalysisAtAStiffness",
            parent: "ZerolBevelGearSetCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "ZerolBevelGearSetCompoundModalAnalysisAtAStiffness._Cast_ZerolBevelGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_5008.BevelGearSetCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(
                _5008.BevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "ZerolBevelGearSetCompoundModalAnalysisAtAStiffness._Cast_ZerolBevelGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_4996.AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4996,
            )

            return self._parent._cast(
                _4996.AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "ZerolBevelGearSetCompoundModalAnalysisAtAStiffness._Cast_ZerolBevelGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_5024.ConicalGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5024,
            )

            return self._parent._cast(
                _5024.ConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_set_compound_modal_analysis_at_a_stiffness(
            self: "ZerolBevelGearSetCompoundModalAnalysisAtAStiffness._Cast_ZerolBevelGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_5050.GearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5050,
            )

            return self._parent._cast(_5050.GearSetCompoundModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_stiffness(
            self: "ZerolBevelGearSetCompoundModalAnalysisAtAStiffness._Cast_ZerolBevelGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_5088.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5088,
            )

            return self._parent._cast(
                _5088.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_stiffness(
            self: "ZerolBevelGearSetCompoundModalAnalysisAtAStiffness._Cast_ZerolBevelGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_4990.AbstractAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4990,
            )

            return self._parent._cast(
                _4990.AbstractAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "ZerolBevelGearSetCompoundModalAnalysisAtAStiffness._Cast_ZerolBevelGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_5069.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5069,
            )

            return self._parent._cast(_5069.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "ZerolBevelGearSetCompoundModalAnalysisAtAStiffness._Cast_ZerolBevelGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ZerolBevelGearSetCompoundModalAnalysisAtAStiffness._Cast_ZerolBevelGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearSetCompoundModalAnalysisAtAStiffness._Cast_ZerolBevelGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "ZerolBevelGearSetCompoundModalAnalysisAtAStiffness._Cast_ZerolBevelGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "ZerolBevelGearSetCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearSetCompoundModalAnalysisAtAStiffness._Cast_ZerolBevelGearSetCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "ZerolBevelGearSetCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2556.ZerolBevelGearSet":
        """mastapy.system_model.part_model.gears.ZerolBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2556.ZerolBevelGearSet":
        """mastapy.system_model.part_model.gears.ZerolBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4989.ZerolBevelGearSetModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.ZerolBevelGearSetModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_gears_compound_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_5116.ZerolBevelGearCompoundModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound.ZerolBevelGearCompoundModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearsCompoundModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_meshes_compound_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_5117.ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound.ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelMeshesCompoundModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4989.ZerolBevelGearSetModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.ZerolBevelGearSetModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ZerolBevelGearSetCompoundModalAnalysisAtAStiffness._Cast_ZerolBevelGearSetCompoundModalAnalysisAtAStiffness":
        return self._Cast_ZerolBevelGearSetCompoundModalAnalysisAtAStiffness(self)
