"""FaceGearMeshModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4637
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "FaceGearMeshModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2313
    from mastapy.system_model.analyses_and_results.static_loads import _6888
    from mastapy.system_model.analyses_and_results.system_deflections import _2756
    from mastapy.system_model.analyses_and_results.modal_analyses import _4644, _4609
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543, _7540
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearMeshModalAnalysis",)


Self = TypeVar("Self", bound="FaceGearMeshModalAnalysis")


class FaceGearMeshModalAnalysis(_4637.GearMeshModalAnalysis):
    """FaceGearMeshModalAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MESH_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearMeshModalAnalysis")

    class _Cast_FaceGearMeshModalAnalysis:
        """Special nested class for casting FaceGearMeshModalAnalysis to subclasses."""

        def __init__(
            self: "FaceGearMeshModalAnalysis._Cast_FaceGearMeshModalAnalysis",
            parent: "FaceGearMeshModalAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_modal_analysis(
            self: "FaceGearMeshModalAnalysis._Cast_FaceGearMeshModalAnalysis",
        ) -> "_4637.GearMeshModalAnalysis":
            return self._parent._cast(_4637.GearMeshModalAnalysis)

        @property
        def inter_mountable_component_connection_modal_analysis(
            self: "FaceGearMeshModalAnalysis._Cast_FaceGearMeshModalAnalysis",
        ) -> "_4644.InterMountableComponentConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4644

            return self._parent._cast(
                _4644.InterMountableComponentConnectionModalAnalysis
            )

        @property
        def connection_modal_analysis(
            self: "FaceGearMeshModalAnalysis._Cast_FaceGearMeshModalAnalysis",
        ) -> "_4609.ConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4609

            return self._parent._cast(_4609.ConnectionModalAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "FaceGearMeshModalAnalysis._Cast_FaceGearMeshModalAnalysis",
        ) -> "_7543.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "FaceGearMeshModalAnalysis._Cast_FaceGearMeshModalAnalysis",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "FaceGearMeshModalAnalysis._Cast_FaceGearMeshModalAnalysis",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearMeshModalAnalysis._Cast_FaceGearMeshModalAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearMeshModalAnalysis._Cast_FaceGearMeshModalAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def face_gear_mesh_modal_analysis(
            self: "FaceGearMeshModalAnalysis._Cast_FaceGearMeshModalAnalysis",
        ) -> "FaceGearMeshModalAnalysis":
            return self._parent

        def __getattr__(
            self: "FaceGearMeshModalAnalysis._Cast_FaceGearMeshModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearMeshModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2313.FaceGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.FaceGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6888.FaceGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FaceGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2756.FaceGearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.FaceGearMeshSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "FaceGearMeshModalAnalysis._Cast_FaceGearMeshModalAnalysis":
        return self._Cast_FaceGearMeshModalAnalysis(self)
