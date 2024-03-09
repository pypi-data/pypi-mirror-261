"""ParetoOptimisationStrategyDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.math_utility.optimisation import _1542
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_OPTIMISATION_STRATEGY_DATABASE = python_net_import(
    "SMT.MastaAPI.MathUtility.Optimisation", "ParetoOptimisationStrategyDatabase"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_set_pareto_optimiser import (
        _924,
        _925,
        _926,
        _927,
        _928,
        _929,
        _930,
        _931,
        _932,
        _934,
        _935,
        _936,
        _937,
    )
    from mastapy.utility.databases import _1830, _1833, _1826


__docformat__ = "restructuredtext en"
__all__ = ("ParetoOptimisationStrategyDatabase",)


Self = TypeVar("Self", bound="ParetoOptimisationStrategyDatabase")


class ParetoOptimisationStrategyDatabase(_1542.DesignSpaceSearchStrategyDatabase):
    """ParetoOptimisationStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _PARETO_OPTIMISATION_STRATEGY_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ParetoOptimisationStrategyDatabase")

    class _Cast_ParetoOptimisationStrategyDatabase:
        """Special nested class for casting ParetoOptimisationStrategyDatabase to subclasses."""

        def __init__(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
            parent: "ParetoOptimisationStrategyDatabase",
        ):
            self._parent = parent

        @property
        def design_space_search_strategy_database(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
        ) -> "_1542.DesignSpaceSearchStrategyDatabase":
            return self._parent._cast(_1542.DesignSpaceSearchStrategyDatabase)

        @property
        def named_database(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
        ) -> "_1830.NamedDatabase":
            pass

            from mastapy.utility.databases import _1830

            return self._parent._cast(_1830.NamedDatabase)

        @property
        def sql_database(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
        ) -> "_1833.SQLDatabase":
            pass

            from mastapy.utility.databases import _1833

            return self._parent._cast(_1833.SQLDatabase)

        @property
        def database(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
        ) -> "_1826.Database":
            pass

            from mastapy.utility.databases import _1826

            return self._parent._cast(_1826.Database)

        @property
        def pareto_conical_rating_optimisation_strategy_database(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
        ) -> "_924.ParetoConicalRatingOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _924

            return self._parent._cast(
                _924.ParetoConicalRatingOptimisationStrategyDatabase
            )

        @property
        def pareto_cylindrical_gear_set_duty_cycle_optimisation_strategy_database(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
        ) -> "_925.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _925

            return self._parent._cast(
                _925.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_cylindrical_gear_set_optimisation_strategy_database(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
        ) -> "_926.ParetoCylindricalGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _926

            return self._parent._cast(
                _926.ParetoCylindricalGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_cylindrical_rating_optimisation_strategy_database(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
        ) -> "_927.ParetoCylindricalRatingOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _927

            return self._parent._cast(
                _927.ParetoCylindricalRatingOptimisationStrategyDatabase
            )

        @property
        def pareto_face_gear_set_duty_cycle_optimisation_strategy_database(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
        ) -> "_928.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _928

            return self._parent._cast(
                _928.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_face_gear_set_optimisation_strategy_database(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
        ) -> "_929.ParetoFaceGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _929

            return self._parent._cast(
                _929.ParetoFaceGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_face_rating_optimisation_strategy_database(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
        ) -> "_930.ParetoFaceRatingOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _930

            return self._parent._cast(_930.ParetoFaceRatingOptimisationStrategyDatabase)

        @property
        def pareto_hypoid_gear_set_duty_cycle_optimisation_strategy_database(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
        ) -> "_931.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _931

            return self._parent._cast(
                _931.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_hypoid_gear_set_optimisation_strategy_database(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
        ) -> "_932.ParetoHypoidGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _932

            return self._parent._cast(
                _932.ParetoHypoidGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_spiral_bevel_gear_set_duty_cycle_optimisation_strategy_database(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
        ) -> "_934.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _934

            return self._parent._cast(
                _934.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_spiral_bevel_gear_set_optimisation_strategy_database(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
        ) -> "_935.ParetoSpiralBevelGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _935

            return self._parent._cast(
                _935.ParetoSpiralBevelGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_straight_bevel_gear_set_duty_cycle_optimisation_strategy_database(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
        ) -> "_936.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _936

            return self._parent._cast(
                _936.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_straight_bevel_gear_set_optimisation_strategy_database(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
        ) -> "_937.ParetoStraightBevelGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _937

            return self._parent._cast(
                _937.ParetoStraightBevelGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_optimisation_strategy_database(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
        ) -> "ParetoOptimisationStrategyDatabase":
            return self._parent

        def __getattr__(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
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
        self: Self, instance_to_wrap: "ParetoOptimisationStrategyDatabase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase":
        return self._Cast_ParetoOptimisationStrategyDatabase(self)
