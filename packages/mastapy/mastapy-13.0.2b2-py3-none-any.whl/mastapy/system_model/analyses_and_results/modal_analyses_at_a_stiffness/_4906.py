"""CylindricalGearMeshModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4918,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "CylindricalGearMeshModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2311
    from mastapy.system_model.analyses_and_results.static_loads import _6866
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4925,
        _4894,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543, _7540
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMeshModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="CylindricalGearMeshModalAnalysisAtAStiffness")


class CylindricalGearMeshModalAnalysisAtAStiffness(
    _4918.GearMeshModalAnalysisAtAStiffness
):
    """CylindricalGearMeshModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearMeshModalAnalysisAtAStiffness"
    )

    class _Cast_CylindricalGearMeshModalAnalysisAtAStiffness:
        """Special nested class for casting CylindricalGearMeshModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "CylindricalGearMeshModalAnalysisAtAStiffness._Cast_CylindricalGearMeshModalAnalysisAtAStiffness",
            parent: "CylindricalGearMeshModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def gear_mesh_modal_analysis_at_a_stiffness(
            self: "CylindricalGearMeshModalAnalysisAtAStiffness._Cast_CylindricalGearMeshModalAnalysisAtAStiffness",
        ) -> "_4918.GearMeshModalAnalysisAtAStiffness":
            return self._parent._cast(_4918.GearMeshModalAnalysisAtAStiffness)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "CylindricalGearMeshModalAnalysisAtAStiffness._Cast_CylindricalGearMeshModalAnalysisAtAStiffness",
        ) -> "_4925.InterMountableComponentConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4925,
            )

            return self._parent._cast(
                _4925.InterMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def connection_modal_analysis_at_a_stiffness(
            self: "CylindricalGearMeshModalAnalysisAtAStiffness._Cast_CylindricalGearMeshModalAnalysisAtAStiffness",
        ) -> "_4894.ConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4894,
            )

            return self._parent._cast(_4894.ConnectionModalAnalysisAtAStiffness)

        @property
        def connection_static_load_analysis_case(
            self: "CylindricalGearMeshModalAnalysisAtAStiffness._Cast_CylindricalGearMeshModalAnalysisAtAStiffness",
        ) -> "_7543.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CylindricalGearMeshModalAnalysisAtAStiffness._Cast_CylindricalGearMeshModalAnalysisAtAStiffness",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CylindricalGearMeshModalAnalysisAtAStiffness._Cast_CylindricalGearMeshModalAnalysisAtAStiffness",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearMeshModalAnalysisAtAStiffness._Cast_CylindricalGearMeshModalAnalysisAtAStiffness",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearMeshModalAnalysisAtAStiffness._Cast_CylindricalGearMeshModalAnalysisAtAStiffness",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cylindrical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "CylindricalGearMeshModalAnalysisAtAStiffness._Cast_CylindricalGearMeshModalAnalysisAtAStiffness",
        ) -> "CylindricalGearMeshModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMeshModalAnalysisAtAStiffness._Cast_CylindricalGearMeshModalAnalysisAtAStiffness",
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
        instance_to_wrap: "CylindricalGearMeshModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2311.CylindricalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6866.CylindricalGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[CylindricalGearMeshModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.CylindricalGearMeshModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearMeshModalAnalysisAtAStiffness._Cast_CylindricalGearMeshModalAnalysisAtAStiffness":
        return self._Cast_CylindricalGearMeshModalAnalysisAtAStiffness(self)
