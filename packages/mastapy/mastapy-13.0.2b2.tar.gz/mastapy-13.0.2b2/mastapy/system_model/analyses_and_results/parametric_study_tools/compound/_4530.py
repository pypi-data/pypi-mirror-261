"""PlanetCarrierCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4522,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "PlanetCarrierCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2471
    from mastapy.system_model.analyses_and_results.static_loads import _6938
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4401
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4470,
        _4524,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("PlanetCarrierCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="PlanetCarrierCompoundParametricStudyTool")


class PlanetCarrierCompoundParametricStudyTool(
    _4522.MountableComponentCompoundParametricStudyTool
):
    """PlanetCarrierCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _PLANET_CARRIER_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetCarrierCompoundParametricStudyTool"
    )

    class _Cast_PlanetCarrierCompoundParametricStudyTool:
        """Special nested class for casting PlanetCarrierCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "PlanetCarrierCompoundParametricStudyTool._Cast_PlanetCarrierCompoundParametricStudyTool",
            parent: "PlanetCarrierCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "PlanetCarrierCompoundParametricStudyTool._Cast_PlanetCarrierCompoundParametricStudyTool",
        ) -> "_4522.MountableComponentCompoundParametricStudyTool":
            return self._parent._cast(
                _4522.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "PlanetCarrierCompoundParametricStudyTool._Cast_PlanetCarrierCompoundParametricStudyTool",
        ) -> "_4470.ComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4470,
            )

            return self._parent._cast(_4470.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "PlanetCarrierCompoundParametricStudyTool._Cast_PlanetCarrierCompoundParametricStudyTool",
        ) -> "_4524.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4524,
            )

            return self._parent._cast(_4524.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "PlanetCarrierCompoundParametricStudyTool._Cast_PlanetCarrierCompoundParametricStudyTool",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetCarrierCompoundParametricStudyTool._Cast_PlanetCarrierCompoundParametricStudyTool",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetCarrierCompoundParametricStudyTool._Cast_PlanetCarrierCompoundParametricStudyTool",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def planet_carrier_compound_parametric_study_tool(
            self: "PlanetCarrierCompoundParametricStudyTool._Cast_PlanetCarrierCompoundParametricStudyTool",
        ) -> "PlanetCarrierCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "PlanetCarrierCompoundParametricStudyTool._Cast_PlanetCarrierCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "PlanetCarrierCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2471.PlanetCarrier":
        """mastapy.system_model.part_model.PlanetCarrier

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def properties_changing_all_load_cases(self: Self) -> "_6938.PlanetCarrierLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PlanetCarrierLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PropertiesChangingAllLoadCases

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4401.PlanetCarrierParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.PlanetCarrierParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4401.PlanetCarrierParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.PlanetCarrierParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PlanetCarrierCompoundParametricStudyTool._Cast_PlanetCarrierCompoundParametricStudyTool":
        return self._Cast_PlanetCarrierCompoundParametricStudyTool(self)
