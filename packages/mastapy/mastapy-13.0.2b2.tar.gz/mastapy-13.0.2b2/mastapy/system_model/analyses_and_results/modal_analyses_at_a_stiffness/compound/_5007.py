"""BevelGearMeshCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _4995,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "BevelGearMeshCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4875,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5002,
        _5090,
        _5096,
        _5099,
        _5117,
        _5023,
        _5049,
        _5055,
        _5025,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="BevelGearMeshCompoundModalAnalysisAtAStiffness")


class BevelGearMeshCompoundModalAnalysisAtAStiffness(
    _4995.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness
):
    """BevelGearMeshCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearMeshCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_BevelGearMeshCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting BevelGearMeshCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "BevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_BevelGearMeshCompoundModalAnalysisAtAStiffness",
            parent: "BevelGearMeshCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_BevelGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_4995.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(
                _4995.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_BevelGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5023.ConicalGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5023,
            )

            return self._parent._cast(
                _5023.ConicalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_BevelGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5049.GearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5049,
            )

            return self._parent._cast(_5049.GearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_BevelGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5055.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5055,
            )

            return self._parent._cast(
                _5055.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def connection_compound_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_BevelGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5025.ConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5025,
            )

            return self._parent._cast(_5025.ConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def connection_compound_analysis(
            self: "BevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_BevelGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_7541.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_BevelGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_BevelGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_BevelGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5002.BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5002,
            )

            return self._parent._cast(
                _5002.BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_BevelGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5090.SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5090,
            )

            return self._parent._cast(
                _5090.SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_BevelGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5096.StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5096,
            )

            return self._parent._cast(
                _5096.StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_BevelGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5099.StraightBevelGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5099,
            )

            return self._parent._cast(
                _5099.StraightBevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_BevelGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5117.ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5117,
            )

            return self._parent._cast(
                _5117.ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_BevelGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "BevelGearMeshCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_BevelGearMeshCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "BevelGearMeshCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4875.BevelGearMeshModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.BevelGearMeshModalAnalysisAtAStiffness]

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
    ) -> "List[_4875.BevelGearMeshModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.BevelGearMeshModalAnalysisAtAStiffness]

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
    ) -> "BevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_BevelGearMeshCompoundModalAnalysisAtAStiffness":
        return self._Cast_BevelGearMeshCompoundModalAnalysisAtAStiffness(self)
