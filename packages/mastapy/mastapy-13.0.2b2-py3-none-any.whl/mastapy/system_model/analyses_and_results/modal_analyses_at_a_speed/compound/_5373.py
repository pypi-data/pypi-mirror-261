"""WormGearMeshCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5308,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "WormGearMeshCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2331
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5243,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5314,
        _5284,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("WormGearMeshCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="WormGearMeshCompoundModalAnalysisAtASpeed")


class WormGearMeshCompoundModalAnalysisAtASpeed(
    _5308.GearMeshCompoundModalAnalysisAtASpeed
):
    """WormGearMeshCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_WormGearMeshCompoundModalAnalysisAtASpeed"
    )

    class _Cast_WormGearMeshCompoundModalAnalysisAtASpeed:
        """Special nested class for casting WormGearMeshCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "WormGearMeshCompoundModalAnalysisAtASpeed._Cast_WormGearMeshCompoundModalAnalysisAtASpeed",
            parent: "WormGearMeshCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_modal_analysis_at_a_speed(
            self: "WormGearMeshCompoundModalAnalysisAtASpeed._Cast_WormGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5308.GearMeshCompoundModalAnalysisAtASpeed":
            return self._parent._cast(_5308.GearMeshCompoundModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "WormGearMeshCompoundModalAnalysisAtASpeed._Cast_WormGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5314.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5314,
            )

            return self._parent._cast(
                _5314.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def connection_compound_modal_analysis_at_a_speed(
            self: "WormGearMeshCompoundModalAnalysisAtASpeed._Cast_WormGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5284.ConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5284,
            )

            return self._parent._cast(_5284.ConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_analysis(
            self: "WormGearMeshCompoundModalAnalysisAtASpeed._Cast_WormGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_7541.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "WormGearMeshCompoundModalAnalysisAtASpeed._Cast_WormGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearMeshCompoundModalAnalysisAtASpeed._Cast_WormGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def worm_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "WormGearMeshCompoundModalAnalysisAtASpeed._Cast_WormGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "WormGearMeshCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "WormGearMeshCompoundModalAnalysisAtASpeed._Cast_WormGearMeshCompoundModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "WormGearMeshCompoundModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2331.WormGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.WormGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2331.WormGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.WormGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5243.WormGearMeshModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.WormGearMeshModalAnalysisAtASpeed]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5243.WormGearMeshModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.WormGearMeshModalAnalysisAtASpeed]

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
    def cast_to(
        self: Self,
    ) -> "WormGearMeshCompoundModalAnalysisAtASpeed._Cast_WormGearMeshCompoundModalAnalysisAtASpeed":
        return self._Cast_WormGearMeshCompoundModalAnalysisAtASpeed(self)
