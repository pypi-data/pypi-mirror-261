"""CouplingConnectionLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6914
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CouplingConnectionLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2348
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6835,
        _6841,
        _6932,
        _6959,
        _6975,
        _6852,
    )
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionLoadCase",)


Self = TypeVar("Self", bound="CouplingConnectionLoadCase")


class CouplingConnectionLoadCase(_6914.InterMountableComponentConnectionLoadCase):
    """CouplingConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingConnectionLoadCase")

    class _Cast_CouplingConnectionLoadCase:
        """Special nested class for casting CouplingConnectionLoadCase to subclasses."""

        def __init__(
            self: "CouplingConnectionLoadCase._Cast_CouplingConnectionLoadCase",
            parent: "CouplingConnectionLoadCase",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_load_case(
            self: "CouplingConnectionLoadCase._Cast_CouplingConnectionLoadCase",
        ) -> "_6914.InterMountableComponentConnectionLoadCase":
            return self._parent._cast(_6914.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(
            self: "CouplingConnectionLoadCase._Cast_CouplingConnectionLoadCase",
        ) -> "_6852.ConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6852

            return self._parent._cast(_6852.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "CouplingConnectionLoadCase._Cast_CouplingConnectionLoadCase",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingConnectionLoadCase._Cast_CouplingConnectionLoadCase",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionLoadCase._Cast_CouplingConnectionLoadCase",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def clutch_connection_load_case(
            self: "CouplingConnectionLoadCase._Cast_CouplingConnectionLoadCase",
        ) -> "_6835.ClutchConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6835

            return self._parent._cast(_6835.ClutchConnectionLoadCase)

        @property
        def concept_coupling_connection_load_case(
            self: "CouplingConnectionLoadCase._Cast_CouplingConnectionLoadCase",
        ) -> "_6841.ConceptCouplingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6841

            return self._parent._cast(_6841.ConceptCouplingConnectionLoadCase)

        @property
        def part_to_part_shear_coupling_connection_load_case(
            self: "CouplingConnectionLoadCase._Cast_CouplingConnectionLoadCase",
        ) -> "_6932.PartToPartShearCouplingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6932

            return self._parent._cast(_6932.PartToPartShearCouplingConnectionLoadCase)

        @property
        def spring_damper_connection_load_case(
            self: "CouplingConnectionLoadCase._Cast_CouplingConnectionLoadCase",
        ) -> "_6959.SpringDamperConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6959

            return self._parent._cast(_6959.SpringDamperConnectionLoadCase)

        @property
        def torque_converter_connection_load_case(
            self: "CouplingConnectionLoadCase._Cast_CouplingConnectionLoadCase",
        ) -> "_6975.TorqueConverterConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6975

            return self._parent._cast(_6975.TorqueConverterConnectionLoadCase)

        @property
        def coupling_connection_load_case(
            self: "CouplingConnectionLoadCase._Cast_CouplingConnectionLoadCase",
        ) -> "CouplingConnectionLoadCase":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionLoadCase._Cast_CouplingConnectionLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingConnectionLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2348.CouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.CouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingConnectionLoadCase._Cast_CouplingConnectionLoadCase":
        return self._Cast_CouplingConnectionLoadCase(self)
