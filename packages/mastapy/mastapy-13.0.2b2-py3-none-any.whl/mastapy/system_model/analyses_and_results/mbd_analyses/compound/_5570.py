"""CouplingHalfCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5608
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "CouplingHalfCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5419
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5554,
        _5559,
        _5573,
        _5613,
        _5619,
        _5623,
        _5635,
        _5645,
        _5646,
        _5647,
        _5650,
        _5651,
        _5556,
        _5610,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="CouplingHalfCompoundMultibodyDynamicsAnalysis")


class CouplingHalfCompoundMultibodyDynamicsAnalysis(
    _5608.MountableComponentCompoundMultibodyDynamicsAnalysis
):
    """CouplingHalfCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting CouplingHalfCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
            parent: "CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_5608.MountableComponentCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5608.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_5556.ComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5556,
            )

            return self._parent._cast(_5556.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_5610.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5610,
            )

            return self._parent._cast(_5610.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def clutch_half_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_5554.ClutchHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5554,
            )

            return self._parent._cast(_5554.ClutchHalfCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_half_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_5559.ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5559,
            )

            return self._parent._cast(
                _5559.ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cvt_pulley_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_5573.CVTPulleyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5573,
            )

            return self._parent._cast(_5573.CVTPulleyCompoundMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_5613.PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5613,
            )

            return self._parent._cast(
                _5613.PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def pulley_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_5619.PulleyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5619,
            )

            return self._parent._cast(_5619.PulleyCompoundMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_5623.RollingRingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5623,
            )

            return self._parent._cast(
                _5623.RollingRingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_half_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_5635.SpringDamperHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5635,
            )

            return self._parent._cast(
                _5635.SpringDamperHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_half_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_5645.SynchroniserHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5645,
            )

            return self._parent._cast(
                _5645.SynchroniserHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_part_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_5646.SynchroniserPartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5646,
            )

            return self._parent._cast(
                _5646.SynchroniserPartCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_sleeve_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_5647.SynchroniserSleeveCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5647,
            )

            return self._parent._cast(
                _5647.SynchroniserSleeveCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_pump_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_5650.TorqueConverterPumpCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5650,
            )

            return self._parent._cast(
                _5650.TorqueConverterPumpCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_turbine_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_5651.TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5651,
            )

            return self._parent._cast(
                _5651.TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis
            )

        @property
        def coupling_half_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "CouplingHalfCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "CouplingHalfCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5419.CouplingHalfMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.CouplingHalfMultibodyDynamicsAnalysis]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5419.CouplingHalfMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.CouplingHalfMultibodyDynamicsAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis":
        return self._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis(self)
