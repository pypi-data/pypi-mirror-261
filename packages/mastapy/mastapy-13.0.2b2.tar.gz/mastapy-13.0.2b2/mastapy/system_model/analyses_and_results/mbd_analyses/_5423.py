"""CVTPulleyMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5478
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "CVTPulleyMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2589
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5419,
        _5466,
        _5406,
        _5469,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7551, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="CVTPulleyMultibodyDynamicsAnalysis")


class CVTPulleyMultibodyDynamicsAnalysis(_5478.PulleyMultibodyDynamicsAnalysis):
    """CVTPulleyMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTPulleyMultibodyDynamicsAnalysis")

    class _Cast_CVTPulleyMultibodyDynamicsAnalysis:
        """Special nested class for casting CVTPulleyMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CVTPulleyMultibodyDynamicsAnalysis._Cast_CVTPulleyMultibodyDynamicsAnalysis",
            parent: "CVTPulleyMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def pulley_multibody_dynamics_analysis(
            self: "CVTPulleyMultibodyDynamicsAnalysis._Cast_CVTPulleyMultibodyDynamicsAnalysis",
        ) -> "_5478.PulleyMultibodyDynamicsAnalysis":
            return self._parent._cast(_5478.PulleyMultibodyDynamicsAnalysis)

        @property
        def coupling_half_multibody_dynamics_analysis(
            self: "CVTPulleyMultibodyDynamicsAnalysis._Cast_CVTPulleyMultibodyDynamicsAnalysis",
        ) -> "_5419.CouplingHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5419

            return self._parent._cast(_5419.CouplingHalfMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "CVTPulleyMultibodyDynamicsAnalysis._Cast_CVTPulleyMultibodyDynamicsAnalysis",
        ) -> "_5466.MountableComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5466

            return self._parent._cast(_5466.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "CVTPulleyMultibodyDynamicsAnalysis._Cast_CVTPulleyMultibodyDynamicsAnalysis",
        ) -> "_5406.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5406

            return self._parent._cast(_5406.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "CVTPulleyMultibodyDynamicsAnalysis._Cast_CVTPulleyMultibodyDynamicsAnalysis",
        ) -> "_5469.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5469

            return self._parent._cast(_5469.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "CVTPulleyMultibodyDynamicsAnalysis._Cast_CVTPulleyMultibodyDynamicsAnalysis",
        ) -> "_7551.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTPulleyMultibodyDynamicsAnalysis._Cast_CVTPulleyMultibodyDynamicsAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTPulleyMultibodyDynamicsAnalysis._Cast_CVTPulleyMultibodyDynamicsAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTPulleyMultibodyDynamicsAnalysis._Cast_CVTPulleyMultibodyDynamicsAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyMultibodyDynamicsAnalysis._Cast_CVTPulleyMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cvt_pulley_multibody_dynamics_analysis(
            self: "CVTPulleyMultibodyDynamicsAnalysis._Cast_CVTPulleyMultibodyDynamicsAnalysis",
        ) -> "CVTPulleyMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTPulleyMultibodyDynamicsAnalysis._Cast_CVTPulleyMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "CVTPulleyMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2589.CVTPulley":
        """mastapy.system_model.part_model.couplings.CVTPulley

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
    ) -> "CVTPulleyMultibodyDynamicsAnalysis._Cast_CVTPulleyMultibodyDynamicsAnalysis":
        return self._Cast_CVTPulleyMultibodyDynamicsAnalysis(self)
