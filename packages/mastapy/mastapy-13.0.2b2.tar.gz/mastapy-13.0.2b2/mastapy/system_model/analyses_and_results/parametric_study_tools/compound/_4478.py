"""ConicalGearMeshCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4504,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "ConicalGearMeshCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4330
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4450,
        _4457,
        _4462,
        _4508,
        _4512,
        _4515,
        _4518,
        _4545,
        _4551,
        _4554,
        _4572,
        _4510,
        _4480,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="ConicalGearMeshCompoundParametricStudyTool")


class ConicalGearMeshCompoundParametricStudyTool(
    _4504.GearMeshCompoundParametricStudyTool
):
    """ConicalGearMeshCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearMeshCompoundParametricStudyTool"
    )

    class _Cast_ConicalGearMeshCompoundParametricStudyTool:
        """Special nested class for casting ConicalGearMeshCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "ConicalGearMeshCompoundParametricStudyTool._Cast_ConicalGearMeshCompoundParametricStudyTool",
            parent: "ConicalGearMeshCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_parametric_study_tool(
            self: "ConicalGearMeshCompoundParametricStudyTool._Cast_ConicalGearMeshCompoundParametricStudyTool",
        ) -> "_4504.GearMeshCompoundParametricStudyTool":
            return self._parent._cast(_4504.GearMeshCompoundParametricStudyTool)

        @property
        def inter_mountable_component_connection_compound_parametric_study_tool(
            self: "ConicalGearMeshCompoundParametricStudyTool._Cast_ConicalGearMeshCompoundParametricStudyTool",
        ) -> "_4510.InterMountableComponentConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4510,
            )

            return self._parent._cast(
                _4510.InterMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def connection_compound_parametric_study_tool(
            self: "ConicalGearMeshCompoundParametricStudyTool._Cast_ConicalGearMeshCompoundParametricStudyTool",
        ) -> "_4480.ConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4480,
            )

            return self._parent._cast(_4480.ConnectionCompoundParametricStudyTool)

        @property
        def connection_compound_analysis(
            self: "ConicalGearMeshCompoundParametricStudyTool._Cast_ConicalGearMeshCompoundParametricStudyTool",
        ) -> "_7541.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearMeshCompoundParametricStudyTool._Cast_ConicalGearMeshCompoundParametricStudyTool",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMeshCompoundParametricStudyTool._Cast_ConicalGearMeshCompoundParametricStudyTool",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_parametric_study_tool(
            self: "ConicalGearMeshCompoundParametricStudyTool._Cast_ConicalGearMeshCompoundParametricStudyTool",
        ) -> "_4450.AGMAGleasonConicalGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4450,
            )

            return self._parent._cast(
                _4450.AGMAGleasonConicalGearMeshCompoundParametricStudyTool
            )

        @property
        def bevel_differential_gear_mesh_compound_parametric_study_tool(
            self: "ConicalGearMeshCompoundParametricStudyTool._Cast_ConicalGearMeshCompoundParametricStudyTool",
        ) -> "_4457.BevelDifferentialGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4457,
            )

            return self._parent._cast(
                _4457.BevelDifferentialGearMeshCompoundParametricStudyTool
            )

        @property
        def bevel_gear_mesh_compound_parametric_study_tool(
            self: "ConicalGearMeshCompoundParametricStudyTool._Cast_ConicalGearMeshCompoundParametricStudyTool",
        ) -> "_4462.BevelGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4462,
            )

            return self._parent._cast(_4462.BevelGearMeshCompoundParametricStudyTool)

        @property
        def hypoid_gear_mesh_compound_parametric_study_tool(
            self: "ConicalGearMeshCompoundParametricStudyTool._Cast_ConicalGearMeshCompoundParametricStudyTool",
        ) -> "_4508.HypoidGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4508,
            )

            return self._parent._cast(_4508.HypoidGearMeshCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_parametric_study_tool(
            self: "ConicalGearMeshCompoundParametricStudyTool._Cast_ConicalGearMeshCompoundParametricStudyTool",
        ) -> "_4512.KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4512,
            )

            return self._parent._cast(
                _4512.KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_parametric_study_tool(
            self: "ConicalGearMeshCompoundParametricStudyTool._Cast_ConicalGearMeshCompoundParametricStudyTool",
        ) -> "_4515.KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4515,
            )

            return self._parent._cast(
                _4515.KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_parametric_study_tool(
            self: "ConicalGearMeshCompoundParametricStudyTool._Cast_ConicalGearMeshCompoundParametricStudyTool",
        ) -> "_4518.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4518,
            )

            return self._parent._cast(
                _4518.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def spiral_bevel_gear_mesh_compound_parametric_study_tool(
            self: "ConicalGearMeshCompoundParametricStudyTool._Cast_ConicalGearMeshCompoundParametricStudyTool",
        ) -> "_4545.SpiralBevelGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4545,
            )

            return self._parent._cast(
                _4545.SpiralBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_parametric_study_tool(
            self: "ConicalGearMeshCompoundParametricStudyTool._Cast_ConicalGearMeshCompoundParametricStudyTool",
        ) -> "_4551.StraightBevelDiffGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4551,
            )

            return self._parent._cast(
                _4551.StraightBevelDiffGearMeshCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_mesh_compound_parametric_study_tool(
            self: "ConicalGearMeshCompoundParametricStudyTool._Cast_ConicalGearMeshCompoundParametricStudyTool",
        ) -> "_4554.StraightBevelGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4554,
            )

            return self._parent._cast(
                _4554.StraightBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def zerol_bevel_gear_mesh_compound_parametric_study_tool(
            self: "ConicalGearMeshCompoundParametricStudyTool._Cast_ConicalGearMeshCompoundParametricStudyTool",
        ) -> "_4572.ZerolBevelGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4572,
            )

            return self._parent._cast(
                _4572.ZerolBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def conical_gear_mesh_compound_parametric_study_tool(
            self: "ConicalGearMeshCompoundParametricStudyTool._Cast_ConicalGearMeshCompoundParametricStudyTool",
        ) -> "ConicalGearMeshCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshCompoundParametricStudyTool._Cast_ConicalGearMeshCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "ConicalGearMeshCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetaries(self: Self) -> "List[ConicalGearMeshCompoundParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ConicalGearMeshCompoundParametricStudyTool]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4330.ConicalGearMeshParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ConicalGearMeshParametricStudyTool]

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
    ) -> "List[_4330.ConicalGearMeshParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ConicalGearMeshParametricStudyTool]

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
    ) -> "ConicalGearMeshCompoundParametricStudyTool._Cast_ConicalGearMeshCompoundParametricStudyTool":
        return self._Cast_ConicalGearMeshCompoundParametricStudyTool(self)
