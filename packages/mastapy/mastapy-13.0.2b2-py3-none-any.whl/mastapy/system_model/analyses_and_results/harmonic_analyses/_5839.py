"""VirtualComponentHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5788
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "VirtualComponentHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2481
    from mastapy.system_model.analyses_and_results.system_deflections import _2837
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5786,
        _5787,
        _5798,
        _5799,
        _5838,
        _5707,
        _5790,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentHarmonicAnalysis",)


Self = TypeVar("Self", bound="VirtualComponentHarmonicAnalysis")


class VirtualComponentHarmonicAnalysis(_5788.MountableComponentHarmonicAnalysis):
    """VirtualComponentHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VirtualComponentHarmonicAnalysis")

    class _Cast_VirtualComponentHarmonicAnalysis:
        """Special nested class for casting VirtualComponentHarmonicAnalysis to subclasses."""

        def __init__(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
            parent: "VirtualComponentHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_harmonic_analysis(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_5788.MountableComponentHarmonicAnalysis":
            return self._parent._cast(_5788.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_5707.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5707,
            )

            return self._parent._cast(_5707.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_5790.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5790,
            )

            return self._parent._cast(_5790.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def mass_disc_harmonic_analysis(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_5786.MassDiscHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5786,
            )

            return self._parent._cast(_5786.MassDiscHarmonicAnalysis)

        @property
        def measurement_component_harmonic_analysis(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_5787.MeasurementComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5787,
            )

            return self._parent._cast(_5787.MeasurementComponentHarmonicAnalysis)

        @property
        def point_load_harmonic_analysis(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_5798.PointLoadHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5798,
            )

            return self._parent._cast(_5798.PointLoadHarmonicAnalysis)

        @property
        def power_load_harmonic_analysis(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_5799.PowerLoadHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5799,
            )

            return self._parent._cast(_5799.PowerLoadHarmonicAnalysis)

        @property
        def unbalanced_mass_harmonic_analysis(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_5838.UnbalancedMassHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5838,
            )

            return self._parent._cast(_5838.UnbalancedMassHarmonicAnalysis)

        @property
        def virtual_component_harmonic_analysis(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "VirtualComponentHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "VirtualComponentHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2481.VirtualComponent":
        """mastapy.system_model.part_model.VirtualComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2837.VirtualComponentSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.VirtualComponentSystemDeflection

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
    ) -> "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis":
        return self._Cast_VirtualComponentHarmonicAnalysis(self)
