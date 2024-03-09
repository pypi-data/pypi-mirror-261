"""CouplingConnectionCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5596
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "CouplingConnectionCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5418
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5553,
        _5558,
        _5612,
        _5634,
        _5649,
        _5566,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="CouplingConnectionCompoundMultibodyDynamicsAnalysis")


class CouplingConnectionCompoundMultibodyDynamicsAnalysis(
    _5596.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
):
    """CouplingConnectionCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingConnectionCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_CouplingConnectionCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting CouplingConnectionCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CouplingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CouplingConnectionCompoundMultibodyDynamicsAnalysis",
            parent: "CouplingConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "CouplingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CouplingConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5596.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5596.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def connection_compound_multibody_dynamics_analysis(
            self: "CouplingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CouplingConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5566.ConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5566,
            )

            return self._parent._cast(_5566.ConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def connection_compound_analysis(
            self: "CouplingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CouplingConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_7541.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CouplingConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CouplingConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def clutch_connection_compound_multibody_dynamics_analysis(
            self: "CouplingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CouplingConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5553.ClutchConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5553,
            )

            return self._parent._cast(
                _5553.ClutchConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_coupling_connection_compound_multibody_dynamics_analysis(
            self: "CouplingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CouplingConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5558.ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5558,
            )

            return self._parent._cast(
                _5558.ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_multibody_dynamics_analysis(
            self: "CouplingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CouplingConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5612.PartToPartShearCouplingConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5612,
            )

            return self._parent._cast(
                _5612.PartToPartShearCouplingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_connection_compound_multibody_dynamics_analysis(
            self: "CouplingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CouplingConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5634.SpringDamperConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5634,
            )

            return self._parent._cast(
                _5634.SpringDamperConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_connection_compound_multibody_dynamics_analysis(
            self: "CouplingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CouplingConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5649.TorqueConverterConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5649,
            )

            return self._parent._cast(
                _5649.TorqueConverterConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def coupling_connection_compound_multibody_dynamics_analysis(
            self: "CouplingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CouplingConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "CouplingConnectionCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CouplingConnectionCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "CouplingConnectionCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5418.CouplingConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.CouplingConnectionMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5418.CouplingConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.CouplingConnectionMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CouplingConnectionCompoundMultibodyDynamicsAnalysis":
        return self._Cast_CouplingConnectionCompoundMultibodyDynamicsAnalysis(self)
