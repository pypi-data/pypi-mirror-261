"""VirtualComponentHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6089,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "VirtualComponentHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2481
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6086,
        _6087,
        _6098,
        _6099,
        _6133,
        _6035,
        _6091,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="VirtualComponentHarmonicAnalysisOfSingleExcitation")


class VirtualComponentHarmonicAnalysisOfSingleExcitation(
    _6089.MountableComponentHarmonicAnalysisOfSingleExcitation
):
    """VirtualComponentHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting VirtualComponentHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
            parent: "VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6089.MountableComponentHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6089.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6035.ComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6035,
            )

            return self._parent._cast(_6035.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6091.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6091,
            )

            return self._parent._cast(_6091.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def mass_disc_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6086.MassDiscHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6086,
            )

            return self._parent._cast(_6086.MassDiscHarmonicAnalysisOfSingleExcitation)

        @property
        def measurement_component_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6087.MeasurementComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6087,
            )

            return self._parent._cast(
                _6087.MeasurementComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def point_load_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6098.PointLoadHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6098,
            )

            return self._parent._cast(_6098.PointLoadHarmonicAnalysisOfSingleExcitation)

        @property
        def power_load_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6099.PowerLoadHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6099,
            )

            return self._parent._cast(_6099.PowerLoadHarmonicAnalysisOfSingleExcitation)

        @property
        def unbalanced_mass_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6133.UnbalancedMassHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6133,
            )

            return self._parent._cast(
                _6133.UnbalancedMassHarmonicAnalysisOfSingleExcitation
            )

        @property
        def virtual_component_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "VirtualComponentHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "VirtualComponentHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
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
    def cast_to(
        self: Self,
    ) -> "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation":
        return self._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation(self)
