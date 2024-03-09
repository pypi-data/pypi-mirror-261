"""OilSealCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6446
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "OilSealCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2468
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6359
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6487,
        _6435,
        _6489,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("OilSealCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="OilSealCompoundDynamicAnalysis")


class OilSealCompoundDynamicAnalysis(_6446.ConnectorCompoundDynamicAnalysis):
    """OilSealCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _OIL_SEAL_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OilSealCompoundDynamicAnalysis")

    class _Cast_OilSealCompoundDynamicAnalysis:
        """Special nested class for casting OilSealCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "OilSealCompoundDynamicAnalysis._Cast_OilSealCompoundDynamicAnalysis",
            parent: "OilSealCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def connector_compound_dynamic_analysis(
            self: "OilSealCompoundDynamicAnalysis._Cast_OilSealCompoundDynamicAnalysis",
        ) -> "_6446.ConnectorCompoundDynamicAnalysis":
            return self._parent._cast(_6446.ConnectorCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "OilSealCompoundDynamicAnalysis._Cast_OilSealCompoundDynamicAnalysis",
        ) -> "_6487.MountableComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6487,
            )

            return self._parent._cast(_6487.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "OilSealCompoundDynamicAnalysis._Cast_OilSealCompoundDynamicAnalysis",
        ) -> "_6435.ComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6435,
            )

            return self._parent._cast(_6435.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "OilSealCompoundDynamicAnalysis._Cast_OilSealCompoundDynamicAnalysis",
        ) -> "_6489.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6489,
            )

            return self._parent._cast(_6489.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "OilSealCompoundDynamicAnalysis._Cast_OilSealCompoundDynamicAnalysis",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "OilSealCompoundDynamicAnalysis._Cast_OilSealCompoundDynamicAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "OilSealCompoundDynamicAnalysis._Cast_OilSealCompoundDynamicAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def oil_seal_compound_dynamic_analysis(
            self: "OilSealCompoundDynamicAnalysis._Cast_OilSealCompoundDynamicAnalysis",
        ) -> "OilSealCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "OilSealCompoundDynamicAnalysis._Cast_OilSealCompoundDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OilSealCompoundDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2468.OilSeal":
        """mastapy.system_model.part_model.OilSeal

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6359.OilSealDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.OilSealDynamicAnalysis]

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
    def component_analysis_cases(self: Self) -> "List[_6359.OilSealDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.OilSealDynamicAnalysis]

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
    ) -> "OilSealCompoundDynamicAnalysis._Cast_OilSealCompoundDynamicAnalysis":
        return self._Cast_OilSealCompoundDynamicAnalysis(self)
