"""CoaxialConnectionCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4542,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "CoaxialConnectionCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2271
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4322
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4489,
        _4448,
        _4480,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="CoaxialConnectionCompoundParametricStudyTool")


class CoaxialConnectionCompoundParametricStudyTool(
    _4542.ShaftToMountableComponentConnectionCompoundParametricStudyTool
):
    """CoaxialConnectionCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CoaxialConnectionCompoundParametricStudyTool"
    )

    class _Cast_CoaxialConnectionCompoundParametricStudyTool:
        """Special nested class for casting CoaxialConnectionCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "CoaxialConnectionCompoundParametricStudyTool._Cast_CoaxialConnectionCompoundParametricStudyTool",
            parent: "CoaxialConnectionCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_compound_parametric_study_tool(
            self: "CoaxialConnectionCompoundParametricStudyTool._Cast_CoaxialConnectionCompoundParametricStudyTool",
        ) -> "_4542.ShaftToMountableComponentConnectionCompoundParametricStudyTool":
            return self._parent._cast(
                _4542.ShaftToMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_parametric_study_tool(
            self: "CoaxialConnectionCompoundParametricStudyTool._Cast_CoaxialConnectionCompoundParametricStudyTool",
        ) -> "_4448.AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4448,
            )

            return self._parent._cast(
                _4448.AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def connection_compound_parametric_study_tool(
            self: "CoaxialConnectionCompoundParametricStudyTool._Cast_CoaxialConnectionCompoundParametricStudyTool",
        ) -> "_4480.ConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4480,
            )

            return self._parent._cast(_4480.ConnectionCompoundParametricStudyTool)

        @property
        def connection_compound_analysis(
            self: "CoaxialConnectionCompoundParametricStudyTool._Cast_CoaxialConnectionCompoundParametricStudyTool",
        ) -> "_7541.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CoaxialConnectionCompoundParametricStudyTool._Cast_CoaxialConnectionCompoundParametricStudyTool",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionCompoundParametricStudyTool._Cast_CoaxialConnectionCompoundParametricStudyTool",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_parametric_study_tool(
            self: "CoaxialConnectionCompoundParametricStudyTool._Cast_CoaxialConnectionCompoundParametricStudyTool",
        ) -> "_4489.CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4489,
            )

            return self._parent._cast(
                _4489.CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool
            )

        @property
        def coaxial_connection_compound_parametric_study_tool(
            self: "CoaxialConnectionCompoundParametricStudyTool._Cast_CoaxialConnectionCompoundParametricStudyTool",
        ) -> "CoaxialConnectionCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionCompoundParametricStudyTool._Cast_CoaxialConnectionCompoundParametricStudyTool",
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
        instance_to_wrap: "CoaxialConnectionCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2271.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2271.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

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
    ) -> "List[_4322.CoaxialConnectionParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.CoaxialConnectionParametricStudyTool]

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
    ) -> "List[_4322.CoaxialConnectionParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.CoaxialConnectionParametricStudyTool]

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
    ) -> "CoaxialConnectionCompoundParametricStudyTool._Cast_CoaxialConnectionCompoundParametricStudyTool":
        return self._Cast_CoaxialConnectionCompoundParametricStudyTool(self)
