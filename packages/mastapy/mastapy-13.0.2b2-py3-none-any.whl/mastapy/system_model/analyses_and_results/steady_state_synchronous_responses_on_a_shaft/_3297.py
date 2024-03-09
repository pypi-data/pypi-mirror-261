"""CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3296,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2529
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3307,
        _3324,
        _3272,
        _3326,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft"
)


class CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft(
    _3296.CylindricalGearSteadyStateSynchronousResponseOnAShaft
):
    """CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft",
            parent: "CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3296.CylindricalGearSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3296.CylindricalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_steady_state_synchronous_response_on_a_shaft(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3307.GearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3307,
            )

            return self._parent._cast(_3307.GearSteadyStateSynchronousResponseOnAShaft)

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3324.MountableComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3324,
            )

            return self._parent._cast(
                _3324.MountableComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3272.ComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3272,
            )

            return self._parent._cast(
                _3272.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3326.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3326,
            )

            return self._parent._cast(_3326.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response_on_a_shaft(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft.TYPE",
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
    ) -> "CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft(
            self
        )
