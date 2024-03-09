"""UnbalancedMassCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5653
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "UnbalancedMassCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2479
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5516
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5608,
        _5556,
        _5610,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("UnbalancedMassCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="UnbalancedMassCompoundMultibodyDynamicsAnalysis")


class UnbalancedMassCompoundMultibodyDynamicsAnalysis(
    _5653.VirtualComponentCompoundMultibodyDynamicsAnalysis
):
    """UnbalancedMassCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_UnbalancedMassCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_UnbalancedMassCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting UnbalancedMassCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "UnbalancedMassCompoundMultibodyDynamicsAnalysis._Cast_UnbalancedMassCompoundMultibodyDynamicsAnalysis",
            parent: "UnbalancedMassCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_multibody_dynamics_analysis(
            self: "UnbalancedMassCompoundMultibodyDynamicsAnalysis._Cast_UnbalancedMassCompoundMultibodyDynamicsAnalysis",
        ) -> "_5653.VirtualComponentCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5653.VirtualComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "UnbalancedMassCompoundMultibodyDynamicsAnalysis._Cast_UnbalancedMassCompoundMultibodyDynamicsAnalysis",
        ) -> "_5608.MountableComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5608,
            )

            return self._parent._cast(
                _5608.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "UnbalancedMassCompoundMultibodyDynamicsAnalysis._Cast_UnbalancedMassCompoundMultibodyDynamicsAnalysis",
        ) -> "_5556.ComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5556,
            )

            return self._parent._cast(_5556.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "UnbalancedMassCompoundMultibodyDynamicsAnalysis._Cast_UnbalancedMassCompoundMultibodyDynamicsAnalysis",
        ) -> "_5610.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5610,
            )

            return self._parent._cast(_5610.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "UnbalancedMassCompoundMultibodyDynamicsAnalysis._Cast_UnbalancedMassCompoundMultibodyDynamicsAnalysis",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "UnbalancedMassCompoundMultibodyDynamicsAnalysis._Cast_UnbalancedMassCompoundMultibodyDynamicsAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "UnbalancedMassCompoundMultibodyDynamicsAnalysis._Cast_UnbalancedMassCompoundMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def unbalanced_mass_compound_multibody_dynamics_analysis(
            self: "UnbalancedMassCompoundMultibodyDynamicsAnalysis._Cast_UnbalancedMassCompoundMultibodyDynamicsAnalysis",
        ) -> "UnbalancedMassCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "UnbalancedMassCompoundMultibodyDynamicsAnalysis._Cast_UnbalancedMassCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "UnbalancedMassCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2479.UnbalancedMass":
        """mastapy.system_model.part_model.UnbalancedMass

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
    ) -> "List[_5516.UnbalancedMassMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.UnbalancedMassMultibodyDynamicsAnalysis]

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
    ) -> "List[_5516.UnbalancedMassMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.UnbalancedMassMultibodyDynamicsAnalysis]

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
    ) -> "UnbalancedMassCompoundMultibodyDynamicsAnalysis._Cast_UnbalancedMassCompoundMultibodyDynamicsAnalysis":
        return self._Cast_UnbalancedMassCompoundMultibodyDynamicsAnalysis(self)
