"""ParetoCylindricalGearSetOptimisationStrategyDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_set_pareto_optimiser import _927
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_CYLINDRICAL_GEAR_SET_OPTIMISATION_STRATEGY_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.GearSetParetoOptimiser",
    "ParetoCylindricalGearSetOptimisationStrategyDatabase",
)

if TYPE_CHECKING:
    from mastapy.math_utility.optimisation import _1554, _1542
    from mastapy.utility.databases import _1830, _1833, _1826


__docformat__ = "restructuredtext en"
__all__ = ("ParetoCylindricalGearSetOptimisationStrategyDatabase",)


Self = TypeVar("Self", bound="ParetoCylindricalGearSetOptimisationStrategyDatabase")


class ParetoCylindricalGearSetOptimisationStrategyDatabase(
    _927.ParetoCylindricalRatingOptimisationStrategyDatabase
):
    """ParetoCylindricalGearSetOptimisationStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _PARETO_CYLINDRICAL_GEAR_SET_OPTIMISATION_STRATEGY_DATABASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase"
    )

    class _Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase:
        """Special nested class for casting ParetoCylindricalGearSetOptimisationStrategyDatabase to subclasses."""

        def __init__(
            self: "ParetoCylindricalGearSetOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase",
            parent: "ParetoCylindricalGearSetOptimisationStrategyDatabase",
        ):
            self._parent = parent

        @property
        def pareto_cylindrical_rating_optimisation_strategy_database(
            self: "ParetoCylindricalGearSetOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase",
        ) -> "_927.ParetoCylindricalRatingOptimisationStrategyDatabase":
            return self._parent._cast(
                _927.ParetoCylindricalRatingOptimisationStrategyDatabase
            )

        @property
        def pareto_optimisation_strategy_database(
            self: "ParetoCylindricalGearSetOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase",
        ) -> "_1554.ParetoOptimisationStrategyDatabase":
            from mastapy.math_utility.optimisation import _1554

            return self._parent._cast(_1554.ParetoOptimisationStrategyDatabase)

        @property
        def design_space_search_strategy_database(
            self: "ParetoCylindricalGearSetOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase",
        ) -> "_1542.DesignSpaceSearchStrategyDatabase":
            from mastapy.math_utility.optimisation import _1542

            return self._parent._cast(_1542.DesignSpaceSearchStrategyDatabase)

        @property
        def named_database(
            self: "ParetoCylindricalGearSetOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase",
        ) -> "_1830.NamedDatabase":
            pass

            from mastapy.utility.databases import _1830

            return self._parent._cast(_1830.NamedDatabase)

        @property
        def sql_database(
            self: "ParetoCylindricalGearSetOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase",
        ) -> "_1833.SQLDatabase":
            pass

            from mastapy.utility.databases import _1833

            return self._parent._cast(_1833.SQLDatabase)

        @property
        def database(
            self: "ParetoCylindricalGearSetOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase",
        ) -> "_1826.Database":
            pass

            from mastapy.utility.databases import _1826

            return self._parent._cast(_1826.Database)

        @property
        def pareto_cylindrical_gear_set_optimisation_strategy_database(
            self: "ParetoCylindricalGearSetOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase",
        ) -> "ParetoCylindricalGearSetOptimisationStrategyDatabase":
            return self._parent

        def __getattr__(
            self: "ParetoCylindricalGearSetOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase",
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
        instance_to_wrap: "ParetoCylindricalGearSetOptimisationStrategyDatabase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ParetoCylindricalGearSetOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase":
        return self._Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase(self)
