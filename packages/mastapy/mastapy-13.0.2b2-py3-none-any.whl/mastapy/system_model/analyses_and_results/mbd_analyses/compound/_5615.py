"""PlanetaryGearSetCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5580
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "PlanetaryGearSetCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5474
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5591,
        _5629,
        _5531,
        _5610,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="PlanetaryGearSetCompoundMultibodyDynamicsAnalysis")


class PlanetaryGearSetCompoundMultibodyDynamicsAnalysis(
    _5580.CylindricalGearSetCompoundMultibodyDynamicsAnalysis
):
    """PlanetaryGearSetCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryGearSetCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_PlanetaryGearSetCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting PlanetaryGearSetCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "PlanetaryGearSetCompoundMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetCompoundMultibodyDynamicsAnalysis",
            parent: "PlanetaryGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_compound_multibody_dynamics_analysis(
            self: "PlanetaryGearSetCompoundMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_5580.CylindricalGearSetCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5580.CylindricalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_set_compound_multibody_dynamics_analysis(
            self: "PlanetaryGearSetCompoundMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_5591.GearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5591,
            )

            return self._parent._cast(_5591.GearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(
            self: "PlanetaryGearSetCompoundMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_5629.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5629,
            )

            return self._parent._cast(
                _5629.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(
            self: "PlanetaryGearSetCompoundMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_5531.AbstractAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5531,
            )

            return self._parent._cast(
                _5531.AbstractAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "PlanetaryGearSetCompoundMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_5610.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5610,
            )

            return self._parent._cast(_5610.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "PlanetaryGearSetCompoundMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetaryGearSetCompoundMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetCompoundMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_multibody_dynamics_analysis(
            self: "PlanetaryGearSetCompoundMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "PlanetaryGearSetCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetCompoundMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "PlanetaryGearSetCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5474.PlanetaryGearSetMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.PlanetaryGearSetMultibodyDynamicsAnalysis]

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
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5474.PlanetaryGearSetMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.PlanetaryGearSetMultibodyDynamicsAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "PlanetaryGearSetCompoundMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetCompoundMultibodyDynamicsAnalysis":
        return self._Cast_PlanetaryGearSetCompoundMultibodyDynamicsAnalysis(self)
