"""CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4469,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
        "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4342
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4542,
        _4448,
        _4480,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",)


Self = TypeVar(
    "Self", bound="CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool"
)


class CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool(
    _4469.CoaxialConnectionCompoundParametricStudyTool
):
    """CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
    )

    class _Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
            parent: "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def coaxial_connection_compound_parametric_study_tool(
            self: "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
        ) -> "_4469.CoaxialConnectionCompoundParametricStudyTool":
            return self._parent._cast(
                _4469.CoaxialConnectionCompoundParametricStudyTool
            )

        @property
        def shaft_to_mountable_component_connection_compound_parametric_study_tool(
            self: "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
        ) -> "_4542.ShaftToMountableComponentConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4542,
            )

            return self._parent._cast(
                _4542.ShaftToMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_parametric_study_tool(
            self: "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
        ) -> "_4448.AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4448,
            )

            return self._parent._cast(
                _4448.AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def connection_compound_parametric_study_tool(
            self: "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
        ) -> "_4480.ConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4480,
            )

            return self._parent._cast(_4480.ConnectionCompoundParametricStudyTool)

        @property
        def connection_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
        ) -> "_7541.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_parametric_study_tool(
            self: "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
        ) -> "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4342.CycloidalDiscCentralBearingConnectionParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.CycloidalDiscCentralBearingConnectionParametricStudyTool]

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
    ) -> "List[_4342.CycloidalDiscCentralBearingConnectionParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.CycloidalDiscCentralBearingConnectionParametricStudyTool]

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
    ) -> "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool":
        return (
            self._Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool(
                self
            )
        )
