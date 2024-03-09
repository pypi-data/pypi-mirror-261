"""ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_set_pareto_optimiser import _924
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_STRAIGHT_BEVEL_GEAR_SET_DUTY_CYCLE_OPTIMISATION_STRATEGY_DATABASE = (
    python_net_import(
        "SMT.MastaAPI.Gears.GearSetParetoOptimiser",
        "ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase",
    )
)

if TYPE_CHECKING:
    from mastapy.math_utility.optimisation import _1554, _1542
    from mastapy.utility.databases import _1830, _1833, _1826


__docformat__ = "restructuredtext en"
__all__ = ("ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase",)


Self = TypeVar(
    "Self", bound="ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase"
)


class ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase(
    _924.ParetoConicalRatingOptimisationStrategyDatabase
):
    """ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _PARETO_STRAIGHT_BEVEL_GEAR_SET_DUTY_CYCLE_OPTIMISATION_STRATEGY_DATABASE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase",
    )

    class _Cast_ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase:
        """Special nested class for casting ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase to subclasses."""

        def __init__(
            self: "ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase",
            parent: "ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase",
        ):
            self._parent = parent

        @property
        def pareto_conical_rating_optimisation_strategy_database(
            self: "ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase",
        ) -> "_924.ParetoConicalRatingOptimisationStrategyDatabase":
            return self._parent._cast(
                _924.ParetoConicalRatingOptimisationStrategyDatabase
            )

        @property
        def pareto_optimisation_strategy_database(
            self: "ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase",
        ) -> "_1554.ParetoOptimisationStrategyDatabase":
            from mastapy.math_utility.optimisation import _1554

            return self._parent._cast(_1554.ParetoOptimisationStrategyDatabase)

        @property
        def design_space_search_strategy_database(
            self: "ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase",
        ) -> "_1542.DesignSpaceSearchStrategyDatabase":
            from mastapy.math_utility.optimisation import _1542

            return self._parent._cast(_1542.DesignSpaceSearchStrategyDatabase)

        @property
        def named_database(
            self: "ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase",
        ) -> "_1830.NamedDatabase":
            pass

            from mastapy.utility.databases import _1830

            return self._parent._cast(_1830.NamedDatabase)

        @property
        def sql_database(
            self: "ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase",
        ) -> "_1833.SQLDatabase":
            pass

            from mastapy.utility.databases import _1833

            return self._parent._cast(_1833.SQLDatabase)

        @property
        def database(
            self: "ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase",
        ) -> "_1826.Database":
            pass

            from mastapy.utility.databases import _1826

            return self._parent._cast(_1826.Database)

        @property
        def pareto_straight_bevel_gear_set_duty_cycle_optimisation_strategy_database(
            self: "ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase",
        ) -> "ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase":
            return self._parent

        def __getattr__(
            self: "ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase",
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
        instance_to_wrap: "ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase":
        return (
            self._Cast_ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase(
                self
            )
        )
