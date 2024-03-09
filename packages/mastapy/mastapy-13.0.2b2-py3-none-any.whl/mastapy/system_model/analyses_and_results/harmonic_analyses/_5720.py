"""CouplingHalfHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5788
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "CouplingHalfHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2586
    from mastapy.system_model.analyses_and_results.system_deflections import _2732
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5703,
        _5709,
        _5724,
        _5792,
        _5800,
        _5806,
        _5818,
        _5829,
        _5831,
        _5832,
        _5835,
        _5836,
        _5707,
        _5790,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfHarmonicAnalysis",)


Self = TypeVar("Self", bound="CouplingHalfHarmonicAnalysis")


class CouplingHalfHarmonicAnalysis(_5788.MountableComponentHarmonicAnalysis):
    """CouplingHalfHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfHarmonicAnalysis")

    class _Cast_CouplingHalfHarmonicAnalysis:
        """Special nested class for casting CouplingHalfHarmonicAnalysis to subclasses."""

        def __init__(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
            parent: "CouplingHalfHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5788.MountableComponentHarmonicAnalysis":
            return self._parent._cast(_5788.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5707.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5707,
            )

            return self._parent._cast(_5707.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5790.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5790,
            )

            return self._parent._cast(_5790.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def clutch_half_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5703.ClutchHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5703,
            )

            return self._parent._cast(_5703.ClutchHalfHarmonicAnalysis)

        @property
        def concept_coupling_half_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5709.ConceptCouplingHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5709,
            )

            return self._parent._cast(_5709.ConceptCouplingHalfHarmonicAnalysis)

        @property
        def cvt_pulley_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5724.CVTPulleyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5724,
            )

            return self._parent._cast(_5724.CVTPulleyHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5792.PartToPartShearCouplingHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5792,
            )

            return self._parent._cast(_5792.PartToPartShearCouplingHalfHarmonicAnalysis)

        @property
        def pulley_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5800.PulleyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5800,
            )

            return self._parent._cast(_5800.PulleyHarmonicAnalysis)

        @property
        def rolling_ring_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5806.RollingRingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5806,
            )

            return self._parent._cast(_5806.RollingRingHarmonicAnalysis)

        @property
        def spring_damper_half_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5818.SpringDamperHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5818,
            )

            return self._parent._cast(_5818.SpringDamperHalfHarmonicAnalysis)

        @property
        def synchroniser_half_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5829.SynchroniserHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5829,
            )

            return self._parent._cast(_5829.SynchroniserHalfHarmonicAnalysis)

        @property
        def synchroniser_part_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5831.SynchroniserPartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5831,
            )

            return self._parent._cast(_5831.SynchroniserPartHarmonicAnalysis)

        @property
        def synchroniser_sleeve_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5832.SynchroniserSleeveHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5832,
            )

            return self._parent._cast(_5832.SynchroniserSleeveHarmonicAnalysis)

        @property
        def torque_converter_pump_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5835.TorqueConverterPumpHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5835,
            )

            return self._parent._cast(_5835.TorqueConverterPumpHarmonicAnalysis)

        @property
        def torque_converter_turbine_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5836.TorqueConverterTurbineHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5836,
            )

            return self._parent._cast(_5836.TorqueConverterTurbineHarmonicAnalysis)

        @property
        def coupling_half_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "CouplingHalfHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingHalfHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2586.CouplingHalf":
        """mastapy.system_model.part_model.couplings.CouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2732.CouplingHalfSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CouplingHalfSystemDeflection

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
    ) -> "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis":
        return self._Cast_CouplingHalfHarmonicAnalysis(self)
