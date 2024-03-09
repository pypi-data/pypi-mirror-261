"""BevelGearCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5535
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "BevelGearCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5397
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5542,
        _5545,
        _5546,
        _5630,
        _5636,
        _5639,
        _5642,
        _5643,
        _5657,
        _5563,
        _5589,
        _5608,
        _5556,
        _5610,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="BevelGearCompoundMultibodyDynamicsAnalysis")


class BevelGearCompoundMultibodyDynamicsAnalysis(
    _5535.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis
):
    """BevelGearCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_BevelGearCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting BevelGearCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "BevelGearCompoundMultibodyDynamicsAnalysis._Cast_BevelGearCompoundMultibodyDynamicsAnalysis",
            parent: "BevelGearCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_compound_multibody_dynamics_analysis(
            self: "BevelGearCompoundMultibodyDynamicsAnalysis._Cast_BevelGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5535.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5535.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_compound_multibody_dynamics_analysis(
            self: "BevelGearCompoundMultibodyDynamicsAnalysis._Cast_BevelGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5563.ConicalGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5563,
            )

            return self._parent._cast(
                _5563.ConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_compound_multibody_dynamics_analysis(
            self: "BevelGearCompoundMultibodyDynamicsAnalysis._Cast_BevelGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5589.GearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5589,
            )

            return self._parent._cast(_5589.GearCompoundMultibodyDynamicsAnalysis)

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "BevelGearCompoundMultibodyDynamicsAnalysis._Cast_BevelGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5608.MountableComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5608,
            )

            return self._parent._cast(
                _5608.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "BevelGearCompoundMultibodyDynamicsAnalysis._Cast_BevelGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5556.ComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5556,
            )

            return self._parent._cast(_5556.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "BevelGearCompoundMultibodyDynamicsAnalysis._Cast_BevelGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5610.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5610,
            )

            return self._parent._cast(_5610.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelGearCompoundMultibodyDynamicsAnalysis._Cast_BevelGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearCompoundMultibodyDynamicsAnalysis._Cast_BevelGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearCompoundMultibodyDynamicsAnalysis._Cast_BevelGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_compound_multibody_dynamics_analysis(
            self: "BevelGearCompoundMultibodyDynamicsAnalysis._Cast_BevelGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5542.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5542,
            )

            return self._parent._cast(
                _5542.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_multibody_dynamics_analysis(
            self: "BevelGearCompoundMultibodyDynamicsAnalysis._Cast_BevelGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5545.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5545,
            )

            return self._parent._cast(
                _5545.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_multibody_dynamics_analysis(
            self: "BevelGearCompoundMultibodyDynamicsAnalysis._Cast_BevelGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5546.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5546,
            )

            return self._parent._cast(
                _5546.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_compound_multibody_dynamics_analysis(
            self: "BevelGearCompoundMultibodyDynamicsAnalysis._Cast_BevelGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5630.SpiralBevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5630,
            )

            return self._parent._cast(
                _5630.SpiralBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_compound_multibody_dynamics_analysis(
            self: "BevelGearCompoundMultibodyDynamicsAnalysis._Cast_BevelGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5636.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5636,
            )

            return self._parent._cast(
                _5636.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_compound_multibody_dynamics_analysis(
            self: "BevelGearCompoundMultibodyDynamicsAnalysis._Cast_BevelGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5639.StraightBevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5639,
            )

            return self._parent._cast(
                _5639.StraightBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_multibody_dynamics_analysis(
            self: "BevelGearCompoundMultibodyDynamicsAnalysis._Cast_BevelGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5642.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5642,
            )

            return self._parent._cast(
                _5642.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_multibody_dynamics_analysis(
            self: "BevelGearCompoundMultibodyDynamicsAnalysis._Cast_BevelGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5643.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5643,
            )

            return self._parent._cast(
                _5643.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_compound_multibody_dynamics_analysis(
            self: "BevelGearCompoundMultibodyDynamicsAnalysis._Cast_BevelGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5657.ZerolBevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5657,
            )

            return self._parent._cast(
                _5657.ZerolBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_compound_multibody_dynamics_analysis(
            self: "BevelGearCompoundMultibodyDynamicsAnalysis._Cast_BevelGearCompoundMultibodyDynamicsAnalysis",
        ) -> "BevelGearCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearCompoundMultibodyDynamicsAnalysis._Cast_BevelGearCompoundMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "BevelGearCompoundMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5397.BevelGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.BevelGearMultibodyDynamicsAnalysis]

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
    ) -> "List[_5397.BevelGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.BevelGearMultibodyDynamicsAnalysis]

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
    ) -> "BevelGearCompoundMultibodyDynamicsAnalysis._Cast_BevelGearCompoundMultibodyDynamicsAnalysis":
        return self._Cast_BevelGearCompoundMultibodyDynamicsAnalysis(self)
