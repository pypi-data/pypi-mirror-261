"""GearMeshCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5055,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "GearMeshCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4918,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _4995,
        _5002,
        _5007,
        _5020,
        _5023,
        _5038,
        _5044,
        _5053,
        _5057,
        _5060,
        _5063,
        _5090,
        _5096,
        _5099,
        _5114,
        _5117,
        _5025,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="GearMeshCompoundModalAnalysisAtAStiffness")


class GearMeshCompoundModalAnalysisAtAStiffness(
    _5055.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness
):
    """GearMeshCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearMeshCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_GearMeshCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting GearMeshCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "GearMeshCompoundModalAnalysisAtAStiffness._Cast_GearMeshCompoundModalAnalysisAtAStiffness",
            parent: "GearMeshCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "GearMeshCompoundModalAnalysisAtAStiffness._Cast_GearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5055.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(
                _5055.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def connection_compound_modal_analysis_at_a_stiffness(
            self: "GearMeshCompoundModalAnalysisAtAStiffness._Cast_GearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5025.ConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5025,
            )

            return self._parent._cast(_5025.ConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def connection_compound_analysis(
            self: "GearMeshCompoundModalAnalysisAtAStiffness._Cast_GearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_7541.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearMeshCompoundModalAnalysisAtAStiffness._Cast_GearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshCompoundModalAnalysisAtAStiffness._Cast_GearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "GearMeshCompoundModalAnalysisAtAStiffness._Cast_GearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_4995.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4995,
            )

            return self._parent._cast(
                _4995.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "GearMeshCompoundModalAnalysisAtAStiffness._Cast_GearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5002.BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5002,
            )

            return self._parent._cast(
                _5002.BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "GearMeshCompoundModalAnalysisAtAStiffness._Cast_GearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5007.BevelGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5007,
            )

            return self._parent._cast(
                _5007.BevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "GearMeshCompoundModalAnalysisAtAStiffness._Cast_GearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5020.ConceptGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5020,
            )

            return self._parent._cast(
                _5020.ConceptGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "GearMeshCompoundModalAnalysisAtAStiffness._Cast_GearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5023.ConicalGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5023,
            )

            return self._parent._cast(
                _5023.ConicalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "GearMeshCompoundModalAnalysisAtAStiffness._Cast_GearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5038.CylindricalGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5038,
            )

            return self._parent._cast(
                _5038.CylindricalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def face_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "GearMeshCompoundModalAnalysisAtAStiffness._Cast_GearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5044.FaceGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5044,
            )

            return self._parent._cast(
                _5044.FaceGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def hypoid_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "GearMeshCompoundModalAnalysisAtAStiffness._Cast_GearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5053.HypoidGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5053,
            )

            return self._parent._cast(
                _5053.HypoidGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "GearMeshCompoundModalAnalysisAtAStiffness._Cast_GearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5057.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5057,
            )

            return self._parent._cast(
                _5057.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "GearMeshCompoundModalAnalysisAtAStiffness._Cast_GearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5060.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5060,
            )

            return self._parent._cast(
                _5060.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "GearMeshCompoundModalAnalysisAtAStiffness._Cast_GearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5063.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5063,
            )

            return self._parent._cast(
                _5063.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "GearMeshCompoundModalAnalysisAtAStiffness._Cast_GearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5090.SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5090,
            )

            return self._parent._cast(
                _5090.SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "GearMeshCompoundModalAnalysisAtAStiffness._Cast_GearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5096.StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5096,
            )

            return self._parent._cast(
                _5096.StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "GearMeshCompoundModalAnalysisAtAStiffness._Cast_GearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5099.StraightBevelGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5099,
            )

            return self._parent._cast(
                _5099.StraightBevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def worm_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "GearMeshCompoundModalAnalysisAtAStiffness._Cast_GearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5114.WormGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5114,
            )

            return self._parent._cast(
                _5114.WormGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "GearMeshCompoundModalAnalysisAtAStiffness._Cast_GearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5117.ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5117,
            )

            return self._parent._cast(
                _5117.ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "GearMeshCompoundModalAnalysisAtAStiffness._Cast_GearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "GearMeshCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "GearMeshCompoundModalAnalysisAtAStiffness._Cast_GearMeshCompoundModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "GearMeshCompoundModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4918.GearMeshModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.GearMeshModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4918.GearMeshModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.GearMeshModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "GearMeshCompoundModalAnalysisAtAStiffness._Cast_GearMeshCompoundModalAnalysisAtAStiffness":
        return self._Cast_GearMeshCompoundModalAnalysisAtAStiffness(self)
