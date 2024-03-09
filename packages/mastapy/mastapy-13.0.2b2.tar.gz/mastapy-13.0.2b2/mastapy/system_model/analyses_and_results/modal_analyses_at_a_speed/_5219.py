"""SpiralBevelGearMeshModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5135
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "SpiralBevelGearMeshModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2325
    from mastapy.system_model.analyses_and_results.static_loads import _6957
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5123,
        _5151,
        _5177,
        _5184,
        _5154,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543, _7540
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMeshModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="SpiralBevelGearMeshModalAnalysisAtASpeed")


class SpiralBevelGearMeshModalAnalysisAtASpeed(
    _5135.BevelGearMeshModalAnalysisAtASpeed
):
    """SpiralBevelGearMeshModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearMeshModalAnalysisAtASpeed"
    )

    class _Cast_SpiralBevelGearMeshModalAnalysisAtASpeed:
        """Special nested class for casting SpiralBevelGearMeshModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "SpiralBevelGearMeshModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshModalAnalysisAtASpeed",
            parent: "SpiralBevelGearMeshModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "SpiralBevelGearMeshModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshModalAnalysisAtASpeed",
        ) -> "_5135.BevelGearMeshModalAnalysisAtASpeed":
            return self._parent._cast(_5135.BevelGearMeshModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_speed(
            self: "SpiralBevelGearMeshModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshModalAnalysisAtASpeed",
        ) -> "_5123.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5123,
            )

            return self._parent._cast(
                _5123.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed
            )

        @property
        def conical_gear_mesh_modal_analysis_at_a_speed(
            self: "SpiralBevelGearMeshModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshModalAnalysisAtASpeed",
        ) -> "_5151.ConicalGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5151,
            )

            return self._parent._cast(_5151.ConicalGearMeshModalAnalysisAtASpeed)

        @property
        def gear_mesh_modal_analysis_at_a_speed(
            self: "SpiralBevelGearMeshModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshModalAnalysisAtASpeed",
        ) -> "_5177.GearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5177,
            )

            return self._parent._cast(_5177.GearMeshModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_speed(
            self: "SpiralBevelGearMeshModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshModalAnalysisAtASpeed",
        ) -> "_5184.InterMountableComponentConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5184,
            )

            return self._parent._cast(
                _5184.InterMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def connection_modal_analysis_at_a_speed(
            self: "SpiralBevelGearMeshModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshModalAnalysisAtASpeed",
        ) -> "_5154.ConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5154,
            )

            return self._parent._cast(_5154.ConnectionModalAnalysisAtASpeed)

        @property
        def connection_static_load_analysis_case(
            self: "SpiralBevelGearMeshModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshModalAnalysisAtASpeed",
        ) -> "_7543.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "SpiralBevelGearMeshModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshModalAnalysisAtASpeed",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "SpiralBevelGearMeshModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshModalAnalysisAtASpeed",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearMeshModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshModalAnalysisAtASpeed",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearMeshModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshModalAnalysisAtASpeed",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "SpiralBevelGearMeshModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshModalAnalysisAtASpeed",
        ) -> "SpiralBevelGearMeshModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearMeshModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "SpiralBevelGearMeshModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2325.SpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6957.SpiralBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearMeshModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshModalAnalysisAtASpeed":
        return self._Cast_SpiralBevelGearMeshModalAnalysisAtASpeed(self)
