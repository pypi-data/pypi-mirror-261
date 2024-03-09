"""KlingelnbergCycloPalloidConicalGear"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.part_model.gears import _2525
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "KlingelnbergCycloPalloidConicalGear"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2540, _2542, _2532
    from mastapy.system_model.part_model import _2466, _2446, _2470
    from mastapy.system_model import _2205


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGear",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGear")


class KlingelnbergCycloPalloidConicalGear(_2525.ConicalGear):
    """KlingelnbergCycloPalloidConicalGear

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_KlingelnbergCycloPalloidConicalGear")

    class _Cast_KlingelnbergCycloPalloidConicalGear:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGear to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGear._Cast_KlingelnbergCycloPalloidConicalGear",
            parent: "KlingelnbergCycloPalloidConicalGear",
        ):
            self._parent = parent

        @property
        def conical_gear(
            self: "KlingelnbergCycloPalloidConicalGear._Cast_KlingelnbergCycloPalloidConicalGear",
        ) -> "_2525.ConicalGear":
            return self._parent._cast(_2525.ConicalGear)

        @property
        def gear(
            self: "KlingelnbergCycloPalloidConicalGear._Cast_KlingelnbergCycloPalloidConicalGear",
        ) -> "_2532.Gear":
            from mastapy.system_model.part_model.gears import _2532

            return self._parent._cast(_2532.Gear)

        @property
        def mountable_component(
            self: "KlingelnbergCycloPalloidConicalGear._Cast_KlingelnbergCycloPalloidConicalGear",
        ) -> "_2466.MountableComponent":
            from mastapy.system_model.part_model import _2466

            return self._parent._cast(_2466.MountableComponent)

        @property
        def component(
            self: "KlingelnbergCycloPalloidConicalGear._Cast_KlingelnbergCycloPalloidConicalGear",
        ) -> "_2446.Component":
            from mastapy.system_model.part_model import _2446

            return self._parent._cast(_2446.Component)

        @property
        def part(
            self: "KlingelnbergCycloPalloidConicalGear._Cast_KlingelnbergCycloPalloidConicalGear",
        ) -> "_2470.Part":
            from mastapy.system_model.part_model import _2470

            return self._parent._cast(_2470.Part)

        @property
        def design_entity(
            self: "KlingelnbergCycloPalloidConicalGear._Cast_KlingelnbergCycloPalloidConicalGear",
        ) -> "_2205.DesignEntity":
            from mastapy.system_model import _2205

            return self._parent._cast(_2205.DesignEntity)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear(
            self: "KlingelnbergCycloPalloidConicalGear._Cast_KlingelnbergCycloPalloidConicalGear",
        ) -> "_2540.KlingelnbergCycloPalloidHypoidGear":
            from mastapy.system_model.part_model.gears import _2540

            return self._parent._cast(_2540.KlingelnbergCycloPalloidHypoidGear)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear(
            self: "KlingelnbergCycloPalloidConicalGear._Cast_KlingelnbergCycloPalloidConicalGear",
        ) -> "_2542.KlingelnbergCycloPalloidSpiralBevelGear":
            from mastapy.system_model.part_model.gears import _2542

            return self._parent._cast(_2542.KlingelnbergCycloPalloidSpiralBevelGear)

        @property
        def klingelnberg_cyclo_palloid_conical_gear(
            self: "KlingelnbergCycloPalloidConicalGear._Cast_KlingelnbergCycloPalloidConicalGear",
        ) -> "KlingelnbergCycloPalloidConicalGear":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGear._Cast_KlingelnbergCycloPalloidConicalGear",
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
        self: Self, instance_to_wrap: "KlingelnbergCycloPalloidConicalGear.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> (
        "KlingelnbergCycloPalloidConicalGear._Cast_KlingelnbergCycloPalloidConicalGear"
    ):
        return self._Cast_KlingelnbergCycloPalloidConicalGear(self)
