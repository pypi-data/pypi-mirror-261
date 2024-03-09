"""BevelGearSetCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5537
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "BevelGearSetCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5398
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5544,
        _5632,
        _5638,
        _5641,
        _5659,
        _5565,
        _5591,
        _5629,
        _5531,
        _5610,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="BevelGearSetCompoundMultibodyDynamicsAnalysis")


class BevelGearSetCompoundMultibodyDynamicsAnalysis(
    _5537.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis
):
    """BevelGearSetCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearSetCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_BevelGearSetCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting BevelGearSetCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "BevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_BevelGearSetCompoundMultibodyDynamicsAnalysis",
            parent: "BevelGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_compound_multibody_dynamics_analysis(
            self: "BevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_BevelGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_5537.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5537.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_set_compound_multibody_dynamics_analysis(
            self: "BevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_BevelGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_5565.ConicalGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5565,
            )

            return self._parent._cast(
                _5565.ConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_set_compound_multibody_dynamics_analysis(
            self: "BevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_BevelGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_5591.GearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5591,
            )

            return self._parent._cast(_5591.GearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(
            self: "BevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_BevelGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_5629.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5629,
            )

            return self._parent._cast(
                _5629.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(
            self: "BevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_BevelGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_5531.AbstractAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5531,
            )

            return self._parent._cast(
                _5531.AbstractAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "BevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_BevelGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_5610.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5610,
            )

            return self._parent._cast(_5610.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_BevelGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_BevelGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_BevelGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_multibody_dynamics_analysis(
            self: "BevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_BevelGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_5544.BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5544,
            )

            return self._parent._cast(
                _5544.BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "BevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_BevelGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_5632.SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5632,
            )

            return self._parent._cast(
                _5632.SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_multibody_dynamics_analysis(
            self: "BevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_BevelGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_5638.StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5638,
            )

            return self._parent._cast(
                _5638.StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "BevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_BevelGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_5641.StraightBevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5641,
            )

            return self._parent._cast(
                _5641.StraightBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "BevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_BevelGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_5659.ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5659,
            )

            return self._parent._cast(
                _5659.ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "BevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_BevelGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "BevelGearSetCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_BevelGearSetCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "BevelGearSetCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5398.BevelGearSetMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.BevelGearSetMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5398.BevelGearSetMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.BevelGearSetMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_BevelGearSetCompoundMultibodyDynamicsAnalysis":
        return self._Cast_BevelGearSetCompoundMultibodyDynamicsAnalysis(self)
