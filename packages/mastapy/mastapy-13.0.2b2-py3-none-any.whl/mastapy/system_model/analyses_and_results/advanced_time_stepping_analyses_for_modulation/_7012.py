"""AdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.analysis_cases import _7539
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "AdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.analysis_cases import _7552, _7537
    from mastapy.system_model.analyses_and_results import _2652


__docformat__ = "restructuredtext en"
__all__ = ("AdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="AdvancedTimeSteppingAnalysisForModulation")


class AdvancedTimeSteppingAnalysisForModulation(_7539.CompoundAnalysisCase):
    """AdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AdvancedTimeSteppingAnalysisForModulation"
    )

    class _Cast_AdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting AdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "AdvancedTimeSteppingAnalysisForModulation._Cast_AdvancedTimeSteppingAnalysisForModulation",
            parent: "AdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def compound_analysis_case(
            self: "AdvancedTimeSteppingAnalysisForModulation._Cast_AdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7539.CompoundAnalysisCase":
            return self._parent._cast(_7539.CompoundAnalysisCase)

        @property
        def static_load_analysis_case(
            self: "AdvancedTimeSteppingAnalysisForModulation._Cast_AdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7552.StaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7552

            return self._parent._cast(_7552.StaticLoadAnalysisCase)

        @property
        def analysis_case(
            self: "AdvancedTimeSteppingAnalysisForModulation._Cast_AdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7537.AnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.AnalysisCase)

        @property
        def context(
            self: "AdvancedTimeSteppingAnalysisForModulation._Cast_AdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2652.Context":
            from mastapy.system_model.analyses_and_results import _2652

            return self._parent._cast(_2652.Context)

        @property
        def advanced_time_stepping_analysis_for_modulation(
            self: "AdvancedTimeSteppingAnalysisForModulation._Cast_AdvancedTimeSteppingAnalysisForModulation",
        ) -> "AdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "AdvancedTimeSteppingAnalysisForModulation._Cast_AdvancedTimeSteppingAnalysisForModulation",
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
        self: Self, instance_to_wrap: "AdvancedTimeSteppingAnalysisForModulation.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "AdvancedTimeSteppingAnalysisForModulation._Cast_AdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_AdvancedTimeSteppingAnalysisForModulation(self)
