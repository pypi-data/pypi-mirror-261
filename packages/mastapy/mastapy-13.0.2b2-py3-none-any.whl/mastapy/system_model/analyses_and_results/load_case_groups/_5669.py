"""SubGroupInSingleDesignState"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.system_model.analyses_and_results.load_case_groups import _5660
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SUB_GROUP_IN_SINGLE_DESIGN_STATE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups",
    "SubGroupInSingleDesignState",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import _6807
    from mastapy.system_model.analyses_and_results.load_case_groups import _5662, _5661


__docformat__ = "restructuredtext en"
__all__ = ("SubGroupInSingleDesignState",)


Self = TypeVar("Self", bound="SubGroupInSingleDesignState")


class SubGroupInSingleDesignState(_5660.AbstractDesignStateLoadCaseGroup):
    """SubGroupInSingleDesignState

    This is a mastapy class.
    """

    TYPE = _SUB_GROUP_IN_SINGLE_DESIGN_STATE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SubGroupInSingleDesignState")

    class _Cast_SubGroupInSingleDesignState:
        """Special nested class for casting SubGroupInSingleDesignState to subclasses."""

        def __init__(
            self: "SubGroupInSingleDesignState._Cast_SubGroupInSingleDesignState",
            parent: "SubGroupInSingleDesignState",
        ):
            self._parent = parent

        @property
        def abstract_design_state_load_case_group(
            self: "SubGroupInSingleDesignState._Cast_SubGroupInSingleDesignState",
        ) -> "_5660.AbstractDesignStateLoadCaseGroup":
            return self._parent._cast(_5660.AbstractDesignStateLoadCaseGroup)

        @property
        def abstract_static_load_case_group(
            self: "SubGroupInSingleDesignState._Cast_SubGroupInSingleDesignState",
        ) -> "_5662.AbstractStaticLoadCaseGroup":
            from mastapy.system_model.analyses_and_results.load_case_groups import _5662

            return self._parent._cast(_5662.AbstractStaticLoadCaseGroup)

        @property
        def abstract_load_case_group(
            self: "SubGroupInSingleDesignState._Cast_SubGroupInSingleDesignState",
        ) -> "_5661.AbstractLoadCaseGroup":
            from mastapy.system_model.analyses_and_results.load_case_groups import _5661

            return self._parent._cast(_5661.AbstractLoadCaseGroup)

        @property
        def sub_group_in_single_design_state(
            self: "SubGroupInSingleDesignState._Cast_SubGroupInSingleDesignState",
        ) -> "SubGroupInSingleDesignState":
            return self._parent

        def __getattr__(
            self: "SubGroupInSingleDesignState._Cast_SubGroupInSingleDesignState",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SubGroupInSingleDesignState.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @enforce_parameter_types
    def remove_static_load(self: Self, static_load: "_6807.StaticLoadCase"):
        """Method does not return.

        Args:
            static_load (mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase)
        """
        self.wrapped.RemoveStaticLoad(static_load.wrapped if static_load else None)

    @property
    def cast_to(
        self: Self,
    ) -> "SubGroupInSingleDesignState._Cast_SubGroupInSingleDesignState":
        return self._Cast_SubGroupInSingleDesignState(self)
