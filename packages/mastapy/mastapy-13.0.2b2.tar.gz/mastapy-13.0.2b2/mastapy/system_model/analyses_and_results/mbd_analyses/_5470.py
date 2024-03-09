"""PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5418
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2350
    from mastapy.system_model.analyses_and_results.static_loads import _6932
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5451, _5416
    from mastapy.system_model.analyses_and_results.analysis_cases import _7544, _7540
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis",)


Self = TypeVar(
    "Self", bound="PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis"
)


class PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis(
    _5418.CouplingConnectionMultibodyDynamicsAnalysis
):
    """PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis",
    )

    class _Cast_PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis:
        """Special nested class for casting PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis",
            parent: "PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_multibody_dynamics_analysis(
            self: "PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_5418.CouplingConnectionMultibodyDynamicsAnalysis":
            return self._parent._cast(_5418.CouplingConnectionMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_5451.InterMountableComponentConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5451

            return self._parent._cast(
                _5451.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_5416.ConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5416

            return self._parent._cast(_5416.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_7544.ConnectionTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_multibody_dynamics_analysis(
            self: "PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2350.PartToPartShearCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(
        self: Self,
    ) -> "_6932.PartToPartShearCouplingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis":
        return self._Cast_PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis(
            self
        )
