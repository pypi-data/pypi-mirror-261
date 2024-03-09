"""ShaftToMountableComponentConnectionParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4301
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "ShaftToMountableComponentConnectionParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2297
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4322,
        _4342,
        _4399,
        _4333,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7540
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionParametricStudyTool",)


Self = TypeVar("Self", bound="ShaftToMountableComponentConnectionParametricStudyTool")


class ShaftToMountableComponentConnectionParametricStudyTool(
    _4301.AbstractShaftToMountableComponentConnectionParametricStudyTool
):
    """ShaftToMountableComponentConnectionParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ShaftToMountableComponentConnectionParametricStudyTool",
    )

    class _Cast_ShaftToMountableComponentConnectionParametricStudyTool:
        """Special nested class for casting ShaftToMountableComponentConnectionParametricStudyTool to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool",
            parent: "ShaftToMountableComponentConnectionParametricStudyTool",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_parametric_study_tool(
            self: "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_4301.AbstractShaftToMountableComponentConnectionParametricStudyTool":
            return self._parent._cast(
                _4301.AbstractShaftToMountableComponentConnectionParametricStudyTool
            )

        @property
        def connection_parametric_study_tool(
            self: "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_4333.ConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4333,
            )

            return self._parent._cast(_4333.ConnectionParametricStudyTool)

        @property
        def connection_analysis_case(
            self: "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def coaxial_connection_parametric_study_tool(
            self: "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_4322.CoaxialConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4322,
            )

            return self._parent._cast(_4322.CoaxialConnectionParametricStudyTool)

        @property
        def cycloidal_disc_central_bearing_connection_parametric_study_tool(
            self: "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_4342.CycloidalDiscCentralBearingConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4342,
            )

            return self._parent._cast(
                _4342.CycloidalDiscCentralBearingConnectionParametricStudyTool
            )

        @property
        def planetary_connection_parametric_study_tool(
            self: "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_4399.PlanetaryConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4399,
            )

            return self._parent._cast(_4399.PlanetaryConnectionParametricStudyTool)

        @property
        def shaft_to_mountable_component_connection_parametric_study_tool(
            self: "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "ShaftToMountableComponentConnectionParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2297.ShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool":
        return self._Cast_ShaftToMountableComponentConnectionParametricStudyTool(self)
