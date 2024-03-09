"""ConicalGearSetLoadDistributionAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.ltca import _846
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_LOAD_DISTRIBUTION_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.LTCA.Conical", "ConicalGearSetLoadDistributionAnalysis"
)

if TYPE_CHECKING:
    from mastapy.gears.analysis import _1229, _1230, _1227, _1218


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetLoadDistributionAnalysis",)


Self = TypeVar("Self", bound="ConicalGearSetLoadDistributionAnalysis")


class ConicalGearSetLoadDistributionAnalysis(_846.GearSetLoadDistributionAnalysis):
    """ConicalGearSetLoadDistributionAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_LOAD_DISTRIBUTION_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearSetLoadDistributionAnalysis"
    )

    class _Cast_ConicalGearSetLoadDistributionAnalysis:
        """Special nested class for casting ConicalGearSetLoadDistributionAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearSetLoadDistributionAnalysis._Cast_ConicalGearSetLoadDistributionAnalysis",
            parent: "ConicalGearSetLoadDistributionAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_load_distribution_analysis(
            self: "ConicalGearSetLoadDistributionAnalysis._Cast_ConicalGearSetLoadDistributionAnalysis",
        ) -> "_846.GearSetLoadDistributionAnalysis":
            return self._parent._cast(_846.GearSetLoadDistributionAnalysis)

        @property
        def gear_set_implementation_analysis(
            self: "ConicalGearSetLoadDistributionAnalysis._Cast_ConicalGearSetLoadDistributionAnalysis",
        ) -> "_1229.GearSetImplementationAnalysis":
            from mastapy.gears.analysis import _1229

            return self._parent._cast(_1229.GearSetImplementationAnalysis)

        @property
        def gear_set_implementation_analysis_abstract(
            self: "ConicalGearSetLoadDistributionAnalysis._Cast_ConicalGearSetLoadDistributionAnalysis",
        ) -> "_1230.GearSetImplementationAnalysisAbstract":
            from mastapy.gears.analysis import _1230

            return self._parent._cast(_1230.GearSetImplementationAnalysisAbstract)

        @property
        def gear_set_design_analysis(
            self: "ConicalGearSetLoadDistributionAnalysis._Cast_ConicalGearSetLoadDistributionAnalysis",
        ) -> "_1227.GearSetDesignAnalysis":
            from mastapy.gears.analysis import _1227

            return self._parent._cast(_1227.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(
            self: "ConicalGearSetLoadDistributionAnalysis._Cast_ConicalGearSetLoadDistributionAnalysis",
        ) -> "_1218.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1218

            return self._parent._cast(_1218.AbstractGearSetAnalysis)

        @property
        def conical_gear_set_load_distribution_analysis(
            self: "ConicalGearSetLoadDistributionAnalysis._Cast_ConicalGearSetLoadDistributionAnalysis",
        ) -> "ConicalGearSetLoadDistributionAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetLoadDistributionAnalysis._Cast_ConicalGearSetLoadDistributionAnalysis",
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
        self: Self, instance_to_wrap: "ConicalGearSetLoadDistributionAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearSetLoadDistributionAnalysis._Cast_ConicalGearSetLoadDistributionAnalysis":
        return self._Cast_ConicalGearSetLoadDistributionAnalysis(self)
