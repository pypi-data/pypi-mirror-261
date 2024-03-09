"""CylindricalPlanetGearStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3815
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "CylindricalPlanetGearStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2529
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3827,
        _3844,
        _3790,
        _3846,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearStabilityAnalysis",)


Self = TypeVar("Self", bound="CylindricalPlanetGearStabilityAnalysis")


class CylindricalPlanetGearStabilityAnalysis(_3815.CylindricalGearStabilityAnalysis):
    """CylindricalPlanetGearStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalPlanetGearStabilityAnalysis"
    )

    class _Cast_CylindricalPlanetGearStabilityAnalysis:
        """Special nested class for casting CylindricalPlanetGearStabilityAnalysis to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
            parent: "CylindricalPlanetGearStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_stability_analysis(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_3815.CylindricalGearStabilityAnalysis":
            return self._parent._cast(_3815.CylindricalGearStabilityAnalysis)

        @property
        def gear_stability_analysis(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_3827.GearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3827,
            )

            return self._parent._cast(_3827.GearStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_3844.MountableComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3844,
            )

            return self._parent._cast(_3844.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_3790.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3790,
            )

            return self._parent._cast(_3790.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_3846.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3846,
            )

            return self._parent._cast(_3846.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_stability_analysis(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "CylindricalPlanetGearStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
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
        self: Self, instance_to_wrap: "CylindricalPlanetGearStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2529.CylindricalPlanetGear":
        """mastapy.system_model.part_model.gears.CylindricalPlanetGear

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
    ) -> "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis":
        return self._Cast_CylindricalPlanetGearStabilityAnalysis(self)
