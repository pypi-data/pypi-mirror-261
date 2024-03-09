"""CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3555,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2529
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3566,
        _3583,
        _3531,
        _3585,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed"
)


class CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed(
    _3555.CylindricalGearSteadyStateSynchronousResponseAtASpeed
):
    """CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed",
            parent: "CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_steady_state_synchronous_response_at_a_speed(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3555.CylindricalGearSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3555.CylindricalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_steady_state_synchronous_response_at_a_speed(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3566.GearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3566,
            )

            return self._parent._cast(_3566.GearSteadyStateSynchronousResponseAtASpeed)

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3583.MountableComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3583,
            )

            return self._parent._cast(
                _3583.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3531.ComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3531,
            )

            return self._parent._cast(
                _3531.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3585.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3585,
            )

            return self._parent._cast(_3585.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed.TYPE",
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
    ) -> "CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed(
            self
        )
