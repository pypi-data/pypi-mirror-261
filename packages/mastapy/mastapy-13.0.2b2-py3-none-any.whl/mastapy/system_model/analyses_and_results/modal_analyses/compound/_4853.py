"""WormGearCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4788
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "WormGearCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2553
    from mastapy.system_model.analyses_and_results.modal_analyses import _4713
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4807,
        _4755,
        _4809,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("WormGearCompoundModalAnalysis",)


Self = TypeVar("Self", bound="WormGearCompoundModalAnalysis")


class WormGearCompoundModalAnalysis(_4788.GearCompoundModalAnalysis):
    """WormGearCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearCompoundModalAnalysis")

    class _Cast_WormGearCompoundModalAnalysis:
        """Special nested class for casting WormGearCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "WormGearCompoundModalAnalysis._Cast_WormGearCompoundModalAnalysis",
            parent: "WormGearCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def gear_compound_modal_analysis(
            self: "WormGearCompoundModalAnalysis._Cast_WormGearCompoundModalAnalysis",
        ) -> "_4788.GearCompoundModalAnalysis":
            return self._parent._cast(_4788.GearCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "WormGearCompoundModalAnalysis._Cast_WormGearCompoundModalAnalysis",
        ) -> "_4807.MountableComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4807,
            )

            return self._parent._cast(_4807.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "WormGearCompoundModalAnalysis._Cast_WormGearCompoundModalAnalysis",
        ) -> "_4755.ComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4755,
            )

            return self._parent._cast(_4755.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "WormGearCompoundModalAnalysis._Cast_WormGearCompoundModalAnalysis",
        ) -> "_4809.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4809,
            )

            return self._parent._cast(_4809.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "WormGearCompoundModalAnalysis._Cast_WormGearCompoundModalAnalysis",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "WormGearCompoundModalAnalysis._Cast_WormGearCompoundModalAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearCompoundModalAnalysis._Cast_WormGearCompoundModalAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def worm_gear_compound_modal_analysis(
            self: "WormGearCompoundModalAnalysis._Cast_WormGearCompoundModalAnalysis",
        ) -> "WormGearCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "WormGearCompoundModalAnalysis._Cast_WormGearCompoundModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGearCompoundModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2553.WormGear":
        """mastapy.system_model.part_model.gears.WormGear

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
    ) -> "List[_4713.WormGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.WormGearModalAnalysis]

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
    def component_analysis_cases(self: Self) -> "List[_4713.WormGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.WormGearModalAnalysis]

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
    ) -> "WormGearCompoundModalAnalysis._Cast_WormGearCompoundModalAnalysis":
        return self._Cast_WormGearCompoundModalAnalysis(self)
