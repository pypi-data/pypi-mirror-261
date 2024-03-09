"""GearCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4807
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "GearCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4638
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4734,
        _4741,
        _4744,
        _4745,
        _4746,
        _4759,
        _4762,
        _4777,
        _4780,
        _4783,
        _4792,
        _4796,
        _4799,
        _4802,
        _4829,
        _4835,
        _4838,
        _4841,
        _4842,
        _4853,
        _4856,
        _4755,
        _4809,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("GearCompoundModalAnalysis",)


Self = TypeVar("Self", bound="GearCompoundModalAnalysis")


class GearCompoundModalAnalysis(_4807.MountableComponentCompoundModalAnalysis):
    """GearCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearCompoundModalAnalysis")

    class _Cast_GearCompoundModalAnalysis:
        """Special nested class for casting GearCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "GearCompoundModalAnalysis._Cast_GearCompoundModalAnalysis",
            parent: "GearCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_modal_analysis(
            self: "GearCompoundModalAnalysis._Cast_GearCompoundModalAnalysis",
        ) -> "_4807.MountableComponentCompoundModalAnalysis":
            return self._parent._cast(_4807.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "GearCompoundModalAnalysis._Cast_GearCompoundModalAnalysis",
        ) -> "_4755.ComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4755,
            )

            return self._parent._cast(_4755.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "GearCompoundModalAnalysis._Cast_GearCompoundModalAnalysis",
        ) -> "_4809.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4809,
            )

            return self._parent._cast(_4809.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "GearCompoundModalAnalysis._Cast_GearCompoundModalAnalysis",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearCompoundModalAnalysis._Cast_GearCompoundModalAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearCompoundModalAnalysis._Cast_GearCompoundModalAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis(
            self: "GearCompoundModalAnalysis._Cast_GearCompoundModalAnalysis",
        ) -> "_4734.AGMAGleasonConicalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4734,
            )

            return self._parent._cast(_4734.AGMAGleasonConicalGearCompoundModalAnalysis)

        @property
        def bevel_differential_gear_compound_modal_analysis(
            self: "GearCompoundModalAnalysis._Cast_GearCompoundModalAnalysis",
        ) -> "_4741.BevelDifferentialGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4741,
            )

            return self._parent._cast(_4741.BevelDifferentialGearCompoundModalAnalysis)

        @property
        def bevel_differential_planet_gear_compound_modal_analysis(
            self: "GearCompoundModalAnalysis._Cast_GearCompoundModalAnalysis",
        ) -> "_4744.BevelDifferentialPlanetGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4744,
            )

            return self._parent._cast(
                _4744.BevelDifferentialPlanetGearCompoundModalAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis(
            self: "GearCompoundModalAnalysis._Cast_GearCompoundModalAnalysis",
        ) -> "_4745.BevelDifferentialSunGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4745,
            )

            return self._parent._cast(
                _4745.BevelDifferentialSunGearCompoundModalAnalysis
            )

        @property
        def bevel_gear_compound_modal_analysis(
            self: "GearCompoundModalAnalysis._Cast_GearCompoundModalAnalysis",
        ) -> "_4746.BevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4746,
            )

            return self._parent._cast(_4746.BevelGearCompoundModalAnalysis)

        @property
        def concept_gear_compound_modal_analysis(
            self: "GearCompoundModalAnalysis._Cast_GearCompoundModalAnalysis",
        ) -> "_4759.ConceptGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4759,
            )

            return self._parent._cast(_4759.ConceptGearCompoundModalAnalysis)

        @property
        def conical_gear_compound_modal_analysis(
            self: "GearCompoundModalAnalysis._Cast_GearCompoundModalAnalysis",
        ) -> "_4762.ConicalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4762,
            )

            return self._parent._cast(_4762.ConicalGearCompoundModalAnalysis)

        @property
        def cylindrical_gear_compound_modal_analysis(
            self: "GearCompoundModalAnalysis._Cast_GearCompoundModalAnalysis",
        ) -> "_4777.CylindricalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4777,
            )

            return self._parent._cast(_4777.CylindricalGearCompoundModalAnalysis)

        @property
        def cylindrical_planet_gear_compound_modal_analysis(
            self: "GearCompoundModalAnalysis._Cast_GearCompoundModalAnalysis",
        ) -> "_4780.CylindricalPlanetGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4780,
            )

            return self._parent._cast(_4780.CylindricalPlanetGearCompoundModalAnalysis)

        @property
        def face_gear_compound_modal_analysis(
            self: "GearCompoundModalAnalysis._Cast_GearCompoundModalAnalysis",
        ) -> "_4783.FaceGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4783,
            )

            return self._parent._cast(_4783.FaceGearCompoundModalAnalysis)

        @property
        def hypoid_gear_compound_modal_analysis(
            self: "GearCompoundModalAnalysis._Cast_GearCompoundModalAnalysis",
        ) -> "_4792.HypoidGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4792,
            )

            return self._parent._cast(_4792.HypoidGearCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis(
            self: "GearCompoundModalAnalysis._Cast_GearCompoundModalAnalysis",
        ) -> "_4796.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4796,
            )

            return self._parent._cast(
                _4796.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis(
            self: "GearCompoundModalAnalysis._Cast_GearCompoundModalAnalysis",
        ) -> "_4799.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4799,
            )

            return self._parent._cast(
                _4799.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis(
            self: "GearCompoundModalAnalysis._Cast_GearCompoundModalAnalysis",
        ) -> "_4802.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4802,
            )

            return self._parent._cast(
                _4802.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis
            )

        @property
        def spiral_bevel_gear_compound_modal_analysis(
            self: "GearCompoundModalAnalysis._Cast_GearCompoundModalAnalysis",
        ) -> "_4829.SpiralBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4829,
            )

            return self._parent._cast(_4829.SpiralBevelGearCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_compound_modal_analysis(
            self: "GearCompoundModalAnalysis._Cast_GearCompoundModalAnalysis",
        ) -> "_4835.StraightBevelDiffGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4835,
            )

            return self._parent._cast(_4835.StraightBevelDiffGearCompoundModalAnalysis)

        @property
        def straight_bevel_gear_compound_modal_analysis(
            self: "GearCompoundModalAnalysis._Cast_GearCompoundModalAnalysis",
        ) -> "_4838.StraightBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4838,
            )

            return self._parent._cast(_4838.StraightBevelGearCompoundModalAnalysis)

        @property
        def straight_bevel_planet_gear_compound_modal_analysis(
            self: "GearCompoundModalAnalysis._Cast_GearCompoundModalAnalysis",
        ) -> "_4841.StraightBevelPlanetGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4841,
            )

            return self._parent._cast(
                _4841.StraightBevelPlanetGearCompoundModalAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis(
            self: "GearCompoundModalAnalysis._Cast_GearCompoundModalAnalysis",
        ) -> "_4842.StraightBevelSunGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4842,
            )

            return self._parent._cast(_4842.StraightBevelSunGearCompoundModalAnalysis)

        @property
        def worm_gear_compound_modal_analysis(
            self: "GearCompoundModalAnalysis._Cast_GearCompoundModalAnalysis",
        ) -> "_4853.WormGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4853,
            )

            return self._parent._cast(_4853.WormGearCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_compound_modal_analysis(
            self: "GearCompoundModalAnalysis._Cast_GearCompoundModalAnalysis",
        ) -> "_4856.ZerolBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4856,
            )

            return self._parent._cast(_4856.ZerolBevelGearCompoundModalAnalysis)

        @property
        def gear_compound_modal_analysis(
            self: "GearCompoundModalAnalysis._Cast_GearCompoundModalAnalysis",
        ) -> "GearCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "GearCompoundModalAnalysis._Cast_GearCompoundModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearCompoundModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_4638.GearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.GearModalAnalysis]

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
    def component_analysis_cases_ready(self: Self) -> "List[_4638.GearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.GearModalAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "GearCompoundModalAnalysis._Cast_GearCompoundModalAnalysis":
        return self._Cast_GearCompoundModalAnalysis(self)
