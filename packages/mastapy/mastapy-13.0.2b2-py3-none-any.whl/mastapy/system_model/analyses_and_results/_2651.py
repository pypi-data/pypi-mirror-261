"""ConnectionAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results import _2655
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults", "ConnectionAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2690,
        _2691,
        _2701,
        _2703,
        _2708,
        _2713,
        _2716,
        _2719,
        _2722,
        _2726,
        _2729,
        _2731,
        _2734,
        _2738,
        _2739,
        _2741,
        _2742,
        _2743,
        _2756,
        _2761,
        _2765,
        _2769,
        _2770,
        _2773,
        _2776,
        _2788,
        _2791,
        _2797,
        _2800,
        _2807,
        _2809,
        _2812,
        _2815,
        _2818,
        _2830,
        _2838,
        _2841,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _2988,
        _2989,
        _2994,
        _2996,
        _3001,
        _3006,
        _3009,
        _3011,
        _3014,
        _3017,
        _3020,
        _3022,
        _3025,
        _3029,
        _3030,
        _3032,
        _3039,
        _3044,
        _3048,
        _3051,
        _3052,
        _3055,
        _3058,
        _3066,
        _3069,
        _3076,
        _3078,
        _3083,
        _3085,
        _3088,
        _3094,
        _3097,
        _3106,
        _3112,
        _3115,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3250,
        _3251,
        _3256,
        _3258,
        _3263,
        _3268,
        _3271,
        _3273,
        _3276,
        _3279,
        _3282,
        _3284,
        _3287,
        _3291,
        _3292,
        _3294,
        _3300,
        _3305,
        _3309,
        _3312,
        _3313,
        _3316,
        _3319,
        _3327,
        _3330,
        _3337,
        _3339,
        _3344,
        _3346,
        _3349,
        _3353,
        _3356,
        _3365,
        _3371,
        _3374,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3509,
        _3510,
        _3515,
        _3517,
        _3522,
        _3527,
        _3530,
        _3532,
        _3535,
        _3538,
        _3541,
        _3543,
        _3546,
        _3550,
        _3551,
        _3553,
        _3559,
        _3564,
        _3568,
        _3571,
        _3572,
        _3575,
        _3578,
        _3586,
        _3589,
        _3596,
        _3598,
        _3603,
        _3605,
        _3608,
        _3612,
        _3615,
        _3624,
        _3630,
        _3633,
    )
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3768,
        _3769,
        _3774,
        _3776,
        _3781,
        _3786,
        _3789,
        _3791,
        _3794,
        _3797,
        _3800,
        _3802,
        _3806,
        _3810,
        _3811,
        _3813,
        _3820,
        _3825,
        _3829,
        _3832,
        _3833,
        _3836,
        _3839,
        _3847,
        _3850,
        _3857,
        _3859,
        _3864,
        _3866,
        _3869,
        _3875,
        _3878,
        _3887,
        _3893,
        _3896,
    )
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4037,
        _4038,
        _4043,
        _4045,
        _4050,
        _4055,
        _4058,
        _4060,
        _4063,
        _4066,
        _4069,
        _4071,
        _4074,
        _4078,
        _4079,
        _4082,
        _4088,
        _4095,
        _4099,
        _4102,
        _4103,
        _4106,
        _4109,
        _4117,
        _4120,
        _4129,
        _4131,
        _4136,
        _4138,
        _4141,
        _4144,
        _4147,
        _4157,
        _4163,
        _4166,
    )
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4301,
        _4302,
        _4307,
        _4309,
        _4314,
        _4319,
        _4322,
        _4324,
        _4327,
        _4330,
        _4333,
        _4335,
        _4338,
        _4342,
        _4344,
        _4345,
        _4358,
        _4363,
        _4367,
        _4370,
        _4371,
        _4374,
        _4377,
        _4396,
        _4399,
        _4406,
        _4408,
        _4413,
        _4415,
        _4418,
        _4421,
        _4424,
        _4433,
        _4439,
        _4442,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4577,
        _4578,
        _4583,
        _4585,
        _4590,
        _4595,
        _4598,
        _4600,
        _4603,
        _4606,
        _4609,
        _4612,
        _4615,
        _4619,
        _4621,
        _4622,
        _4631,
        _4637,
        _4641,
        _4644,
        _4645,
        _4648,
        _4651,
        _4665,
        _4668,
        _4675,
        _4677,
        _4683,
        _4685,
        _4688,
        _4691,
        _4694,
        _4703,
        _4712,
        _4715,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4862,
        _4863,
        _4868,
        _4870,
        _4875,
        _4880,
        _4883,
        _4885,
        _4888,
        _4891,
        _4894,
        _4896,
        _4899,
        _4903,
        _4905,
        _4906,
        _4913,
        _4918,
        _4922,
        _4925,
        _4926,
        _4929,
        _4932,
        _4941,
        _4944,
        _4951,
        _4953,
        _4958,
        _4960,
        _4963,
        _4966,
        _4969,
        _4978,
        _4984,
        _4987,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5122,
        _5123,
        _5128,
        _5130,
        _5135,
        _5140,
        _5143,
        _5145,
        _5148,
        _5151,
        _5154,
        _5156,
        _5159,
        _5163,
        _5165,
        _5166,
        _5172,
        _5177,
        _5181,
        _5184,
        _5185,
        _5188,
        _5191,
        _5200,
        _5203,
        _5210,
        _5212,
        _5217,
        _5219,
        _5222,
        _5225,
        _5228,
        _5237,
        _5243,
        _5246,
    )
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5381,
        _5382,
        _5389,
        _5391,
        _5396,
        _5401,
        _5405,
        _5407,
        _5410,
        _5413,
        _5416,
        _5418,
        _5421,
        _5425,
        _5427,
        _5428,
        _5434,
        _5439,
        _5444,
        _5451,
        _5452,
        _5455,
        _5458,
        _5470,
        _5473,
        _5480,
        _5482,
        _5489,
        _5492,
        _5495,
        _5498,
        _5501,
        _5510,
        _5519,
        _5522,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5684,
        _5686,
        _5690,
        _5693,
        _5698,
        _5702,
        _5705,
        _5708,
        _5712,
        _5715,
        _5717,
        _5719,
        _5722,
        _5726,
        _5728,
        _5730,
        _5750,
        _5757,
        _5774,
        _5776,
        _5778,
        _5781,
        _5784,
        _5791,
        _5795,
        _5803,
        _5805,
        _5810,
        _5815,
        _5817,
        _5822,
        _5825,
        _5833,
        _5841,
        _5844,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6013,
        _6015,
        _6019,
        _6022,
        _6027,
        _6031,
        _6034,
        _6036,
        _6040,
        _6043,
        _6045,
        _6047,
        _6050,
        _6054,
        _6056,
        _6058,
        _6064,
        _6069,
        _6074,
        _6076,
        _6078,
        _6081,
        _6084,
        _6092,
        _6095,
        _6102,
        _6104,
        _6109,
        _6112,
        _6114,
        _6118,
        _6121,
        _6129,
        _6136,
        _6139,
    )
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6282,
        _6284,
        _6288,
        _6291,
        _6296,
        _6300,
        _6303,
        _6305,
        _6309,
        _6312,
        _6314,
        _6316,
        _6319,
        _6323,
        _6325,
        _6327,
        _6335,
        _6340,
        _6344,
        _6346,
        _6348,
        _6351,
        _6354,
        _6361,
        _6364,
        _6371,
        _6373,
        _6378,
        _6381,
        _6383,
        _6387,
        _6390,
        _6398,
        _6405,
        _6408,
    )
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6548,
        _6550,
        _6554,
        _6557,
        _6562,
        _6566,
        _6569,
        _6571,
        _6575,
        _6578,
        _6580,
        _6582,
        _6588,
        _6592,
        _6594,
        _6596,
        _6602,
        _6607,
        _6611,
        _6613,
        _6615,
        _6618,
        _6621,
        _6628,
        _6631,
        _6638,
        _6640,
        _6645,
        _6648,
        _6650,
        _6654,
        _6657,
        _6665,
        _6672,
        _6675,
    )
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6812,
        _6817,
        _6823,
        _6826,
        _6831,
        _6835,
        _6839,
        _6841,
        _6845,
        _6849,
        _6852,
        _6854,
        _6857,
        _6861,
        _6863,
        _6866,
        _6888,
        _6895,
        _6909,
        _6914,
        _6916,
        _6919,
        _6922,
        _6932,
        _6935,
        _6947,
        _6949,
        _6954,
        _6957,
        _6959,
        _6963,
        _6966,
        _6975,
        _6986,
        _6989,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7011,
        _7017,
        _7022,
        _7025,
        _7030,
        _7035,
        _7037,
        _7040,
        _7043,
        _7046,
        _7048,
        _7051,
        _7054,
        _7058,
        _7059,
        _7061,
        _7067,
        _7072,
        _7077,
        _7079,
        _7081,
        _7084,
        _7087,
        _7095,
        _7097,
        _7104,
        _7107,
        _7111,
        _7114,
        _7117,
        _7120,
        _7123,
        _7132,
        _7138,
        _7141,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7275,
        _7280,
        _7284,
        _7287,
        _7292,
        _7297,
        _7299,
        _7302,
        _7305,
        _7308,
        _7310,
        _7314,
        _7317,
        _7321,
        _7322,
        _7324,
        _7331,
        _7336,
        _7340,
        _7342,
        _7344,
        _7347,
        _7350,
        _7359,
        _7361,
        _7368,
        _7371,
        _7375,
        _7378,
        _7381,
        _7384,
        _7387,
        _7396,
        _7403,
        _7406,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7540,
        _7542,
        _7543,
        _7544,
    )
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionAnalysis",)


Self = TypeVar("Self", bound="ConnectionAnalysis")


class ConnectionAnalysis(_2655.DesignEntitySingleContextAnalysis):
    """ConnectionAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTION_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectionAnalysis")

    class _Cast_ConnectionAnalysis:
        """Special nested class for casting ConnectionAnalysis to subclasses."""

        def __init__(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
            parent: "ConnectionAnalysis",
        ):
            self._parent = parent

        @property
        def design_entity_single_context_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2690.AbstractShaftToMountableComponentConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2690,
            )

            return self._parent._cast(
                _2690.AbstractShaftToMountableComponentConnectionSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_mesh_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2691.AGMAGleasonConicalGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2691,
            )

            return self._parent._cast(_2691.AGMAGleasonConicalGearMeshSystemDeflection)

        @property
        def belt_connection_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2701.BeltConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2701,
            )

            return self._parent._cast(_2701.BeltConnectionSystemDeflection)

        @property
        def bevel_differential_gear_mesh_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2703.BevelDifferentialGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2703,
            )

            return self._parent._cast(_2703.BevelDifferentialGearMeshSystemDeflection)

        @property
        def bevel_gear_mesh_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2708.BevelGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2708,
            )

            return self._parent._cast(_2708.BevelGearMeshSystemDeflection)

        @property
        def clutch_connection_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2713.ClutchConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2713,
            )

            return self._parent._cast(_2713.ClutchConnectionSystemDeflection)

        @property
        def coaxial_connection_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2716.CoaxialConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2716,
            )

            return self._parent._cast(_2716.CoaxialConnectionSystemDeflection)

        @property
        def concept_coupling_connection_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2719.ConceptCouplingConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2719,
            )

            return self._parent._cast(_2719.ConceptCouplingConnectionSystemDeflection)

        @property
        def concept_gear_mesh_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2722.ConceptGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2722,
            )

            return self._parent._cast(_2722.ConceptGearMeshSystemDeflection)

        @property
        def conical_gear_mesh_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2726.ConicalGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2726,
            )

            return self._parent._cast(_2726.ConicalGearMeshSystemDeflection)

        @property
        def connection_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2729.ConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2729,
            )

            return self._parent._cast(_2729.ConnectionSystemDeflection)

        @property
        def coupling_connection_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2731.CouplingConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2731,
            )

            return self._parent._cast(_2731.CouplingConnectionSystemDeflection)

        @property
        def cvt_belt_connection_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2734.CVTBeltConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2734,
            )

            return self._parent._cast(_2734.CVTBeltConnectionSystemDeflection)

        @property
        def cycloidal_disc_central_bearing_connection_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2738.CycloidalDiscCentralBearingConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2738,
            )

            return self._parent._cast(
                _2738.CycloidalDiscCentralBearingConnectionSystemDeflection
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2739.CycloidalDiscPlanetaryBearingConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2739,
            )

            return self._parent._cast(
                _2739.CycloidalDiscPlanetaryBearingConnectionSystemDeflection
            )

        @property
        def cylindrical_gear_mesh_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2741.CylindricalGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2741,
            )

            return self._parent._cast(_2741.CylindricalGearMeshSystemDeflection)

        @property
        def cylindrical_gear_mesh_system_deflection_timestep(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2742.CylindricalGearMeshSystemDeflectionTimestep":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2742,
            )

            return self._parent._cast(_2742.CylindricalGearMeshSystemDeflectionTimestep)

        @property
        def cylindrical_gear_mesh_system_deflection_with_ltca_results(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2743.CylindricalGearMeshSystemDeflectionWithLTCAResults":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2743,
            )

            return self._parent._cast(
                _2743.CylindricalGearMeshSystemDeflectionWithLTCAResults
            )

        @property
        def face_gear_mesh_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2756.FaceGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2756,
            )

            return self._parent._cast(_2756.FaceGearMeshSystemDeflection)

        @property
        def gear_mesh_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2761.GearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2761,
            )

            return self._parent._cast(_2761.GearMeshSystemDeflection)

        @property
        def hypoid_gear_mesh_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2765.HypoidGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2765,
            )

            return self._parent._cast(_2765.HypoidGearMeshSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2769.InterMountableComponentConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2769,
            )

            return self._parent._cast(
                _2769.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2770.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2770,
            )

            return self._parent._cast(
                _2770.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2773.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2773,
            )

            return self._parent._cast(
                _2773.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2776.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2776,
            )

            return self._parent._cast(
                _2776.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_connection_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2788.PartToPartShearCouplingConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2788,
            )

            return self._parent._cast(
                _2788.PartToPartShearCouplingConnectionSystemDeflection
            )

        @property
        def planetary_connection_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2791.PlanetaryConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2791,
            )

            return self._parent._cast(_2791.PlanetaryConnectionSystemDeflection)

        @property
        def ring_pins_to_disc_connection_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2797.RingPinsToDiscConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2797,
            )

            return self._parent._cast(_2797.RingPinsToDiscConnectionSystemDeflection)

        @property
        def rolling_ring_connection_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2800.RollingRingConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2800,
            )

            return self._parent._cast(_2800.RollingRingConnectionSystemDeflection)

        @property
        def shaft_to_mountable_component_connection_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2807.ShaftToMountableComponentConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2807,
            )

            return self._parent._cast(
                _2807.ShaftToMountableComponentConnectionSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2809.SpiralBevelGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2809,
            )

            return self._parent._cast(_2809.SpiralBevelGearMeshSystemDeflection)

        @property
        def spring_damper_connection_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2812.SpringDamperConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2812,
            )

            return self._parent._cast(_2812.SpringDamperConnectionSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2815.StraightBevelDiffGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2815,
            )

            return self._parent._cast(_2815.StraightBevelDiffGearMeshSystemDeflection)

        @property
        def straight_bevel_gear_mesh_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2818.StraightBevelGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2818,
            )

            return self._parent._cast(_2818.StraightBevelGearMeshSystemDeflection)

        @property
        def torque_converter_connection_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2830.TorqueConverterConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2830,
            )

            return self._parent._cast(_2830.TorqueConverterConnectionSystemDeflection)

        @property
        def worm_gear_mesh_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2838.WormGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2838,
            )

            return self._parent._cast(_2838.WormGearMeshSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2841.ZerolBevelGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2841,
            )

            return self._parent._cast(_2841.ZerolBevelGearMeshSystemDeflection)

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2988.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2988,
            )

            return self._parent._cast(
                _2988.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2989.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2989,
            )

            return self._parent._cast(
                _2989.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def belt_connection_steady_state_synchronous_response(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2994.BeltConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2994,
            )

            return self._parent._cast(
                _2994.BeltConnectionSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_2996.BevelDifferentialGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2996,
            )

            return self._parent._cast(
                _2996.BevelDifferentialGearMeshSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3001.BevelGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3001,
            )

            return self._parent._cast(_3001.BevelGearMeshSteadyStateSynchronousResponse)

        @property
        def clutch_connection_steady_state_synchronous_response(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3006.ClutchConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3006,
            )

            return self._parent._cast(
                _3006.ClutchConnectionSteadyStateSynchronousResponse
            )

        @property
        def coaxial_connection_steady_state_synchronous_response(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3009.CoaxialConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3009,
            )

            return self._parent._cast(
                _3009.CoaxialConnectionSteadyStateSynchronousResponse
            )

        @property
        def concept_coupling_connection_steady_state_synchronous_response(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3011.ConceptCouplingConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3011,
            )

            return self._parent._cast(
                _3011.ConceptCouplingConnectionSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3014.ConceptGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3014,
            )

            return self._parent._cast(
                _3014.ConceptGearMeshSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3017.ConicalGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3017,
            )

            return self._parent._cast(
                _3017.ConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3020.ConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3020,
            )

            return self._parent._cast(_3020.ConnectionSteadyStateSynchronousResponse)

        @property
        def coupling_connection_steady_state_synchronous_response(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3022.CouplingConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3022,
            )

            return self._parent._cast(
                _3022.CouplingConnectionSteadyStateSynchronousResponse
            )

        @property
        def cvt_belt_connection_steady_state_synchronous_response(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3025.CVTBeltConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3025,
            )

            return self._parent._cast(
                _3025.CVTBeltConnectionSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> (
            "_3029.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3029,
            )

            return self._parent._cast(
                _3029.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_steady_state_synchronous_response(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3030.CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3030,
            )

            return self._parent._cast(
                _3030.CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3032.CylindricalGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3032,
            )

            return self._parent._cast(
                _3032.CylindricalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def face_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3039.FaceGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3039,
            )

            return self._parent._cast(_3039.FaceGearMeshSteadyStateSynchronousResponse)

        @property
        def gear_mesh_steady_state_synchronous_response(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3044.GearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3044,
            )

            return self._parent._cast(_3044.GearMeshSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3048.HypoidGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3048,
            )

            return self._parent._cast(
                _3048.HypoidGearMeshSteadyStateSynchronousResponse
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3051.InterMountableComponentConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3051,
            )

            return self._parent._cast(
                _3051.InterMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3052.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3052,
            )

            return self._parent._cast(
                _3052.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> (
            "_3055.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3055,
            )

            return self._parent._cast(
                _3055.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3058.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3058,
            )

            return self._parent._cast(
                _3058.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_connection_steady_state_synchronous_response(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3066.PartToPartShearCouplingConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3066,
            )

            return self._parent._cast(
                _3066.PartToPartShearCouplingConnectionSteadyStateSynchronousResponse
            )

        @property
        def planetary_connection_steady_state_synchronous_response(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3069.PlanetaryConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3069,
            )

            return self._parent._cast(
                _3069.PlanetaryConnectionSteadyStateSynchronousResponse
            )

        @property
        def ring_pins_to_disc_connection_steady_state_synchronous_response(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3076.RingPinsToDiscConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3076,
            )

            return self._parent._cast(
                _3076.RingPinsToDiscConnectionSteadyStateSynchronousResponse
            )

        @property
        def rolling_ring_connection_steady_state_synchronous_response(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3078.RollingRingConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3078,
            )

            return self._parent._cast(
                _3078.RollingRingConnectionSteadyStateSynchronousResponse
            )

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3083.ShaftToMountableComponentConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3083,
            )

            return self._parent._cast(
                _3083.ShaftToMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3085.SpiralBevelGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3085,
            )

            return self._parent._cast(
                _3085.SpiralBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_connection_steady_state_synchronous_response(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3088.SpringDamperConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3088,
            )

            return self._parent._cast(
                _3088.SpringDamperConnectionSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3094.StraightBevelDiffGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3094,
            )

            return self._parent._cast(
                _3094.StraightBevelDiffGearMeshSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3097.StraightBevelGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3097,
            )

            return self._parent._cast(
                _3097.StraightBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_connection_steady_state_synchronous_response(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3106.TorqueConverterConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3106,
            )

            return self._parent._cast(
                _3106.TorqueConverterConnectionSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3112.WormGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3112,
            )

            return self._parent._cast(_3112.WormGearMeshSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3115.ZerolBevelGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3115,
            )

            return self._parent._cast(
                _3115.ZerolBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3250.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3250,
            )

            return self._parent._cast(
                _3250.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3251.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3251,
            )

            return self._parent._cast(
                _3251.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def belt_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3256.BeltConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3256,
            )

            return self._parent._cast(
                _3256.BeltConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3258.BevelDifferentialGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3258,
            )

            return self._parent._cast(
                _3258.BevelDifferentialGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3263.BevelGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3263,
            )

            return self._parent._cast(
                _3263.BevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def clutch_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3268.ClutchConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3268,
            )

            return self._parent._cast(
                _3268.ClutchConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coaxial_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3271.CoaxialConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3271,
            )

            return self._parent._cast(
                _3271.CoaxialConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3273.ConceptCouplingConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3273,
            )

            return self._parent._cast(
                _3273.ConceptCouplingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3276.ConceptGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3276,
            )

            return self._parent._cast(
                _3276.ConceptGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3279.ConicalGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3279,
            )

            return self._parent._cast(
                _3279.ConicalGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3282.ConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3282,
            )

            return self._parent._cast(
                _3282.ConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3284.CouplingConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3284,
            )

            return self._parent._cast(
                _3284.CouplingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_belt_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3287.CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3287,
            )

            return self._parent._cast(
                _3287.CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3291.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3291,
            )

            return self._parent._cast(
                _3291.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3292.CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3292,
            )

            return self._parent._cast(
                _3292.CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3294.CylindricalGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3294,
            )

            return self._parent._cast(
                _3294.CylindricalGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3300.FaceGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3300,
            )

            return self._parent._cast(
                _3300.FaceGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3305.GearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3305,
            )

            return self._parent._cast(
                _3305.GearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3309.HypoidGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3309,
            )

            return self._parent._cast(
                _3309.HypoidGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3312.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3312,
            )

            return self._parent._cast(
                _3312.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3313.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3313,
            )

            return self._parent._cast(
                _3313.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3316.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3316,
            )

            return self._parent._cast(
                _3316.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3319.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3319,
            )

            return self._parent._cast(
                _3319.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3327.PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3327,
            )

            return self._parent._cast(
                _3327.PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planetary_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3330.PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3330,
            )

            return self._parent._cast(
                _3330.PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def ring_pins_to_disc_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3337.RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3337,
            )

            return self._parent._cast(
                _3337.RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3339.RollingRingConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3339,
            )

            return self._parent._cast(
                _3339.RollingRingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3344.ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3344,
            )

            return self._parent._cast(
                _3344.ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3346.SpiralBevelGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3346,
            )

            return self._parent._cast(
                _3346.SpiralBevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3349.SpringDamperConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3349,
            )

            return self._parent._cast(
                _3349.SpringDamperConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3353.StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3353,
            )

            return self._parent._cast(
                _3353.StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3356.StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3356,
            )

            return self._parent._cast(
                _3356.StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3365.TorqueConverterConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3365,
            )

            return self._parent._cast(
                _3365.TorqueConverterConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3371.WormGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3371,
            )

            return self._parent._cast(
                _3371.WormGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3374.ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3374,
            )

            return self._parent._cast(
                _3374.ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3509.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3509,
            )

            return self._parent._cast(
                _3509.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3510.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3510,
            )

            return self._parent._cast(
                _3510.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def belt_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3515.BeltConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3515,
            )

            return self._parent._cast(
                _3515.BeltConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3517.BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3517,
            )

            return self._parent._cast(
                _3517.BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3522.BevelGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3522,
            )

            return self._parent._cast(
                _3522.BevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def clutch_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3527.ClutchConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3527,
            )

            return self._parent._cast(
                _3527.ClutchConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coaxial_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3530.CoaxialConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3530,
            )

            return self._parent._cast(
                _3530.CoaxialConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3532.ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3532,
            )

            return self._parent._cast(
                _3532.ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3535.ConceptGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3535,
            )

            return self._parent._cast(
                _3535.ConceptGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3538.ConicalGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3538,
            )

            return self._parent._cast(
                _3538.ConicalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3541.ConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3541,
            )

            return self._parent._cast(
                _3541.ConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3543.CouplingConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3543,
            )

            return self._parent._cast(
                _3543.CouplingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_belt_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3546.CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3546,
            )

            return self._parent._cast(
                _3546.CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3550.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3550,
            )

            return self._parent._cast(
                _3550.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3551.CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3551,
            )

            return self._parent._cast(
                _3551.CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3553.CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3553,
            )

            return self._parent._cast(
                _3553.CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3559.FaceGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3559,
            )

            return self._parent._cast(
                _3559.FaceGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3564.GearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3564,
            )

            return self._parent._cast(
                _3564.GearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3568.HypoidGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3568,
            )

            return self._parent._cast(
                _3568.HypoidGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3571.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3571,
            )

            return self._parent._cast(
                _3571.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3572.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3572,
            )

            return self._parent._cast(
                _3572.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3575.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3575,
            )

            return self._parent._cast(
                _3575.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3578.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3578,
            )

            return self._parent._cast(
                _3578.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3586.PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3586,
            )

            return self._parent._cast(
                _3586.PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planetary_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3589.PlanetaryConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3589,
            )

            return self._parent._cast(
                _3589.PlanetaryConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def ring_pins_to_disc_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3596.RingPinsToDiscConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3596,
            )

            return self._parent._cast(
                _3596.RingPinsToDiscConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3598.RollingRingConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3598,
            )

            return self._parent._cast(
                _3598.RollingRingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3603.ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3603,
            )

            return self._parent._cast(
                _3603.ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3605.SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3605,
            )

            return self._parent._cast(
                _3605.SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3608.SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3608,
            )

            return self._parent._cast(
                _3608.SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3612.StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3612,
            )

            return self._parent._cast(
                _3612.StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3615.StraightBevelGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3615,
            )

            return self._parent._cast(
                _3615.StraightBevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3624.TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3624,
            )

            return self._parent._cast(
                _3624.TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3630.WormGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3630,
            )

            return self._parent._cast(
                _3630.WormGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3633.ZerolBevelGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3633,
            )

            return self._parent._cast(
                _3633.ZerolBevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_to_mountable_component_connection_stability_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3768.AbstractShaftToMountableComponentConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3768,
            )

            return self._parent._cast(
                _3768.AbstractShaftToMountableComponentConnectionStabilityAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_stability_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3769.AGMAGleasonConicalGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3769,
            )

            return self._parent._cast(_3769.AGMAGleasonConicalGearMeshStabilityAnalysis)

        @property
        def belt_connection_stability_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3774.BeltConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3774,
            )

            return self._parent._cast(_3774.BeltConnectionStabilityAnalysis)

        @property
        def bevel_differential_gear_mesh_stability_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3776.BevelDifferentialGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3776,
            )

            return self._parent._cast(_3776.BevelDifferentialGearMeshStabilityAnalysis)

        @property
        def bevel_gear_mesh_stability_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3781.BevelGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3781,
            )

            return self._parent._cast(_3781.BevelGearMeshStabilityAnalysis)

        @property
        def clutch_connection_stability_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3786.ClutchConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3786,
            )

            return self._parent._cast(_3786.ClutchConnectionStabilityAnalysis)

        @property
        def coaxial_connection_stability_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3789.CoaxialConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3789,
            )

            return self._parent._cast(_3789.CoaxialConnectionStabilityAnalysis)

        @property
        def concept_coupling_connection_stability_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3791.ConceptCouplingConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3791,
            )

            return self._parent._cast(_3791.ConceptCouplingConnectionStabilityAnalysis)

        @property
        def concept_gear_mesh_stability_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3794.ConceptGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3794,
            )

            return self._parent._cast(_3794.ConceptGearMeshStabilityAnalysis)

        @property
        def conical_gear_mesh_stability_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3797.ConicalGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3797,
            )

            return self._parent._cast(_3797.ConicalGearMeshStabilityAnalysis)

        @property
        def connection_stability_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3800.ConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3800,
            )

            return self._parent._cast(_3800.ConnectionStabilityAnalysis)

        @property
        def coupling_connection_stability_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3802.CouplingConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3802,
            )

            return self._parent._cast(_3802.CouplingConnectionStabilityAnalysis)

        @property
        def cvt_belt_connection_stability_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3806.CVTBeltConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3806,
            )

            return self._parent._cast(_3806.CVTBeltConnectionStabilityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_stability_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3810.CycloidalDiscCentralBearingConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3810,
            )

            return self._parent._cast(
                _3810.CycloidalDiscCentralBearingConnectionStabilityAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_stability_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3811.CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3811,
            )

            return self._parent._cast(
                _3811.CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis
            )

        @property
        def cylindrical_gear_mesh_stability_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3813.CylindricalGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3813,
            )

            return self._parent._cast(_3813.CylindricalGearMeshStabilityAnalysis)

        @property
        def face_gear_mesh_stability_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3820.FaceGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3820,
            )

            return self._parent._cast(_3820.FaceGearMeshStabilityAnalysis)

        @property
        def gear_mesh_stability_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3825.GearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3825,
            )

            return self._parent._cast(_3825.GearMeshStabilityAnalysis)

        @property
        def hypoid_gear_mesh_stability_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3829.HypoidGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3829,
            )

            return self._parent._cast(_3829.HypoidGearMeshStabilityAnalysis)

        @property
        def inter_mountable_component_connection_stability_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3832.InterMountableComponentConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3832,
            )

            return self._parent._cast(
                _3832.InterMountableComponentConnectionStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_stability_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3833.KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3833,
            )

            return self._parent._cast(
                _3833.KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_stability_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3836.KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3836,
            )

            return self._parent._cast(
                _3836.KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_stability_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3839.KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3839,
            )

            return self._parent._cast(
                _3839.KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_stability_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3847.PartToPartShearCouplingConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3847,
            )

            return self._parent._cast(
                _3847.PartToPartShearCouplingConnectionStabilityAnalysis
            )

        @property
        def planetary_connection_stability_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3850.PlanetaryConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3850,
            )

            return self._parent._cast(_3850.PlanetaryConnectionStabilityAnalysis)

        @property
        def ring_pins_to_disc_connection_stability_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3857.RingPinsToDiscConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3857,
            )

            return self._parent._cast(_3857.RingPinsToDiscConnectionStabilityAnalysis)

        @property
        def rolling_ring_connection_stability_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3859.RollingRingConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3859,
            )

            return self._parent._cast(_3859.RollingRingConnectionStabilityAnalysis)

        @property
        def shaft_to_mountable_component_connection_stability_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3864.ShaftToMountableComponentConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3864,
            )

            return self._parent._cast(
                _3864.ShaftToMountableComponentConnectionStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_stability_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3866.SpiralBevelGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3866,
            )

            return self._parent._cast(_3866.SpiralBevelGearMeshStabilityAnalysis)

        @property
        def spring_damper_connection_stability_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3869.SpringDamperConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3869,
            )

            return self._parent._cast(_3869.SpringDamperConnectionStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_stability_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3875.StraightBevelDiffGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3875,
            )

            return self._parent._cast(_3875.StraightBevelDiffGearMeshStabilityAnalysis)

        @property
        def straight_bevel_gear_mesh_stability_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3878.StraightBevelGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3878,
            )

            return self._parent._cast(_3878.StraightBevelGearMeshStabilityAnalysis)

        @property
        def torque_converter_connection_stability_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3887.TorqueConverterConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3887,
            )

            return self._parent._cast(_3887.TorqueConverterConnectionStabilityAnalysis)

        @property
        def worm_gear_mesh_stability_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3893.WormGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3893,
            )

            return self._parent._cast(_3893.WormGearMeshStabilityAnalysis)

        @property
        def zerol_bevel_gear_mesh_stability_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_3896.ZerolBevelGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3896,
            )

            return self._parent._cast(_3896.ZerolBevelGearMeshStabilityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_power_flow(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4037.AbstractShaftToMountableComponentConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4037

            return self._parent._cast(
                _4037.AbstractShaftToMountableComponentConnectionPowerFlow
            )

        @property
        def agma_gleason_conical_gear_mesh_power_flow(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4038.AGMAGleasonConicalGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4038

            return self._parent._cast(_4038.AGMAGleasonConicalGearMeshPowerFlow)

        @property
        def belt_connection_power_flow(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4043.BeltConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4043

            return self._parent._cast(_4043.BeltConnectionPowerFlow)

        @property
        def bevel_differential_gear_mesh_power_flow(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4045.BevelDifferentialGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4045

            return self._parent._cast(_4045.BevelDifferentialGearMeshPowerFlow)

        @property
        def bevel_gear_mesh_power_flow(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4050.BevelGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4050

            return self._parent._cast(_4050.BevelGearMeshPowerFlow)

        @property
        def clutch_connection_power_flow(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4055.ClutchConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4055

            return self._parent._cast(_4055.ClutchConnectionPowerFlow)

        @property
        def coaxial_connection_power_flow(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4058.CoaxialConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4058

            return self._parent._cast(_4058.CoaxialConnectionPowerFlow)

        @property
        def concept_coupling_connection_power_flow(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4060.ConceptCouplingConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4060

            return self._parent._cast(_4060.ConceptCouplingConnectionPowerFlow)

        @property
        def concept_gear_mesh_power_flow(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4063.ConceptGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4063

            return self._parent._cast(_4063.ConceptGearMeshPowerFlow)

        @property
        def conical_gear_mesh_power_flow(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4066.ConicalGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4066

            return self._parent._cast(_4066.ConicalGearMeshPowerFlow)

        @property
        def connection_power_flow(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4069.ConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4069

            return self._parent._cast(_4069.ConnectionPowerFlow)

        @property
        def coupling_connection_power_flow(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4071.CouplingConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4071

            return self._parent._cast(_4071.CouplingConnectionPowerFlow)

        @property
        def cvt_belt_connection_power_flow(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4074.CVTBeltConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4074

            return self._parent._cast(_4074.CVTBeltConnectionPowerFlow)

        @property
        def cycloidal_disc_central_bearing_connection_power_flow(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4078.CycloidalDiscCentralBearingConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4078

            return self._parent._cast(
                _4078.CycloidalDiscCentralBearingConnectionPowerFlow
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_power_flow(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4079.CycloidalDiscPlanetaryBearingConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4079

            return self._parent._cast(
                _4079.CycloidalDiscPlanetaryBearingConnectionPowerFlow
            )

        @property
        def cylindrical_gear_mesh_power_flow(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4082.CylindricalGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4082

            return self._parent._cast(_4082.CylindricalGearMeshPowerFlow)

        @property
        def face_gear_mesh_power_flow(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4088.FaceGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4088

            return self._parent._cast(_4088.FaceGearMeshPowerFlow)

        @property
        def gear_mesh_power_flow(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4095.GearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4095

            return self._parent._cast(_4095.GearMeshPowerFlow)

        @property
        def hypoid_gear_mesh_power_flow(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4099.HypoidGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4099

            return self._parent._cast(_4099.HypoidGearMeshPowerFlow)

        @property
        def inter_mountable_component_connection_power_flow(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4102.InterMountableComponentConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4102

            return self._parent._cast(_4102.InterMountableComponentConnectionPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_power_flow(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4103.KlingelnbergCycloPalloidConicalGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4103

            return self._parent._cast(
                _4103.KlingelnbergCycloPalloidConicalGearMeshPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_power_flow(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4106.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4106

            return self._parent._cast(
                _4106.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_power_flow(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4109.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4109

            return self._parent._cast(
                _4109.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow
            )

        @property
        def part_to_part_shear_coupling_connection_power_flow(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4117.PartToPartShearCouplingConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4117

            return self._parent._cast(_4117.PartToPartShearCouplingConnectionPowerFlow)

        @property
        def planetary_connection_power_flow(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4120.PlanetaryConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4120

            return self._parent._cast(_4120.PlanetaryConnectionPowerFlow)

        @property
        def ring_pins_to_disc_connection_power_flow(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4129.RingPinsToDiscConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4129

            return self._parent._cast(_4129.RingPinsToDiscConnectionPowerFlow)

        @property
        def rolling_ring_connection_power_flow(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4131.RollingRingConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4131

            return self._parent._cast(_4131.RollingRingConnectionPowerFlow)

        @property
        def shaft_to_mountable_component_connection_power_flow(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4136.ShaftToMountableComponentConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4136

            return self._parent._cast(
                _4136.ShaftToMountableComponentConnectionPowerFlow
            )

        @property
        def spiral_bevel_gear_mesh_power_flow(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4138.SpiralBevelGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4138

            return self._parent._cast(_4138.SpiralBevelGearMeshPowerFlow)

        @property
        def spring_damper_connection_power_flow(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4141.SpringDamperConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4141

            return self._parent._cast(_4141.SpringDamperConnectionPowerFlow)

        @property
        def straight_bevel_diff_gear_mesh_power_flow(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4144.StraightBevelDiffGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4144

            return self._parent._cast(_4144.StraightBevelDiffGearMeshPowerFlow)

        @property
        def straight_bevel_gear_mesh_power_flow(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4147.StraightBevelGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4147

            return self._parent._cast(_4147.StraightBevelGearMeshPowerFlow)

        @property
        def torque_converter_connection_power_flow(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4157.TorqueConverterConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4157

            return self._parent._cast(_4157.TorqueConverterConnectionPowerFlow)

        @property
        def worm_gear_mesh_power_flow(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4163.WormGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4163

            return self._parent._cast(_4163.WormGearMeshPowerFlow)

        @property
        def zerol_bevel_gear_mesh_power_flow(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4166.ZerolBevelGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4166

            return self._parent._cast(_4166.ZerolBevelGearMeshPowerFlow)

        @property
        def abstract_shaft_to_mountable_component_connection_parametric_study_tool(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4301.AbstractShaftToMountableComponentConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4301,
            )

            return self._parent._cast(
                _4301.AbstractShaftToMountableComponentConnectionParametricStudyTool
            )

        @property
        def agma_gleason_conical_gear_mesh_parametric_study_tool(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4302.AGMAGleasonConicalGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4302,
            )

            return self._parent._cast(
                _4302.AGMAGleasonConicalGearMeshParametricStudyTool
            )

        @property
        def belt_connection_parametric_study_tool(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4307.BeltConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4307,
            )

            return self._parent._cast(_4307.BeltConnectionParametricStudyTool)

        @property
        def bevel_differential_gear_mesh_parametric_study_tool(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4309.BevelDifferentialGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4309,
            )

            return self._parent._cast(
                _4309.BevelDifferentialGearMeshParametricStudyTool
            )

        @property
        def bevel_gear_mesh_parametric_study_tool(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4314.BevelGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4314,
            )

            return self._parent._cast(_4314.BevelGearMeshParametricStudyTool)

        @property
        def clutch_connection_parametric_study_tool(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4319.ClutchConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4319,
            )

            return self._parent._cast(_4319.ClutchConnectionParametricStudyTool)

        @property
        def coaxial_connection_parametric_study_tool(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4322.CoaxialConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4322,
            )

            return self._parent._cast(_4322.CoaxialConnectionParametricStudyTool)

        @property
        def concept_coupling_connection_parametric_study_tool(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4324.ConceptCouplingConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4324,
            )

            return self._parent._cast(
                _4324.ConceptCouplingConnectionParametricStudyTool
            )

        @property
        def concept_gear_mesh_parametric_study_tool(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4327.ConceptGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4327,
            )

            return self._parent._cast(_4327.ConceptGearMeshParametricStudyTool)

        @property
        def conical_gear_mesh_parametric_study_tool(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4330.ConicalGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4330,
            )

            return self._parent._cast(_4330.ConicalGearMeshParametricStudyTool)

        @property
        def connection_parametric_study_tool(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4333.ConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4333,
            )

            return self._parent._cast(_4333.ConnectionParametricStudyTool)

        @property
        def coupling_connection_parametric_study_tool(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4335.CouplingConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4335,
            )

            return self._parent._cast(_4335.CouplingConnectionParametricStudyTool)

        @property
        def cvt_belt_connection_parametric_study_tool(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4338.CVTBeltConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4338,
            )

            return self._parent._cast(_4338.CVTBeltConnectionParametricStudyTool)

        @property
        def cycloidal_disc_central_bearing_connection_parametric_study_tool(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4342.CycloidalDiscCentralBearingConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4342,
            )

            return self._parent._cast(
                _4342.CycloidalDiscCentralBearingConnectionParametricStudyTool
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_parametric_study_tool(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4344.CycloidalDiscPlanetaryBearingConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4344,
            )

            return self._parent._cast(
                _4344.CycloidalDiscPlanetaryBearingConnectionParametricStudyTool
            )

        @property
        def cylindrical_gear_mesh_parametric_study_tool(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4345.CylindricalGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4345,
            )

            return self._parent._cast(_4345.CylindricalGearMeshParametricStudyTool)

        @property
        def face_gear_mesh_parametric_study_tool(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4358.FaceGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4358,
            )

            return self._parent._cast(_4358.FaceGearMeshParametricStudyTool)

        @property
        def gear_mesh_parametric_study_tool(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4363.GearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4363,
            )

            return self._parent._cast(_4363.GearMeshParametricStudyTool)

        @property
        def hypoid_gear_mesh_parametric_study_tool(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4367.HypoidGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4367,
            )

            return self._parent._cast(_4367.HypoidGearMeshParametricStudyTool)

        @property
        def inter_mountable_component_connection_parametric_study_tool(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4370.InterMountableComponentConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4370,
            )

            return self._parent._cast(
                _4370.InterMountableComponentConnectionParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_parametric_study_tool(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4371.KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4371,
            )

            return self._parent._cast(
                _4371.KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_parametric_study_tool(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4374.KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4374,
            )

            return self._parent._cast(
                _4374.KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_parametric_study_tool(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4377.KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4377,
            )

            return self._parent._cast(
                _4377.KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool
            )

        @property
        def part_to_part_shear_coupling_connection_parametric_study_tool(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4396.PartToPartShearCouplingConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4396,
            )

            return self._parent._cast(
                _4396.PartToPartShearCouplingConnectionParametricStudyTool
            )

        @property
        def planetary_connection_parametric_study_tool(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4399.PlanetaryConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4399,
            )

            return self._parent._cast(_4399.PlanetaryConnectionParametricStudyTool)

        @property
        def ring_pins_to_disc_connection_parametric_study_tool(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4406.RingPinsToDiscConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4406,
            )

            return self._parent._cast(_4406.RingPinsToDiscConnectionParametricStudyTool)

        @property
        def rolling_ring_connection_parametric_study_tool(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4408.RollingRingConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4408,
            )

            return self._parent._cast(_4408.RollingRingConnectionParametricStudyTool)

        @property
        def shaft_to_mountable_component_connection_parametric_study_tool(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4413.ShaftToMountableComponentConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4413,
            )

            return self._parent._cast(
                _4413.ShaftToMountableComponentConnectionParametricStudyTool
            )

        @property
        def spiral_bevel_gear_mesh_parametric_study_tool(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4415.SpiralBevelGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4415,
            )

            return self._parent._cast(_4415.SpiralBevelGearMeshParametricStudyTool)

        @property
        def spring_damper_connection_parametric_study_tool(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4418.SpringDamperConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4418,
            )

            return self._parent._cast(_4418.SpringDamperConnectionParametricStudyTool)

        @property
        def straight_bevel_diff_gear_mesh_parametric_study_tool(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4421.StraightBevelDiffGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4421,
            )

            return self._parent._cast(
                _4421.StraightBevelDiffGearMeshParametricStudyTool
            )

        @property
        def straight_bevel_gear_mesh_parametric_study_tool(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4424.StraightBevelGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4424,
            )

            return self._parent._cast(_4424.StraightBevelGearMeshParametricStudyTool)

        @property
        def torque_converter_connection_parametric_study_tool(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4433.TorqueConverterConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4433,
            )

            return self._parent._cast(
                _4433.TorqueConverterConnectionParametricStudyTool
            )

        @property
        def worm_gear_mesh_parametric_study_tool(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4439.WormGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4439,
            )

            return self._parent._cast(_4439.WormGearMeshParametricStudyTool)

        @property
        def zerol_bevel_gear_mesh_parametric_study_tool(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4442.ZerolBevelGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4442,
            )

            return self._parent._cast(_4442.ZerolBevelGearMeshParametricStudyTool)

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4577.AbstractShaftToMountableComponentConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4577

            return self._parent._cast(
                _4577.AbstractShaftToMountableComponentConnectionModalAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4578.AGMAGleasonConicalGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4578

            return self._parent._cast(_4578.AGMAGleasonConicalGearMeshModalAnalysis)

        @property
        def belt_connection_modal_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4583.BeltConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4583

            return self._parent._cast(_4583.BeltConnectionModalAnalysis)

        @property
        def bevel_differential_gear_mesh_modal_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4585.BevelDifferentialGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4585

            return self._parent._cast(_4585.BevelDifferentialGearMeshModalAnalysis)

        @property
        def bevel_gear_mesh_modal_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4590.BevelGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4590

            return self._parent._cast(_4590.BevelGearMeshModalAnalysis)

        @property
        def clutch_connection_modal_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4595.ClutchConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4595

            return self._parent._cast(_4595.ClutchConnectionModalAnalysis)

        @property
        def coaxial_connection_modal_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4598.CoaxialConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4598

            return self._parent._cast(_4598.CoaxialConnectionModalAnalysis)

        @property
        def concept_coupling_connection_modal_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4600.ConceptCouplingConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4600

            return self._parent._cast(_4600.ConceptCouplingConnectionModalAnalysis)

        @property
        def concept_gear_mesh_modal_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4603.ConceptGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4603

            return self._parent._cast(_4603.ConceptGearMeshModalAnalysis)

        @property
        def conical_gear_mesh_modal_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4606.ConicalGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4606

            return self._parent._cast(_4606.ConicalGearMeshModalAnalysis)

        @property
        def connection_modal_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4609.ConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4609

            return self._parent._cast(_4609.ConnectionModalAnalysis)

        @property
        def coupling_connection_modal_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4612.CouplingConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4612

            return self._parent._cast(_4612.CouplingConnectionModalAnalysis)

        @property
        def cvt_belt_connection_modal_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4615.CVTBeltConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4615

            return self._parent._cast(_4615.CVTBeltConnectionModalAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_modal_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4619.CycloidalDiscCentralBearingConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4619

            return self._parent._cast(
                _4619.CycloidalDiscCentralBearingConnectionModalAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_modal_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4621.CycloidalDiscPlanetaryBearingConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4621

            return self._parent._cast(
                _4621.CycloidalDiscPlanetaryBearingConnectionModalAnalysis
            )

        @property
        def cylindrical_gear_mesh_modal_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4622.CylindricalGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4622

            return self._parent._cast(_4622.CylindricalGearMeshModalAnalysis)

        @property
        def face_gear_mesh_modal_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4631.FaceGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4631

            return self._parent._cast(_4631.FaceGearMeshModalAnalysis)

        @property
        def gear_mesh_modal_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4637.GearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4637

            return self._parent._cast(_4637.GearMeshModalAnalysis)

        @property
        def hypoid_gear_mesh_modal_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4641.HypoidGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4641

            return self._parent._cast(_4641.HypoidGearMeshModalAnalysis)

        @property
        def inter_mountable_component_connection_modal_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4644.InterMountableComponentConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4644

            return self._parent._cast(
                _4644.InterMountableComponentConnectionModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4645.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4645

            return self._parent._cast(
                _4645.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4648.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4648

            return self._parent._cast(
                _4648.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4651.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4651

            return self._parent._cast(
                _4651.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_modal_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4665.PartToPartShearCouplingConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4665

            return self._parent._cast(
                _4665.PartToPartShearCouplingConnectionModalAnalysis
            )

        @property
        def planetary_connection_modal_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4668.PlanetaryConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4668

            return self._parent._cast(_4668.PlanetaryConnectionModalAnalysis)

        @property
        def ring_pins_to_disc_connection_modal_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4675.RingPinsToDiscConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4675

            return self._parent._cast(_4675.RingPinsToDiscConnectionModalAnalysis)

        @property
        def rolling_ring_connection_modal_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4677.RollingRingConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4677

            return self._parent._cast(_4677.RollingRingConnectionModalAnalysis)

        @property
        def shaft_to_mountable_component_connection_modal_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4683.ShaftToMountableComponentConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4683

            return self._parent._cast(
                _4683.ShaftToMountableComponentConnectionModalAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_modal_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4685.SpiralBevelGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4685

            return self._parent._cast(_4685.SpiralBevelGearMeshModalAnalysis)

        @property
        def spring_damper_connection_modal_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4688.SpringDamperConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4688

            return self._parent._cast(_4688.SpringDamperConnectionModalAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4691.StraightBevelDiffGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4691

            return self._parent._cast(_4691.StraightBevelDiffGearMeshModalAnalysis)

        @property
        def straight_bevel_gear_mesh_modal_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4694.StraightBevelGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4694

            return self._parent._cast(_4694.StraightBevelGearMeshModalAnalysis)

        @property
        def torque_converter_connection_modal_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4703.TorqueConverterConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4703

            return self._parent._cast(_4703.TorqueConverterConnectionModalAnalysis)

        @property
        def worm_gear_mesh_modal_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4712.WormGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4712

            return self._parent._cast(_4712.WormGearMeshModalAnalysis)

        @property
        def zerol_bevel_gear_mesh_modal_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4715.ZerolBevelGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4715

            return self._parent._cast(_4715.ZerolBevelGearMeshModalAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> (
            "_4862.AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4862,
            )

            return self._parent._cast(
                _4862.AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4863.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4863,
            )

            return self._parent._cast(
                _4863.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness
            )

        @property
        def belt_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4868.BeltConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4868,
            )

            return self._parent._cast(_4868.BeltConnectionModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4870.BevelDifferentialGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4870,
            )

            return self._parent._cast(
                _4870.BevelDifferentialGearMeshModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4875.BevelGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4875,
            )

            return self._parent._cast(_4875.BevelGearMeshModalAnalysisAtAStiffness)

        @property
        def clutch_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4880.ClutchConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4880,
            )

            return self._parent._cast(_4880.ClutchConnectionModalAnalysisAtAStiffness)

        @property
        def coaxial_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4883.CoaxialConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4883,
            )

            return self._parent._cast(_4883.CoaxialConnectionModalAnalysisAtAStiffness)

        @property
        def concept_coupling_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4885.ConceptCouplingConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4885,
            )

            return self._parent._cast(
                _4885.ConceptCouplingConnectionModalAnalysisAtAStiffness
            )

        @property
        def concept_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4888.ConceptGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4888,
            )

            return self._parent._cast(_4888.ConceptGearMeshModalAnalysisAtAStiffness)

        @property
        def conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4891.ConicalGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4891,
            )

            return self._parent._cast(_4891.ConicalGearMeshModalAnalysisAtAStiffness)

        @property
        def connection_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4894.ConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4894,
            )

            return self._parent._cast(_4894.ConnectionModalAnalysisAtAStiffness)

        @property
        def coupling_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4896.CouplingConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4896,
            )

            return self._parent._cast(_4896.CouplingConnectionModalAnalysisAtAStiffness)

        @property
        def cvt_belt_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4899.CVTBeltConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4899,
            )

            return self._parent._cast(_4899.CVTBeltConnectionModalAnalysisAtAStiffness)

        @property
        def cycloidal_disc_central_bearing_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4903.CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4903,
            )

            return self._parent._cast(
                _4903.CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4905.CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4905,
            )

            return self._parent._cast(
                _4905.CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4906.CylindricalGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4906,
            )

            return self._parent._cast(
                _4906.CylindricalGearMeshModalAnalysisAtAStiffness
            )

        @property
        def face_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4913.FaceGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4913,
            )

            return self._parent._cast(_4913.FaceGearMeshModalAnalysisAtAStiffness)

        @property
        def gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4918.GearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4918,
            )

            return self._parent._cast(_4918.GearMeshModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4922.HypoidGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4922,
            )

            return self._parent._cast(_4922.HypoidGearMeshModalAnalysisAtAStiffness)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4925.InterMountableComponentConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4925,
            )

            return self._parent._cast(
                _4925.InterMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4926.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4926,
            )

            return self._parent._cast(
                _4926.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4929.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4929,
            )

            return self._parent._cast(
                _4929.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> (
            "_4932.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtAStiffness"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4932,
            )

            return self._parent._cast(
                _4932.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtAStiffness
            )

        @property
        def part_to_part_shear_coupling_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4941.PartToPartShearCouplingConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4941,
            )

            return self._parent._cast(
                _4941.PartToPartShearCouplingConnectionModalAnalysisAtAStiffness
            )

        @property
        def planetary_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4944.PlanetaryConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4944,
            )

            return self._parent._cast(
                _4944.PlanetaryConnectionModalAnalysisAtAStiffness
            )

        @property
        def ring_pins_to_disc_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4951.RingPinsToDiscConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4951,
            )

            return self._parent._cast(
                _4951.RingPinsToDiscConnectionModalAnalysisAtAStiffness
            )

        @property
        def rolling_ring_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4953.RollingRingConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4953,
            )

            return self._parent._cast(
                _4953.RollingRingConnectionModalAnalysisAtAStiffness
            )

        @property
        def shaft_to_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4958.ShaftToMountableComponentConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4958,
            )

            return self._parent._cast(
                _4958.ShaftToMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4960.SpiralBevelGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4960,
            )

            return self._parent._cast(
                _4960.SpiralBevelGearMeshModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4963.SpringDamperConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4963,
            )

            return self._parent._cast(
                _4963.SpringDamperConnectionModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4966.StraightBevelDiffGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4966,
            )

            return self._parent._cast(
                _4966.StraightBevelDiffGearMeshModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4969.StraightBevelGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4969,
            )

            return self._parent._cast(
                _4969.StraightBevelGearMeshModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4978.TorqueConverterConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4978,
            )

            return self._parent._cast(
                _4978.TorqueConverterConnectionModalAnalysisAtAStiffness
            )

        @property
        def worm_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4984.WormGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4984,
            )

            return self._parent._cast(_4984.WormGearMeshModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_4987.ZerolBevelGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4987,
            )

            return self._parent._cast(_4987.ZerolBevelGearMeshModalAnalysisAtAStiffness)

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5122.AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5122,
            )

            return self._parent._cast(
                _5122.AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5123.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5123,
            )

            return self._parent._cast(
                _5123.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed
            )

        @property
        def belt_connection_modal_analysis_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5128.BeltConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5128,
            )

            return self._parent._cast(_5128.BeltConnectionModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5130.BevelDifferentialGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5130,
            )

            return self._parent._cast(
                _5130.BevelDifferentialGearMeshModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5135.BevelGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5135,
            )

            return self._parent._cast(_5135.BevelGearMeshModalAnalysisAtASpeed)

        @property
        def clutch_connection_modal_analysis_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5140.ClutchConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5140,
            )

            return self._parent._cast(_5140.ClutchConnectionModalAnalysisAtASpeed)

        @property
        def coaxial_connection_modal_analysis_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5143.CoaxialConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5143,
            )

            return self._parent._cast(_5143.CoaxialConnectionModalAnalysisAtASpeed)

        @property
        def concept_coupling_connection_modal_analysis_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5145.ConceptCouplingConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5145,
            )

            return self._parent._cast(
                _5145.ConceptCouplingConnectionModalAnalysisAtASpeed
            )

        @property
        def concept_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5148.ConceptGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5148,
            )

            return self._parent._cast(_5148.ConceptGearMeshModalAnalysisAtASpeed)

        @property
        def conical_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5151.ConicalGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5151,
            )

            return self._parent._cast(_5151.ConicalGearMeshModalAnalysisAtASpeed)

        @property
        def connection_modal_analysis_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5154.ConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5154,
            )

            return self._parent._cast(_5154.ConnectionModalAnalysisAtASpeed)

        @property
        def coupling_connection_modal_analysis_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5156.CouplingConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5156,
            )

            return self._parent._cast(_5156.CouplingConnectionModalAnalysisAtASpeed)

        @property
        def cvt_belt_connection_modal_analysis_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5159.CVTBeltConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5159,
            )

            return self._parent._cast(_5159.CVTBeltConnectionModalAnalysisAtASpeed)

        @property
        def cycloidal_disc_central_bearing_connection_modal_analysis_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5163.CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5163,
            )

            return self._parent._cast(
                _5163.CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_modal_analysis_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5165.CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5165,
            )

            return self._parent._cast(
                _5165.CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed
            )

        @property
        def cylindrical_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5166.CylindricalGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5166,
            )

            return self._parent._cast(_5166.CylindricalGearMeshModalAnalysisAtASpeed)

        @property
        def face_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5172.FaceGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5172,
            )

            return self._parent._cast(_5172.FaceGearMeshModalAnalysisAtASpeed)

        @property
        def gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5177.GearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5177,
            )

            return self._parent._cast(_5177.GearMeshModalAnalysisAtASpeed)

        @property
        def hypoid_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5181.HypoidGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5181,
            )

            return self._parent._cast(_5181.HypoidGearMeshModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5184.InterMountableComponentConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5184,
            )

            return self._parent._cast(
                _5184.InterMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5185.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5185,
            )

            return self._parent._cast(
                _5185.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5188.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5188,
            )

            return self._parent._cast(
                _5188.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5191.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5191,
            )

            return self._parent._cast(
                _5191.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_connection_modal_analysis_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5200.PartToPartShearCouplingConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5200,
            )

            return self._parent._cast(
                _5200.PartToPartShearCouplingConnectionModalAnalysisAtASpeed
            )

        @property
        def planetary_connection_modal_analysis_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5203.PlanetaryConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5203,
            )

            return self._parent._cast(_5203.PlanetaryConnectionModalAnalysisAtASpeed)

        @property
        def ring_pins_to_disc_connection_modal_analysis_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5210.RingPinsToDiscConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5210,
            )

            return self._parent._cast(
                _5210.RingPinsToDiscConnectionModalAnalysisAtASpeed
            )

        @property
        def rolling_ring_connection_modal_analysis_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5212.RollingRingConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5212,
            )

            return self._parent._cast(_5212.RollingRingConnectionModalAnalysisAtASpeed)

        @property
        def shaft_to_mountable_component_connection_modal_analysis_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5217.ShaftToMountableComponentConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5217,
            )

            return self._parent._cast(
                _5217.ShaftToMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5219.SpiralBevelGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5219,
            )

            return self._parent._cast(_5219.SpiralBevelGearMeshModalAnalysisAtASpeed)

        @property
        def spring_damper_connection_modal_analysis_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5222.SpringDamperConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5222,
            )

            return self._parent._cast(_5222.SpringDamperConnectionModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5225.StraightBevelDiffGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5225,
            )

            return self._parent._cast(
                _5225.StraightBevelDiffGearMeshModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5228.StraightBevelGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5228,
            )

            return self._parent._cast(_5228.StraightBevelGearMeshModalAnalysisAtASpeed)

        @property
        def torque_converter_connection_modal_analysis_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5237.TorqueConverterConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5237,
            )

            return self._parent._cast(
                _5237.TorqueConverterConnectionModalAnalysisAtASpeed
            )

        @property
        def worm_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5243.WormGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5243,
            )

            return self._parent._cast(_5243.WormGearMeshModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5246.ZerolBevelGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5246,
            )

            return self._parent._cast(_5246.ZerolBevelGearMeshModalAnalysisAtASpeed)

        @property
        def abstract_shaft_to_mountable_component_connection_multibody_dynamics_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> (
            "_5381.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5381

            return self._parent._cast(
                _5381.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5382.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5382

            return self._parent._cast(
                _5382.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def belt_connection_multibody_dynamics_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5389.BeltConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5389

            return self._parent._cast(_5389.BeltConnectionMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5391.BevelDifferentialGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5391

            return self._parent._cast(
                _5391.BevelDifferentialGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5396.BevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5396

            return self._parent._cast(_5396.BevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def clutch_connection_multibody_dynamics_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5401.ClutchConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5401

            return self._parent._cast(_5401.ClutchConnectionMultibodyDynamicsAnalysis)

        @property
        def coaxial_connection_multibody_dynamics_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5405.CoaxialConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5405

            return self._parent._cast(_5405.CoaxialConnectionMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_connection_multibody_dynamics_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5407.ConceptCouplingConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5407

            return self._parent._cast(
                _5407.ConceptCouplingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5410.ConceptGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5410

            return self._parent._cast(_5410.ConceptGearMeshMultibodyDynamicsAnalysis)

        @property
        def conical_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5413.ConicalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5413

            return self._parent._cast(_5413.ConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def connection_multibody_dynamics_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5416.ConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5416

            return self._parent._cast(_5416.ConnectionMultibodyDynamicsAnalysis)

        @property
        def coupling_connection_multibody_dynamics_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5418.CouplingConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5418

            return self._parent._cast(_5418.CouplingConnectionMultibodyDynamicsAnalysis)

        @property
        def cvt_belt_connection_multibody_dynamics_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5421.CVTBeltConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5421

            return self._parent._cast(_5421.CVTBeltConnectionMultibodyDynamicsAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_multibody_dynamics_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5425.CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5425

            return self._parent._cast(
                _5425.CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_multibody_dynamics_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5427.CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5427

            return self._parent._cast(
                _5427.CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5428.CylindricalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5428

            return self._parent._cast(
                _5428.CylindricalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def face_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5434.FaceGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5434

            return self._parent._cast(_5434.FaceGearMeshMultibodyDynamicsAnalysis)

        @property
        def gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5439.GearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5439

            return self._parent._cast(_5439.GearMeshMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5444.HypoidGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5444

            return self._parent._cast(_5444.HypoidGearMeshMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5451.InterMountableComponentConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5451

            return self._parent._cast(
                _5451.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5452.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5452

            return self._parent._cast(
                _5452.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5455.KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5455

            return self._parent._cast(
                _5455.KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> (
            "_5458.KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5458

            return self._parent._cast(
                _5458.KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_multibody_dynamics_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5470.PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5470

            return self._parent._cast(
                _5470.PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def planetary_connection_multibody_dynamics_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5473.PlanetaryConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5473

            return self._parent._cast(
                _5473.PlanetaryConnectionMultibodyDynamicsAnalysis
            )

        @property
        def ring_pins_to_disc_connection_multibody_dynamics_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5480.RingPinsToDiscConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5480

            return self._parent._cast(
                _5480.RingPinsToDiscConnectionMultibodyDynamicsAnalysis
            )

        @property
        def rolling_ring_connection_multibody_dynamics_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5482.RollingRingConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5482

            return self._parent._cast(
                _5482.RollingRingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_multibody_dynamics_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5489.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5489

            return self._parent._cast(
                _5489.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5492.SpiralBevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5492

            return self._parent._cast(
                _5492.SpiralBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_connection_multibody_dynamics_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5495.SpringDamperConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5495

            return self._parent._cast(
                _5495.SpringDamperConnectionMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5498.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5498

            return self._parent._cast(
                _5498.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5501.StraightBevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5501

            return self._parent._cast(
                _5501.StraightBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_connection_multibody_dynamics_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5510.TorqueConverterConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5510

            return self._parent._cast(
                _5510.TorqueConverterConnectionMultibodyDynamicsAnalysis
            )

        @property
        def worm_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5519.WormGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5519

            return self._parent._cast(_5519.WormGearMeshMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5522.ZerolBevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5522

            return self._parent._cast(_5522.ZerolBevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_harmonic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5684.AbstractShaftToMountableComponentConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5684,
            )

            return self._parent._cast(
                _5684.AbstractShaftToMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_harmonic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5686.AGMAGleasonConicalGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5686,
            )

            return self._parent._cast(_5686.AGMAGleasonConicalGearMeshHarmonicAnalysis)

        @property
        def belt_connection_harmonic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5690.BeltConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5690,
            )

            return self._parent._cast(_5690.BeltConnectionHarmonicAnalysis)

        @property
        def bevel_differential_gear_mesh_harmonic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5693.BevelDifferentialGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5693,
            )

            return self._parent._cast(_5693.BevelDifferentialGearMeshHarmonicAnalysis)

        @property
        def bevel_gear_mesh_harmonic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5698.BevelGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5698,
            )

            return self._parent._cast(_5698.BevelGearMeshHarmonicAnalysis)

        @property
        def clutch_connection_harmonic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5702.ClutchConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5702,
            )

            return self._parent._cast(_5702.ClutchConnectionHarmonicAnalysis)

        @property
        def coaxial_connection_harmonic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5705.CoaxialConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5705,
            )

            return self._parent._cast(_5705.CoaxialConnectionHarmonicAnalysis)

        @property
        def concept_coupling_connection_harmonic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5708.ConceptCouplingConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5708,
            )

            return self._parent._cast(_5708.ConceptCouplingConnectionHarmonicAnalysis)

        @property
        def concept_gear_mesh_harmonic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5712.ConceptGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5712,
            )

            return self._parent._cast(_5712.ConceptGearMeshHarmonicAnalysis)

        @property
        def conical_gear_mesh_harmonic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5715.ConicalGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5715,
            )

            return self._parent._cast(_5715.ConicalGearMeshHarmonicAnalysis)

        @property
        def connection_harmonic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5717.ConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5717,
            )

            return self._parent._cast(_5717.ConnectionHarmonicAnalysis)

        @property
        def coupling_connection_harmonic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5719.CouplingConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5719,
            )

            return self._parent._cast(_5719.CouplingConnectionHarmonicAnalysis)

        @property
        def cvt_belt_connection_harmonic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5722.CVTBeltConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5722,
            )

            return self._parent._cast(_5722.CVTBeltConnectionHarmonicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_harmonic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5726.CycloidalDiscCentralBearingConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5726,
            )

            return self._parent._cast(
                _5726.CycloidalDiscCentralBearingConnectionHarmonicAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_harmonic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5728.CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5728,
            )

            return self._parent._cast(
                _5728.CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis
            )

        @property
        def cylindrical_gear_mesh_harmonic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5730.CylindricalGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5730,
            )

            return self._parent._cast(_5730.CylindricalGearMeshHarmonicAnalysis)

        @property
        def face_gear_mesh_harmonic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5750.FaceGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5750,
            )

            return self._parent._cast(_5750.FaceGearMeshHarmonicAnalysis)

        @property
        def gear_mesh_harmonic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5757.GearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5757,
            )

            return self._parent._cast(_5757.GearMeshHarmonicAnalysis)

        @property
        def hypoid_gear_mesh_harmonic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5774.HypoidGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5774,
            )

            return self._parent._cast(_5774.HypoidGearMeshHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_harmonic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5776.InterMountableComponentConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5776,
            )

            return self._parent._cast(
                _5776.InterMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_harmonic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5778.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5778,
            )

            return self._parent._cast(
                _5778.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_harmonic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5781.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5781,
            )

            return self._parent._cast(
                _5781.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_harmonic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5784.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5784,
            )

            return self._parent._cast(
                _5784.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_harmonic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5791.PartToPartShearCouplingConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5791,
            )

            return self._parent._cast(
                _5791.PartToPartShearCouplingConnectionHarmonicAnalysis
            )

        @property
        def planetary_connection_harmonic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5795.PlanetaryConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5795,
            )

            return self._parent._cast(_5795.PlanetaryConnectionHarmonicAnalysis)

        @property
        def ring_pins_to_disc_connection_harmonic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5803.RingPinsToDiscConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5803,
            )

            return self._parent._cast(_5803.RingPinsToDiscConnectionHarmonicAnalysis)

        @property
        def rolling_ring_connection_harmonic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5805.RollingRingConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5805,
            )

            return self._parent._cast(_5805.RollingRingConnectionHarmonicAnalysis)

        @property
        def shaft_to_mountable_component_connection_harmonic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5810.ShaftToMountableComponentConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5810,
            )

            return self._parent._cast(
                _5810.ShaftToMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_harmonic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5815.SpiralBevelGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5815,
            )

            return self._parent._cast(_5815.SpiralBevelGearMeshHarmonicAnalysis)

        @property
        def spring_damper_connection_harmonic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5817.SpringDamperConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5817,
            )

            return self._parent._cast(_5817.SpringDamperConnectionHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_harmonic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5822.StraightBevelDiffGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5822,
            )

            return self._parent._cast(_5822.StraightBevelDiffGearMeshHarmonicAnalysis)

        @property
        def straight_bevel_gear_mesh_harmonic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5825.StraightBevelGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5825,
            )

            return self._parent._cast(_5825.StraightBevelGearMeshHarmonicAnalysis)

        @property
        def torque_converter_connection_harmonic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5833.TorqueConverterConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5833,
            )

            return self._parent._cast(_5833.TorqueConverterConnectionHarmonicAnalysis)

        @property
        def worm_gear_mesh_harmonic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5841.WormGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5841,
            )

            return self._parent._cast(_5841.WormGearMeshHarmonicAnalysis)

        @property
        def zerol_bevel_gear_mesh_harmonic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_5844.ZerolBevelGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5844,
            )

            return self._parent._cast(_5844.ZerolBevelGearMeshHarmonicAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6013.AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6013,
            )

            return self._parent._cast(
                _6013.AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6015.AGMAGleasonConicalGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6015,
            )

            return self._parent._cast(
                _6015.AGMAGleasonConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def belt_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6019.BeltConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6019,
            )

            return self._parent._cast(
                _6019.BeltConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6022.BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6022,
            )

            return self._parent._cast(
                _6022.BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6027.BevelGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6027,
            )

            return self._parent._cast(
                _6027.BevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def clutch_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6031.ClutchConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6031,
            )

            return self._parent._cast(
                _6031.ClutchConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coaxial_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6034.CoaxialConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6034,
            )

            return self._parent._cast(
                _6034.CoaxialConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6036.ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6036,
            )

            return self._parent._cast(
                _6036.ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6040.ConceptGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6040,
            )

            return self._parent._cast(
                _6040.ConceptGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6043.ConicalGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6043,
            )

            return self._parent._cast(
                _6043.ConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6045.ConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6045,
            )

            return self._parent._cast(
                _6045.ConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6047.CouplingConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6047,
            )

            return self._parent._cast(
                _6047.CouplingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cvt_belt_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6050.CVTBeltConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6050,
            )

            return self._parent._cast(
                _6050.CVTBeltConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_central_bearing_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6054.CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6054,
            )

            return self._parent._cast(
                _6054.CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6056.CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6056,
            )

            return self._parent._cast(
                _6056.CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6058.CylindricalGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6058,
            )

            return self._parent._cast(
                _6058.CylindricalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6064.FaceGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6064,
            )

            return self._parent._cast(
                _6064.FaceGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6069.GearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6069,
            )

            return self._parent._cast(_6069.GearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def hypoid_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6074.HypoidGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6074,
            )

            return self._parent._cast(
                _6074.HypoidGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def inter_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> (
            "_6076.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6076,
            )

            return self._parent._cast(
                _6076.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6078.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6078,
            )

            return self._parent._cast(
                _6078.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6081.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6081,
            )

            return self._parent._cast(
                _6081.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6084.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6084,
            )

            return self._parent._cast(
                _6084.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> (
            "_6092.PartToPartShearCouplingConnectionHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6092,
            )

            return self._parent._cast(
                _6092.PartToPartShearCouplingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planetary_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6095.PlanetaryConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6095,
            )

            return self._parent._cast(
                _6095.PlanetaryConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def ring_pins_to_disc_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6102.RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6102,
            )

            return self._parent._cast(
                _6102.RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6104.RollingRingConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6104,
            )

            return self._parent._cast(
                _6104.RollingRingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_to_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6109.ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6109,
            )

            return self._parent._cast(
                _6109.ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6112.SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6112,
            )

            return self._parent._cast(
                _6112.SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6114.SpringDamperConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6114,
            )

            return self._parent._cast(
                _6114.SpringDamperConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6118.StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6118,
            )

            return self._parent._cast(
                _6118.StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6121.StraightBevelGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6121,
            )

            return self._parent._cast(
                _6121.StraightBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6129.TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6129,
            )

            return self._parent._cast(
                _6129.TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6136.WormGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6136,
            )

            return self._parent._cast(
                _6136.WormGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6139.ZerolBevelGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6139,
            )

            return self._parent._cast(
                _6139.ZerolBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_to_mountable_component_connection_dynamic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6282.AbstractShaftToMountableComponentConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6282

            return self._parent._cast(
                _6282.AbstractShaftToMountableComponentConnectionDynamicAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_dynamic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6284.AGMAGleasonConicalGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6284

            return self._parent._cast(_6284.AGMAGleasonConicalGearMeshDynamicAnalysis)

        @property
        def belt_connection_dynamic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6288.BeltConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6288

            return self._parent._cast(_6288.BeltConnectionDynamicAnalysis)

        @property
        def bevel_differential_gear_mesh_dynamic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6291.BevelDifferentialGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6291

            return self._parent._cast(_6291.BevelDifferentialGearMeshDynamicAnalysis)

        @property
        def bevel_gear_mesh_dynamic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6296.BevelGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6296

            return self._parent._cast(_6296.BevelGearMeshDynamicAnalysis)

        @property
        def clutch_connection_dynamic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6300.ClutchConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6300

            return self._parent._cast(_6300.ClutchConnectionDynamicAnalysis)

        @property
        def coaxial_connection_dynamic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6303.CoaxialConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6303

            return self._parent._cast(_6303.CoaxialConnectionDynamicAnalysis)

        @property
        def concept_coupling_connection_dynamic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6305.ConceptCouplingConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6305

            return self._parent._cast(_6305.ConceptCouplingConnectionDynamicAnalysis)

        @property
        def concept_gear_mesh_dynamic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6309.ConceptGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6309

            return self._parent._cast(_6309.ConceptGearMeshDynamicAnalysis)

        @property
        def conical_gear_mesh_dynamic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6312.ConicalGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6312

            return self._parent._cast(_6312.ConicalGearMeshDynamicAnalysis)

        @property
        def connection_dynamic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6314.ConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6314

            return self._parent._cast(_6314.ConnectionDynamicAnalysis)

        @property
        def coupling_connection_dynamic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6316.CouplingConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6316

            return self._parent._cast(_6316.CouplingConnectionDynamicAnalysis)

        @property
        def cvt_belt_connection_dynamic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6319.CVTBeltConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6319

            return self._parent._cast(_6319.CVTBeltConnectionDynamicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_dynamic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6323.CycloidalDiscCentralBearingConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6323

            return self._parent._cast(
                _6323.CycloidalDiscCentralBearingConnectionDynamicAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_dynamic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6325.CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6325

            return self._parent._cast(
                _6325.CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis
            )

        @property
        def cylindrical_gear_mesh_dynamic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6327.CylindricalGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6327

            return self._parent._cast(_6327.CylindricalGearMeshDynamicAnalysis)

        @property
        def face_gear_mesh_dynamic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6335.FaceGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6335

            return self._parent._cast(_6335.FaceGearMeshDynamicAnalysis)

        @property
        def gear_mesh_dynamic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6340.GearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6340

            return self._parent._cast(_6340.GearMeshDynamicAnalysis)

        @property
        def hypoid_gear_mesh_dynamic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6344.HypoidGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6344

            return self._parent._cast(_6344.HypoidGearMeshDynamicAnalysis)

        @property
        def inter_mountable_component_connection_dynamic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6346.InterMountableComponentConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6346

            return self._parent._cast(
                _6346.InterMountableComponentConnectionDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_dynamic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6348.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6348

            return self._parent._cast(
                _6348.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_dynamic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6351.KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6351

            return self._parent._cast(
                _6351.KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_dynamic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6354.KlingelnbergCycloPalloidSpiralBevelGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6354

            return self._parent._cast(
                _6354.KlingelnbergCycloPalloidSpiralBevelGearMeshDynamicAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_dynamic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6361.PartToPartShearCouplingConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6361

            return self._parent._cast(
                _6361.PartToPartShearCouplingConnectionDynamicAnalysis
            )

        @property
        def planetary_connection_dynamic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6364.PlanetaryConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6364

            return self._parent._cast(_6364.PlanetaryConnectionDynamicAnalysis)

        @property
        def ring_pins_to_disc_connection_dynamic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6371.RingPinsToDiscConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6371

            return self._parent._cast(_6371.RingPinsToDiscConnectionDynamicAnalysis)

        @property
        def rolling_ring_connection_dynamic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6373.RollingRingConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6373

            return self._parent._cast(_6373.RollingRingConnectionDynamicAnalysis)

        @property
        def shaft_to_mountable_component_connection_dynamic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6378.ShaftToMountableComponentConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6378

            return self._parent._cast(
                _6378.ShaftToMountableComponentConnectionDynamicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_dynamic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6381.SpiralBevelGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6381

            return self._parent._cast(_6381.SpiralBevelGearMeshDynamicAnalysis)

        @property
        def spring_damper_connection_dynamic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6383.SpringDamperConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6383

            return self._parent._cast(_6383.SpringDamperConnectionDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_dynamic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6387.StraightBevelDiffGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6387

            return self._parent._cast(_6387.StraightBevelDiffGearMeshDynamicAnalysis)

        @property
        def straight_bevel_gear_mesh_dynamic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6390.StraightBevelGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6390

            return self._parent._cast(_6390.StraightBevelGearMeshDynamicAnalysis)

        @property
        def torque_converter_connection_dynamic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6398.TorqueConverterConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6398

            return self._parent._cast(_6398.TorqueConverterConnectionDynamicAnalysis)

        @property
        def worm_gear_mesh_dynamic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6405.WormGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6405

            return self._parent._cast(_6405.WormGearMeshDynamicAnalysis)

        @property
        def zerol_bevel_gear_mesh_dynamic_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6408.ZerolBevelGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6408

            return self._parent._cast(_6408.ZerolBevelGearMeshDynamicAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_critical_speed_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6548.AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6548,
            )

            return self._parent._cast(
                _6548.AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_critical_speed_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6550.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6550,
            )

            return self._parent._cast(
                _6550.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis
            )

        @property
        def belt_connection_critical_speed_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6554.BeltConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6554,
            )

            return self._parent._cast(_6554.BeltConnectionCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_mesh_critical_speed_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6557.BevelDifferentialGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6557,
            )

            return self._parent._cast(
                _6557.BevelDifferentialGearMeshCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_mesh_critical_speed_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6562.BevelGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6562,
            )

            return self._parent._cast(_6562.BevelGearMeshCriticalSpeedAnalysis)

        @property
        def clutch_connection_critical_speed_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6566.ClutchConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6566,
            )

            return self._parent._cast(_6566.ClutchConnectionCriticalSpeedAnalysis)

        @property
        def coaxial_connection_critical_speed_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6569.CoaxialConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6569,
            )

            return self._parent._cast(_6569.CoaxialConnectionCriticalSpeedAnalysis)

        @property
        def concept_coupling_connection_critical_speed_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6571.ConceptCouplingConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6571,
            )

            return self._parent._cast(
                _6571.ConceptCouplingConnectionCriticalSpeedAnalysis
            )

        @property
        def concept_gear_mesh_critical_speed_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6575.ConceptGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6575,
            )

            return self._parent._cast(_6575.ConceptGearMeshCriticalSpeedAnalysis)

        @property
        def conical_gear_mesh_critical_speed_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6578.ConicalGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6578,
            )

            return self._parent._cast(_6578.ConicalGearMeshCriticalSpeedAnalysis)

        @property
        def connection_critical_speed_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6580.ConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6580,
            )

            return self._parent._cast(_6580.ConnectionCriticalSpeedAnalysis)

        @property
        def coupling_connection_critical_speed_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6582.CouplingConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6582,
            )

            return self._parent._cast(_6582.CouplingConnectionCriticalSpeedAnalysis)

        @property
        def cvt_belt_connection_critical_speed_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6588.CVTBeltConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6588,
            )

            return self._parent._cast(_6588.CVTBeltConnectionCriticalSpeedAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_critical_speed_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6592.CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6592,
            )

            return self._parent._cast(
                _6592.CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_critical_speed_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6594.CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6594,
            )

            return self._parent._cast(
                _6594.CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis
            )

        @property
        def cylindrical_gear_mesh_critical_speed_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6596.CylindricalGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6596,
            )

            return self._parent._cast(_6596.CylindricalGearMeshCriticalSpeedAnalysis)

        @property
        def face_gear_mesh_critical_speed_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6602.FaceGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6602,
            )

            return self._parent._cast(_6602.FaceGearMeshCriticalSpeedAnalysis)

        @property
        def gear_mesh_critical_speed_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6607.GearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6607,
            )

            return self._parent._cast(_6607.GearMeshCriticalSpeedAnalysis)

        @property
        def hypoid_gear_mesh_critical_speed_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6611.HypoidGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6611,
            )

            return self._parent._cast(_6611.HypoidGearMeshCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_critical_speed_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6613.InterMountableComponentConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6613,
            )

            return self._parent._cast(
                _6613.InterMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_critical_speed_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6615.KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6615,
            )

            return self._parent._cast(
                _6615.KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_critical_speed_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6618.KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6618,
            )

            return self._parent._cast(
                _6618.KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_critical_speed_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6621.KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6621,
            )

            return self._parent._cast(
                _6621.KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_critical_speed_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6628.PartToPartShearCouplingConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6628,
            )

            return self._parent._cast(
                _6628.PartToPartShearCouplingConnectionCriticalSpeedAnalysis
            )

        @property
        def planetary_connection_critical_speed_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6631.PlanetaryConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6631,
            )

            return self._parent._cast(_6631.PlanetaryConnectionCriticalSpeedAnalysis)

        @property
        def ring_pins_to_disc_connection_critical_speed_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6638.RingPinsToDiscConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6638,
            )

            return self._parent._cast(
                _6638.RingPinsToDiscConnectionCriticalSpeedAnalysis
            )

        @property
        def rolling_ring_connection_critical_speed_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6640.RollingRingConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6640,
            )

            return self._parent._cast(_6640.RollingRingConnectionCriticalSpeedAnalysis)

        @property
        def shaft_to_mountable_component_connection_critical_speed_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6645.ShaftToMountableComponentConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6645,
            )

            return self._parent._cast(
                _6645.ShaftToMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_critical_speed_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6648.SpiralBevelGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6648,
            )

            return self._parent._cast(_6648.SpiralBevelGearMeshCriticalSpeedAnalysis)

        @property
        def spring_damper_connection_critical_speed_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6650.SpringDamperConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6650,
            )

            return self._parent._cast(_6650.SpringDamperConnectionCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_critical_speed_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6654.StraightBevelDiffGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6654,
            )

            return self._parent._cast(
                _6654.StraightBevelDiffGearMeshCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_mesh_critical_speed_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6657.StraightBevelGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6657,
            )

            return self._parent._cast(_6657.StraightBevelGearMeshCriticalSpeedAnalysis)

        @property
        def torque_converter_connection_critical_speed_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6665.TorqueConverterConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6665,
            )

            return self._parent._cast(
                _6665.TorqueConverterConnectionCriticalSpeedAnalysis
            )

        @property
        def worm_gear_mesh_critical_speed_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6672.WormGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6672,
            )

            return self._parent._cast(_6672.WormGearMeshCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_mesh_critical_speed_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6675.ZerolBevelGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6675,
            )

            return self._parent._cast(_6675.ZerolBevelGearMeshCriticalSpeedAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_load_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6812.AbstractShaftToMountableComponentConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6812

            return self._parent._cast(
                _6812.AbstractShaftToMountableComponentConnectionLoadCase
            )

        @property
        def agma_gleason_conical_gear_mesh_load_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6817.AGMAGleasonConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6817

            return self._parent._cast(_6817.AGMAGleasonConicalGearMeshLoadCase)

        @property
        def belt_connection_load_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6823.BeltConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6823

            return self._parent._cast(_6823.BeltConnectionLoadCase)

        @property
        def bevel_differential_gear_mesh_load_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6826.BevelDifferentialGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6826

            return self._parent._cast(_6826.BevelDifferentialGearMeshLoadCase)

        @property
        def bevel_gear_mesh_load_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6831.BevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6831

            return self._parent._cast(_6831.BevelGearMeshLoadCase)

        @property
        def clutch_connection_load_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6835.ClutchConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6835

            return self._parent._cast(_6835.ClutchConnectionLoadCase)

        @property
        def coaxial_connection_load_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6839.CoaxialConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6839

            return self._parent._cast(_6839.CoaxialConnectionLoadCase)

        @property
        def concept_coupling_connection_load_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6841.ConceptCouplingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6841

            return self._parent._cast(_6841.ConceptCouplingConnectionLoadCase)

        @property
        def concept_gear_mesh_load_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6845.ConceptGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6845

            return self._parent._cast(_6845.ConceptGearMeshLoadCase)

        @property
        def conical_gear_mesh_load_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6849.ConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6849

            return self._parent._cast(_6849.ConicalGearMeshLoadCase)

        @property
        def connection_load_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6852.ConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6852

            return self._parent._cast(_6852.ConnectionLoadCase)

        @property
        def coupling_connection_load_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6854.CouplingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6854

            return self._parent._cast(_6854.CouplingConnectionLoadCase)

        @property
        def cvt_belt_connection_load_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6857.CVTBeltConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6857

            return self._parent._cast(_6857.CVTBeltConnectionLoadCase)

        @property
        def cycloidal_disc_central_bearing_connection_load_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6861.CycloidalDiscCentralBearingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6861

            return self._parent._cast(
                _6861.CycloidalDiscCentralBearingConnectionLoadCase
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_load_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6863.CycloidalDiscPlanetaryBearingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6863

            return self._parent._cast(
                _6863.CycloidalDiscPlanetaryBearingConnectionLoadCase
            )

        @property
        def cylindrical_gear_mesh_load_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6866.CylindricalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6866

            return self._parent._cast(_6866.CylindricalGearMeshLoadCase)

        @property
        def face_gear_mesh_load_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6888.FaceGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6888

            return self._parent._cast(_6888.FaceGearMeshLoadCase)

        @property
        def gear_mesh_load_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6895.GearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6895

            return self._parent._cast(_6895.GearMeshLoadCase)

        @property
        def hypoid_gear_mesh_load_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6909.HypoidGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6909

            return self._parent._cast(_6909.HypoidGearMeshLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6914.InterMountableComponentConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6914

            return self._parent._cast(_6914.InterMountableComponentConnectionLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6916.KlingelnbergCycloPalloidConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6916

            return self._parent._cast(
                _6916.KlingelnbergCycloPalloidConicalGearMeshLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6919.KlingelnbergCycloPalloidHypoidGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6919

            return self._parent._cast(
                _6919.KlingelnbergCycloPalloidHypoidGearMeshLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6922.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6922

            return self._parent._cast(
                _6922.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase
            )

        @property
        def part_to_part_shear_coupling_connection_load_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6932.PartToPartShearCouplingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6932

            return self._parent._cast(_6932.PartToPartShearCouplingConnectionLoadCase)

        @property
        def planetary_connection_load_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6935.PlanetaryConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6935

            return self._parent._cast(_6935.PlanetaryConnectionLoadCase)

        @property
        def ring_pins_to_disc_connection_load_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6947.RingPinsToDiscConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6947

            return self._parent._cast(_6947.RingPinsToDiscConnectionLoadCase)

        @property
        def rolling_ring_connection_load_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6949.RollingRingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6949

            return self._parent._cast(_6949.RollingRingConnectionLoadCase)

        @property
        def shaft_to_mountable_component_connection_load_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6954.ShaftToMountableComponentConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6954

            return self._parent._cast(_6954.ShaftToMountableComponentConnectionLoadCase)

        @property
        def spiral_bevel_gear_mesh_load_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6957.SpiralBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6957

            return self._parent._cast(_6957.SpiralBevelGearMeshLoadCase)

        @property
        def spring_damper_connection_load_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6959.SpringDamperConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6959

            return self._parent._cast(_6959.SpringDamperConnectionLoadCase)

        @property
        def straight_bevel_diff_gear_mesh_load_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6963.StraightBevelDiffGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6963

            return self._parent._cast(_6963.StraightBevelDiffGearMeshLoadCase)

        @property
        def straight_bevel_gear_mesh_load_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6966.StraightBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6966

            return self._parent._cast(_6966.StraightBevelGearMeshLoadCase)

        @property
        def torque_converter_connection_load_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6975.TorqueConverterConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6975

            return self._parent._cast(_6975.TorqueConverterConnectionLoadCase)

        @property
        def worm_gear_mesh_load_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6986.WormGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6986

            return self._parent._cast(_6986.WormGearMeshLoadCase)

        @property
        def zerol_bevel_gear_mesh_load_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_6989.ZerolBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6989

            return self._parent._cast(_6989.ZerolBevelGearMeshLoadCase)

        @property
        def abstract_shaft_to_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7011.AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7011,
            )

            return self._parent._cast(
                _7011.AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> (
            "_7017.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7017,
            )

            return self._parent._cast(
                _7017.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def belt_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7022.BeltConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7022,
            )

            return self._parent._cast(
                _7022.BeltConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7025.BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7025,
            )

            return self._parent._cast(
                _7025.BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7030.BevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7030,
            )

            return self._parent._cast(
                _7030.BevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7035.ClutchConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7035,
            )

            return self._parent._cast(
                _7035.ClutchConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coaxial_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7037.CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7037,
            )

            return self._parent._cast(
                _7037.CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7040.ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7040,
            )

            return self._parent._cast(
                _7040.ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7043.ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7043,
            )

            return self._parent._cast(
                _7043.ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7046.ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7046,
            )

            return self._parent._cast(
                _7046.ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7048.ConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7048,
            )

            return self._parent._cast(
                _7048.ConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7051.CouplingConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7051,
            )

            return self._parent._cast(
                _7051.CouplingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_belt_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7054.CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7054,
            )

            return self._parent._cast(
                _7054.CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_central_bearing_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7058.CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7058,
            )

            return self._parent._cast(
                _7058.CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7059.CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7059,
            )

            return self._parent._cast(
                _7059.CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7061.CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7061,
            )

            return self._parent._cast(
                _7061.CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7067.FaceGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7067,
            )

            return self._parent._cast(
                _7067.FaceGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7072.GearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7072,
            )

            return self._parent._cast(
                _7072.GearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7077.HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7077,
            )

            return self._parent._cast(
                _7077.HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def inter_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7079.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7079,
            )

            return self._parent._cast(
                _7079.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7081.KlingelnbergCycloPalloidConicalGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7081,
            )

            return self._parent._cast(
                _7081.KlingelnbergCycloPalloidConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7084.KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7084,
            )

            return self._parent._cast(
                _7084.KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7087.KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7087,
            )

            return self._parent._cast(
                _7087.KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7095.PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7095,
            )

            return self._parent._cast(
                _7095.PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planetary_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7097.PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7097,
            )

            return self._parent._cast(
                _7097.PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def ring_pins_to_disc_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7104.RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7104,
            )

            return self._parent._cast(
                _7104.RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7107.RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7107,
            )

            return self._parent._cast(
                _7107.RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_to_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7111.ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7111,
            )

            return self._parent._cast(
                _7111.ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7114.SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7114,
            )

            return self._parent._cast(
                _7114.SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7117.SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7117,
            )

            return self._parent._cast(
                _7117.SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7120.StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7120,
            )

            return self._parent._cast(
                _7120.StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7123.StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7123,
            )

            return self._parent._cast(
                _7123.StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7132.TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7132,
            )

            return self._parent._cast(
                _7132.TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7138.WormGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7138,
            )

            return self._parent._cast(
                _7138.WormGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7141.ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7141,
            )

            return self._parent._cast(
                _7141.ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_to_mountable_component_connection_advanced_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> (
            "_7275.AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection"
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7275,
            )

            return self._parent._cast(
                _7275.AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_mesh_advanced_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7280.AGMAGleasonConicalGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7280,
            )

            return self._parent._cast(
                _7280.AGMAGleasonConicalGearMeshAdvancedSystemDeflection
            )

        @property
        def belt_connection_advanced_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7284.BeltConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7284,
            )

            return self._parent._cast(_7284.BeltConnectionAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_mesh_advanced_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7287.BevelDifferentialGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7287,
            )

            return self._parent._cast(
                _7287.BevelDifferentialGearMeshAdvancedSystemDeflection
            )

        @property
        def bevel_gear_mesh_advanced_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7292.BevelGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7292,
            )

            return self._parent._cast(_7292.BevelGearMeshAdvancedSystemDeflection)

        @property
        def clutch_connection_advanced_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7297.ClutchConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7297,
            )

            return self._parent._cast(_7297.ClutchConnectionAdvancedSystemDeflection)

        @property
        def coaxial_connection_advanced_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7299.CoaxialConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7299,
            )

            return self._parent._cast(_7299.CoaxialConnectionAdvancedSystemDeflection)

        @property
        def concept_coupling_connection_advanced_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7302.ConceptCouplingConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7302,
            )

            return self._parent._cast(
                _7302.ConceptCouplingConnectionAdvancedSystemDeflection
            )

        @property
        def concept_gear_mesh_advanced_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7305.ConceptGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7305,
            )

            return self._parent._cast(_7305.ConceptGearMeshAdvancedSystemDeflection)

        @property
        def conical_gear_mesh_advanced_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7308.ConicalGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7308,
            )

            return self._parent._cast(_7308.ConicalGearMeshAdvancedSystemDeflection)

        @property
        def connection_advanced_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7310.ConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7310,
            )

            return self._parent._cast(_7310.ConnectionAdvancedSystemDeflection)

        @property
        def coupling_connection_advanced_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7314.CouplingConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7314,
            )

            return self._parent._cast(_7314.CouplingConnectionAdvancedSystemDeflection)

        @property
        def cvt_belt_connection_advanced_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7317.CVTBeltConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7317,
            )

            return self._parent._cast(_7317.CVTBeltConnectionAdvancedSystemDeflection)

        @property
        def cycloidal_disc_central_bearing_connection_advanced_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7321.CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7321,
            )

            return self._parent._cast(
                _7321.CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_advanced_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7322.CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7322,
            )

            return self._parent._cast(
                _7322.CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection
            )

        @property
        def cylindrical_gear_mesh_advanced_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7324.CylindricalGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7324,
            )

            return self._parent._cast(_7324.CylindricalGearMeshAdvancedSystemDeflection)

        @property
        def face_gear_mesh_advanced_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7331.FaceGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7331,
            )

            return self._parent._cast(_7331.FaceGearMeshAdvancedSystemDeflection)

        @property
        def gear_mesh_advanced_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7336.GearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7336,
            )

            return self._parent._cast(_7336.GearMeshAdvancedSystemDeflection)

        @property
        def hypoid_gear_mesh_advanced_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7340.HypoidGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7340,
            )

            return self._parent._cast(_7340.HypoidGearMeshAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_advanced_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7342.InterMountableComponentConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7342,
            )

            return self._parent._cast(
                _7342.InterMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_advanced_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7344.KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7344,
            )

            return self._parent._cast(
                _7344.KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_advanced_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7347.KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7347,
            )

            return self._parent._cast(
                _7347.KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_advanced_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> (
            "_7350.KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection"
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7350,
            )

            return self._parent._cast(
                _7350.KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_connection_advanced_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7359.PartToPartShearCouplingConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7359,
            )

            return self._parent._cast(
                _7359.PartToPartShearCouplingConnectionAdvancedSystemDeflection
            )

        @property
        def planetary_connection_advanced_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7361.PlanetaryConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7361,
            )

            return self._parent._cast(_7361.PlanetaryConnectionAdvancedSystemDeflection)

        @property
        def ring_pins_to_disc_connection_advanced_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7368.RingPinsToDiscConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7368,
            )

            return self._parent._cast(
                _7368.RingPinsToDiscConnectionAdvancedSystemDeflection
            )

        @property
        def rolling_ring_connection_advanced_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7371.RollingRingConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7371,
            )

            return self._parent._cast(
                _7371.RollingRingConnectionAdvancedSystemDeflection
            )

        @property
        def shaft_to_mountable_component_connection_advanced_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7375.ShaftToMountableComponentConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7375,
            )

            return self._parent._cast(
                _7375.ShaftToMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_advanced_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7378.SpiralBevelGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7378,
            )

            return self._parent._cast(_7378.SpiralBevelGearMeshAdvancedSystemDeflection)

        @property
        def spring_damper_connection_advanced_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7381.SpringDamperConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7381,
            )

            return self._parent._cast(
                _7381.SpringDamperConnectionAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_mesh_advanced_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7384.StraightBevelDiffGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7384,
            )

            return self._parent._cast(
                _7384.StraightBevelDiffGearMeshAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_advanced_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7387.StraightBevelGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7387,
            )

            return self._parent._cast(
                _7387.StraightBevelGearMeshAdvancedSystemDeflection
            )

        @property
        def torque_converter_connection_advanced_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7396.TorqueConverterConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7396,
            )

            return self._parent._cast(
                _7396.TorqueConverterConnectionAdvancedSystemDeflection
            )

        @property
        def worm_gear_mesh_advanced_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7403.WormGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7403,
            )

            return self._parent._cast(_7403.WormGearMeshAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_advanced_system_deflection(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7406.ZerolBevelGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7406,
            )

            return self._parent._cast(_7406.ZerolBevelGearMeshAdvancedSystemDeflection)

        @property
        def connection_analysis_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_fe_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7542.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7543.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_time_series_load_analysis_case(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "_7544.ConnectionTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis(
            self: "ConnectionAnalysis._Cast_ConnectionAnalysis",
        ) -> "ConnectionAnalysis":
            return self._parent

        def __getattr__(self: "ConnectionAnalysis._Cast_ConnectionAnalysis", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectionAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def short_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShortName

        if temp is None:
            return ""

        return temp

    @property
    def cast_to(self: Self) -> "ConnectionAnalysis._Cast_ConnectionAnalysis":
        return self._Cast_ConnectionAnalysis(self)
