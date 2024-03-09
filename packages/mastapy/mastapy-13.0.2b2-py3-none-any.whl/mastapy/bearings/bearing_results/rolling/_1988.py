"""LoadedAngularContactThrustBallBearingResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling import _1985
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ANGULAR_CONTACT_THRUST_BALL_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedAngularContactThrustBallBearingResults",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2004, _2035
    from mastapy.bearings.bearing_results import _1956, _1959, _1951
    from mastapy.bearings import _1877


__docformat__ = "restructuredtext en"
__all__ = ("LoadedAngularContactThrustBallBearingResults",)


Self = TypeVar("Self", bound="LoadedAngularContactThrustBallBearingResults")


class LoadedAngularContactThrustBallBearingResults(
    _1985.LoadedAngularContactBallBearingResults
):
    """LoadedAngularContactThrustBallBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_ANGULAR_CONTACT_THRUST_BALL_BEARING_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedAngularContactThrustBallBearingResults"
    )

    class _Cast_LoadedAngularContactThrustBallBearingResults:
        """Special nested class for casting LoadedAngularContactThrustBallBearingResults to subclasses."""

        def __init__(
            self: "LoadedAngularContactThrustBallBearingResults._Cast_LoadedAngularContactThrustBallBearingResults",
            parent: "LoadedAngularContactThrustBallBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_angular_contact_ball_bearing_results(
            self: "LoadedAngularContactThrustBallBearingResults._Cast_LoadedAngularContactThrustBallBearingResults",
        ) -> "_1985.LoadedAngularContactBallBearingResults":
            return self._parent._cast(_1985.LoadedAngularContactBallBearingResults)

        @property
        def loaded_ball_bearing_results(
            self: "LoadedAngularContactThrustBallBearingResults._Cast_LoadedAngularContactThrustBallBearingResults",
        ) -> "_2004.LoadedBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2004

            return self._parent._cast(_2004.LoadedBallBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedAngularContactThrustBallBearingResults._Cast_LoadedAngularContactThrustBallBearingResults",
        ) -> "_2035.LoadedRollingBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2035

            return self._parent._cast(_2035.LoadedRollingBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedAngularContactThrustBallBearingResults._Cast_LoadedAngularContactThrustBallBearingResults",
        ) -> "_1956.LoadedDetailedBearingResults":
            from mastapy.bearings.bearing_results import _1956

            return self._parent._cast(_1956.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedAngularContactThrustBallBearingResults._Cast_LoadedAngularContactThrustBallBearingResults",
        ) -> "_1959.LoadedNonLinearBearingResults":
            from mastapy.bearings.bearing_results import _1959

            return self._parent._cast(_1959.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedAngularContactThrustBallBearingResults._Cast_LoadedAngularContactThrustBallBearingResults",
        ) -> "_1951.LoadedBearingResults":
            from mastapy.bearings.bearing_results import _1951

            return self._parent._cast(_1951.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedAngularContactThrustBallBearingResults._Cast_LoadedAngularContactThrustBallBearingResults",
        ) -> "_1877.BearingLoadCaseResultsLightweight":
            from mastapy.bearings import _1877

            return self._parent._cast(_1877.BearingLoadCaseResultsLightweight)

        @property
        def loaded_angular_contact_thrust_ball_bearing_results(
            self: "LoadedAngularContactThrustBallBearingResults._Cast_LoadedAngularContactThrustBallBearingResults",
        ) -> "LoadedAngularContactThrustBallBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedAngularContactThrustBallBearingResults._Cast_LoadedAngularContactThrustBallBearingResults",
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
        instance_to_wrap: "LoadedAngularContactThrustBallBearingResults.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedAngularContactThrustBallBearingResults._Cast_LoadedAngularContactThrustBallBearingResults":
        return self._Cast_LoadedAngularContactThrustBallBearingResults(self)
