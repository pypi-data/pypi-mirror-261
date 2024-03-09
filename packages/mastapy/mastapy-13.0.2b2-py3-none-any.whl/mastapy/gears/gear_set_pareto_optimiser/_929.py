"""ParetoFaceGearSetOptimisationStrategyDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_set_pareto_optimiser import _930
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_FACE_GEAR_SET_OPTIMISATION_STRATEGY_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.GearSetParetoOptimiser",
    "ParetoFaceGearSetOptimisationStrategyDatabase",
)

if TYPE_CHECKING:
    from mastapy.math_utility.optimisation import _1554, _1542
    from mastapy.utility.databases import _1830, _1833, _1826


__docformat__ = "restructuredtext en"
__all__ = ("ParetoFaceGearSetOptimisationStrategyDatabase",)


Self = TypeVar("Self", bound="ParetoFaceGearSetOptimisationStrategyDatabase")


class ParetoFaceGearSetOptimisationStrategyDatabase(
    _930.ParetoFaceRatingOptimisationStrategyDatabase
):
    """ParetoFaceGearSetOptimisationStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _PARETO_FACE_GEAR_SET_OPTIMISATION_STRATEGY_DATABASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ParetoFaceGearSetOptimisationStrategyDatabase"
    )

    class _Cast_ParetoFaceGearSetOptimisationStrategyDatabase:
        """Special nested class for casting ParetoFaceGearSetOptimisationStrategyDatabase to subclasses."""

        def __init__(
            self: "ParetoFaceGearSetOptimisationStrategyDatabase._Cast_ParetoFaceGearSetOptimisationStrategyDatabase",
            parent: "ParetoFaceGearSetOptimisationStrategyDatabase",
        ):
            self._parent = parent

        @property
        def pareto_face_rating_optimisation_strategy_database(
            self: "ParetoFaceGearSetOptimisationStrategyDatabase._Cast_ParetoFaceGearSetOptimisationStrategyDatabase",
        ) -> "_930.ParetoFaceRatingOptimisationStrategyDatabase":
            return self._parent._cast(_930.ParetoFaceRatingOptimisationStrategyDatabase)

        @property
        def pareto_optimisation_strategy_database(
            self: "ParetoFaceGearSetOptimisationStrategyDatabase._Cast_ParetoFaceGearSetOptimisationStrategyDatabase",
        ) -> "_1554.ParetoOptimisationStrategyDatabase":
            from mastapy.math_utility.optimisation import _1554

            return self._parent._cast(_1554.ParetoOptimisationStrategyDatabase)

        @property
        def design_space_search_strategy_database(
            self: "ParetoFaceGearSetOptimisationStrategyDatabase._Cast_ParetoFaceGearSetOptimisationStrategyDatabase",
        ) -> "_1542.DesignSpaceSearchStrategyDatabase":
            from mastapy.math_utility.optimisation import _1542

            return self._parent._cast(_1542.DesignSpaceSearchStrategyDatabase)

        @property
        def named_database(
            self: "ParetoFaceGearSetOptimisationStrategyDatabase._Cast_ParetoFaceGearSetOptimisationStrategyDatabase",
        ) -> "_1830.NamedDatabase":
            pass

            from mastapy.utility.databases import _1830

            return self._parent._cast(_1830.NamedDatabase)

        @property
        def sql_database(
            self: "ParetoFaceGearSetOptimisationStrategyDatabase._Cast_ParetoFaceGearSetOptimisationStrategyDatabase",
        ) -> "_1833.SQLDatabase":
            pass

            from mastapy.utility.databases import _1833

            return self._parent._cast(_1833.SQLDatabase)

        @property
        def database(
            self: "ParetoFaceGearSetOptimisationStrategyDatabase._Cast_ParetoFaceGearSetOptimisationStrategyDatabase",
        ) -> "_1826.Database":
            pass

            from mastapy.utility.databases import _1826

            return self._parent._cast(_1826.Database)

        @property
        def pareto_face_gear_set_optimisation_strategy_database(
            self: "ParetoFaceGearSetOptimisationStrategyDatabase._Cast_ParetoFaceGearSetOptimisationStrategyDatabase",
        ) -> "ParetoFaceGearSetOptimisationStrategyDatabase":
            return self._parent

        def __getattr__(
            self: "ParetoFaceGearSetOptimisationStrategyDatabase._Cast_ParetoFaceGearSetOptimisationStrategyDatabase",
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
        instance_to_wrap: "ParetoFaceGearSetOptimisationStrategyDatabase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ParetoFaceGearSetOptimisationStrategyDatabase._Cast_ParetoFaceGearSetOptimisationStrategyDatabase":
        return self._Cast_ParetoFaceGearSetOptimisationStrategyDatabase(self)
