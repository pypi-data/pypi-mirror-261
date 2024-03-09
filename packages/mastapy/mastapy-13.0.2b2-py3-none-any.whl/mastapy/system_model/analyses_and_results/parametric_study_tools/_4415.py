"""SpiralBevelGearMeshParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4314
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "SpiralBevelGearMeshParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2325
    from mastapy.system_model.analyses_and_results.static_loads import _6957
    from mastapy.system_model.analyses_and_results.system_deflections import _2809
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4302,
        _4330,
        _4363,
        _4370,
        _4333,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7540
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMeshParametricStudyTool",)


Self = TypeVar("Self", bound="SpiralBevelGearMeshParametricStudyTool")


class SpiralBevelGearMeshParametricStudyTool(_4314.BevelGearMeshParametricStudyTool):
    """SpiralBevelGearMeshParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearMeshParametricStudyTool"
    )

    class _Cast_SpiralBevelGearMeshParametricStudyTool:
        """Special nested class for casting SpiralBevelGearMeshParametricStudyTool to subclasses."""

        def __init__(
            self: "SpiralBevelGearMeshParametricStudyTool._Cast_SpiralBevelGearMeshParametricStudyTool",
            parent: "SpiralBevelGearMeshParametricStudyTool",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_parametric_study_tool(
            self: "SpiralBevelGearMeshParametricStudyTool._Cast_SpiralBevelGearMeshParametricStudyTool",
        ) -> "_4314.BevelGearMeshParametricStudyTool":
            return self._parent._cast(_4314.BevelGearMeshParametricStudyTool)

        @property
        def agma_gleason_conical_gear_mesh_parametric_study_tool(
            self: "SpiralBevelGearMeshParametricStudyTool._Cast_SpiralBevelGearMeshParametricStudyTool",
        ) -> "_4302.AGMAGleasonConicalGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4302,
            )

            return self._parent._cast(
                _4302.AGMAGleasonConicalGearMeshParametricStudyTool
            )

        @property
        def conical_gear_mesh_parametric_study_tool(
            self: "SpiralBevelGearMeshParametricStudyTool._Cast_SpiralBevelGearMeshParametricStudyTool",
        ) -> "_4330.ConicalGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4330,
            )

            return self._parent._cast(_4330.ConicalGearMeshParametricStudyTool)

        @property
        def gear_mesh_parametric_study_tool(
            self: "SpiralBevelGearMeshParametricStudyTool._Cast_SpiralBevelGearMeshParametricStudyTool",
        ) -> "_4363.GearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4363,
            )

            return self._parent._cast(_4363.GearMeshParametricStudyTool)

        @property
        def inter_mountable_component_connection_parametric_study_tool(
            self: "SpiralBevelGearMeshParametricStudyTool._Cast_SpiralBevelGearMeshParametricStudyTool",
        ) -> "_4370.InterMountableComponentConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4370,
            )

            return self._parent._cast(
                _4370.InterMountableComponentConnectionParametricStudyTool
            )

        @property
        def connection_parametric_study_tool(
            self: "SpiralBevelGearMeshParametricStudyTool._Cast_SpiralBevelGearMeshParametricStudyTool",
        ) -> "_4333.ConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4333,
            )

            return self._parent._cast(_4333.ConnectionParametricStudyTool)

        @property
        def connection_analysis_case(
            self: "SpiralBevelGearMeshParametricStudyTool._Cast_SpiralBevelGearMeshParametricStudyTool",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "SpiralBevelGearMeshParametricStudyTool._Cast_SpiralBevelGearMeshParametricStudyTool",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearMeshParametricStudyTool._Cast_SpiralBevelGearMeshParametricStudyTool",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearMeshParametricStudyTool._Cast_SpiralBevelGearMeshParametricStudyTool",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_mesh_parametric_study_tool(
            self: "SpiralBevelGearMeshParametricStudyTool._Cast_SpiralBevelGearMeshParametricStudyTool",
        ) -> "SpiralBevelGearMeshParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearMeshParametricStudyTool._Cast_SpiralBevelGearMeshParametricStudyTool",
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
        self: Self, instance_to_wrap: "SpiralBevelGearMeshParametricStudyTool.TYPE"
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
    def connection_system_deflection_results(
        self: Self,
    ) -> "List[_2809.SpiralBevelGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.SpiralBevelGearMeshSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearMeshParametricStudyTool._Cast_SpiralBevelGearMeshParametricStudyTool":
        return self._Cast_SpiralBevelGearMeshParametricStudyTool(self)
