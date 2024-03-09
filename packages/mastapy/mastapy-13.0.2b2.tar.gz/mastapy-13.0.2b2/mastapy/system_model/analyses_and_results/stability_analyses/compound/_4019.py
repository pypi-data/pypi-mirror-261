"""TorqueConverterTurbineCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3938
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "TorqueConverterTurbineCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2612
    from mastapy.system_model.analyses_and_results.stability_analyses import _3890
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3976,
        _3924,
        _3978,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterTurbineCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="TorqueConverterTurbineCompoundStabilityAnalysis")


class TorqueConverterTurbineCompoundStabilityAnalysis(
    _3938.CouplingHalfCompoundStabilityAnalysis
):
    """TorqueConverterTurbineCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterTurbineCompoundStabilityAnalysis"
    )

    class _Cast_TorqueConverterTurbineCompoundStabilityAnalysis:
        """Special nested class for casting TorqueConverterTurbineCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "TorqueConverterTurbineCompoundStabilityAnalysis._Cast_TorqueConverterTurbineCompoundStabilityAnalysis",
            parent: "TorqueConverterTurbineCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_stability_analysis(
            self: "TorqueConverterTurbineCompoundStabilityAnalysis._Cast_TorqueConverterTurbineCompoundStabilityAnalysis",
        ) -> "_3938.CouplingHalfCompoundStabilityAnalysis":
            return self._parent._cast(_3938.CouplingHalfCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "TorqueConverterTurbineCompoundStabilityAnalysis._Cast_TorqueConverterTurbineCompoundStabilityAnalysis",
        ) -> "_3976.MountableComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3976,
            )

            return self._parent._cast(_3976.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "TorqueConverterTurbineCompoundStabilityAnalysis._Cast_TorqueConverterTurbineCompoundStabilityAnalysis",
        ) -> "_3924.ComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3924,
            )

            return self._parent._cast(_3924.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "TorqueConverterTurbineCompoundStabilityAnalysis._Cast_TorqueConverterTurbineCompoundStabilityAnalysis",
        ) -> "_3978.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3978,
            )

            return self._parent._cast(_3978.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "TorqueConverterTurbineCompoundStabilityAnalysis._Cast_TorqueConverterTurbineCompoundStabilityAnalysis",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterTurbineCompoundStabilityAnalysis._Cast_TorqueConverterTurbineCompoundStabilityAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterTurbineCompoundStabilityAnalysis._Cast_TorqueConverterTurbineCompoundStabilityAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def torque_converter_turbine_compound_stability_analysis(
            self: "TorqueConverterTurbineCompoundStabilityAnalysis._Cast_TorqueConverterTurbineCompoundStabilityAnalysis",
        ) -> "TorqueConverterTurbineCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "TorqueConverterTurbineCompoundStabilityAnalysis._Cast_TorqueConverterTurbineCompoundStabilityAnalysis",
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
        instance_to_wrap: "TorqueConverterTurbineCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2612.TorqueConverterTurbine":
        """mastapy.system_model.part_model.couplings.TorqueConverterTurbine

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
    ) -> "List[_3890.TorqueConverterTurbineStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.TorqueConverterTurbineStabilityAnalysis]

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
    ) -> "List[_3890.TorqueConverterTurbineStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.TorqueConverterTurbineStabilityAnalysis]

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
    ) -> "TorqueConverterTurbineCompoundStabilityAnalysis._Cast_TorqueConverterTurbineCompoundStabilityAnalysis":
        return self._Cast_TorqueConverterTurbineCompoundStabilityAnalysis(self)
