"""DesignSpaceSearchStrategyDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.databases import _1830
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DESIGN_SPACE_SEARCH_STRATEGY_DATABASE = python_net_import(
    "SMT.MastaAPI.MathUtility.Optimisation", "DesignSpaceSearchStrategyDatabase"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_set_pareto_optimiser import (
        _919,
        _921,
        _922,
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
    from mastapy.math_utility.optimisation import _1554
    from mastapy.utility.databases import _1833, _1826


__docformat__ = "restructuredtext en"
__all__ = ("DesignSpaceSearchStrategyDatabase",)


Self = TypeVar("Self", bound="DesignSpaceSearchStrategyDatabase")


class DesignSpaceSearchStrategyDatabase(
    _1830.NamedDatabase["_1551.ParetoOptimisationStrategy"]
):
    """DesignSpaceSearchStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _DESIGN_SPACE_SEARCH_STRATEGY_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DesignSpaceSearchStrategyDatabase")

    class _Cast_DesignSpaceSearchStrategyDatabase:
        """Special nested class for casting DesignSpaceSearchStrategyDatabase to subclasses."""

        def __init__(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
            parent: "DesignSpaceSearchStrategyDatabase",
        ):
            self._parent = parent

        @property
        def named_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_1830.NamedDatabase":
            return self._parent._cast(_1830.NamedDatabase)

        @property
        def sql_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_1833.SQLDatabase":
            pass

            from mastapy.utility.databases import _1833

            return self._parent._cast(_1833.SQLDatabase)

        @property
        def database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_1826.Database":
            pass

            from mastapy.utility.databases import _1826

            return self._parent._cast(_1826.Database)

        @property
        def micro_geometry_design_space_search_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_919.MicroGeometryDesignSpaceSearchStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _919

            return self._parent._cast(
                _919.MicroGeometryDesignSpaceSearchStrategyDatabase
            )

        @property
        def micro_geometry_gear_set_design_space_search_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_921.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _921

            return self._parent._cast(
                _921.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase
            )

        @property
        def micro_geometry_gear_set_duty_cycle_design_space_search_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_922.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _922

            return self._parent._cast(
                _922.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase
            )

        @property
        def pareto_conical_rating_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_924.ParetoConicalRatingOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _924

            return self._parent._cast(
                _924.ParetoConicalRatingOptimisationStrategyDatabase
            )

        @property
        def pareto_cylindrical_gear_set_duty_cycle_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_925.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _925

            return self._parent._cast(
                _925.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_cylindrical_gear_set_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_926.ParetoCylindricalGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _926

            return self._parent._cast(
                _926.ParetoCylindricalGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_cylindrical_rating_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_927.ParetoCylindricalRatingOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _927

            return self._parent._cast(
                _927.ParetoCylindricalRatingOptimisationStrategyDatabase
            )

        @property
        def pareto_face_gear_set_duty_cycle_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_928.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _928

            return self._parent._cast(
                _928.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_face_gear_set_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_929.ParetoFaceGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _929

            return self._parent._cast(
                _929.ParetoFaceGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_face_rating_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_930.ParetoFaceRatingOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _930

            return self._parent._cast(_930.ParetoFaceRatingOptimisationStrategyDatabase)

        @property
        def pareto_hypoid_gear_set_duty_cycle_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_931.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _931

            return self._parent._cast(
                _931.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_hypoid_gear_set_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_932.ParetoHypoidGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _932

            return self._parent._cast(
                _932.ParetoHypoidGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_spiral_bevel_gear_set_duty_cycle_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_934.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _934

            return self._parent._cast(
                _934.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_spiral_bevel_gear_set_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_935.ParetoSpiralBevelGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _935

            return self._parent._cast(
                _935.ParetoSpiralBevelGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_straight_bevel_gear_set_duty_cycle_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_936.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _936

            return self._parent._cast(
                _936.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_straight_bevel_gear_set_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_937.ParetoStraightBevelGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _937

            return self._parent._cast(
                _937.ParetoStraightBevelGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_1554.ParetoOptimisationStrategyDatabase":
            from mastapy.math_utility.optimisation import _1554

            return self._parent._cast(_1554.ParetoOptimisationStrategyDatabase)

        @property
        def design_space_search_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "DesignSpaceSearchStrategyDatabase":
            return self._parent

        def __getattr__(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
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
        self: Self, instance_to_wrap: "DesignSpaceSearchStrategyDatabase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase":
        return self._Cast_DesignSpaceSearchStrategyDatabase(self)
