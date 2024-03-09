"""AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5563
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5383
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5542,
        _5545,
        _5546,
        _5547,
        _5593,
        _5630,
        _5636,
        _5639,
        _5642,
        _5643,
        _5657,
        _5589,
        _5608,
        _5556,
        _5610,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis")


class AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis(
    _5563.ConicalGearCompoundMultibodyDynamicsAnalysis
):
    """AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
    )

    class _Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
            parent: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5563.ConicalGearCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5563.ConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5589.GearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5589,
            )

            return self._parent._cast(_5589.GearCompoundMultibodyDynamicsAnalysis)

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5608.MountableComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5608,
            )

            return self._parent._cast(
                _5608.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5556.ComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5556,
            )

            return self._parent._cast(_5556.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5610.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5610,
            )

            return self._parent._cast(_5610.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5542.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5542,
            )

            return self._parent._cast(
                _5542.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5545.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5545,
            )

            return self._parent._cast(
                _5545.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5546.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5546,
            )

            return self._parent._cast(
                _5546.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5547.BevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5547,
            )

            return self._parent._cast(_5547.BevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5593.HypoidGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5593,
            )

            return self._parent._cast(_5593.HypoidGearCompoundMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5630.SpiralBevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5630,
            )

            return self._parent._cast(
                _5630.SpiralBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5636.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5636,
            )

            return self._parent._cast(
                _5636.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5639.StraightBevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5639,
            )

            return self._parent._cast(
                _5639.StraightBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5642.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5642,
            )

            return self._parent._cast(
                _5642.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5643.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5643,
            )

            return self._parent._cast(
                _5643.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5657.ZerolBevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5657,
            )

            return self._parent._cast(
                _5657.ZerolBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
        ) -> "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5383.AGMAGleasonConicalGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.AGMAGleasonConicalGearMultibodyDynamicsAnalysis]

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
    ) -> "List[_5383.AGMAGleasonConicalGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.AGMAGleasonConicalGearMultibodyDynamicsAnalysis]

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
    ) -> "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis":
        return self._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis(self)
