"""SpiralBevelGearSetModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4877,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "SpiralBevelGearSetModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2546
    from mastapy.system_model.analyses_and_results.static_loads import _6958
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4961,
        _4960,
        _4865,
        _4893,
        _4920,
        _4959,
        _4859,
        _4940,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearSetModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="SpiralBevelGearSetModalAnalysisAtAStiffness")


class SpiralBevelGearSetModalAnalysisAtAStiffness(
    _4877.BevelGearSetModalAnalysisAtAStiffness
):
    """SpiralBevelGearSetModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearSetModalAnalysisAtAStiffness"
    )

    class _Cast_SpiralBevelGearSetModalAnalysisAtAStiffness:
        """Special nested class for casting SpiralBevelGearSetModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "SpiralBevelGearSetModalAnalysisAtAStiffness._Cast_SpiralBevelGearSetModalAnalysisAtAStiffness",
            parent: "SpiralBevelGearSetModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "SpiralBevelGearSetModalAnalysisAtAStiffness._Cast_SpiralBevelGearSetModalAnalysisAtAStiffness",
        ) -> "_4877.BevelGearSetModalAnalysisAtAStiffness":
            return self._parent._cast(_4877.BevelGearSetModalAnalysisAtAStiffness)

        @property
        def agma_gleason_conical_gear_set_modal_analysis_at_a_stiffness(
            self: "SpiralBevelGearSetModalAnalysisAtAStiffness._Cast_SpiralBevelGearSetModalAnalysisAtAStiffness",
        ) -> "_4865.AGMAGleasonConicalGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4865,
            )

            return self._parent._cast(
                _4865.AGMAGleasonConicalGearSetModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_set_modal_analysis_at_a_stiffness(
            self: "SpiralBevelGearSetModalAnalysisAtAStiffness._Cast_SpiralBevelGearSetModalAnalysisAtAStiffness",
        ) -> "_4893.ConicalGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4893,
            )

            return self._parent._cast(_4893.ConicalGearSetModalAnalysisAtAStiffness)

        @property
        def gear_set_modal_analysis_at_a_stiffness(
            self: "SpiralBevelGearSetModalAnalysisAtAStiffness._Cast_SpiralBevelGearSetModalAnalysisAtAStiffness",
        ) -> "_4920.GearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4920,
            )

            return self._parent._cast(_4920.GearSetModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(
            self: "SpiralBevelGearSetModalAnalysisAtAStiffness._Cast_SpiralBevelGearSetModalAnalysisAtAStiffness",
        ) -> "_4959.SpecialisedAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4959,
            )

            return self._parent._cast(
                _4959.SpecialisedAssemblyModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "SpiralBevelGearSetModalAnalysisAtAStiffness._Cast_SpiralBevelGearSetModalAnalysisAtAStiffness",
        ) -> "_4859.AbstractAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4859,
            )

            return self._parent._cast(_4859.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "SpiralBevelGearSetModalAnalysisAtAStiffness._Cast_SpiralBevelGearSetModalAnalysisAtAStiffness",
        ) -> "_4940.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4940,
            )

            return self._parent._cast(_4940.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "SpiralBevelGearSetModalAnalysisAtAStiffness._Cast_SpiralBevelGearSetModalAnalysisAtAStiffness",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpiralBevelGearSetModalAnalysisAtAStiffness._Cast_SpiralBevelGearSetModalAnalysisAtAStiffness",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpiralBevelGearSetModalAnalysisAtAStiffness._Cast_SpiralBevelGearSetModalAnalysisAtAStiffness",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearSetModalAnalysisAtAStiffness._Cast_SpiralBevelGearSetModalAnalysisAtAStiffness",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearSetModalAnalysisAtAStiffness._Cast_SpiralBevelGearSetModalAnalysisAtAStiffness",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "SpiralBevelGearSetModalAnalysisAtAStiffness._Cast_SpiralBevelGearSetModalAnalysisAtAStiffness",
        ) -> "SpiralBevelGearSetModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearSetModalAnalysisAtAStiffness._Cast_SpiralBevelGearSetModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "SpiralBevelGearSetModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2546.SpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.SpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6958.SpiralBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def spiral_bevel_gears_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_4961.SpiralBevelGearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.SpiralBevelGearModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelGearsModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_meshes_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_4960.SpiralBevelGearMeshModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.SpiralBevelGearMeshModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelMeshesModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearSetModalAnalysisAtAStiffness._Cast_SpiralBevelGearSetModalAnalysisAtAStiffness":
        return self._Cast_SpiralBevelGearSetModalAnalysisAtAStiffness(self)
