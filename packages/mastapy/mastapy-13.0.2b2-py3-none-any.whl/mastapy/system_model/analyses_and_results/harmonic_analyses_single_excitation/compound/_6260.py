"""TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6180,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2610
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6131,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6218,
        _6166,
        _6220,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation"
)


class TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation(
    _6180.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
):
    """TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_PUMP_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_harmonic_analysis_of_single_excitation(
            self: "TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6180.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6180.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_compound_harmonic_analysis_of_single_excitation(
            self: "TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6218.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6218,
            )

            return self._parent._cast(
                _6218.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_compound_harmonic_analysis_of_single_excitation(
            self: "TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6166.ComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6166,
            )

            return self._parent._cast(
                _6166.ComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6220.PartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6220,
            )

            return self._parent._cast(
                _6220.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def torque_converter_pump_compound_harmonic_analysis_of_single_excitation(
            self: "TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2610.TorqueConverterPump":
        """mastapy.system_model.part_model.couplings.TorqueConverterPump

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
    ) -> "List[_6131.TorqueConverterPumpHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.TorqueConverterPumpHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6131.TorqueConverterPumpHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.TorqueConverterPumpHarmonicAnalysisOfSingleExcitation]

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
    ) -> "TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation(
            self
        )
