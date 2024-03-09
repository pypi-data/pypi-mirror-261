"""PartCompoundAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from PIL.Image import Image

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7545
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases", "PartCompoundAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2853,
        _2854,
        _2855,
        _2857,
        _2859,
        _2860,
        _2861,
        _2863,
        _2864,
        _2866,
        _2867,
        _2868,
        _2869,
        _2871,
        _2872,
        _2873,
        _2874,
        _2876,
        _2878,
        _2879,
        _2881,
        _2882,
        _2884,
        _2885,
        _2887,
        _2889,
        _2890,
        _2892,
        _2894,
        _2895,
        _2896,
        _2898,
        _2900,
        _2902,
        _2903,
        _2904,
        _2906,
        _2907,
        _2909,
        _2910,
        _2911,
        _2912,
        _2914,
        _2915,
        _2916,
        _2918,
        _2920,
        _2922,
        _2923,
        _2925,
        _2926,
        _2928,
        _2929,
        _2930,
        _2931,
        _2932,
        _2933,
        _2934,
        _2936,
        _2938,
        _2939,
        _2940,
        _2941,
        _2942,
        _2943,
        _2945,
        _2946,
        _2948,
        _2949,
        _2951,
        _2953,
        _2954,
        _2956,
        _2957,
        _2959,
        _2960,
        _2962,
        _2963,
        _2965,
        _2966,
        _2967,
        _2968,
        _2969,
        _2970,
        _2971,
        _2972,
        _2974,
        _2975,
        _2976,
        _2977,
        _2978,
        _2980,
        _2981,
        _2983,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3118,
        _3119,
        _3120,
        _3122,
        _3124,
        _3125,
        _3126,
        _3128,
        _3129,
        _3131,
        _3132,
        _3133,
        _3134,
        _3136,
        _3137,
        _3138,
        _3139,
        _3141,
        _3143,
        _3144,
        _3146,
        _3147,
        _3149,
        _3150,
        _3152,
        _3154,
        _3155,
        _3157,
        _3159,
        _3160,
        _3161,
        _3163,
        _3165,
        _3167,
        _3168,
        _3169,
        _3170,
        _3171,
        _3173,
        _3174,
        _3175,
        _3176,
        _3178,
        _3179,
        _3180,
        _3182,
        _3184,
        _3186,
        _3187,
        _3189,
        _3190,
        _3192,
        _3193,
        _3194,
        _3195,
        _3196,
        _3197,
        _3198,
        _3200,
        _3202,
        _3203,
        _3204,
        _3205,
        _3206,
        _3207,
        _3209,
        _3210,
        _3212,
        _3213,
        _3214,
        _3216,
        _3217,
        _3219,
        _3220,
        _3222,
        _3223,
        _3225,
        _3226,
        _3228,
        _3229,
        _3230,
        _3231,
        _3232,
        _3233,
        _3234,
        _3235,
        _3237,
        _3238,
        _3239,
        _3240,
        _3241,
        _3243,
        _3244,
        _3246,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3377,
        _3378,
        _3379,
        _3381,
        _3383,
        _3384,
        _3385,
        _3387,
        _3388,
        _3390,
        _3391,
        _3392,
        _3393,
        _3395,
        _3396,
        _3397,
        _3398,
        _3400,
        _3402,
        _3403,
        _3405,
        _3406,
        _3408,
        _3409,
        _3411,
        _3413,
        _3414,
        _3416,
        _3418,
        _3419,
        _3420,
        _3422,
        _3424,
        _3426,
        _3427,
        _3428,
        _3429,
        _3430,
        _3432,
        _3433,
        _3434,
        _3435,
        _3437,
        _3438,
        _3439,
        _3441,
        _3443,
        _3445,
        _3446,
        _3448,
        _3449,
        _3451,
        _3452,
        _3453,
        _3454,
        _3455,
        _3456,
        _3457,
        _3459,
        _3461,
        _3462,
        _3463,
        _3464,
        _3465,
        _3466,
        _3468,
        _3469,
        _3471,
        _3472,
        _3473,
        _3475,
        _3476,
        _3478,
        _3479,
        _3481,
        _3482,
        _3484,
        _3485,
        _3487,
        _3488,
        _3489,
        _3490,
        _3491,
        _3492,
        _3493,
        _3494,
        _3496,
        _3497,
        _3498,
        _3499,
        _3500,
        _3502,
        _3503,
        _3505,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3636,
        _3637,
        _3638,
        _3640,
        _3642,
        _3643,
        _3644,
        _3646,
        _3647,
        _3649,
        _3650,
        _3651,
        _3652,
        _3654,
        _3655,
        _3656,
        _3657,
        _3659,
        _3661,
        _3662,
        _3664,
        _3665,
        _3667,
        _3668,
        _3670,
        _3672,
        _3673,
        _3675,
        _3677,
        _3678,
        _3679,
        _3681,
        _3683,
        _3685,
        _3686,
        _3687,
        _3688,
        _3689,
        _3691,
        _3692,
        _3693,
        _3694,
        _3696,
        _3697,
        _3698,
        _3700,
        _3702,
        _3704,
        _3705,
        _3707,
        _3708,
        _3710,
        _3711,
        _3712,
        _3713,
        _3714,
        _3715,
        _3716,
        _3718,
        _3720,
        _3721,
        _3722,
        _3723,
        _3724,
        _3725,
        _3727,
        _3728,
        _3730,
        _3731,
        _3732,
        _3734,
        _3735,
        _3737,
        _3738,
        _3740,
        _3741,
        _3743,
        _3744,
        _3746,
        _3747,
        _3748,
        _3749,
        _3750,
        _3751,
        _3752,
        _3753,
        _3755,
        _3756,
        _3757,
        _3758,
        _3759,
        _3761,
        _3762,
        _3764,
    )
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3899,
        _3900,
        _3901,
        _3903,
        _3905,
        _3906,
        _3907,
        _3909,
        _3910,
        _3912,
        _3913,
        _3914,
        _3915,
        _3917,
        _3918,
        _3919,
        _3920,
        _3922,
        _3924,
        _3925,
        _3927,
        _3928,
        _3930,
        _3931,
        _3933,
        _3935,
        _3936,
        _3938,
        _3940,
        _3941,
        _3942,
        _3944,
        _3946,
        _3948,
        _3949,
        _3950,
        _3951,
        _3952,
        _3954,
        _3955,
        _3956,
        _3957,
        _3959,
        _3960,
        _3961,
        _3963,
        _3965,
        _3967,
        _3968,
        _3970,
        _3971,
        _3973,
        _3974,
        _3975,
        _3976,
        _3977,
        _3978,
        _3979,
        _3981,
        _3983,
        _3984,
        _3985,
        _3986,
        _3987,
        _3988,
        _3990,
        _3991,
        _3993,
        _3994,
        _3995,
        _3997,
        _3998,
        _4000,
        _4001,
        _4003,
        _4004,
        _4006,
        _4007,
        _4009,
        _4010,
        _4011,
        _4012,
        _4013,
        _4014,
        _4015,
        _4016,
        _4018,
        _4019,
        _4020,
        _4021,
        _4022,
        _4024,
        _4025,
        _4027,
    )
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4169,
        _4170,
        _4171,
        _4173,
        _4175,
        _4176,
        _4177,
        _4179,
        _4180,
        _4182,
        _4183,
        _4184,
        _4185,
        _4187,
        _4188,
        _4189,
        _4190,
        _4192,
        _4194,
        _4195,
        _4197,
        _4198,
        _4200,
        _4201,
        _4203,
        _4205,
        _4206,
        _4208,
        _4210,
        _4211,
        _4212,
        _4214,
        _4216,
        _4218,
        _4219,
        _4220,
        _4221,
        _4222,
        _4224,
        _4225,
        _4226,
        _4227,
        _4229,
        _4230,
        _4231,
        _4233,
        _4235,
        _4237,
        _4238,
        _4240,
        _4241,
        _4243,
        _4244,
        _4245,
        _4246,
        _4247,
        _4248,
        _4249,
        _4251,
        _4253,
        _4254,
        _4255,
        _4256,
        _4257,
        _4258,
        _4260,
        _4261,
        _4263,
        _4264,
        _4265,
        _4267,
        _4268,
        _4270,
        _4271,
        _4273,
        _4274,
        _4276,
        _4277,
        _4279,
        _4280,
        _4281,
        _4282,
        _4283,
        _4284,
        _4285,
        _4286,
        _4288,
        _4289,
        _4290,
        _4291,
        _4292,
        _4294,
        _4295,
        _4297,
    )
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4445,
        _4446,
        _4447,
        _4449,
        _4451,
        _4452,
        _4453,
        _4455,
        _4456,
        _4458,
        _4459,
        _4460,
        _4461,
        _4463,
        _4464,
        _4465,
        _4466,
        _4468,
        _4470,
        _4471,
        _4473,
        _4474,
        _4476,
        _4477,
        _4479,
        _4481,
        _4482,
        _4484,
        _4486,
        _4487,
        _4488,
        _4490,
        _4492,
        _4494,
        _4495,
        _4496,
        _4497,
        _4498,
        _4500,
        _4501,
        _4502,
        _4503,
        _4505,
        _4506,
        _4507,
        _4509,
        _4511,
        _4513,
        _4514,
        _4516,
        _4517,
        _4519,
        _4520,
        _4521,
        _4522,
        _4523,
        _4524,
        _4525,
        _4527,
        _4529,
        _4530,
        _4531,
        _4532,
        _4533,
        _4534,
        _4536,
        _4537,
        _4539,
        _4540,
        _4541,
        _4543,
        _4544,
        _4546,
        _4547,
        _4549,
        _4550,
        _4552,
        _4553,
        _4555,
        _4556,
        _4557,
        _4558,
        _4559,
        _4560,
        _4561,
        _4562,
        _4564,
        _4565,
        _4566,
        _4567,
        _4568,
        _4570,
        _4571,
        _4573,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4730,
        _4731,
        _4732,
        _4734,
        _4736,
        _4737,
        _4738,
        _4740,
        _4741,
        _4743,
        _4744,
        _4745,
        _4746,
        _4748,
        _4749,
        _4750,
        _4751,
        _4753,
        _4755,
        _4756,
        _4758,
        _4759,
        _4761,
        _4762,
        _4764,
        _4766,
        _4767,
        _4769,
        _4771,
        _4772,
        _4773,
        _4775,
        _4777,
        _4779,
        _4780,
        _4781,
        _4782,
        _4783,
        _4785,
        _4786,
        _4787,
        _4788,
        _4790,
        _4791,
        _4792,
        _4794,
        _4796,
        _4798,
        _4799,
        _4801,
        _4802,
        _4804,
        _4805,
        _4806,
        _4807,
        _4808,
        _4809,
        _4810,
        _4812,
        _4814,
        _4815,
        _4816,
        _4817,
        _4818,
        _4819,
        _4821,
        _4822,
        _4824,
        _4825,
        _4826,
        _4828,
        _4829,
        _4831,
        _4832,
        _4834,
        _4835,
        _4837,
        _4838,
        _4840,
        _4841,
        _4842,
        _4843,
        _4844,
        _4845,
        _4846,
        _4847,
        _4849,
        _4850,
        _4851,
        _4852,
        _4853,
        _4855,
        _4856,
        _4858,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _4990,
        _4991,
        _4992,
        _4994,
        _4996,
        _4997,
        _4998,
        _5000,
        _5001,
        _5003,
        _5004,
        _5005,
        _5006,
        _5008,
        _5009,
        _5010,
        _5011,
        _5013,
        _5015,
        _5016,
        _5018,
        _5019,
        _5021,
        _5022,
        _5024,
        _5026,
        _5027,
        _5029,
        _5031,
        _5032,
        _5033,
        _5035,
        _5037,
        _5039,
        _5040,
        _5041,
        _5042,
        _5043,
        _5045,
        _5046,
        _5047,
        _5048,
        _5050,
        _5051,
        _5052,
        _5054,
        _5056,
        _5058,
        _5059,
        _5061,
        _5062,
        _5064,
        _5065,
        _5066,
        _5067,
        _5068,
        _5069,
        _5070,
        _5072,
        _5074,
        _5075,
        _5076,
        _5077,
        _5078,
        _5079,
        _5081,
        _5082,
        _5084,
        _5085,
        _5086,
        _5088,
        _5089,
        _5091,
        _5092,
        _5094,
        _5095,
        _5097,
        _5098,
        _5100,
        _5101,
        _5102,
        _5103,
        _5104,
        _5105,
        _5106,
        _5107,
        _5109,
        _5110,
        _5111,
        _5112,
        _5113,
        _5115,
        _5116,
        _5118,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5249,
        _5250,
        _5251,
        _5253,
        _5255,
        _5256,
        _5257,
        _5259,
        _5260,
        _5262,
        _5263,
        _5264,
        _5265,
        _5267,
        _5268,
        _5269,
        _5270,
        _5272,
        _5274,
        _5275,
        _5277,
        _5278,
        _5280,
        _5281,
        _5283,
        _5285,
        _5286,
        _5288,
        _5290,
        _5291,
        _5292,
        _5294,
        _5296,
        _5298,
        _5299,
        _5300,
        _5301,
        _5302,
        _5304,
        _5305,
        _5306,
        _5307,
        _5309,
        _5310,
        _5311,
        _5313,
        _5315,
        _5317,
        _5318,
        _5320,
        _5321,
        _5323,
        _5324,
        _5325,
        _5326,
        _5327,
        _5328,
        _5329,
        _5331,
        _5333,
        _5334,
        _5335,
        _5336,
        _5337,
        _5338,
        _5340,
        _5341,
        _5343,
        _5344,
        _5345,
        _5347,
        _5348,
        _5350,
        _5351,
        _5353,
        _5354,
        _5356,
        _5357,
        _5359,
        _5360,
        _5361,
        _5362,
        _5363,
        _5364,
        _5365,
        _5366,
        _5368,
        _5369,
        _5370,
        _5371,
        _5372,
        _5374,
        _5375,
        _5377,
    )
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5531,
        _5532,
        _5533,
        _5535,
        _5537,
        _5538,
        _5539,
        _5541,
        _5542,
        _5544,
        _5545,
        _5546,
        _5547,
        _5549,
        _5550,
        _5551,
        _5552,
        _5554,
        _5556,
        _5557,
        _5559,
        _5560,
        _5562,
        _5563,
        _5565,
        _5567,
        _5568,
        _5570,
        _5572,
        _5573,
        _5574,
        _5576,
        _5578,
        _5580,
        _5581,
        _5582,
        _5583,
        _5584,
        _5586,
        _5587,
        _5588,
        _5589,
        _5591,
        _5592,
        _5593,
        _5595,
        _5597,
        _5599,
        _5600,
        _5602,
        _5603,
        _5605,
        _5606,
        _5607,
        _5608,
        _5609,
        _5610,
        _5611,
        _5613,
        _5615,
        _5616,
        _5617,
        _5618,
        _5619,
        _5620,
        _5622,
        _5623,
        _5625,
        _5626,
        _5627,
        _5629,
        _5630,
        _5632,
        _5633,
        _5635,
        _5636,
        _5638,
        _5639,
        _5641,
        _5642,
        _5643,
        _5644,
        _5645,
        _5646,
        _5647,
        _5648,
        _5650,
        _5651,
        _5652,
        _5653,
        _5654,
        _5656,
        _5657,
        _5659,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5881,
        _5882,
        _5883,
        _5885,
        _5887,
        _5888,
        _5889,
        _5891,
        _5892,
        _5894,
        _5895,
        _5896,
        _5897,
        _5899,
        _5900,
        _5901,
        _5902,
        _5904,
        _5906,
        _5907,
        _5909,
        _5910,
        _5912,
        _5913,
        _5915,
        _5917,
        _5918,
        _5920,
        _5922,
        _5923,
        _5924,
        _5926,
        _5928,
        _5930,
        _5931,
        _5932,
        _5933,
        _5934,
        _5936,
        _5937,
        _5938,
        _5939,
        _5941,
        _5942,
        _5943,
        _5945,
        _5947,
        _5949,
        _5950,
        _5952,
        _5953,
        _5955,
        _5956,
        _5957,
        _5958,
        _5959,
        _5960,
        _5961,
        _5963,
        _5965,
        _5966,
        _5967,
        _5968,
        _5969,
        _5970,
        _5972,
        _5973,
        _5975,
        _5976,
        _5977,
        _5979,
        _5980,
        _5982,
        _5983,
        _5985,
        _5986,
        _5988,
        _5989,
        _5991,
        _5992,
        _5993,
        _5994,
        _5995,
        _5996,
        _5997,
        _5998,
        _6000,
        _6001,
        _6002,
        _6003,
        _6004,
        _6006,
        _6007,
        _6009,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6141,
        _6142,
        _6143,
        _6145,
        _6147,
        _6148,
        _6149,
        _6151,
        _6152,
        _6154,
        _6155,
        _6156,
        _6157,
        _6159,
        _6160,
        _6161,
        _6162,
        _6164,
        _6166,
        _6167,
        _6169,
        _6170,
        _6172,
        _6173,
        _6175,
        _6177,
        _6178,
        _6180,
        _6182,
        _6183,
        _6184,
        _6186,
        _6188,
        _6190,
        _6191,
        _6192,
        _6193,
        _6194,
        _6196,
        _6197,
        _6198,
        _6199,
        _6201,
        _6202,
        _6203,
        _6205,
        _6207,
        _6209,
        _6210,
        _6212,
        _6213,
        _6215,
        _6216,
        _6217,
        _6218,
        _6219,
        _6220,
        _6221,
        _6223,
        _6225,
        _6226,
        _6227,
        _6228,
        _6229,
        _6230,
        _6232,
        _6233,
        _6235,
        _6236,
        _6237,
        _6239,
        _6240,
        _6242,
        _6243,
        _6245,
        _6246,
        _6248,
        _6249,
        _6251,
        _6252,
        _6253,
        _6254,
        _6255,
        _6256,
        _6257,
        _6258,
        _6260,
        _6261,
        _6262,
        _6263,
        _6264,
        _6266,
        _6267,
        _6269,
    )
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6410,
        _6411,
        _6412,
        _6414,
        _6416,
        _6417,
        _6418,
        _6420,
        _6421,
        _6423,
        _6424,
        _6425,
        _6426,
        _6428,
        _6429,
        _6430,
        _6431,
        _6433,
        _6435,
        _6436,
        _6438,
        _6439,
        _6441,
        _6442,
        _6444,
        _6446,
        _6447,
        _6449,
        _6451,
        _6452,
        _6453,
        _6455,
        _6457,
        _6459,
        _6460,
        _6461,
        _6462,
        _6463,
        _6465,
        _6466,
        _6467,
        _6468,
        _6470,
        _6471,
        _6472,
        _6474,
        _6476,
        _6478,
        _6479,
        _6481,
        _6482,
        _6484,
        _6485,
        _6486,
        _6487,
        _6488,
        _6489,
        _6490,
        _6492,
        _6494,
        _6495,
        _6496,
        _6497,
        _6498,
        _6499,
        _6501,
        _6502,
        _6504,
        _6505,
        _6506,
        _6508,
        _6509,
        _6511,
        _6512,
        _6514,
        _6515,
        _6517,
        _6518,
        _6520,
        _6521,
        _6522,
        _6523,
        _6524,
        _6525,
        _6526,
        _6527,
        _6529,
        _6530,
        _6531,
        _6532,
        _6533,
        _6535,
        _6536,
        _6538,
    )
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6677,
        _6678,
        _6679,
        _6681,
        _6683,
        _6684,
        _6685,
        _6687,
        _6688,
        _6690,
        _6691,
        _6692,
        _6693,
        _6695,
        _6696,
        _6697,
        _6698,
        _6700,
        _6702,
        _6703,
        _6705,
        _6706,
        _6708,
        _6709,
        _6711,
        _6713,
        _6714,
        _6716,
        _6718,
        _6719,
        _6720,
        _6722,
        _6724,
        _6726,
        _6727,
        _6728,
        _6729,
        _6730,
        _6732,
        _6733,
        _6734,
        _6735,
        _6737,
        _6738,
        _6739,
        _6741,
        _6743,
        _6745,
        _6746,
        _6748,
        _6749,
        _6751,
        _6752,
        _6753,
        _6754,
        _6755,
        _6756,
        _6757,
        _6759,
        _6761,
        _6762,
        _6763,
        _6764,
        _6765,
        _6766,
        _6768,
        _6769,
        _6771,
        _6772,
        _6773,
        _6775,
        _6776,
        _6778,
        _6779,
        _6781,
        _6782,
        _6784,
        _6785,
        _6787,
        _6788,
        _6789,
        _6790,
        _6791,
        _6792,
        _6793,
        _6794,
        _6796,
        _6797,
        _6798,
        _6799,
        _6800,
        _6802,
        _6803,
        _6805,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7143,
        _7144,
        _7145,
        _7147,
        _7149,
        _7150,
        _7151,
        _7153,
        _7154,
        _7156,
        _7157,
        _7158,
        _7159,
        _7161,
        _7162,
        _7163,
        _7164,
        _7166,
        _7168,
        _7169,
        _7171,
        _7172,
        _7174,
        _7175,
        _7177,
        _7179,
        _7180,
        _7182,
        _7184,
        _7185,
        _7186,
        _7188,
        _7190,
        _7192,
        _7193,
        _7194,
        _7195,
        _7196,
        _7198,
        _7199,
        _7200,
        _7201,
        _7203,
        _7204,
        _7205,
        _7207,
        _7209,
        _7211,
        _7212,
        _7214,
        _7215,
        _7217,
        _7218,
        _7219,
        _7220,
        _7221,
        _7222,
        _7223,
        _7225,
        _7227,
        _7228,
        _7229,
        _7230,
        _7231,
        _7232,
        _7234,
        _7235,
        _7237,
        _7238,
        _7239,
        _7241,
        _7242,
        _7244,
        _7245,
        _7247,
        _7248,
        _7250,
        _7251,
        _7253,
        _7254,
        _7255,
        _7256,
        _7257,
        _7258,
        _7259,
        _7260,
        _7262,
        _7263,
        _7264,
        _7265,
        _7266,
        _7268,
        _7269,
        _7271,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7408,
        _7409,
        _7410,
        _7412,
        _7414,
        _7415,
        _7416,
        _7418,
        _7419,
        _7421,
        _7422,
        _7423,
        _7424,
        _7426,
        _7427,
        _7428,
        _7429,
        _7431,
        _7433,
        _7434,
        _7436,
        _7437,
        _7439,
        _7440,
        _7442,
        _7444,
        _7445,
        _7447,
        _7449,
        _7450,
        _7451,
        _7453,
        _7455,
        _7457,
        _7458,
        _7459,
        _7460,
        _7461,
        _7463,
        _7464,
        _7465,
        _7466,
        _7468,
        _7469,
        _7470,
        _7472,
        _7474,
        _7476,
        _7477,
        _7479,
        _7480,
        _7482,
        _7483,
        _7484,
        _7485,
        _7486,
        _7487,
        _7488,
        _7490,
        _7492,
        _7493,
        _7494,
        _7495,
        _7496,
        _7497,
        _7499,
        _7500,
        _7502,
        _7503,
        _7504,
        _7506,
        _7507,
        _7509,
        _7510,
        _7512,
        _7513,
        _7515,
        _7516,
        _7518,
        _7519,
        _7520,
        _7521,
        _7522,
        _7523,
        _7524,
        _7525,
        _7527,
        _7528,
        _7529,
        _7530,
        _7531,
        _7533,
        _7534,
        _7536,
    )
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("PartCompoundAnalysis",)


Self = TypeVar("Self", bound="PartCompoundAnalysis")


class PartCompoundAnalysis(_7545.DesignEntityCompoundAnalysis):
    """PartCompoundAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartCompoundAnalysis")

    class _Cast_PartCompoundAnalysis:
        """Special nested class for casting PartCompoundAnalysis to subclasses."""

        def __init__(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
            parent: "PartCompoundAnalysis",
        ):
            self._parent = parent

        @property
        def design_entity_compound_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def abstract_assembly_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2853.AbstractAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2853,
            )

            return self._parent._cast(_2853.AbstractAssemblyCompoundSystemDeflection)

        @property
        def abstract_shaft_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2854.AbstractShaftCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2854,
            )

            return self._parent._cast(_2854.AbstractShaftCompoundSystemDeflection)

        @property
        def abstract_shaft_or_housing_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2855.AbstractShaftOrHousingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2855,
            )

            return self._parent._cast(
                _2855.AbstractShaftOrHousingCompoundSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2857.AGMAGleasonConicalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2857,
            )

            return self._parent._cast(
                _2857.AGMAGleasonConicalGearCompoundSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2859.AGMAGleasonConicalGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2859,
            )

            return self._parent._cast(
                _2859.AGMAGleasonConicalGearSetCompoundSystemDeflection
            )

        @property
        def assembly_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2860.AssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2860,
            )

            return self._parent._cast(_2860.AssemblyCompoundSystemDeflection)

        @property
        def bearing_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2861.BearingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2861,
            )

            return self._parent._cast(_2861.BearingCompoundSystemDeflection)

        @property
        def belt_drive_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2863.BeltDriveCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2863,
            )

            return self._parent._cast(_2863.BeltDriveCompoundSystemDeflection)

        @property
        def bevel_differential_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2864.BevelDifferentialGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2864,
            )

            return self._parent._cast(
                _2864.BevelDifferentialGearCompoundSystemDeflection
            )

        @property
        def bevel_differential_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2866.BevelDifferentialGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2866,
            )

            return self._parent._cast(
                _2866.BevelDifferentialGearSetCompoundSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2867.BevelDifferentialPlanetGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2867,
            )

            return self._parent._cast(
                _2867.BevelDifferentialPlanetGearCompoundSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2868.BevelDifferentialSunGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2868,
            )

            return self._parent._cast(
                _2868.BevelDifferentialSunGearCompoundSystemDeflection
            )

        @property
        def bevel_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2869.BevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2869,
            )

            return self._parent._cast(_2869.BevelGearCompoundSystemDeflection)

        @property
        def bevel_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2871.BevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2871,
            )

            return self._parent._cast(_2871.BevelGearSetCompoundSystemDeflection)

        @property
        def bolt_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2872.BoltCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2872,
            )

            return self._parent._cast(_2872.BoltCompoundSystemDeflection)

        @property
        def bolted_joint_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2873.BoltedJointCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2873,
            )

            return self._parent._cast(_2873.BoltedJointCompoundSystemDeflection)

        @property
        def clutch_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2874.ClutchCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2874,
            )

            return self._parent._cast(_2874.ClutchCompoundSystemDeflection)

        @property
        def clutch_half_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2876.ClutchHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2876,
            )

            return self._parent._cast(_2876.ClutchHalfCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2878.ComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2878,
            )

            return self._parent._cast(_2878.ComponentCompoundSystemDeflection)

        @property
        def concept_coupling_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2879.ConceptCouplingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2879,
            )

            return self._parent._cast(_2879.ConceptCouplingCompoundSystemDeflection)

        @property
        def concept_coupling_half_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2881.ConceptCouplingHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2881,
            )

            return self._parent._cast(_2881.ConceptCouplingHalfCompoundSystemDeflection)

        @property
        def concept_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2882.ConceptGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2882,
            )

            return self._parent._cast(_2882.ConceptGearCompoundSystemDeflection)

        @property
        def concept_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2884.ConceptGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2884,
            )

            return self._parent._cast(_2884.ConceptGearSetCompoundSystemDeflection)

        @property
        def conical_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2885.ConicalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2885,
            )

            return self._parent._cast(_2885.ConicalGearCompoundSystemDeflection)

        @property
        def conical_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2887.ConicalGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2887,
            )

            return self._parent._cast(_2887.ConicalGearSetCompoundSystemDeflection)

        @property
        def connector_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2889.ConnectorCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2889,
            )

            return self._parent._cast(_2889.ConnectorCompoundSystemDeflection)

        @property
        def coupling_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2890.CouplingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2890,
            )

            return self._parent._cast(_2890.CouplingCompoundSystemDeflection)

        @property
        def coupling_half_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2892.CouplingHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2892,
            )

            return self._parent._cast(_2892.CouplingHalfCompoundSystemDeflection)

        @property
        def cvt_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2894.CVTCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2894,
            )

            return self._parent._cast(_2894.CVTCompoundSystemDeflection)

        @property
        def cvt_pulley_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2895.CVTPulleyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2895,
            )

            return self._parent._cast(_2895.CVTPulleyCompoundSystemDeflection)

        @property
        def cycloidal_assembly_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2896.CycloidalAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2896,
            )

            return self._parent._cast(_2896.CycloidalAssemblyCompoundSystemDeflection)

        @property
        def cycloidal_disc_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2898.CycloidalDiscCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2898,
            )

            return self._parent._cast(_2898.CycloidalDiscCompoundSystemDeflection)

        @property
        def cylindrical_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2900.CylindricalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2900,
            )

            return self._parent._cast(_2900.CylindricalGearCompoundSystemDeflection)

        @property
        def cylindrical_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2902.CylindricalGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2902,
            )

            return self._parent._cast(_2902.CylindricalGearSetCompoundSystemDeflection)

        @property
        def cylindrical_planet_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2903.CylindricalPlanetGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2903,
            )

            return self._parent._cast(
                _2903.CylindricalPlanetGearCompoundSystemDeflection
            )

        @property
        def datum_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2904.DatumCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2904,
            )

            return self._parent._cast(_2904.DatumCompoundSystemDeflection)

        @property
        def external_cad_model_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2906.ExternalCADModelCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2906,
            )

            return self._parent._cast(_2906.ExternalCADModelCompoundSystemDeflection)

        @property
        def face_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2907.FaceGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2907,
            )

            return self._parent._cast(_2907.FaceGearCompoundSystemDeflection)

        @property
        def face_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2909.FaceGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2909,
            )

            return self._parent._cast(_2909.FaceGearSetCompoundSystemDeflection)

        @property
        def fe_part_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2910.FEPartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2910,
            )

            return self._parent._cast(_2910.FEPartCompoundSystemDeflection)

        @property
        def flexible_pin_assembly_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2911.FlexiblePinAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2911,
            )

            return self._parent._cast(_2911.FlexiblePinAssemblyCompoundSystemDeflection)

        @property
        def gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2912.GearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2912,
            )

            return self._parent._cast(_2912.GearCompoundSystemDeflection)

        @property
        def gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2914.GearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2914,
            )

            return self._parent._cast(_2914.GearSetCompoundSystemDeflection)

        @property
        def guide_dxf_model_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2915.GuideDxfModelCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2915,
            )

            return self._parent._cast(_2915.GuideDxfModelCompoundSystemDeflection)

        @property
        def hypoid_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2916.HypoidGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2916,
            )

            return self._parent._cast(_2916.HypoidGearCompoundSystemDeflection)

        @property
        def hypoid_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2918.HypoidGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2918,
            )

            return self._parent._cast(_2918.HypoidGearSetCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2920.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2920,
            )

            return self._parent._cast(
                _2920.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2922.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2922,
            )

            return self._parent._cast(
                _2922.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2923.KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2923,
            )

            return self._parent._cast(
                _2923.KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2925.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2925,
            )

            return self._parent._cast(
                _2925.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2926.KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2926,
            )

            return self._parent._cast(
                _2926.KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2928.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2928,
            )

            return self._parent._cast(
                _2928.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection
            )

        @property
        def mass_disc_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2929.MassDiscCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2929,
            )

            return self._parent._cast(_2929.MassDiscCompoundSystemDeflection)

        @property
        def measurement_component_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2930.MeasurementComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2930,
            )

            return self._parent._cast(
                _2930.MeasurementComponentCompoundSystemDeflection
            )

        @property
        def mountable_component_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2931.MountableComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2931,
            )

            return self._parent._cast(_2931.MountableComponentCompoundSystemDeflection)

        @property
        def oil_seal_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2932.OilSealCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2932,
            )

            return self._parent._cast(_2932.OilSealCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2933.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2933,
            )

            return self._parent._cast(_2933.PartCompoundSystemDeflection)

        @property
        def part_to_part_shear_coupling_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2934.PartToPartShearCouplingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2934,
            )

            return self._parent._cast(
                _2934.PartToPartShearCouplingCompoundSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_half_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2936.PartToPartShearCouplingHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2936,
            )

            return self._parent._cast(
                _2936.PartToPartShearCouplingHalfCompoundSystemDeflection
            )

        @property
        def planetary_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2938.PlanetaryGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2938,
            )

            return self._parent._cast(_2938.PlanetaryGearSetCompoundSystemDeflection)

        @property
        def planet_carrier_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2939.PlanetCarrierCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2939,
            )

            return self._parent._cast(_2939.PlanetCarrierCompoundSystemDeflection)

        @property
        def point_load_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2940.PointLoadCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2940,
            )

            return self._parent._cast(_2940.PointLoadCompoundSystemDeflection)

        @property
        def power_load_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2941.PowerLoadCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2941,
            )

            return self._parent._cast(_2941.PowerLoadCompoundSystemDeflection)

        @property
        def pulley_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2942.PulleyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2942,
            )

            return self._parent._cast(_2942.PulleyCompoundSystemDeflection)

        @property
        def ring_pins_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2943.RingPinsCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2943,
            )

            return self._parent._cast(_2943.RingPinsCompoundSystemDeflection)

        @property
        def rolling_ring_assembly_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2945.RollingRingAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2945,
            )

            return self._parent._cast(_2945.RollingRingAssemblyCompoundSystemDeflection)

        @property
        def rolling_ring_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2946.RollingRingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2946,
            )

            return self._parent._cast(_2946.RollingRingCompoundSystemDeflection)

        @property
        def root_assembly_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2948.RootAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2948,
            )

            return self._parent._cast(_2948.RootAssemblyCompoundSystemDeflection)

        @property
        def shaft_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2949.ShaftCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2949,
            )

            return self._parent._cast(_2949.ShaftCompoundSystemDeflection)

        @property
        def shaft_hub_connection_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2951.ShaftHubConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2951,
            )

            return self._parent._cast(_2951.ShaftHubConnectionCompoundSystemDeflection)

        @property
        def specialised_assembly_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2953.SpecialisedAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2953,
            )

            return self._parent._cast(_2953.SpecialisedAssemblyCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2954.SpiralBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2954,
            )

            return self._parent._cast(_2954.SpiralBevelGearCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2956.SpiralBevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2956,
            )

            return self._parent._cast(_2956.SpiralBevelGearSetCompoundSystemDeflection)

        @property
        def spring_damper_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2957.SpringDamperCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2957,
            )

            return self._parent._cast(_2957.SpringDamperCompoundSystemDeflection)

        @property
        def spring_damper_half_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2959.SpringDamperHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2959,
            )

            return self._parent._cast(_2959.SpringDamperHalfCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2960.StraightBevelDiffGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2960,
            )

            return self._parent._cast(
                _2960.StraightBevelDiffGearCompoundSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2962.StraightBevelDiffGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2962,
            )

            return self._parent._cast(
                _2962.StraightBevelDiffGearSetCompoundSystemDeflection
            )

        @property
        def straight_bevel_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2963.StraightBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2963,
            )

            return self._parent._cast(_2963.StraightBevelGearCompoundSystemDeflection)

        @property
        def straight_bevel_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2965.StraightBevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2965,
            )

            return self._parent._cast(
                _2965.StraightBevelGearSetCompoundSystemDeflection
            )

        @property
        def straight_bevel_planet_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2966.StraightBevelPlanetGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2966,
            )

            return self._parent._cast(
                _2966.StraightBevelPlanetGearCompoundSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2967.StraightBevelSunGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2967,
            )

            return self._parent._cast(
                _2967.StraightBevelSunGearCompoundSystemDeflection
            )

        @property
        def synchroniser_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2968.SynchroniserCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2968,
            )

            return self._parent._cast(_2968.SynchroniserCompoundSystemDeflection)

        @property
        def synchroniser_half_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2969.SynchroniserHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2969,
            )

            return self._parent._cast(_2969.SynchroniserHalfCompoundSystemDeflection)

        @property
        def synchroniser_part_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2970.SynchroniserPartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2970,
            )

            return self._parent._cast(_2970.SynchroniserPartCompoundSystemDeflection)

        @property
        def synchroniser_sleeve_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2971.SynchroniserSleeveCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2971,
            )

            return self._parent._cast(_2971.SynchroniserSleeveCompoundSystemDeflection)

        @property
        def torque_converter_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2972.TorqueConverterCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2972,
            )

            return self._parent._cast(_2972.TorqueConverterCompoundSystemDeflection)

        @property
        def torque_converter_pump_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2974.TorqueConverterPumpCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2974,
            )

            return self._parent._cast(_2974.TorqueConverterPumpCompoundSystemDeflection)

        @property
        def torque_converter_turbine_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2975.TorqueConverterTurbineCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2975,
            )

            return self._parent._cast(
                _2975.TorqueConverterTurbineCompoundSystemDeflection
            )

        @property
        def unbalanced_mass_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2976.UnbalancedMassCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2976,
            )

            return self._parent._cast(_2976.UnbalancedMassCompoundSystemDeflection)

        @property
        def virtual_component_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2977.VirtualComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2977,
            )

            return self._parent._cast(_2977.VirtualComponentCompoundSystemDeflection)

        @property
        def worm_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2978.WormGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2978,
            )

            return self._parent._cast(_2978.WormGearCompoundSystemDeflection)

        @property
        def worm_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2980.WormGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2980,
            )

            return self._parent._cast(_2980.WormGearSetCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2981.ZerolBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2981,
            )

            return self._parent._cast(_2981.ZerolBevelGearCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_2983.ZerolBevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2983,
            )

            return self._parent._cast(_2983.ZerolBevelGearSetCompoundSystemDeflection)

        @property
        def abstract_assembly_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3118.AbstractAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3118,
            )

            return self._parent._cast(
                _3118.AbstractAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_shaft_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3119.AbstractShaftCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3119,
            )

            return self._parent._cast(
                _3119.AbstractShaftCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_shaft_or_housing_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3120.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3120,
            )

            return self._parent._cast(
                _3120.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3122.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3122,
            )

            return self._parent._cast(
                _3122.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3124.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3124,
            )

            return self._parent._cast(
                _3124.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def assembly_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3125.AssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3125,
            )

            return self._parent._cast(
                _3125.AssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def bearing_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3126.BearingCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3126,
            )

            return self._parent._cast(
                _3126.BearingCompoundSteadyStateSynchronousResponse
            )

        @property
        def belt_drive_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3128.BeltDriveCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3128,
            )

            return self._parent._cast(
                _3128.BeltDriveCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3129.BevelDifferentialGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3129,
            )

            return self._parent._cast(
                _3129.BevelDifferentialGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3131.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3131,
            )

            return self._parent._cast(
                _3131.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3132.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3132,
            )

            return self._parent._cast(
                _3132.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_sun_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3133.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3133,
            )

            return self._parent._cast(
                _3133.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3134.BevelGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3134,
            )

            return self._parent._cast(
                _3134.BevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3136.BevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3136,
            )

            return self._parent._cast(
                _3136.BevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def bolt_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3137.BoltCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3137,
            )

            return self._parent._cast(_3137.BoltCompoundSteadyStateSynchronousResponse)

        @property
        def bolted_joint_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3138.BoltedJointCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3138,
            )

            return self._parent._cast(
                _3138.BoltedJointCompoundSteadyStateSynchronousResponse
            )

        @property
        def clutch_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3139.ClutchCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3139,
            )

            return self._parent._cast(
                _3139.ClutchCompoundSteadyStateSynchronousResponse
            )

        @property
        def clutch_half_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3141.ClutchHalfCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3141,
            )

            return self._parent._cast(
                _3141.ClutchHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3143.ComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3143,
            )

            return self._parent._cast(
                _3143.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_coupling_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3144.ConceptCouplingCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3144,
            )

            return self._parent._cast(
                _3144.ConceptCouplingCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_coupling_half_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3146.ConceptCouplingHalfCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3146,
            )

            return self._parent._cast(
                _3146.ConceptCouplingHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3147.ConceptGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3147,
            )

            return self._parent._cast(
                _3147.ConceptGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3149.ConceptGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3149,
            )

            return self._parent._cast(
                _3149.ConceptGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3150.ConicalGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3150,
            )

            return self._parent._cast(
                _3150.ConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3152.ConicalGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3152,
            )

            return self._parent._cast(
                _3152.ConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def connector_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3154.ConnectorCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3154,
            )

            return self._parent._cast(
                _3154.ConnectorCompoundSteadyStateSynchronousResponse
            )

        @property
        def coupling_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3155.CouplingCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3155,
            )

            return self._parent._cast(
                _3155.CouplingCompoundSteadyStateSynchronousResponse
            )

        @property
        def coupling_half_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3157.CouplingHalfCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3157,
            )

            return self._parent._cast(
                _3157.CouplingHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def cvt_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3159.CVTCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3159,
            )

            return self._parent._cast(_3159.CVTCompoundSteadyStateSynchronousResponse)

        @property
        def cvt_pulley_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3160.CVTPulleyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3160,
            )

            return self._parent._cast(
                _3160.CVTPulleyCompoundSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_assembly_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3161.CycloidalAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3161,
            )

            return self._parent._cast(
                _3161.CycloidalAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3163.CycloidalDiscCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3163,
            )

            return self._parent._cast(
                _3163.CycloidalDiscCompoundSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3165.CylindricalGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3165,
            )

            return self._parent._cast(
                _3165.CylindricalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3167.CylindricalGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3167,
            )

            return self._parent._cast(
                _3167.CylindricalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_planet_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3168.CylindricalPlanetGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3168,
            )

            return self._parent._cast(
                _3168.CylindricalPlanetGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def datum_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3169.DatumCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3169,
            )

            return self._parent._cast(_3169.DatumCompoundSteadyStateSynchronousResponse)

        @property
        def external_cad_model_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3170.ExternalCADModelCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3170,
            )

            return self._parent._cast(
                _3170.ExternalCADModelCompoundSteadyStateSynchronousResponse
            )

        @property
        def face_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3171.FaceGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3171,
            )

            return self._parent._cast(
                _3171.FaceGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def face_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3173.FaceGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3173,
            )

            return self._parent._cast(
                _3173.FaceGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def fe_part_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3174.FEPartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3174,
            )

            return self._parent._cast(
                _3174.FEPartCompoundSteadyStateSynchronousResponse
            )

        @property
        def flexible_pin_assembly_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3175.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3175,
            )

            return self._parent._cast(
                _3175.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3176.GearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3176,
            )

            return self._parent._cast(_3176.GearCompoundSteadyStateSynchronousResponse)

        @property
        def gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3178.GearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3178,
            )

            return self._parent._cast(
                _3178.GearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def guide_dxf_model_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3179.GuideDxfModelCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3179,
            )

            return self._parent._cast(
                _3179.GuideDxfModelCompoundSteadyStateSynchronousResponse
            )

        @property
        def hypoid_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3180.HypoidGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3180,
            )

            return self._parent._cast(
                _3180.HypoidGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def hypoid_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3182.HypoidGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3182,
            )

            return self._parent._cast(
                _3182.HypoidGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3184.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3184,
            )

            return self._parent._cast(
                _3184.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3186.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3186,
            )

            return self._parent._cast(
                _3186.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3187.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3187,
            )

            return self._parent._cast(
                _3187.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3189.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3189,
            )

            return self._parent._cast(
                _3189.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3190.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3190,
            )

            return self._parent._cast(
                _3190.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3192.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3192,
            )

            return self._parent._cast(
                _3192.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def mass_disc_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3193.MassDiscCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3193,
            )

            return self._parent._cast(
                _3193.MassDiscCompoundSteadyStateSynchronousResponse
            )

        @property
        def measurement_component_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3194.MeasurementComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3194,
            )

            return self._parent._cast(
                _3194.MeasurementComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3195.MountableComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3195,
            )

            return self._parent._cast(
                _3195.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def oil_seal_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3196.OilSealCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3196,
            )

            return self._parent._cast(
                _3196.OilSealCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3197.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3197,
            )

            return self._parent._cast(_3197.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_to_part_shear_coupling_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3198.PartToPartShearCouplingCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3198,
            )

            return self._parent._cast(
                _3198.PartToPartShearCouplingCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3200.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3200,
            )

            return self._parent._cast(
                _3200.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def planetary_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3202.PlanetaryGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3202,
            )

            return self._parent._cast(
                _3202.PlanetaryGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def planet_carrier_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3203.PlanetCarrierCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3203,
            )

            return self._parent._cast(
                _3203.PlanetCarrierCompoundSteadyStateSynchronousResponse
            )

        @property
        def point_load_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3204.PointLoadCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3204,
            )

            return self._parent._cast(
                _3204.PointLoadCompoundSteadyStateSynchronousResponse
            )

        @property
        def power_load_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3205.PowerLoadCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3205,
            )

            return self._parent._cast(
                _3205.PowerLoadCompoundSteadyStateSynchronousResponse
            )

        @property
        def pulley_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3206.PulleyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3206,
            )

            return self._parent._cast(
                _3206.PulleyCompoundSteadyStateSynchronousResponse
            )

        @property
        def ring_pins_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3207.RingPinsCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3207,
            )

            return self._parent._cast(
                _3207.RingPinsCompoundSteadyStateSynchronousResponse
            )

        @property
        def rolling_ring_assembly_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3209.RollingRingAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3209,
            )

            return self._parent._cast(
                _3209.RollingRingAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def rolling_ring_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3210.RollingRingCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3210,
            )

            return self._parent._cast(
                _3210.RollingRingCompoundSteadyStateSynchronousResponse
            )

        @property
        def root_assembly_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3212.RootAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3212,
            )

            return self._parent._cast(
                _3212.RootAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def shaft_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3213.ShaftCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3213,
            )

            return self._parent._cast(_3213.ShaftCompoundSteadyStateSynchronousResponse)

        @property
        def shaft_hub_connection_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3214.ShaftHubConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3214,
            )

            return self._parent._cast(
                _3214.ShaftHubConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3216.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3216,
            )

            return self._parent._cast(
                _3216.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3217.SpiralBevelGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3217,
            )

            return self._parent._cast(
                _3217.SpiralBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3219.SpiralBevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3219,
            )

            return self._parent._cast(
                _3219.SpiralBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3220.SpringDamperCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3220,
            )

            return self._parent._cast(
                _3220.SpringDamperCompoundSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_half_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3222.SpringDamperHalfCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3222,
            )

            return self._parent._cast(
                _3222.SpringDamperHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3223.StraightBevelDiffGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3223,
            )

            return self._parent._cast(
                _3223.StraightBevelDiffGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3225.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3225,
            )

            return self._parent._cast(
                _3225.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3226.StraightBevelGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3226,
            )

            return self._parent._cast(
                _3226.StraightBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3228.StraightBevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3228,
            )

            return self._parent._cast(
                _3228.StraightBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3229.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3229,
            )

            return self._parent._cast(
                _3229.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3230.StraightBevelSunGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3230,
            )

            return self._parent._cast(
                _3230.StraightBevelSunGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3231.SynchroniserCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3231,
            )

            return self._parent._cast(
                _3231.SynchroniserCompoundSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_half_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3232.SynchroniserHalfCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3232,
            )

            return self._parent._cast(
                _3232.SynchroniserHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_part_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3233.SynchroniserPartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3233,
            )

            return self._parent._cast(
                _3233.SynchroniserPartCompoundSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_sleeve_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3234.SynchroniserSleeveCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3234,
            )

            return self._parent._cast(
                _3234.SynchroniserSleeveCompoundSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3235.TorqueConverterCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3235,
            )

            return self._parent._cast(
                _3235.TorqueConverterCompoundSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_pump_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3237.TorqueConverterPumpCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3237,
            )

            return self._parent._cast(
                _3237.TorqueConverterPumpCompoundSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_turbine_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3238.TorqueConverterTurbineCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3238,
            )

            return self._parent._cast(
                _3238.TorqueConverterTurbineCompoundSteadyStateSynchronousResponse
            )

        @property
        def unbalanced_mass_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3239.UnbalancedMassCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3239,
            )

            return self._parent._cast(
                _3239.UnbalancedMassCompoundSteadyStateSynchronousResponse
            )

        @property
        def virtual_component_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3240.VirtualComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3240,
            )

            return self._parent._cast(
                _3240.VirtualComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3241.WormGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3241,
            )

            return self._parent._cast(
                _3241.WormGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3243.WormGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3243,
            )

            return self._parent._cast(
                _3243.WormGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3244.ZerolBevelGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3244,
            )

            return self._parent._cast(
                _3244.ZerolBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3246.ZerolBevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3246,
            )

            return self._parent._cast(
                _3246.ZerolBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3377.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3377,
            )

            return self._parent._cast(
                _3377.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3378.AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3378,
            )

            return self._parent._cast(
                _3378.AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_or_housing_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_3379.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3379,
            )

            return self._parent._cast(
                _3379.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_3381.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3381,
            )

            return self._parent._cast(
                _3381.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3383.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3383,
            )

            return self._parent._cast(
                _3383.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3384.AssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3384,
            )

            return self._parent._cast(
                _3384.AssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bearing_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3385.BearingCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3385,
            )

            return self._parent._cast(
                _3385.BearingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def belt_drive_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3387.BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3387,
            )

            return self._parent._cast(
                _3387.BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_3388.BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3388,
            )

            return self._parent._cast(
                _3388.BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3390.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3390,
            )

            return self._parent._cast(
                _3390.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3391.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3391,
            )

            return self._parent._cast(
                _3391.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_sun_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3392.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3392,
            )

            return self._parent._cast(
                _3392.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3393.BevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3393,
            )

            return self._parent._cast(
                _3393.BevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3395.BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3395,
            )

            return self._parent._cast(
                _3395.BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bolt_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3396.BoltCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3396,
            )

            return self._parent._cast(
                _3396.BoltCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bolted_joint_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3397.BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3397,
            )

            return self._parent._cast(
                _3397.BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def clutch_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3398.ClutchCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3398,
            )

            return self._parent._cast(
                _3398.ClutchCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def clutch_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3400.ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3400,
            )

            return self._parent._cast(
                _3400.ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3402.ComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3402,
            )

            return self._parent._cast(
                _3402.ComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3403.ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3403,
            )

            return self._parent._cast(
                _3403.ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3405.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3405,
            )

            return self._parent._cast(
                _3405.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3406.ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3406,
            )

            return self._parent._cast(
                _3406.ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3408.ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3408,
            )

            return self._parent._cast(
                _3408.ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3409.ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3409,
            )

            return self._parent._cast(
                _3409.ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3411.ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3411,
            )

            return self._parent._cast(
                _3411.ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connector_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3413.ConnectorCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3413,
            )

            return self._parent._cast(
                _3413.ConnectorCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3414.CouplingCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3414,
            )

            return self._parent._cast(
                _3414.CouplingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3416.CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3416,
            )

            return self._parent._cast(
                _3416.CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3418.CVTCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3418,
            )

            return self._parent._cast(
                _3418.CVTCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_pulley_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3419.CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3419,
            )

            return self._parent._cast(
                _3419.CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3420.CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3420,
            )

            return self._parent._cast(
                _3420.CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_disc_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3422.CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3422,
            )

            return self._parent._cast(
                _3422.CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3424.CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3424,
            )

            return self._parent._cast(
                _3424.CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3426.CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3426,
            )

            return self._parent._cast(
                _3426.CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_3427.CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3427,
            )

            return self._parent._cast(
                _3427.CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def datum_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3428.DatumCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3428,
            )

            return self._parent._cast(
                _3428.DatumCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def external_cad_model_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3429.ExternalCADModelCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3429,
            )

            return self._parent._cast(
                _3429.ExternalCADModelCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3430.FaceGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3430,
            )

            return self._parent._cast(
                _3430.FaceGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3432.FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3432,
            )

            return self._parent._cast(
                _3432.FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def fe_part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3433.FEPartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3433,
            )

            return self._parent._cast(
                _3433.FEPartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def flexible_pin_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3434.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3434,
            )

            return self._parent._cast(
                _3434.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3435.GearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3435,
            )

            return self._parent._cast(
                _3435.GearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3437.GearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3437,
            )

            return self._parent._cast(
                _3437.GearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def guide_dxf_model_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3438.GuideDxfModelCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3438,
            )

            return self._parent._cast(
                _3438.GuideDxfModelCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3439.HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3439,
            )

            return self._parent._cast(
                _3439.HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3441.HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3441,
            )

            return self._parent._cast(
                _3441.HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3443.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3443,
            )

            return self._parent._cast(
                _3443.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3445.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3445,
            )

            return self._parent._cast(
                _3445.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3446.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3446,
            )

            return self._parent._cast(
                _3446.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3448.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3448,
            )

            return self._parent._cast(
                _3448.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3449.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3449,
            )

            return self._parent._cast(
                _3449.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3451.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3451,
            )

            return self._parent._cast(
                _3451.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mass_disc_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3452.MassDiscCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3452,
            )

            return self._parent._cast(
                _3452.MassDiscCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def measurement_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3453.MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3453,
            )

            return self._parent._cast(
                _3453.MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3454.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3454,
            )

            return self._parent._cast(
                _3454.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def oil_seal_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3455.OilSealCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3455,
            )

            return self._parent._cast(
                _3455.OilSealCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3456.PartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3456,
            )

            return self._parent._cast(
                _3456.PartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3457.PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3457,
            )

            return self._parent._cast(
                _3457.PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3459.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3459,
            )

            return self._parent._cast(
                _3459.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planetary_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3461.PlanetaryGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3461,
            )

            return self._parent._cast(
                _3461.PlanetaryGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planet_carrier_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3462.PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3462,
            )

            return self._parent._cast(
                _3462.PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def point_load_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3463.PointLoadCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3463,
            )

            return self._parent._cast(
                _3463.PointLoadCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def power_load_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3464.PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3464,
            )

            return self._parent._cast(
                _3464.PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def pulley_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3465.PulleyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3465,
            )

            return self._parent._cast(
                _3465.PulleyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def ring_pins_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3466.RingPinsCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3466,
            )

            return self._parent._cast(
                _3466.RingPinsCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3468.RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3468,
            )

            return self._parent._cast(
                _3468.RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3469.RollingRingCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3469,
            )

            return self._parent._cast(
                _3469.RollingRingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def root_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3471.RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3471,
            )

            return self._parent._cast(
                _3471.RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3472.ShaftCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3472,
            )

            return self._parent._cast(
                _3472.ShaftCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_hub_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3473.ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3473,
            )

            return self._parent._cast(
                _3473.ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3475.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3475,
            )

            return self._parent._cast(
                _3475.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3476.SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3476,
            )

            return self._parent._cast(
                _3476.SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3478.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3478,
            )

            return self._parent._cast(
                _3478.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3479.SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3479,
            )

            return self._parent._cast(
                _3479.SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3481.SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3481,
            )

            return self._parent._cast(
                _3481.SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_3482.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3482,
            )

            return self._parent._cast(
                _3482.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3484.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3484,
            )

            return self._parent._cast(
                _3484.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3485.StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3485,
            )

            return self._parent._cast(
                _3485.StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3487.StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3487,
            )

            return self._parent._cast(
                _3487.StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3488.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3488,
            )

            return self._parent._cast(
                _3488.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3489.StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3489,
            )

            return self._parent._cast(
                _3489.StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3490.SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3490,
            )

            return self._parent._cast(
                _3490.SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3491.SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3491,
            )

            return self._parent._cast(
                _3491.SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3492.SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3492,
            )

            return self._parent._cast(
                _3492.SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_sleeve_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3493.SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3493,
            )

            return self._parent._cast(
                _3493.SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3494.TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3494,
            )

            return self._parent._cast(
                _3494.TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_pump_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3496.TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3496,
            )

            return self._parent._cast(
                _3496.TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_turbine_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_3497.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3497,
            )

            return self._parent._cast(
                _3497.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def unbalanced_mass_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3498.UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3498,
            )

            return self._parent._cast(
                _3498.UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def virtual_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3499.VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3499,
            )

            return self._parent._cast(
                _3499.VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3500.WormGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3500,
            )

            return self._parent._cast(
                _3500.WormGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3502.WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3502,
            )

            return self._parent._cast(
                _3502.WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3503.ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3503,
            )

            return self._parent._cast(
                _3503.ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3505.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3505,
            )

            return self._parent._cast(
                _3505.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3636.AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3636,
            )

            return self._parent._cast(
                _3636.AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3637.AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3637,
            )

            return self._parent._cast(
                _3637.AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_or_housing_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_3638.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3638,
            )

            return self._parent._cast(
                _3638.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_3640.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3640,
            )

            return self._parent._cast(
                _3640.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3642.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3642,
            )

            return self._parent._cast(
                _3642.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3643.AssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3643,
            )

            return self._parent._cast(
                _3643.AssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bearing_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3644.BearingCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3644,
            )

            return self._parent._cast(
                _3644.BearingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def belt_drive_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3646.BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3646,
            )

            return self._parent._cast(
                _3646.BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_3647.BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3647,
            )

            return self._parent._cast(
                _3647.BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3649.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3649,
            )

            return self._parent._cast(
                _3649.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3650.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3650,
            )

            return self._parent._cast(
                _3650.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_sun_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3651.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3651,
            )

            return self._parent._cast(
                _3651.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3652.BevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3652,
            )

            return self._parent._cast(
                _3652.BevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3654.BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3654,
            )

            return self._parent._cast(
                _3654.BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bolt_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3655.BoltCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3655,
            )

            return self._parent._cast(
                _3655.BoltCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bolted_joint_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3656.BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3656,
            )

            return self._parent._cast(
                _3656.BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def clutch_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3657.ClutchCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3657,
            )

            return self._parent._cast(
                _3657.ClutchCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def clutch_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3659.ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3659,
            )

            return self._parent._cast(
                _3659.ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3661.ComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3661,
            )

            return self._parent._cast(
                _3661.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3662.ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3662,
            )

            return self._parent._cast(
                _3662.ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3664.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3664,
            )

            return self._parent._cast(
                _3664.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3665.ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3665,
            )

            return self._parent._cast(
                _3665.ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3667.ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3667,
            )

            return self._parent._cast(
                _3667.ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3668.ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3668,
            )

            return self._parent._cast(
                _3668.ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3670.ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3670,
            )

            return self._parent._cast(
                _3670.ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connector_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3672.ConnectorCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3672,
            )

            return self._parent._cast(
                _3672.ConnectorCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3673.CouplingCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3673,
            )

            return self._parent._cast(
                _3673.CouplingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3675.CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3675,
            )

            return self._parent._cast(
                _3675.CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3677.CVTCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3677,
            )

            return self._parent._cast(
                _3677.CVTCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_pulley_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3678.CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3678,
            )

            return self._parent._cast(
                _3678.CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3679.CycloidalAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3679,
            )

            return self._parent._cast(
                _3679.CycloidalAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_disc_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3681.CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3681,
            )

            return self._parent._cast(
                _3681.CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3683.CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3683,
            )

            return self._parent._cast(
                _3683.CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3685.CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3685,
            )

            return self._parent._cast(
                _3685.CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_planet_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_3686.CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3686,
            )

            return self._parent._cast(
                _3686.CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def datum_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3687.DatumCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3687,
            )

            return self._parent._cast(
                _3687.DatumCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def external_cad_model_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3688.ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3688,
            )

            return self._parent._cast(
                _3688.ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3689.FaceGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3689,
            )

            return self._parent._cast(
                _3689.FaceGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3691.FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3691,
            )

            return self._parent._cast(
                _3691.FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def fe_part_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3692.FEPartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3692,
            )

            return self._parent._cast(
                _3692.FEPartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def flexible_pin_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3693.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3693,
            )

            return self._parent._cast(
                _3693.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3694.GearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3694,
            )

            return self._parent._cast(
                _3694.GearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3696.GearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3696,
            )

            return self._parent._cast(
                _3696.GearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def guide_dxf_model_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3697.GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3697,
            )

            return self._parent._cast(
                _3697.GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3698.HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3698,
            )

            return self._parent._cast(
                _3698.HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3700.HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3700,
            )

            return self._parent._cast(
                _3700.HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3702.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3702,
            )

            return self._parent._cast(
                _3702.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3704.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3704,
            )

            return self._parent._cast(
                _3704.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3705.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3705,
            )

            return self._parent._cast(
                _3705.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3707.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3707,
            )

            return self._parent._cast(
                _3707.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3708.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3708,
            )

            return self._parent._cast(
                _3708.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3710.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3710,
            )

            return self._parent._cast(
                _3710.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mass_disc_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3711.MassDiscCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3711,
            )

            return self._parent._cast(
                _3711.MassDiscCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def measurement_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3712.MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3712,
            )

            return self._parent._cast(
                _3712.MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3713.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3713,
            )

            return self._parent._cast(
                _3713.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def oil_seal_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3714.OilSealCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3714,
            )

            return self._parent._cast(
                _3714.OilSealCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3715.PartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3715,
            )

            return self._parent._cast(
                _3715.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3716.PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3716,
            )

            return self._parent._cast(
                _3716.PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3718.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3718,
            )

            return self._parent._cast(
                _3718.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planetary_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3720.PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3720,
            )

            return self._parent._cast(
                _3720.PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planet_carrier_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3721.PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3721,
            )

            return self._parent._cast(
                _3721.PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def point_load_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3722.PointLoadCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3722,
            )

            return self._parent._cast(
                _3722.PointLoadCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def power_load_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3723.PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3723,
            )

            return self._parent._cast(
                _3723.PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def pulley_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3724.PulleyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3724,
            )

            return self._parent._cast(
                _3724.PulleyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def ring_pins_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3725.RingPinsCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3725,
            )

            return self._parent._cast(
                _3725.RingPinsCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3727.RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3727,
            )

            return self._parent._cast(
                _3727.RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3728.RollingRingCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3728,
            )

            return self._parent._cast(
                _3728.RollingRingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def root_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3730.RootAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3730,
            )

            return self._parent._cast(
                _3730.RootAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3731.ShaftCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3731,
            )

            return self._parent._cast(
                _3731.ShaftCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_hub_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3732.ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3732,
            )

            return self._parent._cast(
                _3732.ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3734.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3734,
            )

            return self._parent._cast(
                _3734.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3735.SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3735,
            )

            return self._parent._cast(
                _3735.SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3737.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3737,
            )

            return self._parent._cast(
                _3737.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3738.SpringDamperCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3738,
            )

            return self._parent._cast(
                _3738.SpringDamperCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3740.SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3740,
            )

            return self._parent._cast(
                _3740.SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_3741.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3741,
            )

            return self._parent._cast(
                _3741.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3743.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3743,
            )

            return self._parent._cast(
                _3743.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3744.StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3744,
            )

            return self._parent._cast(
                _3744.StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3746.StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3746,
            )

            return self._parent._cast(
                _3746.StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3747.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3747,
            )

            return self._parent._cast(
                _3747.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3748.StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3748,
            )

            return self._parent._cast(
                _3748.StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3749.SynchroniserCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3749,
            )

            return self._parent._cast(
                _3749.SynchroniserCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3750.SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3750,
            )

            return self._parent._cast(
                _3750.SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_part_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3751.SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3751,
            )

            return self._parent._cast(
                _3751.SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_sleeve_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3752.SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3752,
            )

            return self._parent._cast(
                _3752.SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3753.TorqueConverterCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3753,
            )

            return self._parent._cast(
                _3753.TorqueConverterCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_pump_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3755.TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3755,
            )

            return self._parent._cast(
                _3755.TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_turbine_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_3756.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3756,
            )

            return self._parent._cast(
                _3756.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def unbalanced_mass_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3757.UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3757,
            )

            return self._parent._cast(
                _3757.UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def virtual_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3758.VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3758,
            )

            return self._parent._cast(
                _3758.VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3759.WormGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3759,
            )

            return self._parent._cast(
                _3759.WormGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3761.WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3761,
            )

            return self._parent._cast(
                _3761.WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3762.ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3762,
            )

            return self._parent._cast(
                _3762.ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3764.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3764,
            )

            return self._parent._cast(
                _3764.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3899.AbstractAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3899,
            )

            return self._parent._cast(_3899.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def abstract_shaft_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3900.AbstractShaftCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3900,
            )

            return self._parent._cast(_3900.AbstractShaftCompoundStabilityAnalysis)

        @property
        def abstract_shaft_or_housing_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3901.AbstractShaftOrHousingCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3901,
            )

            return self._parent._cast(
                _3901.AbstractShaftOrHousingCompoundStabilityAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3903.AGMAGleasonConicalGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3903,
            )

            return self._parent._cast(
                _3903.AGMAGleasonConicalGearCompoundStabilityAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3905.AGMAGleasonConicalGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3905,
            )

            return self._parent._cast(
                _3905.AGMAGleasonConicalGearSetCompoundStabilityAnalysis
            )

        @property
        def assembly_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3906.AssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3906,
            )

            return self._parent._cast(_3906.AssemblyCompoundStabilityAnalysis)

        @property
        def bearing_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3907.BearingCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3907,
            )

            return self._parent._cast(_3907.BearingCompoundStabilityAnalysis)

        @property
        def belt_drive_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3909.BeltDriveCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3909,
            )

            return self._parent._cast(_3909.BeltDriveCompoundStabilityAnalysis)

        @property
        def bevel_differential_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3910.BevelDifferentialGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3910,
            )

            return self._parent._cast(
                _3910.BevelDifferentialGearCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3912.BevelDifferentialGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3912,
            )

            return self._parent._cast(
                _3912.BevelDifferentialGearSetCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3913.BevelDifferentialPlanetGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3913,
            )

            return self._parent._cast(
                _3913.BevelDifferentialPlanetGearCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3914.BevelDifferentialSunGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3914,
            )

            return self._parent._cast(
                _3914.BevelDifferentialSunGearCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3915.BevelGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3915,
            )

            return self._parent._cast(_3915.BevelGearCompoundStabilityAnalysis)

        @property
        def bevel_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3917.BevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3917,
            )

            return self._parent._cast(_3917.BevelGearSetCompoundStabilityAnalysis)

        @property
        def bolt_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3918.BoltCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3918,
            )

            return self._parent._cast(_3918.BoltCompoundStabilityAnalysis)

        @property
        def bolted_joint_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3919.BoltedJointCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3919,
            )

            return self._parent._cast(_3919.BoltedJointCompoundStabilityAnalysis)

        @property
        def clutch_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3920.ClutchCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3920,
            )

            return self._parent._cast(_3920.ClutchCompoundStabilityAnalysis)

        @property
        def clutch_half_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3922.ClutchHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3922,
            )

            return self._parent._cast(_3922.ClutchHalfCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3924.ComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3924,
            )

            return self._parent._cast(_3924.ComponentCompoundStabilityAnalysis)

        @property
        def concept_coupling_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3925.ConceptCouplingCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3925,
            )

            return self._parent._cast(_3925.ConceptCouplingCompoundStabilityAnalysis)

        @property
        def concept_coupling_half_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3927.ConceptCouplingHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3927,
            )

            return self._parent._cast(
                _3927.ConceptCouplingHalfCompoundStabilityAnalysis
            )

        @property
        def concept_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3928.ConceptGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3928,
            )

            return self._parent._cast(_3928.ConceptGearCompoundStabilityAnalysis)

        @property
        def concept_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3930.ConceptGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3930,
            )

            return self._parent._cast(_3930.ConceptGearSetCompoundStabilityAnalysis)

        @property
        def conical_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3931.ConicalGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3931,
            )

            return self._parent._cast(_3931.ConicalGearCompoundStabilityAnalysis)

        @property
        def conical_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3933.ConicalGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3933,
            )

            return self._parent._cast(_3933.ConicalGearSetCompoundStabilityAnalysis)

        @property
        def connector_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3935.ConnectorCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3935,
            )

            return self._parent._cast(_3935.ConnectorCompoundStabilityAnalysis)

        @property
        def coupling_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3936.CouplingCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3936,
            )

            return self._parent._cast(_3936.CouplingCompoundStabilityAnalysis)

        @property
        def coupling_half_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3938.CouplingHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3938,
            )

            return self._parent._cast(_3938.CouplingHalfCompoundStabilityAnalysis)

        @property
        def cvt_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3940.CVTCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3940,
            )

            return self._parent._cast(_3940.CVTCompoundStabilityAnalysis)

        @property
        def cvt_pulley_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3941.CVTPulleyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3941,
            )

            return self._parent._cast(_3941.CVTPulleyCompoundStabilityAnalysis)

        @property
        def cycloidal_assembly_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3942.CycloidalAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3942,
            )

            return self._parent._cast(_3942.CycloidalAssemblyCompoundStabilityAnalysis)

        @property
        def cycloidal_disc_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3944.CycloidalDiscCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3944,
            )

            return self._parent._cast(_3944.CycloidalDiscCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3946.CylindricalGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3946,
            )

            return self._parent._cast(_3946.CylindricalGearCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3948.CylindricalGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3948,
            )

            return self._parent._cast(_3948.CylindricalGearSetCompoundStabilityAnalysis)

        @property
        def cylindrical_planet_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3949.CylindricalPlanetGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3949,
            )

            return self._parent._cast(
                _3949.CylindricalPlanetGearCompoundStabilityAnalysis
            )

        @property
        def datum_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3950.DatumCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3950,
            )

            return self._parent._cast(_3950.DatumCompoundStabilityAnalysis)

        @property
        def external_cad_model_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3951.ExternalCADModelCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3951,
            )

            return self._parent._cast(_3951.ExternalCADModelCompoundStabilityAnalysis)

        @property
        def face_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3952.FaceGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3952,
            )

            return self._parent._cast(_3952.FaceGearCompoundStabilityAnalysis)

        @property
        def face_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3954.FaceGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3954,
            )

            return self._parent._cast(_3954.FaceGearSetCompoundStabilityAnalysis)

        @property
        def fe_part_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3955.FEPartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3955,
            )

            return self._parent._cast(_3955.FEPartCompoundStabilityAnalysis)

        @property
        def flexible_pin_assembly_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3956.FlexiblePinAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3956,
            )

            return self._parent._cast(
                _3956.FlexiblePinAssemblyCompoundStabilityAnalysis
            )

        @property
        def gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3957.GearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3957,
            )

            return self._parent._cast(_3957.GearCompoundStabilityAnalysis)

        @property
        def gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3959.GearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3959,
            )

            return self._parent._cast(_3959.GearSetCompoundStabilityAnalysis)

        @property
        def guide_dxf_model_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3960.GuideDxfModelCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3960,
            )

            return self._parent._cast(_3960.GuideDxfModelCompoundStabilityAnalysis)

        @property
        def hypoid_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3961.HypoidGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3961,
            )

            return self._parent._cast(_3961.HypoidGearCompoundStabilityAnalysis)

        @property
        def hypoid_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3963.HypoidGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3963,
            )

            return self._parent._cast(_3963.HypoidGearSetCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3965.KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3965,
            )

            return self._parent._cast(
                _3965.KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3967.KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3967,
            )

            return self._parent._cast(
                _3967.KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3968.KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3968,
            )

            return self._parent._cast(
                _3968.KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3970.KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3970,
            )

            return self._parent._cast(
                _3970.KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3971.KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3971,
            )

            return self._parent._cast(
                _3971.KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_3973.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3973,
            )

            return self._parent._cast(
                _3973.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis
            )

        @property
        def mass_disc_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3974.MassDiscCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3974,
            )

            return self._parent._cast(_3974.MassDiscCompoundStabilityAnalysis)

        @property
        def measurement_component_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3975.MeasurementComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3975,
            )

            return self._parent._cast(
                _3975.MeasurementComponentCompoundStabilityAnalysis
            )

        @property
        def mountable_component_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3976.MountableComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3976,
            )

            return self._parent._cast(_3976.MountableComponentCompoundStabilityAnalysis)

        @property
        def oil_seal_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3977.OilSealCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3977,
            )

            return self._parent._cast(_3977.OilSealCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3978.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3978,
            )

            return self._parent._cast(_3978.PartCompoundStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3979.PartToPartShearCouplingCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3979,
            )

            return self._parent._cast(
                _3979.PartToPartShearCouplingCompoundStabilityAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3981.PartToPartShearCouplingHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3981,
            )

            return self._parent._cast(
                _3981.PartToPartShearCouplingHalfCompoundStabilityAnalysis
            )

        @property
        def planetary_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3983.PlanetaryGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3983,
            )

            return self._parent._cast(_3983.PlanetaryGearSetCompoundStabilityAnalysis)

        @property
        def planet_carrier_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3984.PlanetCarrierCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3984,
            )

            return self._parent._cast(_3984.PlanetCarrierCompoundStabilityAnalysis)

        @property
        def point_load_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3985.PointLoadCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3985,
            )

            return self._parent._cast(_3985.PointLoadCompoundStabilityAnalysis)

        @property
        def power_load_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3986.PowerLoadCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3986,
            )

            return self._parent._cast(_3986.PowerLoadCompoundStabilityAnalysis)

        @property
        def pulley_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3987.PulleyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3987,
            )

            return self._parent._cast(_3987.PulleyCompoundStabilityAnalysis)

        @property
        def ring_pins_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3988.RingPinsCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3988,
            )

            return self._parent._cast(_3988.RingPinsCompoundStabilityAnalysis)

        @property
        def rolling_ring_assembly_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3990.RollingRingAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3990,
            )

            return self._parent._cast(
                _3990.RollingRingAssemblyCompoundStabilityAnalysis
            )

        @property
        def rolling_ring_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3991.RollingRingCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3991,
            )

            return self._parent._cast(_3991.RollingRingCompoundStabilityAnalysis)

        @property
        def root_assembly_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3993.RootAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3993,
            )

            return self._parent._cast(_3993.RootAssemblyCompoundStabilityAnalysis)

        @property
        def shaft_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3994.ShaftCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3994,
            )

            return self._parent._cast(_3994.ShaftCompoundStabilityAnalysis)

        @property
        def shaft_hub_connection_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3995.ShaftHubConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3995,
            )

            return self._parent._cast(_3995.ShaftHubConnectionCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3997.SpecialisedAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3997,
            )

            return self._parent._cast(
                _3997.SpecialisedAssemblyCompoundStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_3998.SpiralBevelGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3998,
            )

            return self._parent._cast(_3998.SpiralBevelGearCompoundStabilityAnalysis)

        @property
        def spiral_bevel_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4000.SpiralBevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4000,
            )

            return self._parent._cast(_4000.SpiralBevelGearSetCompoundStabilityAnalysis)

        @property
        def spring_damper_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4001.SpringDamperCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4001,
            )

            return self._parent._cast(_4001.SpringDamperCompoundStabilityAnalysis)

        @property
        def spring_damper_half_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4003.SpringDamperHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4003,
            )

            return self._parent._cast(_4003.SpringDamperHalfCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4004.StraightBevelDiffGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4004,
            )

            return self._parent._cast(
                _4004.StraightBevelDiffGearCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4006.StraightBevelDiffGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4006,
            )

            return self._parent._cast(
                _4006.StraightBevelDiffGearSetCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4007.StraightBevelGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4007,
            )

            return self._parent._cast(_4007.StraightBevelGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4009.StraightBevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4009,
            )

            return self._parent._cast(
                _4009.StraightBevelGearSetCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4010.StraightBevelPlanetGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4010,
            )

            return self._parent._cast(
                _4010.StraightBevelPlanetGearCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4011.StraightBevelSunGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4011,
            )

            return self._parent._cast(
                _4011.StraightBevelSunGearCompoundStabilityAnalysis
            )

        @property
        def synchroniser_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4012.SynchroniserCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4012,
            )

            return self._parent._cast(_4012.SynchroniserCompoundStabilityAnalysis)

        @property
        def synchroniser_half_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4013.SynchroniserHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4013,
            )

            return self._parent._cast(_4013.SynchroniserHalfCompoundStabilityAnalysis)

        @property
        def synchroniser_part_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4014.SynchroniserPartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4014,
            )

            return self._parent._cast(_4014.SynchroniserPartCompoundStabilityAnalysis)

        @property
        def synchroniser_sleeve_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4015.SynchroniserSleeveCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4015,
            )

            return self._parent._cast(_4015.SynchroniserSleeveCompoundStabilityAnalysis)

        @property
        def torque_converter_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4016.TorqueConverterCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4016,
            )

            return self._parent._cast(_4016.TorqueConverterCompoundStabilityAnalysis)

        @property
        def torque_converter_pump_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4018.TorqueConverterPumpCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4018,
            )

            return self._parent._cast(
                _4018.TorqueConverterPumpCompoundStabilityAnalysis
            )

        @property
        def torque_converter_turbine_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4019.TorqueConverterTurbineCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4019,
            )

            return self._parent._cast(
                _4019.TorqueConverterTurbineCompoundStabilityAnalysis
            )

        @property
        def unbalanced_mass_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4020.UnbalancedMassCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4020,
            )

            return self._parent._cast(_4020.UnbalancedMassCompoundStabilityAnalysis)

        @property
        def virtual_component_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4021.VirtualComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4021,
            )

            return self._parent._cast(_4021.VirtualComponentCompoundStabilityAnalysis)

        @property
        def worm_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4022.WormGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4022,
            )

            return self._parent._cast(_4022.WormGearCompoundStabilityAnalysis)

        @property
        def worm_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4024.WormGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4024,
            )

            return self._parent._cast(_4024.WormGearSetCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4025.ZerolBevelGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4025,
            )

            return self._parent._cast(_4025.ZerolBevelGearCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4027.ZerolBevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4027,
            )

            return self._parent._cast(_4027.ZerolBevelGearSetCompoundStabilityAnalysis)

        @property
        def abstract_assembly_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4169.AbstractAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4169,
            )

            return self._parent._cast(_4169.AbstractAssemblyCompoundPowerFlow)

        @property
        def abstract_shaft_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4170.AbstractShaftCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4170,
            )

            return self._parent._cast(_4170.AbstractShaftCompoundPowerFlow)

        @property
        def abstract_shaft_or_housing_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4171.AbstractShaftOrHousingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4171,
            )

            return self._parent._cast(_4171.AbstractShaftOrHousingCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4173.AGMAGleasonConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4173,
            )

            return self._parent._cast(_4173.AGMAGleasonConicalGearCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4175.AGMAGleasonConicalGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4175,
            )

            return self._parent._cast(_4175.AGMAGleasonConicalGearSetCompoundPowerFlow)

        @property
        def assembly_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4176.AssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4176,
            )

            return self._parent._cast(_4176.AssemblyCompoundPowerFlow)

        @property
        def bearing_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4177.BearingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4177,
            )

            return self._parent._cast(_4177.BearingCompoundPowerFlow)

        @property
        def belt_drive_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4179.BeltDriveCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4179,
            )

            return self._parent._cast(_4179.BeltDriveCompoundPowerFlow)

        @property
        def bevel_differential_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4180.BevelDifferentialGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4180,
            )

            return self._parent._cast(_4180.BevelDifferentialGearCompoundPowerFlow)

        @property
        def bevel_differential_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4182.BevelDifferentialGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4182,
            )

            return self._parent._cast(_4182.BevelDifferentialGearSetCompoundPowerFlow)

        @property
        def bevel_differential_planet_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4183.BevelDifferentialPlanetGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4183,
            )

            return self._parent._cast(
                _4183.BevelDifferentialPlanetGearCompoundPowerFlow
            )

        @property
        def bevel_differential_sun_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4184.BevelDifferentialSunGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4184,
            )

            return self._parent._cast(_4184.BevelDifferentialSunGearCompoundPowerFlow)

        @property
        def bevel_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4185.BevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4185,
            )

            return self._parent._cast(_4185.BevelGearCompoundPowerFlow)

        @property
        def bevel_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4187.BevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4187,
            )

            return self._parent._cast(_4187.BevelGearSetCompoundPowerFlow)

        @property
        def bolt_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4188.BoltCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4188,
            )

            return self._parent._cast(_4188.BoltCompoundPowerFlow)

        @property
        def bolted_joint_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4189.BoltedJointCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4189,
            )

            return self._parent._cast(_4189.BoltedJointCompoundPowerFlow)

        @property
        def clutch_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4190.ClutchCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4190,
            )

            return self._parent._cast(_4190.ClutchCompoundPowerFlow)

        @property
        def clutch_half_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4192.ClutchHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4192,
            )

            return self._parent._cast(_4192.ClutchHalfCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4194.ComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4194,
            )

            return self._parent._cast(_4194.ComponentCompoundPowerFlow)

        @property
        def concept_coupling_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4195.ConceptCouplingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4195,
            )

            return self._parent._cast(_4195.ConceptCouplingCompoundPowerFlow)

        @property
        def concept_coupling_half_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4197.ConceptCouplingHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4197,
            )

            return self._parent._cast(_4197.ConceptCouplingHalfCompoundPowerFlow)

        @property
        def concept_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4198.ConceptGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4198,
            )

            return self._parent._cast(_4198.ConceptGearCompoundPowerFlow)

        @property
        def concept_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4200.ConceptGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4200,
            )

            return self._parent._cast(_4200.ConceptGearSetCompoundPowerFlow)

        @property
        def conical_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4201.ConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4201,
            )

            return self._parent._cast(_4201.ConicalGearCompoundPowerFlow)

        @property
        def conical_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4203.ConicalGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4203,
            )

            return self._parent._cast(_4203.ConicalGearSetCompoundPowerFlow)

        @property
        def connector_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4205.ConnectorCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4205,
            )

            return self._parent._cast(_4205.ConnectorCompoundPowerFlow)

        @property
        def coupling_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4206.CouplingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4206,
            )

            return self._parent._cast(_4206.CouplingCompoundPowerFlow)

        @property
        def coupling_half_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4208.CouplingHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4208,
            )

            return self._parent._cast(_4208.CouplingHalfCompoundPowerFlow)

        @property
        def cvt_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4210.CVTCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4210,
            )

            return self._parent._cast(_4210.CVTCompoundPowerFlow)

        @property
        def cvt_pulley_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4211.CVTPulleyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4211,
            )

            return self._parent._cast(_4211.CVTPulleyCompoundPowerFlow)

        @property
        def cycloidal_assembly_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4212.CycloidalAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4212,
            )

            return self._parent._cast(_4212.CycloidalAssemblyCompoundPowerFlow)

        @property
        def cycloidal_disc_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4214.CycloidalDiscCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4214,
            )

            return self._parent._cast(_4214.CycloidalDiscCompoundPowerFlow)

        @property
        def cylindrical_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4216.CylindricalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4216,
            )

            return self._parent._cast(_4216.CylindricalGearCompoundPowerFlow)

        @property
        def cylindrical_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4218.CylindricalGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4218,
            )

            return self._parent._cast(_4218.CylindricalGearSetCompoundPowerFlow)

        @property
        def cylindrical_planet_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4219.CylindricalPlanetGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4219,
            )

            return self._parent._cast(_4219.CylindricalPlanetGearCompoundPowerFlow)

        @property
        def datum_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4220.DatumCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4220,
            )

            return self._parent._cast(_4220.DatumCompoundPowerFlow)

        @property
        def external_cad_model_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4221.ExternalCADModelCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4221,
            )

            return self._parent._cast(_4221.ExternalCADModelCompoundPowerFlow)

        @property
        def face_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4222.FaceGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4222,
            )

            return self._parent._cast(_4222.FaceGearCompoundPowerFlow)

        @property
        def face_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4224.FaceGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4224,
            )

            return self._parent._cast(_4224.FaceGearSetCompoundPowerFlow)

        @property
        def fe_part_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4225.FEPartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4225,
            )

            return self._parent._cast(_4225.FEPartCompoundPowerFlow)

        @property
        def flexible_pin_assembly_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4226.FlexiblePinAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4226,
            )

            return self._parent._cast(_4226.FlexiblePinAssemblyCompoundPowerFlow)

        @property
        def gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4227.GearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4227,
            )

            return self._parent._cast(_4227.GearCompoundPowerFlow)

        @property
        def gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4229.GearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4229,
            )

            return self._parent._cast(_4229.GearSetCompoundPowerFlow)

        @property
        def guide_dxf_model_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4230.GuideDxfModelCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4230,
            )

            return self._parent._cast(_4230.GuideDxfModelCompoundPowerFlow)

        @property
        def hypoid_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4231.HypoidGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4231,
            )

            return self._parent._cast(_4231.HypoidGearCompoundPowerFlow)

        @property
        def hypoid_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4233.HypoidGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4233,
            )

            return self._parent._cast(_4233.HypoidGearSetCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4235.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4235,
            )

            return self._parent._cast(
                _4235.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4237.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4237,
            )

            return self._parent._cast(
                _4237.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4238.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4238,
            )

            return self._parent._cast(
                _4238.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4240.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4240,
            )

            return self._parent._cast(
                _4240.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4241.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4241,
            )

            return self._parent._cast(
                _4241.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4243.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4243,
            )

            return self._parent._cast(
                _4243.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow
            )

        @property
        def mass_disc_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4244.MassDiscCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4244,
            )

            return self._parent._cast(_4244.MassDiscCompoundPowerFlow)

        @property
        def measurement_component_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4245.MeasurementComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4245,
            )

            return self._parent._cast(_4245.MeasurementComponentCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4246.MountableComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4246,
            )

            return self._parent._cast(_4246.MountableComponentCompoundPowerFlow)

        @property
        def oil_seal_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4247.OilSealCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4247,
            )

            return self._parent._cast(_4247.OilSealCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4248.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4248,
            )

            return self._parent._cast(_4248.PartCompoundPowerFlow)

        @property
        def part_to_part_shear_coupling_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4249.PartToPartShearCouplingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4249,
            )

            return self._parent._cast(_4249.PartToPartShearCouplingCompoundPowerFlow)

        @property
        def part_to_part_shear_coupling_half_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4251.PartToPartShearCouplingHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4251,
            )

            return self._parent._cast(
                _4251.PartToPartShearCouplingHalfCompoundPowerFlow
            )

        @property
        def planetary_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4253.PlanetaryGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4253,
            )

            return self._parent._cast(_4253.PlanetaryGearSetCompoundPowerFlow)

        @property
        def planet_carrier_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4254.PlanetCarrierCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4254,
            )

            return self._parent._cast(_4254.PlanetCarrierCompoundPowerFlow)

        @property
        def point_load_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4255.PointLoadCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4255,
            )

            return self._parent._cast(_4255.PointLoadCompoundPowerFlow)

        @property
        def power_load_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4256.PowerLoadCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4256,
            )

            return self._parent._cast(_4256.PowerLoadCompoundPowerFlow)

        @property
        def pulley_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4257.PulleyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4257,
            )

            return self._parent._cast(_4257.PulleyCompoundPowerFlow)

        @property
        def ring_pins_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4258.RingPinsCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4258,
            )

            return self._parent._cast(_4258.RingPinsCompoundPowerFlow)

        @property
        def rolling_ring_assembly_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4260.RollingRingAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4260,
            )

            return self._parent._cast(_4260.RollingRingAssemblyCompoundPowerFlow)

        @property
        def rolling_ring_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4261.RollingRingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4261,
            )

            return self._parent._cast(_4261.RollingRingCompoundPowerFlow)

        @property
        def root_assembly_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4263.RootAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4263,
            )

            return self._parent._cast(_4263.RootAssemblyCompoundPowerFlow)

        @property
        def shaft_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4264.ShaftCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4264,
            )

            return self._parent._cast(_4264.ShaftCompoundPowerFlow)

        @property
        def shaft_hub_connection_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4265.ShaftHubConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4265,
            )

            return self._parent._cast(_4265.ShaftHubConnectionCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4267.SpecialisedAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4267,
            )

            return self._parent._cast(_4267.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def spiral_bevel_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4268.SpiralBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4268,
            )

            return self._parent._cast(_4268.SpiralBevelGearCompoundPowerFlow)

        @property
        def spiral_bevel_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4270.SpiralBevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4270,
            )

            return self._parent._cast(_4270.SpiralBevelGearSetCompoundPowerFlow)

        @property
        def spring_damper_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4271.SpringDamperCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4271,
            )

            return self._parent._cast(_4271.SpringDamperCompoundPowerFlow)

        @property
        def spring_damper_half_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4273.SpringDamperHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4273,
            )

            return self._parent._cast(_4273.SpringDamperHalfCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4274.StraightBevelDiffGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4274,
            )

            return self._parent._cast(_4274.StraightBevelDiffGearCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4276.StraightBevelDiffGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4276,
            )

            return self._parent._cast(_4276.StraightBevelDiffGearSetCompoundPowerFlow)

        @property
        def straight_bevel_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4277.StraightBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4277,
            )

            return self._parent._cast(_4277.StraightBevelGearCompoundPowerFlow)

        @property
        def straight_bevel_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4279.StraightBevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4279,
            )

            return self._parent._cast(_4279.StraightBevelGearSetCompoundPowerFlow)

        @property
        def straight_bevel_planet_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4280.StraightBevelPlanetGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4280,
            )

            return self._parent._cast(_4280.StraightBevelPlanetGearCompoundPowerFlow)

        @property
        def straight_bevel_sun_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4281.StraightBevelSunGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4281,
            )

            return self._parent._cast(_4281.StraightBevelSunGearCompoundPowerFlow)

        @property
        def synchroniser_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4282.SynchroniserCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4282,
            )

            return self._parent._cast(_4282.SynchroniserCompoundPowerFlow)

        @property
        def synchroniser_half_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4283.SynchroniserHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4283,
            )

            return self._parent._cast(_4283.SynchroniserHalfCompoundPowerFlow)

        @property
        def synchroniser_part_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4284.SynchroniserPartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4284,
            )

            return self._parent._cast(_4284.SynchroniserPartCompoundPowerFlow)

        @property
        def synchroniser_sleeve_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4285.SynchroniserSleeveCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4285,
            )

            return self._parent._cast(_4285.SynchroniserSleeveCompoundPowerFlow)

        @property
        def torque_converter_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4286.TorqueConverterCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4286,
            )

            return self._parent._cast(_4286.TorqueConverterCompoundPowerFlow)

        @property
        def torque_converter_pump_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4288.TorqueConverterPumpCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4288,
            )

            return self._parent._cast(_4288.TorqueConverterPumpCompoundPowerFlow)

        @property
        def torque_converter_turbine_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4289.TorqueConverterTurbineCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4289,
            )

            return self._parent._cast(_4289.TorqueConverterTurbineCompoundPowerFlow)

        @property
        def unbalanced_mass_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4290.UnbalancedMassCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4290,
            )

            return self._parent._cast(_4290.UnbalancedMassCompoundPowerFlow)

        @property
        def virtual_component_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4291.VirtualComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4291,
            )

            return self._parent._cast(_4291.VirtualComponentCompoundPowerFlow)

        @property
        def worm_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4292.WormGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4292,
            )

            return self._parent._cast(_4292.WormGearCompoundPowerFlow)

        @property
        def worm_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4294.WormGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4294,
            )

            return self._parent._cast(_4294.WormGearSetCompoundPowerFlow)

        @property
        def zerol_bevel_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4295.ZerolBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4295,
            )

            return self._parent._cast(_4295.ZerolBevelGearCompoundPowerFlow)

        @property
        def zerol_bevel_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4297.ZerolBevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4297,
            )

            return self._parent._cast(_4297.ZerolBevelGearSetCompoundPowerFlow)

        @property
        def abstract_assembly_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4445.AbstractAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4445,
            )

            return self._parent._cast(_4445.AbstractAssemblyCompoundParametricStudyTool)

        @property
        def abstract_shaft_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4446.AbstractShaftCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4446,
            )

            return self._parent._cast(_4446.AbstractShaftCompoundParametricStudyTool)

        @property
        def abstract_shaft_or_housing_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4447.AbstractShaftOrHousingCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4447,
            )

            return self._parent._cast(
                _4447.AbstractShaftOrHousingCompoundParametricStudyTool
            )

        @property
        def agma_gleason_conical_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4449.AGMAGleasonConicalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4449,
            )

            return self._parent._cast(
                _4449.AGMAGleasonConicalGearCompoundParametricStudyTool
            )

        @property
        def agma_gleason_conical_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4451.AGMAGleasonConicalGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4451,
            )

            return self._parent._cast(
                _4451.AGMAGleasonConicalGearSetCompoundParametricStudyTool
            )

        @property
        def assembly_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4452.AssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4452,
            )

            return self._parent._cast(_4452.AssemblyCompoundParametricStudyTool)

        @property
        def bearing_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4453.BearingCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4453,
            )

            return self._parent._cast(_4453.BearingCompoundParametricStudyTool)

        @property
        def belt_drive_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4455.BeltDriveCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4455,
            )

            return self._parent._cast(_4455.BeltDriveCompoundParametricStudyTool)

        @property
        def bevel_differential_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4456.BevelDifferentialGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4456,
            )

            return self._parent._cast(
                _4456.BevelDifferentialGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4458.BevelDifferentialGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4458,
            )

            return self._parent._cast(
                _4458.BevelDifferentialGearSetCompoundParametricStudyTool
            )

        @property
        def bevel_differential_planet_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4459.BevelDifferentialPlanetGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4459,
            )

            return self._parent._cast(
                _4459.BevelDifferentialPlanetGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_sun_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4460.BevelDifferentialSunGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4460,
            )

            return self._parent._cast(
                _4460.BevelDifferentialSunGearCompoundParametricStudyTool
            )

        @property
        def bevel_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4461.BevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4461,
            )

            return self._parent._cast(_4461.BevelGearCompoundParametricStudyTool)

        @property
        def bevel_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4463.BevelGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4463,
            )

            return self._parent._cast(_4463.BevelGearSetCompoundParametricStudyTool)

        @property
        def bolt_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4464.BoltCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4464,
            )

            return self._parent._cast(_4464.BoltCompoundParametricStudyTool)

        @property
        def bolted_joint_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4465.BoltedJointCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4465,
            )

            return self._parent._cast(_4465.BoltedJointCompoundParametricStudyTool)

        @property
        def clutch_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4466.ClutchCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4466,
            )

            return self._parent._cast(_4466.ClutchCompoundParametricStudyTool)

        @property
        def clutch_half_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4468.ClutchHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4468,
            )

            return self._parent._cast(_4468.ClutchHalfCompoundParametricStudyTool)

        @property
        def component_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4470.ComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4470,
            )

            return self._parent._cast(_4470.ComponentCompoundParametricStudyTool)

        @property
        def concept_coupling_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4471.ConceptCouplingCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4471,
            )

            return self._parent._cast(_4471.ConceptCouplingCompoundParametricStudyTool)

        @property
        def concept_coupling_half_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4473.ConceptCouplingHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4473,
            )

            return self._parent._cast(
                _4473.ConceptCouplingHalfCompoundParametricStudyTool
            )

        @property
        def concept_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4474.ConceptGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4474,
            )

            return self._parent._cast(_4474.ConceptGearCompoundParametricStudyTool)

        @property
        def concept_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4476.ConceptGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4476,
            )

            return self._parent._cast(_4476.ConceptGearSetCompoundParametricStudyTool)

        @property
        def conical_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4477.ConicalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4477,
            )

            return self._parent._cast(_4477.ConicalGearCompoundParametricStudyTool)

        @property
        def conical_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4479.ConicalGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4479,
            )

            return self._parent._cast(_4479.ConicalGearSetCompoundParametricStudyTool)

        @property
        def connector_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4481.ConnectorCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4481,
            )

            return self._parent._cast(_4481.ConnectorCompoundParametricStudyTool)

        @property
        def coupling_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4482.CouplingCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4482,
            )

            return self._parent._cast(_4482.CouplingCompoundParametricStudyTool)

        @property
        def coupling_half_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4484.CouplingHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4484,
            )

            return self._parent._cast(_4484.CouplingHalfCompoundParametricStudyTool)

        @property
        def cvt_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4486.CVTCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4486,
            )

            return self._parent._cast(_4486.CVTCompoundParametricStudyTool)

        @property
        def cvt_pulley_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4487.CVTPulleyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4487,
            )

            return self._parent._cast(_4487.CVTPulleyCompoundParametricStudyTool)

        @property
        def cycloidal_assembly_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4488.CycloidalAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4488,
            )

            return self._parent._cast(
                _4488.CycloidalAssemblyCompoundParametricStudyTool
            )

        @property
        def cycloidal_disc_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4490.CycloidalDiscCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4490,
            )

            return self._parent._cast(_4490.CycloidalDiscCompoundParametricStudyTool)

        @property
        def cylindrical_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4492.CylindricalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4492,
            )

            return self._parent._cast(_4492.CylindricalGearCompoundParametricStudyTool)

        @property
        def cylindrical_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4494.CylindricalGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4494,
            )

            return self._parent._cast(
                _4494.CylindricalGearSetCompoundParametricStudyTool
            )

        @property
        def cylindrical_planet_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4495.CylindricalPlanetGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4495,
            )

            return self._parent._cast(
                _4495.CylindricalPlanetGearCompoundParametricStudyTool
            )

        @property
        def datum_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4496.DatumCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4496,
            )

            return self._parent._cast(_4496.DatumCompoundParametricStudyTool)

        @property
        def external_cad_model_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4497.ExternalCADModelCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4497,
            )

            return self._parent._cast(_4497.ExternalCADModelCompoundParametricStudyTool)

        @property
        def face_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4498.FaceGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4498,
            )

            return self._parent._cast(_4498.FaceGearCompoundParametricStudyTool)

        @property
        def face_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4500.FaceGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4500,
            )

            return self._parent._cast(_4500.FaceGearSetCompoundParametricStudyTool)

        @property
        def fe_part_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4501.FEPartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4501,
            )

            return self._parent._cast(_4501.FEPartCompoundParametricStudyTool)

        @property
        def flexible_pin_assembly_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4502.FlexiblePinAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4502,
            )

            return self._parent._cast(
                _4502.FlexiblePinAssemblyCompoundParametricStudyTool
            )

        @property
        def gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4503.GearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4503,
            )

            return self._parent._cast(_4503.GearCompoundParametricStudyTool)

        @property
        def gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4505.GearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4505,
            )

            return self._parent._cast(_4505.GearSetCompoundParametricStudyTool)

        @property
        def guide_dxf_model_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4506.GuideDxfModelCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4506,
            )

            return self._parent._cast(_4506.GuideDxfModelCompoundParametricStudyTool)

        @property
        def hypoid_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4507.HypoidGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4507,
            )

            return self._parent._cast(_4507.HypoidGearCompoundParametricStudyTool)

        @property
        def hypoid_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4509.HypoidGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4509,
            )

            return self._parent._cast(_4509.HypoidGearSetCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4511.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4511,
            )

            return self._parent._cast(
                _4511.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4513.KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4513,
            )

            return self._parent._cast(
                _4513.KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4514.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4514,
            )

            return self._parent._cast(
                _4514.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4516.KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4516,
            )

            return self._parent._cast(
                _4516.KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4517.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4517,
            )

            return self._parent._cast(
                _4517.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4519.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4519,
            )

            return self._parent._cast(
                _4519.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool
            )

        @property
        def mass_disc_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4520.MassDiscCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4520,
            )

            return self._parent._cast(_4520.MassDiscCompoundParametricStudyTool)

        @property
        def measurement_component_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4521.MeasurementComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4521,
            )

            return self._parent._cast(
                _4521.MeasurementComponentCompoundParametricStudyTool
            )

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4522.MountableComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4522,
            )

            return self._parent._cast(
                _4522.MountableComponentCompoundParametricStudyTool
            )

        @property
        def oil_seal_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4523.OilSealCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4523,
            )

            return self._parent._cast(_4523.OilSealCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4524.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4524,
            )

            return self._parent._cast(_4524.PartCompoundParametricStudyTool)

        @property
        def part_to_part_shear_coupling_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4525.PartToPartShearCouplingCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4525,
            )

            return self._parent._cast(
                _4525.PartToPartShearCouplingCompoundParametricStudyTool
            )

        @property
        def part_to_part_shear_coupling_half_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4527.PartToPartShearCouplingHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4527,
            )

            return self._parent._cast(
                _4527.PartToPartShearCouplingHalfCompoundParametricStudyTool
            )

        @property
        def planetary_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4529.PlanetaryGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4529,
            )

            return self._parent._cast(_4529.PlanetaryGearSetCompoundParametricStudyTool)

        @property
        def planet_carrier_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4530.PlanetCarrierCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4530,
            )

            return self._parent._cast(_4530.PlanetCarrierCompoundParametricStudyTool)

        @property
        def point_load_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4531.PointLoadCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4531,
            )

            return self._parent._cast(_4531.PointLoadCompoundParametricStudyTool)

        @property
        def power_load_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4532.PowerLoadCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4532,
            )

            return self._parent._cast(_4532.PowerLoadCompoundParametricStudyTool)

        @property
        def pulley_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4533.PulleyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4533,
            )

            return self._parent._cast(_4533.PulleyCompoundParametricStudyTool)

        @property
        def ring_pins_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4534.RingPinsCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4534,
            )

            return self._parent._cast(_4534.RingPinsCompoundParametricStudyTool)

        @property
        def rolling_ring_assembly_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4536.RollingRingAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4536,
            )

            return self._parent._cast(
                _4536.RollingRingAssemblyCompoundParametricStudyTool
            )

        @property
        def rolling_ring_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4537.RollingRingCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4537,
            )

            return self._parent._cast(_4537.RollingRingCompoundParametricStudyTool)

        @property
        def root_assembly_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4539.RootAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4539,
            )

            return self._parent._cast(_4539.RootAssemblyCompoundParametricStudyTool)

        @property
        def shaft_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4540.ShaftCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4540,
            )

            return self._parent._cast(_4540.ShaftCompoundParametricStudyTool)

        @property
        def shaft_hub_connection_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4541.ShaftHubConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4541,
            )

            return self._parent._cast(
                _4541.ShaftHubConnectionCompoundParametricStudyTool
            )

        @property
        def specialised_assembly_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4543.SpecialisedAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4543,
            )

            return self._parent._cast(
                _4543.SpecialisedAssemblyCompoundParametricStudyTool
            )

        @property
        def spiral_bevel_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4544.SpiralBevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4544,
            )

            return self._parent._cast(_4544.SpiralBevelGearCompoundParametricStudyTool)

        @property
        def spiral_bevel_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4546.SpiralBevelGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4546,
            )

            return self._parent._cast(
                _4546.SpiralBevelGearSetCompoundParametricStudyTool
            )

        @property
        def spring_damper_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4547.SpringDamperCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4547,
            )

            return self._parent._cast(_4547.SpringDamperCompoundParametricStudyTool)

        @property
        def spring_damper_half_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4549.SpringDamperHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4549,
            )

            return self._parent._cast(_4549.SpringDamperHalfCompoundParametricStudyTool)

        @property
        def straight_bevel_diff_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4550.StraightBevelDiffGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4550,
            )

            return self._parent._cast(
                _4550.StraightBevelDiffGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_diff_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4552.StraightBevelDiffGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4552,
            )

            return self._parent._cast(
                _4552.StraightBevelDiffGearSetCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4553.StraightBevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4553,
            )

            return self._parent._cast(
                _4553.StraightBevelGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4555.StraightBevelGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4555,
            )

            return self._parent._cast(
                _4555.StraightBevelGearSetCompoundParametricStudyTool
            )

        @property
        def straight_bevel_planet_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4556.StraightBevelPlanetGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4556,
            )

            return self._parent._cast(
                _4556.StraightBevelPlanetGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_sun_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4557.StraightBevelSunGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4557,
            )

            return self._parent._cast(
                _4557.StraightBevelSunGearCompoundParametricStudyTool
            )

        @property
        def synchroniser_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4558.SynchroniserCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4558,
            )

            return self._parent._cast(_4558.SynchroniserCompoundParametricStudyTool)

        @property
        def synchroniser_half_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4559.SynchroniserHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4559,
            )

            return self._parent._cast(_4559.SynchroniserHalfCompoundParametricStudyTool)

        @property
        def synchroniser_part_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4560.SynchroniserPartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4560,
            )

            return self._parent._cast(_4560.SynchroniserPartCompoundParametricStudyTool)

        @property
        def synchroniser_sleeve_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4561.SynchroniserSleeveCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4561,
            )

            return self._parent._cast(
                _4561.SynchroniserSleeveCompoundParametricStudyTool
            )

        @property
        def torque_converter_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4562.TorqueConverterCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4562,
            )

            return self._parent._cast(_4562.TorqueConverterCompoundParametricStudyTool)

        @property
        def torque_converter_pump_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4564.TorqueConverterPumpCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4564,
            )

            return self._parent._cast(
                _4564.TorqueConverterPumpCompoundParametricStudyTool
            )

        @property
        def torque_converter_turbine_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4565.TorqueConverterTurbineCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4565,
            )

            return self._parent._cast(
                _4565.TorqueConverterTurbineCompoundParametricStudyTool
            )

        @property
        def unbalanced_mass_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4566.UnbalancedMassCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4566,
            )

            return self._parent._cast(_4566.UnbalancedMassCompoundParametricStudyTool)

        @property
        def virtual_component_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4567.VirtualComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4567,
            )

            return self._parent._cast(_4567.VirtualComponentCompoundParametricStudyTool)

        @property
        def worm_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4568.WormGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4568,
            )

            return self._parent._cast(_4568.WormGearCompoundParametricStudyTool)

        @property
        def worm_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4570.WormGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4570,
            )

            return self._parent._cast(_4570.WormGearSetCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4571.ZerolBevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4571,
            )

            return self._parent._cast(_4571.ZerolBevelGearCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4573.ZerolBevelGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4573,
            )

            return self._parent._cast(
                _4573.ZerolBevelGearSetCompoundParametricStudyTool
            )

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4730.AbstractAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4730,
            )

            return self._parent._cast(_4730.AbstractAssemblyCompoundModalAnalysis)

        @property
        def abstract_shaft_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4731.AbstractShaftCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4731,
            )

            return self._parent._cast(_4731.AbstractShaftCompoundModalAnalysis)

        @property
        def abstract_shaft_or_housing_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4732.AbstractShaftOrHousingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4732,
            )

            return self._parent._cast(_4732.AbstractShaftOrHousingCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4734.AGMAGleasonConicalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4734,
            )

            return self._parent._cast(_4734.AGMAGleasonConicalGearCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4736.AGMAGleasonConicalGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4736,
            )

            return self._parent._cast(
                _4736.AGMAGleasonConicalGearSetCompoundModalAnalysis
            )

        @property
        def assembly_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4737.AssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4737,
            )

            return self._parent._cast(_4737.AssemblyCompoundModalAnalysis)

        @property
        def bearing_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4738.BearingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4738,
            )

            return self._parent._cast(_4738.BearingCompoundModalAnalysis)

        @property
        def belt_drive_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4740.BeltDriveCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4740,
            )

            return self._parent._cast(_4740.BeltDriveCompoundModalAnalysis)

        @property
        def bevel_differential_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4741.BevelDifferentialGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4741,
            )

            return self._parent._cast(_4741.BevelDifferentialGearCompoundModalAnalysis)

        @property
        def bevel_differential_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4743.BevelDifferentialGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4743,
            )

            return self._parent._cast(
                _4743.BevelDifferentialGearSetCompoundModalAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4744.BevelDifferentialPlanetGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4744,
            )

            return self._parent._cast(
                _4744.BevelDifferentialPlanetGearCompoundModalAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4745.BevelDifferentialSunGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4745,
            )

            return self._parent._cast(
                _4745.BevelDifferentialSunGearCompoundModalAnalysis
            )

        @property
        def bevel_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4746.BevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4746,
            )

            return self._parent._cast(_4746.BevelGearCompoundModalAnalysis)

        @property
        def bevel_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4748.BevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4748,
            )

            return self._parent._cast(_4748.BevelGearSetCompoundModalAnalysis)

        @property
        def bolt_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4749.BoltCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4749,
            )

            return self._parent._cast(_4749.BoltCompoundModalAnalysis)

        @property
        def bolted_joint_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4750.BoltedJointCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4750,
            )

            return self._parent._cast(_4750.BoltedJointCompoundModalAnalysis)

        @property
        def clutch_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4751.ClutchCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4751,
            )

            return self._parent._cast(_4751.ClutchCompoundModalAnalysis)

        @property
        def clutch_half_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4753.ClutchHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4753,
            )

            return self._parent._cast(_4753.ClutchHalfCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4755.ComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4755,
            )

            return self._parent._cast(_4755.ComponentCompoundModalAnalysis)

        @property
        def concept_coupling_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4756.ConceptCouplingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4756,
            )

            return self._parent._cast(_4756.ConceptCouplingCompoundModalAnalysis)

        @property
        def concept_coupling_half_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4758.ConceptCouplingHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4758,
            )

            return self._parent._cast(_4758.ConceptCouplingHalfCompoundModalAnalysis)

        @property
        def concept_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4759.ConceptGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4759,
            )

            return self._parent._cast(_4759.ConceptGearCompoundModalAnalysis)

        @property
        def concept_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4761.ConceptGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4761,
            )

            return self._parent._cast(_4761.ConceptGearSetCompoundModalAnalysis)

        @property
        def conical_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4762.ConicalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4762,
            )

            return self._parent._cast(_4762.ConicalGearCompoundModalAnalysis)

        @property
        def conical_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4764.ConicalGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4764,
            )

            return self._parent._cast(_4764.ConicalGearSetCompoundModalAnalysis)

        @property
        def connector_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4766.ConnectorCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4766,
            )

            return self._parent._cast(_4766.ConnectorCompoundModalAnalysis)

        @property
        def coupling_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4767.CouplingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4767,
            )

            return self._parent._cast(_4767.CouplingCompoundModalAnalysis)

        @property
        def coupling_half_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4769.CouplingHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4769,
            )

            return self._parent._cast(_4769.CouplingHalfCompoundModalAnalysis)

        @property
        def cvt_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4771.CVTCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4771,
            )

            return self._parent._cast(_4771.CVTCompoundModalAnalysis)

        @property
        def cvt_pulley_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4772.CVTPulleyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4772,
            )

            return self._parent._cast(_4772.CVTPulleyCompoundModalAnalysis)

        @property
        def cycloidal_assembly_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4773.CycloidalAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4773,
            )

            return self._parent._cast(_4773.CycloidalAssemblyCompoundModalAnalysis)

        @property
        def cycloidal_disc_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4775.CycloidalDiscCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4775,
            )

            return self._parent._cast(_4775.CycloidalDiscCompoundModalAnalysis)

        @property
        def cylindrical_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4777.CylindricalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4777,
            )

            return self._parent._cast(_4777.CylindricalGearCompoundModalAnalysis)

        @property
        def cylindrical_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4779.CylindricalGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4779,
            )

            return self._parent._cast(_4779.CylindricalGearSetCompoundModalAnalysis)

        @property
        def cylindrical_planet_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4780.CylindricalPlanetGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4780,
            )

            return self._parent._cast(_4780.CylindricalPlanetGearCompoundModalAnalysis)

        @property
        def datum_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4781.DatumCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4781,
            )

            return self._parent._cast(_4781.DatumCompoundModalAnalysis)

        @property
        def external_cad_model_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4782.ExternalCADModelCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4782,
            )

            return self._parent._cast(_4782.ExternalCADModelCompoundModalAnalysis)

        @property
        def face_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4783.FaceGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4783,
            )

            return self._parent._cast(_4783.FaceGearCompoundModalAnalysis)

        @property
        def face_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4785.FaceGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4785,
            )

            return self._parent._cast(_4785.FaceGearSetCompoundModalAnalysis)

        @property
        def fe_part_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4786.FEPartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4786,
            )

            return self._parent._cast(_4786.FEPartCompoundModalAnalysis)

        @property
        def flexible_pin_assembly_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4787.FlexiblePinAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4787,
            )

            return self._parent._cast(_4787.FlexiblePinAssemblyCompoundModalAnalysis)

        @property
        def gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4788.GearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4788,
            )

            return self._parent._cast(_4788.GearCompoundModalAnalysis)

        @property
        def gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4790.GearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4790,
            )

            return self._parent._cast(_4790.GearSetCompoundModalAnalysis)

        @property
        def guide_dxf_model_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4791.GuideDxfModelCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4791,
            )

            return self._parent._cast(_4791.GuideDxfModelCompoundModalAnalysis)

        @property
        def hypoid_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4792.HypoidGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4792,
            )

            return self._parent._cast(_4792.HypoidGearCompoundModalAnalysis)

        @property
        def hypoid_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4794.HypoidGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4794,
            )

            return self._parent._cast(_4794.HypoidGearSetCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4796.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4796,
            )

            return self._parent._cast(
                _4796.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4798.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4798,
            )

            return self._parent._cast(
                _4798.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4799.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4799,
            )

            return self._parent._cast(
                _4799.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4801.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4801,
            )

            return self._parent._cast(
                _4801.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4802.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4802,
            )

            return self._parent._cast(
                _4802.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4804.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4804,
            )

            return self._parent._cast(
                _4804.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis
            )

        @property
        def mass_disc_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4805.MassDiscCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4805,
            )

            return self._parent._cast(_4805.MassDiscCompoundModalAnalysis)

        @property
        def measurement_component_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4806.MeasurementComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4806,
            )

            return self._parent._cast(_4806.MeasurementComponentCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4807.MountableComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4807,
            )

            return self._parent._cast(_4807.MountableComponentCompoundModalAnalysis)

        @property
        def oil_seal_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4808.OilSealCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4808,
            )

            return self._parent._cast(_4808.OilSealCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4809.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4809,
            )

            return self._parent._cast(_4809.PartCompoundModalAnalysis)

        @property
        def part_to_part_shear_coupling_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4810.PartToPartShearCouplingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4810,
            )

            return self._parent._cast(
                _4810.PartToPartShearCouplingCompoundModalAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4812.PartToPartShearCouplingHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4812,
            )

            return self._parent._cast(
                _4812.PartToPartShearCouplingHalfCompoundModalAnalysis
            )

        @property
        def planetary_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4814.PlanetaryGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4814,
            )

            return self._parent._cast(_4814.PlanetaryGearSetCompoundModalAnalysis)

        @property
        def planet_carrier_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4815.PlanetCarrierCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4815,
            )

            return self._parent._cast(_4815.PlanetCarrierCompoundModalAnalysis)

        @property
        def point_load_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4816.PointLoadCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4816,
            )

            return self._parent._cast(_4816.PointLoadCompoundModalAnalysis)

        @property
        def power_load_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4817.PowerLoadCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4817,
            )

            return self._parent._cast(_4817.PowerLoadCompoundModalAnalysis)

        @property
        def pulley_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4818.PulleyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4818,
            )

            return self._parent._cast(_4818.PulleyCompoundModalAnalysis)

        @property
        def ring_pins_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4819.RingPinsCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4819,
            )

            return self._parent._cast(_4819.RingPinsCompoundModalAnalysis)

        @property
        def rolling_ring_assembly_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4821.RollingRingAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4821,
            )

            return self._parent._cast(_4821.RollingRingAssemblyCompoundModalAnalysis)

        @property
        def rolling_ring_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4822.RollingRingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4822,
            )

            return self._parent._cast(_4822.RollingRingCompoundModalAnalysis)

        @property
        def root_assembly_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4824.RootAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4824,
            )

            return self._parent._cast(_4824.RootAssemblyCompoundModalAnalysis)

        @property
        def shaft_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4825.ShaftCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4825,
            )

            return self._parent._cast(_4825.ShaftCompoundModalAnalysis)

        @property
        def shaft_hub_connection_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4826.ShaftHubConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4826,
            )

            return self._parent._cast(_4826.ShaftHubConnectionCompoundModalAnalysis)

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4828.SpecialisedAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4828,
            )

            return self._parent._cast(_4828.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4829.SpiralBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4829,
            )

            return self._parent._cast(_4829.SpiralBevelGearCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4831.SpiralBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4831,
            )

            return self._parent._cast(_4831.SpiralBevelGearSetCompoundModalAnalysis)

        @property
        def spring_damper_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4832.SpringDamperCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4832,
            )

            return self._parent._cast(_4832.SpringDamperCompoundModalAnalysis)

        @property
        def spring_damper_half_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4834.SpringDamperHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4834,
            )

            return self._parent._cast(_4834.SpringDamperHalfCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4835.StraightBevelDiffGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4835,
            )

            return self._parent._cast(_4835.StraightBevelDiffGearCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4837.StraightBevelDiffGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4837,
            )

            return self._parent._cast(
                _4837.StraightBevelDiffGearSetCompoundModalAnalysis
            )

        @property
        def straight_bevel_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4838.StraightBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4838,
            )

            return self._parent._cast(_4838.StraightBevelGearCompoundModalAnalysis)

        @property
        def straight_bevel_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4840.StraightBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4840,
            )

            return self._parent._cast(_4840.StraightBevelGearSetCompoundModalAnalysis)

        @property
        def straight_bevel_planet_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4841.StraightBevelPlanetGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4841,
            )

            return self._parent._cast(
                _4841.StraightBevelPlanetGearCompoundModalAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4842.StraightBevelSunGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4842,
            )

            return self._parent._cast(_4842.StraightBevelSunGearCompoundModalAnalysis)

        @property
        def synchroniser_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4843.SynchroniserCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4843,
            )

            return self._parent._cast(_4843.SynchroniserCompoundModalAnalysis)

        @property
        def synchroniser_half_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4844.SynchroniserHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4844,
            )

            return self._parent._cast(_4844.SynchroniserHalfCompoundModalAnalysis)

        @property
        def synchroniser_part_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4845.SynchroniserPartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4845,
            )

            return self._parent._cast(_4845.SynchroniserPartCompoundModalAnalysis)

        @property
        def synchroniser_sleeve_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4846.SynchroniserSleeveCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4846,
            )

            return self._parent._cast(_4846.SynchroniserSleeveCompoundModalAnalysis)

        @property
        def torque_converter_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4847.TorqueConverterCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4847,
            )

            return self._parent._cast(_4847.TorqueConverterCompoundModalAnalysis)

        @property
        def torque_converter_pump_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4849.TorqueConverterPumpCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4849,
            )

            return self._parent._cast(_4849.TorqueConverterPumpCompoundModalAnalysis)

        @property
        def torque_converter_turbine_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4850.TorqueConverterTurbineCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4850,
            )

            return self._parent._cast(_4850.TorqueConverterTurbineCompoundModalAnalysis)

        @property
        def unbalanced_mass_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4851.UnbalancedMassCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4851,
            )

            return self._parent._cast(_4851.UnbalancedMassCompoundModalAnalysis)

        @property
        def virtual_component_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4852.VirtualComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4852,
            )

            return self._parent._cast(_4852.VirtualComponentCompoundModalAnalysis)

        @property
        def worm_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4853.WormGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4853,
            )

            return self._parent._cast(_4853.WormGearCompoundModalAnalysis)

        @property
        def worm_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4855.WormGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4855,
            )

            return self._parent._cast(_4855.WormGearSetCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4856.ZerolBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4856,
            )

            return self._parent._cast(_4856.ZerolBevelGearCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4858.ZerolBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4858,
            )

            return self._parent._cast(_4858.ZerolBevelGearSetCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4990.AbstractAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4990,
            )

            return self._parent._cast(
                _4990.AbstractAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_shaft_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4991.AbstractShaftCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4991,
            )

            return self._parent._cast(
                _4991.AbstractShaftCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_shaft_or_housing_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4992.AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4992,
            )

            return self._parent._cast(
                _4992.AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness
            )

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4994.AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4994,
            )

            return self._parent._cast(
                _4994.AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4996.AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4996,
            )

            return self._parent._cast(
                _4996.AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def assembly_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4997.AssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4997,
            )

            return self._parent._cast(_4997.AssemblyCompoundModalAnalysisAtAStiffness)

        @property
        def bearing_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_4998.BearingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4998,
            )

            return self._parent._cast(_4998.BearingCompoundModalAnalysisAtAStiffness)

        @property
        def belt_drive_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5000.BeltDriveCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5000,
            )

            return self._parent._cast(_5000.BeltDriveCompoundModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5001.BevelDifferentialGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5001,
            )

            return self._parent._cast(
                _5001.BevelDifferentialGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5003.BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5003,
            )

            return self._parent._cast(
                _5003.BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5004.BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5004,
            )

            return self._parent._cast(
                _5004.BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5005.BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5005,
            )

            return self._parent._cast(
                _5005.BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5006.BevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5006,
            )

            return self._parent._cast(_5006.BevelGearCompoundModalAnalysisAtAStiffness)

        @property
        def bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5008.BevelGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5008,
            )

            return self._parent._cast(
                _5008.BevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def bolt_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5009.BoltCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5009,
            )

            return self._parent._cast(_5009.BoltCompoundModalAnalysisAtAStiffness)

        @property
        def bolted_joint_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5010.BoltedJointCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5010,
            )

            return self._parent._cast(
                _5010.BoltedJointCompoundModalAnalysisAtAStiffness
            )

        @property
        def clutch_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5011.ClutchCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5011,
            )

            return self._parent._cast(_5011.ClutchCompoundModalAnalysisAtAStiffness)

        @property
        def clutch_half_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5013.ClutchHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5013,
            )

            return self._parent._cast(_5013.ClutchHalfCompoundModalAnalysisAtAStiffness)

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5015.ComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5015,
            )

            return self._parent._cast(_5015.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def concept_coupling_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5016.ConceptCouplingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5016,
            )

            return self._parent._cast(
                _5016.ConceptCouplingCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5018.ConceptCouplingHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5018,
            )

            return self._parent._cast(
                _5018.ConceptCouplingHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5019.ConceptGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5019,
            )

            return self._parent._cast(
                _5019.ConceptGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5021.ConceptGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5021,
            )

            return self._parent._cast(
                _5021.ConceptGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5022.ConicalGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5022,
            )

            return self._parent._cast(
                _5022.ConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5024.ConicalGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5024,
            )

            return self._parent._cast(
                _5024.ConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def connector_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5026.ConnectorCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5026,
            )

            return self._parent._cast(_5026.ConnectorCompoundModalAnalysisAtAStiffness)

        @property
        def coupling_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5027.CouplingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5027,
            )

            return self._parent._cast(_5027.CouplingCompoundModalAnalysisAtAStiffness)

        @property
        def coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5029.CouplingHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5029,
            )

            return self._parent._cast(
                _5029.CouplingHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def cvt_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5031.CVTCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5031,
            )

            return self._parent._cast(_5031.CVTCompoundModalAnalysisAtAStiffness)

        @property
        def cvt_pulley_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5032.CVTPulleyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5032,
            )

            return self._parent._cast(_5032.CVTPulleyCompoundModalAnalysisAtAStiffness)

        @property
        def cycloidal_assembly_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5033.CycloidalAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5033,
            )

            return self._parent._cast(
                _5033.CycloidalAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def cycloidal_disc_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5035.CycloidalDiscCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5035,
            )

            return self._parent._cast(
                _5035.CycloidalDiscCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5037.CylindricalGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5037,
            )

            return self._parent._cast(
                _5037.CylindricalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5039.CylindricalGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5039,
            )

            return self._parent._cast(
                _5039.CylindricalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5040.CylindricalPlanetGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5040,
            )

            return self._parent._cast(
                _5040.CylindricalPlanetGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def datum_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5041.DatumCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5041,
            )

            return self._parent._cast(_5041.DatumCompoundModalAnalysisAtAStiffness)

        @property
        def external_cad_model_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5042.ExternalCADModelCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5042,
            )

            return self._parent._cast(
                _5042.ExternalCADModelCompoundModalAnalysisAtAStiffness
            )

        @property
        def face_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5043.FaceGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5043,
            )

            return self._parent._cast(_5043.FaceGearCompoundModalAnalysisAtAStiffness)

        @property
        def face_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5045.FaceGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5045,
            )

            return self._parent._cast(
                _5045.FaceGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def fe_part_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5046.FEPartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5046,
            )

            return self._parent._cast(_5046.FEPartCompoundModalAnalysisAtAStiffness)

        @property
        def flexible_pin_assembly_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5047.FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5047,
            )

            return self._parent._cast(
                _5047.FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5048.GearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5048,
            )

            return self._parent._cast(_5048.GearCompoundModalAnalysisAtAStiffness)

        @property
        def gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5050.GearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5050,
            )

            return self._parent._cast(_5050.GearSetCompoundModalAnalysisAtAStiffness)

        @property
        def guide_dxf_model_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5051.GuideDxfModelCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5051,
            )

            return self._parent._cast(
                _5051.GuideDxfModelCompoundModalAnalysisAtAStiffness
            )

        @property
        def hypoid_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5052.HypoidGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5052,
            )

            return self._parent._cast(_5052.HypoidGearCompoundModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5054.HypoidGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5054,
            )

            return self._parent._cast(
                _5054.HypoidGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_5056.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5056,
            )

            return self._parent._cast(
                _5056.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5058.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5058,
            )

            return self._parent._cast(
                _5058.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_5059.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5059,
            )

            return self._parent._cast(
                _5059.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5061.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5061,
            )

            return self._parent._cast(
                _5061.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5062.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5062,
            )

            return self._parent._cast(
                _5062.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5064.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5064,
            )

            return self._parent._cast(
                _5064.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def mass_disc_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5065.MassDiscCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5065,
            )

            return self._parent._cast(_5065.MassDiscCompoundModalAnalysisAtAStiffness)

        @property
        def measurement_component_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5066.MeasurementComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5066,
            )

            return self._parent._cast(
                _5066.MeasurementComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5067.MountableComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5067,
            )

            return self._parent._cast(
                _5067.MountableComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def oil_seal_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5068.OilSealCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5068,
            )

            return self._parent._cast(_5068.OilSealCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5069.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5069,
            )

            return self._parent._cast(_5069.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_to_part_shear_coupling_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5070.PartToPartShearCouplingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5070,
            )

            return self._parent._cast(
                _5070.PartToPartShearCouplingCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5072.PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5072,
            )

            return self._parent._cast(
                _5072.PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def planetary_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5074.PlanetaryGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5074,
            )

            return self._parent._cast(
                _5074.PlanetaryGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def planet_carrier_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5075.PlanetCarrierCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5075,
            )

            return self._parent._cast(
                _5075.PlanetCarrierCompoundModalAnalysisAtAStiffness
            )

        @property
        def point_load_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5076.PointLoadCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5076,
            )

            return self._parent._cast(_5076.PointLoadCompoundModalAnalysisAtAStiffness)

        @property
        def power_load_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5077.PowerLoadCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5077,
            )

            return self._parent._cast(_5077.PowerLoadCompoundModalAnalysisAtAStiffness)

        @property
        def pulley_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5078.PulleyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5078,
            )

            return self._parent._cast(_5078.PulleyCompoundModalAnalysisAtAStiffness)

        @property
        def ring_pins_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5079.RingPinsCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5079,
            )

            return self._parent._cast(_5079.RingPinsCompoundModalAnalysisAtAStiffness)

        @property
        def rolling_ring_assembly_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5081.RollingRingAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5081,
            )

            return self._parent._cast(
                _5081.RollingRingAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def rolling_ring_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5082.RollingRingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5082,
            )

            return self._parent._cast(
                _5082.RollingRingCompoundModalAnalysisAtAStiffness
            )

        @property
        def root_assembly_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5084.RootAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5084,
            )

            return self._parent._cast(
                _5084.RootAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def shaft_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5085.ShaftCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5085,
            )

            return self._parent._cast(_5085.ShaftCompoundModalAnalysisAtAStiffness)

        @property
        def shaft_hub_connection_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5086.ShaftHubConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5086,
            )

            return self._parent._cast(
                _5086.ShaftHubConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def specialised_assembly_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5088.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5088,
            )

            return self._parent._cast(
                _5088.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5089.SpiralBevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5089,
            )

            return self._parent._cast(
                _5089.SpiralBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5091.SpiralBevelGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5091,
            )

            return self._parent._cast(
                _5091.SpiralBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5092.SpringDamperCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5092,
            )

            return self._parent._cast(
                _5092.SpringDamperCompoundModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_half_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5094.SpringDamperHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5094,
            )

            return self._parent._cast(
                _5094.SpringDamperHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5095.StraightBevelDiffGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5095,
            )

            return self._parent._cast(
                _5095.StraightBevelDiffGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5097.StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5097,
            )

            return self._parent._cast(
                _5097.StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5098.StraightBevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5098,
            )

            return self._parent._cast(
                _5098.StraightBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5100.StraightBevelGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5100,
            )

            return self._parent._cast(
                _5100.StraightBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5101.StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5101,
            )

            return self._parent._cast(
                _5101.StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5102.StraightBevelSunGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5102,
            )

            return self._parent._cast(
                _5102.StraightBevelSunGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5103.SynchroniserCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5103,
            )

            return self._parent._cast(
                _5103.SynchroniserCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_half_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5104.SynchroniserHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5104,
            )

            return self._parent._cast(
                _5104.SynchroniserHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_part_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5105.SynchroniserPartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5105,
            )

            return self._parent._cast(
                _5105.SynchroniserPartCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_sleeve_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5106.SynchroniserSleeveCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5106,
            )

            return self._parent._cast(
                _5106.SynchroniserSleeveCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5107.TorqueConverterCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5107,
            )

            return self._parent._cast(
                _5107.TorqueConverterCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_pump_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5109.TorqueConverterPumpCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5109,
            )

            return self._parent._cast(
                _5109.TorqueConverterPumpCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_turbine_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5110.TorqueConverterTurbineCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5110,
            )

            return self._parent._cast(
                _5110.TorqueConverterTurbineCompoundModalAnalysisAtAStiffness
            )

        @property
        def unbalanced_mass_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5111.UnbalancedMassCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5111,
            )

            return self._parent._cast(
                _5111.UnbalancedMassCompoundModalAnalysisAtAStiffness
            )

        @property
        def virtual_component_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5112.VirtualComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5112,
            )

            return self._parent._cast(
                _5112.VirtualComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def worm_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5113.WormGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5113,
            )

            return self._parent._cast(_5113.WormGearCompoundModalAnalysisAtAStiffness)

        @property
        def worm_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5115.WormGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5115,
            )

            return self._parent._cast(
                _5115.WormGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5116.ZerolBevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5116,
            )

            return self._parent._cast(
                _5116.ZerolBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5118.ZerolBevelGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5118,
            )

            return self._parent._cast(
                _5118.ZerolBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5249.AbstractAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5249,
            )

            return self._parent._cast(
                _5249.AbstractAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_shaft_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5250.AbstractShaftCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5250,
            )

            return self._parent._cast(_5250.AbstractShaftCompoundModalAnalysisAtASpeed)

        @property
        def abstract_shaft_or_housing_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5251.AbstractShaftOrHousingCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5251,
            )

            return self._parent._cast(
                _5251.AbstractShaftOrHousingCompoundModalAnalysisAtASpeed
            )

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5253.AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5253,
            )

            return self._parent._cast(
                _5253.AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed
            )

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5255.AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5255,
            )

            return self._parent._cast(
                _5255.AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def assembly_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5256.AssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5256,
            )

            return self._parent._cast(_5256.AssemblyCompoundModalAnalysisAtASpeed)

        @property
        def bearing_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5257.BearingCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5257,
            )

            return self._parent._cast(_5257.BearingCompoundModalAnalysisAtASpeed)

        @property
        def belt_drive_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5259.BeltDriveCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5259,
            )

            return self._parent._cast(_5259.BeltDriveCompoundModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5260.BevelDifferentialGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5260,
            )

            return self._parent._cast(
                _5260.BevelDifferentialGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5262.BevelDifferentialGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5262,
            )

            return self._parent._cast(
                _5262.BevelDifferentialGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_planet_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5263.BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5263,
            )

            return self._parent._cast(
                _5263.BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5264.BevelDifferentialSunGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5264,
            )

            return self._parent._cast(
                _5264.BevelDifferentialSunGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5265.BevelGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5265,
            )

            return self._parent._cast(_5265.BevelGearCompoundModalAnalysisAtASpeed)

        @property
        def bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5267.BevelGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5267,
            )

            return self._parent._cast(_5267.BevelGearSetCompoundModalAnalysisAtASpeed)

        @property
        def bolt_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5268.BoltCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5268,
            )

            return self._parent._cast(_5268.BoltCompoundModalAnalysisAtASpeed)

        @property
        def bolted_joint_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5269.BoltedJointCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5269,
            )

            return self._parent._cast(_5269.BoltedJointCompoundModalAnalysisAtASpeed)

        @property
        def clutch_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5270.ClutchCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5270,
            )

            return self._parent._cast(_5270.ClutchCompoundModalAnalysisAtASpeed)

        @property
        def clutch_half_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5272.ClutchHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5272,
            )

            return self._parent._cast(_5272.ClutchHalfCompoundModalAnalysisAtASpeed)

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5274.ComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5274,
            )

            return self._parent._cast(_5274.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def concept_coupling_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5275.ConceptCouplingCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5275,
            )

            return self._parent._cast(
                _5275.ConceptCouplingCompoundModalAnalysisAtASpeed
            )

        @property
        def concept_coupling_half_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5277.ConceptCouplingHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5277,
            )

            return self._parent._cast(
                _5277.ConceptCouplingHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def concept_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5278.ConceptGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5278,
            )

            return self._parent._cast(_5278.ConceptGearCompoundModalAnalysisAtASpeed)

        @property
        def concept_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5280.ConceptGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5280,
            )

            return self._parent._cast(_5280.ConceptGearSetCompoundModalAnalysisAtASpeed)

        @property
        def conical_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5281.ConicalGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5281,
            )

            return self._parent._cast(_5281.ConicalGearCompoundModalAnalysisAtASpeed)

        @property
        def conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5283.ConicalGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5283,
            )

            return self._parent._cast(_5283.ConicalGearSetCompoundModalAnalysisAtASpeed)

        @property
        def connector_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5285.ConnectorCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5285,
            )

            return self._parent._cast(_5285.ConnectorCompoundModalAnalysisAtASpeed)

        @property
        def coupling_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5286.CouplingCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5286,
            )

            return self._parent._cast(_5286.CouplingCompoundModalAnalysisAtASpeed)

        @property
        def coupling_half_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5288.CouplingHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5288,
            )

            return self._parent._cast(_5288.CouplingHalfCompoundModalAnalysisAtASpeed)

        @property
        def cvt_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5290.CVTCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5290,
            )

            return self._parent._cast(_5290.CVTCompoundModalAnalysisAtASpeed)

        @property
        def cvt_pulley_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5291.CVTPulleyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5291,
            )

            return self._parent._cast(_5291.CVTPulleyCompoundModalAnalysisAtASpeed)

        @property
        def cycloidal_assembly_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5292.CycloidalAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5292,
            )

            return self._parent._cast(
                _5292.CycloidalAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def cycloidal_disc_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5294.CycloidalDiscCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5294,
            )

            return self._parent._cast(_5294.CycloidalDiscCompoundModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5296.CylindricalGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5296,
            )

            return self._parent._cast(
                _5296.CylindricalGearCompoundModalAnalysisAtASpeed
            )

        @property
        def cylindrical_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5298.CylindricalGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5298,
            )

            return self._parent._cast(
                _5298.CylindricalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def cylindrical_planet_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5299.CylindricalPlanetGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5299,
            )

            return self._parent._cast(
                _5299.CylindricalPlanetGearCompoundModalAnalysisAtASpeed
            )

        @property
        def datum_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5300.DatumCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5300,
            )

            return self._parent._cast(_5300.DatumCompoundModalAnalysisAtASpeed)

        @property
        def external_cad_model_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5301.ExternalCADModelCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5301,
            )

            return self._parent._cast(
                _5301.ExternalCADModelCompoundModalAnalysisAtASpeed
            )

        @property
        def face_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5302.FaceGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5302,
            )

            return self._parent._cast(_5302.FaceGearCompoundModalAnalysisAtASpeed)

        @property
        def face_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5304.FaceGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5304,
            )

            return self._parent._cast(_5304.FaceGearSetCompoundModalAnalysisAtASpeed)

        @property
        def fe_part_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5305.FEPartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5305,
            )

            return self._parent._cast(_5305.FEPartCompoundModalAnalysisAtASpeed)

        @property
        def flexible_pin_assembly_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5306.FlexiblePinAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5306,
            )

            return self._parent._cast(
                _5306.FlexiblePinAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5307.GearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5307,
            )

            return self._parent._cast(_5307.GearCompoundModalAnalysisAtASpeed)

        @property
        def gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5309.GearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5309,
            )

            return self._parent._cast(_5309.GearSetCompoundModalAnalysisAtASpeed)

        @property
        def guide_dxf_model_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5310.GuideDxfModelCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5310,
            )

            return self._parent._cast(_5310.GuideDxfModelCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5311.HypoidGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5311,
            )

            return self._parent._cast(_5311.HypoidGearCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5313.HypoidGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5313,
            )

            return self._parent._cast(_5313.HypoidGearSetCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5315.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5315,
            )

            return self._parent._cast(
                _5315.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_5317.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5317,
            )

            return self._parent._cast(
                _5317.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5318.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5318,
            )

            return self._parent._cast(
                _5318.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5320.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5320,
            )

            return self._parent._cast(
                _5320.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_5321.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5321,
            )

            return self._parent._cast(
                _5321.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5323.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5323,
            )

            return self._parent._cast(
                _5323.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def mass_disc_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5324.MassDiscCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5324,
            )

            return self._parent._cast(_5324.MassDiscCompoundModalAnalysisAtASpeed)

        @property
        def measurement_component_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5325.MeasurementComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5325,
            )

            return self._parent._cast(
                _5325.MeasurementComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5326.MountableComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5326,
            )

            return self._parent._cast(
                _5326.MountableComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def oil_seal_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5327.OilSealCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5327,
            )

            return self._parent._cast(_5327.OilSealCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5328.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5328,
            )

            return self._parent._cast(_5328.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_to_part_shear_coupling_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5329.PartToPartShearCouplingCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5329,
            )

            return self._parent._cast(
                _5329.PartToPartShearCouplingCompoundModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5331.PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5331,
            )

            return self._parent._cast(
                _5331.PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def planetary_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5333.PlanetaryGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5333,
            )

            return self._parent._cast(
                _5333.PlanetaryGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def planet_carrier_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5334.PlanetCarrierCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5334,
            )

            return self._parent._cast(_5334.PlanetCarrierCompoundModalAnalysisAtASpeed)

        @property
        def point_load_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5335.PointLoadCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5335,
            )

            return self._parent._cast(_5335.PointLoadCompoundModalAnalysisAtASpeed)

        @property
        def power_load_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5336.PowerLoadCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5336,
            )

            return self._parent._cast(_5336.PowerLoadCompoundModalAnalysisAtASpeed)

        @property
        def pulley_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5337.PulleyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5337,
            )

            return self._parent._cast(_5337.PulleyCompoundModalAnalysisAtASpeed)

        @property
        def ring_pins_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5338.RingPinsCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5338,
            )

            return self._parent._cast(_5338.RingPinsCompoundModalAnalysisAtASpeed)

        @property
        def rolling_ring_assembly_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5340.RollingRingAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5340,
            )

            return self._parent._cast(
                _5340.RollingRingAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def rolling_ring_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5341.RollingRingCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5341,
            )

            return self._parent._cast(_5341.RollingRingCompoundModalAnalysisAtASpeed)

        @property
        def root_assembly_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5343.RootAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5343,
            )

            return self._parent._cast(_5343.RootAssemblyCompoundModalAnalysisAtASpeed)

        @property
        def shaft_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5344.ShaftCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5344,
            )

            return self._parent._cast(_5344.ShaftCompoundModalAnalysisAtASpeed)

        @property
        def shaft_hub_connection_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5345.ShaftHubConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5345,
            )

            return self._parent._cast(
                _5345.ShaftHubConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5347.SpecialisedAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5347,
            )

            return self._parent._cast(
                _5347.SpecialisedAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5348.SpiralBevelGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5348,
            )

            return self._parent._cast(
                _5348.SpiralBevelGearCompoundModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5350.SpiralBevelGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5350,
            )

            return self._parent._cast(
                _5350.SpiralBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def spring_damper_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5351.SpringDamperCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5351,
            )

            return self._parent._cast(_5351.SpringDamperCompoundModalAnalysisAtASpeed)

        @property
        def spring_damper_half_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5353.SpringDamperHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5353,
            )

            return self._parent._cast(
                _5353.SpringDamperHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_diff_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5354.StraightBevelDiffGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5354,
            )

            return self._parent._cast(
                _5354.StraightBevelDiffGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5356.StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5356,
            )

            return self._parent._cast(
                _5356.StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5357.StraightBevelGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5357,
            )

            return self._parent._cast(
                _5357.StraightBevelGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5359.StraightBevelGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5359,
            )

            return self._parent._cast(
                _5359.StraightBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_planet_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5360.StraightBevelPlanetGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5360,
            )

            return self._parent._cast(
                _5360.StraightBevelPlanetGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5361.StraightBevelSunGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5361,
            )

            return self._parent._cast(
                _5361.StraightBevelSunGearCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5362.SynchroniserCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5362,
            )

            return self._parent._cast(_5362.SynchroniserCompoundModalAnalysisAtASpeed)

        @property
        def synchroniser_half_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5363.SynchroniserHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5363,
            )

            return self._parent._cast(
                _5363.SynchroniserHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_part_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5364.SynchroniserPartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5364,
            )

            return self._parent._cast(
                _5364.SynchroniserPartCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_sleeve_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5365.SynchroniserSleeveCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5365,
            )

            return self._parent._cast(
                _5365.SynchroniserSleeveCompoundModalAnalysisAtASpeed
            )

        @property
        def torque_converter_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5366.TorqueConverterCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5366,
            )

            return self._parent._cast(
                _5366.TorqueConverterCompoundModalAnalysisAtASpeed
            )

        @property
        def torque_converter_pump_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5368.TorqueConverterPumpCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5368,
            )

            return self._parent._cast(
                _5368.TorqueConverterPumpCompoundModalAnalysisAtASpeed
            )

        @property
        def torque_converter_turbine_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5369.TorqueConverterTurbineCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5369,
            )

            return self._parent._cast(
                _5369.TorqueConverterTurbineCompoundModalAnalysisAtASpeed
            )

        @property
        def unbalanced_mass_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5370.UnbalancedMassCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5370,
            )

            return self._parent._cast(_5370.UnbalancedMassCompoundModalAnalysisAtASpeed)

        @property
        def virtual_component_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5371.VirtualComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5371,
            )

            return self._parent._cast(
                _5371.VirtualComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def worm_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5372.WormGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5372,
            )

            return self._parent._cast(_5372.WormGearCompoundModalAnalysisAtASpeed)

        @property
        def worm_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5374.WormGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5374,
            )

            return self._parent._cast(_5374.WormGearSetCompoundModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5375.ZerolBevelGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5375,
            )

            return self._parent._cast(_5375.ZerolBevelGearCompoundModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5377.ZerolBevelGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5377,
            )

            return self._parent._cast(
                _5377.ZerolBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5531.AbstractAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5531,
            )

            return self._parent._cast(
                _5531.AbstractAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_shaft_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5532.AbstractShaftCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5532,
            )

            return self._parent._cast(
                _5532.AbstractShaftCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_shaft_or_housing_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5533.AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5533,
            )

            return self._parent._cast(
                _5533.AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5535.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5535,
            )

            return self._parent._cast(
                _5535.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5537.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5537,
            )

            return self._parent._cast(
                _5537.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def assembly_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5538.AssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5538,
            )

            return self._parent._cast(_5538.AssemblyCompoundMultibodyDynamicsAnalysis)

        @property
        def bearing_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5539.BearingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5539,
            )

            return self._parent._cast(_5539.BearingCompoundMultibodyDynamicsAnalysis)

        @property
        def belt_drive_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5541.BeltDriveCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5541,
            )

            return self._parent._cast(_5541.BeltDriveCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5542.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5542,
            )

            return self._parent._cast(
                _5542.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5544.BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5544,
            )

            return self._parent._cast(
                _5544.BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5545.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5545,
            )

            return self._parent._cast(
                _5545.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5546.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5546,
            )

            return self._parent._cast(
                _5546.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5547.BevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5547,
            )

            return self._parent._cast(_5547.BevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5549.BevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5549,
            )

            return self._parent._cast(
                _5549.BevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bolt_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5550.BoltCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5550,
            )

            return self._parent._cast(_5550.BoltCompoundMultibodyDynamicsAnalysis)

        @property
        def bolted_joint_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5551.BoltedJointCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5551,
            )

            return self._parent._cast(
                _5551.BoltedJointCompoundMultibodyDynamicsAnalysis
            )

        @property
        def clutch_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5552.ClutchCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5552,
            )

            return self._parent._cast(_5552.ClutchCompoundMultibodyDynamicsAnalysis)

        @property
        def clutch_half_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5554.ClutchHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5554,
            )

            return self._parent._cast(_5554.ClutchHalfCompoundMultibodyDynamicsAnalysis)

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5556.ComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5556,
            )

            return self._parent._cast(_5556.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5557.ConceptCouplingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5557,
            )

            return self._parent._cast(
                _5557.ConceptCouplingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_coupling_half_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5559.ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5559,
            )

            return self._parent._cast(
                _5559.ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5560.ConceptGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5560,
            )

            return self._parent._cast(
                _5560.ConceptGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5562.ConceptGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5562,
            )

            return self._parent._cast(
                _5562.ConceptGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5563.ConicalGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5563,
            )

            return self._parent._cast(
                _5563.ConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5565.ConicalGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5565,
            )

            return self._parent._cast(
                _5565.ConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def connector_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5567.ConnectorCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5567,
            )

            return self._parent._cast(_5567.ConnectorCompoundMultibodyDynamicsAnalysis)

        @property
        def coupling_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5568.CouplingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5568,
            )

            return self._parent._cast(_5568.CouplingCompoundMultibodyDynamicsAnalysis)

        @property
        def coupling_half_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5570.CouplingHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5570,
            )

            return self._parent._cast(
                _5570.CouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cvt_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5572.CVTCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5572,
            )

            return self._parent._cast(_5572.CVTCompoundMultibodyDynamicsAnalysis)

        @property
        def cvt_pulley_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5573.CVTPulleyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5573,
            )

            return self._parent._cast(_5573.CVTPulleyCompoundMultibodyDynamicsAnalysis)

        @property
        def cycloidal_assembly_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5574.CycloidalAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5574,
            )

            return self._parent._cast(
                _5574.CycloidalAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cycloidal_disc_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5576.CycloidalDiscCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5576,
            )

            return self._parent._cast(
                _5576.CycloidalDiscCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5578.CylindricalGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5578,
            )

            return self._parent._cast(
                _5578.CylindricalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5580.CylindricalGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5580,
            )

            return self._parent._cast(
                _5580.CylindricalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_planet_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5581.CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5581,
            )

            return self._parent._cast(
                _5581.CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def datum_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5582.DatumCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5582,
            )

            return self._parent._cast(_5582.DatumCompoundMultibodyDynamicsAnalysis)

        @property
        def external_cad_model_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5583.ExternalCADModelCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5583,
            )

            return self._parent._cast(
                _5583.ExternalCADModelCompoundMultibodyDynamicsAnalysis
            )

        @property
        def face_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5584.FaceGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5584,
            )

            return self._parent._cast(_5584.FaceGearCompoundMultibodyDynamicsAnalysis)

        @property
        def face_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5586.FaceGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5586,
            )

            return self._parent._cast(
                _5586.FaceGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def fe_part_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5587.FEPartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5587,
            )

            return self._parent._cast(_5587.FEPartCompoundMultibodyDynamicsAnalysis)

        @property
        def flexible_pin_assembly_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5588.FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5588,
            )

            return self._parent._cast(
                _5588.FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5589.GearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5589,
            )

            return self._parent._cast(_5589.GearCompoundMultibodyDynamicsAnalysis)

        @property
        def gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5591.GearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5591,
            )

            return self._parent._cast(_5591.GearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def guide_dxf_model_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5592.GuideDxfModelCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5592,
            )

            return self._parent._cast(
                _5592.GuideDxfModelCompoundMultibodyDynamicsAnalysis
            )

        @property
        def hypoid_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5593.HypoidGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5593,
            )

            return self._parent._cast(_5593.HypoidGearCompoundMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5595.HypoidGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5595,
            )

            return self._parent._cast(
                _5595.HypoidGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_5597.KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5597,
            )

            return self._parent._cast(
                _5597.KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5599.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5599,
            )

            return self._parent._cast(
                _5599.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_5600.KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5600,
            )

            return self._parent._cast(
                _5600.KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5602.KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5602,
            )

            return self._parent._cast(
                _5602.KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5603.KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5603,
            )

            return self._parent._cast(
                _5603.KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5605.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5605,
            )

            return self._parent._cast(
                _5605.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def mass_disc_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5606.MassDiscCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5606,
            )

            return self._parent._cast(_5606.MassDiscCompoundMultibodyDynamicsAnalysis)

        @property
        def measurement_component_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5607.MeasurementComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5607,
            )

            return self._parent._cast(
                _5607.MeasurementComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5608.MountableComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5608,
            )

            return self._parent._cast(
                _5608.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def oil_seal_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5609.OilSealCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5609,
            )

            return self._parent._cast(_5609.OilSealCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5610.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5610,
            )

            return self._parent._cast(_5610.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5611.PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5611,
            )

            return self._parent._cast(
                _5611.PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5613.PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5613,
            )

            return self._parent._cast(
                _5613.PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def planetary_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5615.PlanetaryGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5615,
            )

            return self._parent._cast(
                _5615.PlanetaryGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def planet_carrier_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5616.PlanetCarrierCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5616,
            )

            return self._parent._cast(
                _5616.PlanetCarrierCompoundMultibodyDynamicsAnalysis
            )

        @property
        def point_load_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5617.PointLoadCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5617,
            )

            return self._parent._cast(_5617.PointLoadCompoundMultibodyDynamicsAnalysis)

        @property
        def power_load_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5618.PowerLoadCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5618,
            )

            return self._parent._cast(_5618.PowerLoadCompoundMultibodyDynamicsAnalysis)

        @property
        def pulley_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5619.PulleyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5619,
            )

            return self._parent._cast(_5619.PulleyCompoundMultibodyDynamicsAnalysis)

        @property
        def ring_pins_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5620.RingPinsCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5620,
            )

            return self._parent._cast(_5620.RingPinsCompoundMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_assembly_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5622.RollingRingAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5622,
            )

            return self._parent._cast(
                _5622.RollingRingAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def rolling_ring_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5623.RollingRingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5623,
            )

            return self._parent._cast(
                _5623.RollingRingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def root_assembly_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5625.RootAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5625,
            )

            return self._parent._cast(
                _5625.RootAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def shaft_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5626.ShaftCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5626,
            )

            return self._parent._cast(_5626.ShaftCompoundMultibodyDynamicsAnalysis)

        @property
        def shaft_hub_connection_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5627.ShaftHubConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5627,
            )

            return self._parent._cast(
                _5627.ShaftHubConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5629.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5629,
            )

            return self._parent._cast(
                _5629.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5630.SpiralBevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5630,
            )

            return self._parent._cast(
                _5630.SpiralBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5632.SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5632,
            )

            return self._parent._cast(
                _5632.SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5633.SpringDamperCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5633,
            )

            return self._parent._cast(
                _5633.SpringDamperCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_half_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5635.SpringDamperHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5635,
            )

            return self._parent._cast(
                _5635.SpringDamperHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5636.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5636,
            )

            return self._parent._cast(
                _5636.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5638.StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5638,
            )

            return self._parent._cast(
                _5638.StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5639.StraightBevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5639,
            )

            return self._parent._cast(
                _5639.StraightBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5641.StraightBevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5641,
            )

            return self._parent._cast(
                _5641.StraightBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5642.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5642,
            )

            return self._parent._cast(
                _5642.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5643.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5643,
            )

            return self._parent._cast(
                _5643.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5644.SynchroniserCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5644,
            )

            return self._parent._cast(
                _5644.SynchroniserCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_half_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5645.SynchroniserHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5645,
            )

            return self._parent._cast(
                _5645.SynchroniserHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_part_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5646.SynchroniserPartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5646,
            )

            return self._parent._cast(
                _5646.SynchroniserPartCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_sleeve_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5647.SynchroniserSleeveCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5647,
            )

            return self._parent._cast(
                _5647.SynchroniserSleeveCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5648.TorqueConverterCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5648,
            )

            return self._parent._cast(
                _5648.TorqueConverterCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_pump_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5650.TorqueConverterPumpCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5650,
            )

            return self._parent._cast(
                _5650.TorqueConverterPumpCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_turbine_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5651.TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5651,
            )

            return self._parent._cast(
                _5651.TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis
            )

        @property
        def unbalanced_mass_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5652.UnbalancedMassCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5652,
            )

            return self._parent._cast(
                _5652.UnbalancedMassCompoundMultibodyDynamicsAnalysis
            )

        @property
        def virtual_component_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5653.VirtualComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5653,
            )

            return self._parent._cast(
                _5653.VirtualComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def worm_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5654.WormGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5654,
            )

            return self._parent._cast(_5654.WormGearCompoundMultibodyDynamicsAnalysis)

        @property
        def worm_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5656.WormGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5656,
            )

            return self._parent._cast(
                _5656.WormGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5657.ZerolBevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5657,
            )

            return self._parent._cast(
                _5657.ZerolBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5659.ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5659,
            )

            return self._parent._cast(
                _5659.ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5881.AbstractAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5881,
            )

            return self._parent._cast(_5881.AbstractAssemblyCompoundHarmonicAnalysis)

        @property
        def abstract_shaft_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5882.AbstractShaftCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5882,
            )

            return self._parent._cast(_5882.AbstractShaftCompoundHarmonicAnalysis)

        @property
        def abstract_shaft_or_housing_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5883.AbstractShaftOrHousingCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5883,
            )

            return self._parent._cast(
                _5883.AbstractShaftOrHousingCompoundHarmonicAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5885.AGMAGleasonConicalGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5885,
            )

            return self._parent._cast(
                _5885.AGMAGleasonConicalGearCompoundHarmonicAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5887.AGMAGleasonConicalGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5887,
            )

            return self._parent._cast(
                _5887.AGMAGleasonConicalGearSetCompoundHarmonicAnalysis
            )

        @property
        def assembly_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5888.AssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5888,
            )

            return self._parent._cast(_5888.AssemblyCompoundHarmonicAnalysis)

        @property
        def bearing_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5889.BearingCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5889,
            )

            return self._parent._cast(_5889.BearingCompoundHarmonicAnalysis)

        @property
        def belt_drive_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5891.BeltDriveCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5891,
            )

            return self._parent._cast(_5891.BeltDriveCompoundHarmonicAnalysis)

        @property
        def bevel_differential_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5892.BevelDifferentialGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5892,
            )

            return self._parent._cast(
                _5892.BevelDifferentialGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5894.BevelDifferentialGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5894,
            )

            return self._parent._cast(
                _5894.BevelDifferentialGearSetCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5895.BevelDifferentialPlanetGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5895,
            )

            return self._parent._cast(
                _5895.BevelDifferentialPlanetGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5896.BevelDifferentialSunGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5896,
            )

            return self._parent._cast(
                _5896.BevelDifferentialSunGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5897.BevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5897,
            )

            return self._parent._cast(_5897.BevelGearCompoundHarmonicAnalysis)

        @property
        def bevel_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5899.BevelGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5899,
            )

            return self._parent._cast(_5899.BevelGearSetCompoundHarmonicAnalysis)

        @property
        def bolt_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5900.BoltCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5900,
            )

            return self._parent._cast(_5900.BoltCompoundHarmonicAnalysis)

        @property
        def bolted_joint_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5901.BoltedJointCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5901,
            )

            return self._parent._cast(_5901.BoltedJointCompoundHarmonicAnalysis)

        @property
        def clutch_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5902.ClutchCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5902,
            )

            return self._parent._cast(_5902.ClutchCompoundHarmonicAnalysis)

        @property
        def clutch_half_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5904.ClutchHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5904,
            )

            return self._parent._cast(_5904.ClutchHalfCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5906.ComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5906,
            )

            return self._parent._cast(_5906.ComponentCompoundHarmonicAnalysis)

        @property
        def concept_coupling_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5907.ConceptCouplingCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5907,
            )

            return self._parent._cast(_5907.ConceptCouplingCompoundHarmonicAnalysis)

        @property
        def concept_coupling_half_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5909.ConceptCouplingHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5909,
            )

            return self._parent._cast(_5909.ConceptCouplingHalfCompoundHarmonicAnalysis)

        @property
        def concept_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5910.ConceptGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5910,
            )

            return self._parent._cast(_5910.ConceptGearCompoundHarmonicAnalysis)

        @property
        def concept_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5912.ConceptGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5912,
            )

            return self._parent._cast(_5912.ConceptGearSetCompoundHarmonicAnalysis)

        @property
        def conical_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5913.ConicalGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5913,
            )

            return self._parent._cast(_5913.ConicalGearCompoundHarmonicAnalysis)

        @property
        def conical_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5915.ConicalGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5915,
            )

            return self._parent._cast(_5915.ConicalGearSetCompoundHarmonicAnalysis)

        @property
        def connector_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5917.ConnectorCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5917,
            )

            return self._parent._cast(_5917.ConnectorCompoundHarmonicAnalysis)

        @property
        def coupling_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5918.CouplingCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5918,
            )

            return self._parent._cast(_5918.CouplingCompoundHarmonicAnalysis)

        @property
        def coupling_half_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5920.CouplingHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5920,
            )

            return self._parent._cast(_5920.CouplingHalfCompoundHarmonicAnalysis)

        @property
        def cvt_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5922.CVTCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5922,
            )

            return self._parent._cast(_5922.CVTCompoundHarmonicAnalysis)

        @property
        def cvt_pulley_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5923.CVTPulleyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5923,
            )

            return self._parent._cast(_5923.CVTPulleyCompoundHarmonicAnalysis)

        @property
        def cycloidal_assembly_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5924.CycloidalAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5924,
            )

            return self._parent._cast(_5924.CycloidalAssemblyCompoundHarmonicAnalysis)

        @property
        def cycloidal_disc_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5926.CycloidalDiscCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5926,
            )

            return self._parent._cast(_5926.CycloidalDiscCompoundHarmonicAnalysis)

        @property
        def cylindrical_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5928.CylindricalGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5928,
            )

            return self._parent._cast(_5928.CylindricalGearCompoundHarmonicAnalysis)

        @property
        def cylindrical_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5930.CylindricalGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5930,
            )

            return self._parent._cast(_5930.CylindricalGearSetCompoundHarmonicAnalysis)

        @property
        def cylindrical_planet_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5931.CylindricalPlanetGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5931,
            )

            return self._parent._cast(
                _5931.CylindricalPlanetGearCompoundHarmonicAnalysis
            )

        @property
        def datum_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5932.DatumCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5932,
            )

            return self._parent._cast(_5932.DatumCompoundHarmonicAnalysis)

        @property
        def external_cad_model_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5933.ExternalCADModelCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5933,
            )

            return self._parent._cast(_5933.ExternalCADModelCompoundHarmonicAnalysis)

        @property
        def face_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5934.FaceGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5934,
            )

            return self._parent._cast(_5934.FaceGearCompoundHarmonicAnalysis)

        @property
        def face_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5936.FaceGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5936,
            )

            return self._parent._cast(_5936.FaceGearSetCompoundHarmonicAnalysis)

        @property
        def fe_part_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5937.FEPartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5937,
            )

            return self._parent._cast(_5937.FEPartCompoundHarmonicAnalysis)

        @property
        def flexible_pin_assembly_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5938.FlexiblePinAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5938,
            )

            return self._parent._cast(_5938.FlexiblePinAssemblyCompoundHarmonicAnalysis)

        @property
        def gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5939.GearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5939,
            )

            return self._parent._cast(_5939.GearCompoundHarmonicAnalysis)

        @property
        def gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5941.GearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5941,
            )

            return self._parent._cast(_5941.GearSetCompoundHarmonicAnalysis)

        @property
        def guide_dxf_model_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5942.GuideDxfModelCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5942,
            )

            return self._parent._cast(_5942.GuideDxfModelCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5943.HypoidGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5943,
            )

            return self._parent._cast(_5943.HypoidGearCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5945.HypoidGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5945,
            )

            return self._parent._cast(_5945.HypoidGearSetCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5947.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5947,
            )

            return self._parent._cast(
                _5947.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5949.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5949,
            )

            return self._parent._cast(
                _5949.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5950.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5950,
            )

            return self._parent._cast(
                _5950.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5952.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5952,
            )

            return self._parent._cast(
                _5952.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5953.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5953,
            )

            return self._parent._cast(
                _5953.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5955.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5955,
            )

            return self._parent._cast(
                _5955.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis
            )

        @property
        def mass_disc_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5956.MassDiscCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5956,
            )

            return self._parent._cast(_5956.MassDiscCompoundHarmonicAnalysis)

        @property
        def measurement_component_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5957.MeasurementComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5957,
            )

            return self._parent._cast(
                _5957.MeasurementComponentCompoundHarmonicAnalysis
            )

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5958.MountableComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5958,
            )

            return self._parent._cast(_5958.MountableComponentCompoundHarmonicAnalysis)

        @property
        def oil_seal_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5959.OilSealCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5959,
            )

            return self._parent._cast(_5959.OilSealCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5960.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5960,
            )

            return self._parent._cast(_5960.PartCompoundHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5961.PartToPartShearCouplingCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5961,
            )

            return self._parent._cast(
                _5961.PartToPartShearCouplingCompoundHarmonicAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5963.PartToPartShearCouplingHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5963,
            )

            return self._parent._cast(
                _5963.PartToPartShearCouplingHalfCompoundHarmonicAnalysis
            )

        @property
        def planetary_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5965.PlanetaryGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5965,
            )

            return self._parent._cast(_5965.PlanetaryGearSetCompoundHarmonicAnalysis)

        @property
        def planet_carrier_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5966.PlanetCarrierCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5966,
            )

            return self._parent._cast(_5966.PlanetCarrierCompoundHarmonicAnalysis)

        @property
        def point_load_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5967.PointLoadCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5967,
            )

            return self._parent._cast(_5967.PointLoadCompoundHarmonicAnalysis)

        @property
        def power_load_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5968.PowerLoadCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5968,
            )

            return self._parent._cast(_5968.PowerLoadCompoundHarmonicAnalysis)

        @property
        def pulley_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5969.PulleyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5969,
            )

            return self._parent._cast(_5969.PulleyCompoundHarmonicAnalysis)

        @property
        def ring_pins_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5970.RingPinsCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5970,
            )

            return self._parent._cast(_5970.RingPinsCompoundHarmonicAnalysis)

        @property
        def rolling_ring_assembly_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5972.RollingRingAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5972,
            )

            return self._parent._cast(_5972.RollingRingAssemblyCompoundHarmonicAnalysis)

        @property
        def rolling_ring_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5973.RollingRingCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5973,
            )

            return self._parent._cast(_5973.RollingRingCompoundHarmonicAnalysis)

        @property
        def root_assembly_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5975.RootAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5975,
            )

            return self._parent._cast(_5975.RootAssemblyCompoundHarmonicAnalysis)

        @property
        def shaft_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5976.ShaftCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5976,
            )

            return self._parent._cast(_5976.ShaftCompoundHarmonicAnalysis)

        @property
        def shaft_hub_connection_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5977.ShaftHubConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5977,
            )

            return self._parent._cast(_5977.ShaftHubConnectionCompoundHarmonicAnalysis)

        @property
        def specialised_assembly_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5979.SpecialisedAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5979,
            )

            return self._parent._cast(_5979.SpecialisedAssemblyCompoundHarmonicAnalysis)

        @property
        def spiral_bevel_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5980.SpiralBevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5980,
            )

            return self._parent._cast(_5980.SpiralBevelGearCompoundHarmonicAnalysis)

        @property
        def spiral_bevel_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5982.SpiralBevelGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5982,
            )

            return self._parent._cast(_5982.SpiralBevelGearSetCompoundHarmonicAnalysis)

        @property
        def spring_damper_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5983.SpringDamperCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5983,
            )

            return self._parent._cast(_5983.SpringDamperCompoundHarmonicAnalysis)

        @property
        def spring_damper_half_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5985.SpringDamperHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5985,
            )

            return self._parent._cast(_5985.SpringDamperHalfCompoundHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5986.StraightBevelDiffGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5986,
            )

            return self._parent._cast(
                _5986.StraightBevelDiffGearCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5988.StraightBevelDiffGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5988,
            )

            return self._parent._cast(
                _5988.StraightBevelDiffGearSetCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5989.StraightBevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5989,
            )

            return self._parent._cast(_5989.StraightBevelGearCompoundHarmonicAnalysis)

        @property
        def straight_bevel_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5991.StraightBevelGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5991,
            )

            return self._parent._cast(
                _5991.StraightBevelGearSetCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5992.StraightBevelPlanetGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5992,
            )

            return self._parent._cast(
                _5992.StraightBevelPlanetGearCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5993.StraightBevelSunGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5993,
            )

            return self._parent._cast(
                _5993.StraightBevelSunGearCompoundHarmonicAnalysis
            )

        @property
        def synchroniser_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5994.SynchroniserCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5994,
            )

            return self._parent._cast(_5994.SynchroniserCompoundHarmonicAnalysis)

        @property
        def synchroniser_half_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5995.SynchroniserHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5995,
            )

            return self._parent._cast(_5995.SynchroniserHalfCompoundHarmonicAnalysis)

        @property
        def synchroniser_part_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5996.SynchroniserPartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5996,
            )

            return self._parent._cast(_5996.SynchroniserPartCompoundHarmonicAnalysis)

        @property
        def synchroniser_sleeve_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5997.SynchroniserSleeveCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5997,
            )

            return self._parent._cast(_5997.SynchroniserSleeveCompoundHarmonicAnalysis)

        @property
        def torque_converter_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_5998.TorqueConverterCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5998,
            )

            return self._parent._cast(_5998.TorqueConverterCompoundHarmonicAnalysis)

        @property
        def torque_converter_pump_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6000.TorqueConverterPumpCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6000,
            )

            return self._parent._cast(_6000.TorqueConverterPumpCompoundHarmonicAnalysis)

        @property
        def torque_converter_turbine_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6001.TorqueConverterTurbineCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6001,
            )

            return self._parent._cast(
                _6001.TorqueConverterTurbineCompoundHarmonicAnalysis
            )

        @property
        def unbalanced_mass_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6002.UnbalancedMassCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6002,
            )

            return self._parent._cast(_6002.UnbalancedMassCompoundHarmonicAnalysis)

        @property
        def virtual_component_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6003.VirtualComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6003,
            )

            return self._parent._cast(_6003.VirtualComponentCompoundHarmonicAnalysis)

        @property
        def worm_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6004.WormGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6004,
            )

            return self._parent._cast(_6004.WormGearCompoundHarmonicAnalysis)

        @property
        def worm_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6006.WormGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6006,
            )

            return self._parent._cast(_6006.WormGearSetCompoundHarmonicAnalysis)

        @property
        def zerol_bevel_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6007.ZerolBevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6007,
            )

            return self._parent._cast(_6007.ZerolBevelGearCompoundHarmonicAnalysis)

        @property
        def zerol_bevel_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6009.ZerolBevelGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6009,
            )

            return self._parent._cast(_6009.ZerolBevelGearSetCompoundHarmonicAnalysis)

        @property
        def abstract_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6141.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6141,
            )

            return self._parent._cast(
                _6141.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6142.AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6142,
            )

            return self._parent._cast(
                _6142.AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_or_housing_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6143.AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6143,
            )

            return self._parent._cast(
                _6143.AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6145.AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6145,
            )

            return self._parent._cast(
                _6145.AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_6147.AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6147,
            )

            return self._parent._cast(
                _6147.AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def assembly_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6148.AssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6148,
            )

            return self._parent._cast(
                _6148.AssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bearing_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6149.BearingCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6149,
            )

            return self._parent._cast(
                _6149.BearingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def belt_drive_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6151.BeltDriveCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6151,
            )

            return self._parent._cast(
                _6151.BeltDriveCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6152.BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6152,
            )

            return self._parent._cast(
                _6152.BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6154.BevelDifferentialGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6154,
            )

            return self._parent._cast(
                _6154.BevelDifferentialGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_planet_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6155.BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6155,
            )

            return self._parent._cast(
                _6155.BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_sun_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6156.BevelDifferentialSunGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6156,
            )

            return self._parent._cast(
                _6156.BevelDifferentialSunGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6157.BevelGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6157,
            )

            return self._parent._cast(
                _6157.BevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6159.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6159,
            )

            return self._parent._cast(
                _6159.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bolt_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6160.BoltCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6160,
            )

            return self._parent._cast(
                _6160.BoltCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bolted_joint_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6161.BoltedJointCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6161,
            )

            return self._parent._cast(
                _6161.BoltedJointCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def clutch_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6162.ClutchCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6162,
            )

            return self._parent._cast(
                _6162.ClutchCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def clutch_half_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6164.ClutchHalfCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6164,
            )

            return self._parent._cast(
                _6164.ClutchHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6166.ComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6166,
            )

            return self._parent._cast(
                _6166.ComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6167.ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6167,
            )

            return self._parent._cast(
                _6167.ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_half_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6169.ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6169,
            )

            return self._parent._cast(
                _6169.ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6170.ConceptGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6170,
            )

            return self._parent._cast(
                _6170.ConceptGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6172.ConceptGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6172,
            )

            return self._parent._cast(
                _6172.ConceptGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6173.ConicalGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6173,
            )

            return self._parent._cast(
                _6173.ConicalGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6175.ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6175,
            )

            return self._parent._cast(
                _6175.ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connector_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6177.ConnectorCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6177,
            )

            return self._parent._cast(
                _6177.ConnectorCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6178.CouplingCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6178,
            )

            return self._parent._cast(
                _6178.CouplingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_half_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6180.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6180,
            )

            return self._parent._cast(
                _6180.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cvt_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6182.CVTCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6182,
            )

            return self._parent._cast(
                _6182.CVTCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cvt_pulley_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6183.CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6183,
            )

            return self._parent._cast(
                _6183.CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6184.CycloidalAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6184,
            )

            return self._parent._cast(
                _6184.CycloidalAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6186.CycloidalDiscCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6186,
            )

            return self._parent._cast(
                _6186.CycloidalDiscCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6188.CylindricalGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6188,
            )

            return self._parent._cast(
                _6188.CylindricalGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6190.CylindricalGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6190,
            )

            return self._parent._cast(
                _6190.CylindricalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_planet_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6191.CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6191,
            )

            return self._parent._cast(
                _6191.CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def datum_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6192.DatumCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6192,
            )

            return self._parent._cast(
                _6192.DatumCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def external_cad_model_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6193.ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6193,
            )

            return self._parent._cast(
                _6193.ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6194.FaceGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6194,
            )

            return self._parent._cast(
                _6194.FaceGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6196.FaceGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6196,
            )

            return self._parent._cast(
                _6196.FaceGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def fe_part_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6197.FEPartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6197,
            )

            return self._parent._cast(
                _6197.FEPartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def flexible_pin_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6198.FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6198,
            )

            return self._parent._cast(
                _6198.FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6199.GearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6199,
            )

            return self._parent._cast(
                _6199.GearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6201.GearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6201,
            )

            return self._parent._cast(
                _6201.GearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def guide_dxf_model_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6202.GuideDxfModelCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6202,
            )

            return self._parent._cast(
                _6202.GuideDxfModelCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6203.HypoidGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6203,
            )

            return self._parent._cast(
                _6203.HypoidGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6205.HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6205,
            )

            return self._parent._cast(
                _6205.HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6207.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6207,
            )

            return self._parent._cast(
                _6207.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6209.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6209,
            )

            return self._parent._cast(
                _6209.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6210.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6210,
            )

            return self._parent._cast(
                _6210.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6212.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6212,
            )

            return self._parent._cast(
                _6212.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6213.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6213,
            )

            return self._parent._cast(
                _6213.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6215.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6215,
            )

            return self._parent._cast(
                _6215.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mass_disc_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6216.MassDiscCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6216,
            )

            return self._parent._cast(
                _6216.MassDiscCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def measurement_component_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6217.MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6217,
            )

            return self._parent._cast(
                _6217.MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6218.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6218,
            )

            return self._parent._cast(
                _6218.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def oil_seal_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6219.OilSealCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6219,
            )

            return self._parent._cast(
                _6219.OilSealCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6220.PartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6220,
            )

            return self._parent._cast(
                _6220.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6221.PartToPartShearCouplingCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6221,
            )

            return self._parent._cast(
                _6221.PartToPartShearCouplingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_half_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6223.PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6223,
            )

            return self._parent._cast(
                _6223.PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planetary_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6225.PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6225,
            )

            return self._parent._cast(
                _6225.PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planet_carrier_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6226.PlanetCarrierCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6226,
            )

            return self._parent._cast(
                _6226.PlanetCarrierCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def point_load_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6227.PointLoadCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6227,
            )

            return self._parent._cast(
                _6227.PointLoadCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def power_load_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6228.PowerLoadCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6228,
            )

            return self._parent._cast(
                _6228.PowerLoadCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def pulley_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6229.PulleyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6229,
            )

            return self._parent._cast(
                _6229.PulleyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def ring_pins_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6230.RingPinsCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6230,
            )

            return self._parent._cast(
                _6230.RingPinsCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6232.RollingRingAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6232,
            )

            return self._parent._cast(
                _6232.RollingRingAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6233.RollingRingCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6233,
            )

            return self._parent._cast(
                _6233.RollingRingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def root_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6235.RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6235,
            )

            return self._parent._cast(
                _6235.RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6236.ShaftCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6236,
            )

            return self._parent._cast(
                _6236.ShaftCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_hub_connection_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6237.ShaftHubConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6237,
            )

            return self._parent._cast(
                _6237.ShaftHubConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def specialised_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6239.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6239,
            )

            return self._parent._cast(
                _6239.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6240.SpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6240,
            )

            return self._parent._cast(
                _6240.SpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6242.SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6242,
            )

            return self._parent._cast(
                _6242.SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6243.SpringDamperCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6243,
            )

            return self._parent._cast(
                _6243.SpringDamperCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_half_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6245.SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6245,
            )

            return self._parent._cast(
                _6245.SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6246.StraightBevelDiffGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6246,
            )

            return self._parent._cast(
                _6246.StraightBevelDiffGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6248.StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6248,
            )

            return self._parent._cast(
                _6248.StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6249.StraightBevelGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6249,
            )

            return self._parent._cast(
                _6249.StraightBevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6251.StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6251,
            )

            return self._parent._cast(
                _6251.StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_planet_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6252.StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6252,
            )

            return self._parent._cast(
                _6252.StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_sun_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6253.StraightBevelSunGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6253,
            )

            return self._parent._cast(
                _6253.StraightBevelSunGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6254.SynchroniserCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6254,
            )

            return self._parent._cast(
                _6254.SynchroniserCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_half_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6255.SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6255,
            )

            return self._parent._cast(
                _6255.SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_part_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6256.SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6256,
            )

            return self._parent._cast(
                _6256.SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_sleeve_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6257.SynchroniserSleeveCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6257,
            )

            return self._parent._cast(
                _6257.SynchroniserSleeveCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6258.TorqueConverterCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6258,
            )

            return self._parent._cast(
                _6258.TorqueConverterCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_pump_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6260.TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6260,
            )

            return self._parent._cast(
                _6260.TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_turbine_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6261.TorqueConverterTurbineCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6261,
            )

            return self._parent._cast(
                _6261.TorqueConverterTurbineCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def unbalanced_mass_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6262.UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6262,
            )

            return self._parent._cast(
                _6262.UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def virtual_component_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6263.VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6263,
            )

            return self._parent._cast(
                _6263.VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6264.WormGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6264,
            )

            return self._parent._cast(
                _6264.WormGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6266.WormGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6266,
            )

            return self._parent._cast(
                _6266.WormGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6267.ZerolBevelGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6267,
            )

            return self._parent._cast(
                _6267.ZerolBevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6269.ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6269,
            )

            return self._parent._cast(
                _6269.ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6410.AbstractAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6410,
            )

            return self._parent._cast(_6410.AbstractAssemblyCompoundDynamicAnalysis)

        @property
        def abstract_shaft_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6411.AbstractShaftCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6411,
            )

            return self._parent._cast(_6411.AbstractShaftCompoundDynamicAnalysis)

        @property
        def abstract_shaft_or_housing_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6412.AbstractShaftOrHousingCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6412,
            )

            return self._parent._cast(
                _6412.AbstractShaftOrHousingCompoundDynamicAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6414.AGMAGleasonConicalGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6414,
            )

            return self._parent._cast(
                _6414.AGMAGleasonConicalGearCompoundDynamicAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6416.AGMAGleasonConicalGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6416,
            )

            return self._parent._cast(
                _6416.AGMAGleasonConicalGearSetCompoundDynamicAnalysis
            )

        @property
        def assembly_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6417.AssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6417,
            )

            return self._parent._cast(_6417.AssemblyCompoundDynamicAnalysis)

        @property
        def bearing_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6418.BearingCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6418,
            )

            return self._parent._cast(_6418.BearingCompoundDynamicAnalysis)

        @property
        def belt_drive_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6420.BeltDriveCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6420,
            )

            return self._parent._cast(_6420.BeltDriveCompoundDynamicAnalysis)

        @property
        def bevel_differential_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6421.BevelDifferentialGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6421,
            )

            return self._parent._cast(
                _6421.BevelDifferentialGearCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6423.BevelDifferentialGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6423,
            )

            return self._parent._cast(
                _6423.BevelDifferentialGearSetCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6424.BevelDifferentialPlanetGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6424,
            )

            return self._parent._cast(
                _6424.BevelDifferentialPlanetGearCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6425.BevelDifferentialSunGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6425,
            )

            return self._parent._cast(
                _6425.BevelDifferentialSunGearCompoundDynamicAnalysis
            )

        @property
        def bevel_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6426.BevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6426,
            )

            return self._parent._cast(_6426.BevelGearCompoundDynamicAnalysis)

        @property
        def bevel_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6428.BevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6428,
            )

            return self._parent._cast(_6428.BevelGearSetCompoundDynamicAnalysis)

        @property
        def bolt_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6429.BoltCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6429,
            )

            return self._parent._cast(_6429.BoltCompoundDynamicAnalysis)

        @property
        def bolted_joint_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6430.BoltedJointCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6430,
            )

            return self._parent._cast(_6430.BoltedJointCompoundDynamicAnalysis)

        @property
        def clutch_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6431.ClutchCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6431,
            )

            return self._parent._cast(_6431.ClutchCompoundDynamicAnalysis)

        @property
        def clutch_half_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6433.ClutchHalfCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6433,
            )

            return self._parent._cast(_6433.ClutchHalfCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6435.ComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6435,
            )

            return self._parent._cast(_6435.ComponentCompoundDynamicAnalysis)

        @property
        def concept_coupling_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6436.ConceptCouplingCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6436,
            )

            return self._parent._cast(_6436.ConceptCouplingCompoundDynamicAnalysis)

        @property
        def concept_coupling_half_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6438.ConceptCouplingHalfCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6438,
            )

            return self._parent._cast(_6438.ConceptCouplingHalfCompoundDynamicAnalysis)

        @property
        def concept_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6439.ConceptGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6439,
            )

            return self._parent._cast(_6439.ConceptGearCompoundDynamicAnalysis)

        @property
        def concept_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6441.ConceptGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6441,
            )

            return self._parent._cast(_6441.ConceptGearSetCompoundDynamicAnalysis)

        @property
        def conical_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6442.ConicalGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6442,
            )

            return self._parent._cast(_6442.ConicalGearCompoundDynamicAnalysis)

        @property
        def conical_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6444.ConicalGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6444,
            )

            return self._parent._cast(_6444.ConicalGearSetCompoundDynamicAnalysis)

        @property
        def connector_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6446.ConnectorCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6446,
            )

            return self._parent._cast(_6446.ConnectorCompoundDynamicAnalysis)

        @property
        def coupling_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6447.CouplingCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6447,
            )

            return self._parent._cast(_6447.CouplingCompoundDynamicAnalysis)

        @property
        def coupling_half_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6449.CouplingHalfCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6449,
            )

            return self._parent._cast(_6449.CouplingHalfCompoundDynamicAnalysis)

        @property
        def cvt_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6451.CVTCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6451,
            )

            return self._parent._cast(_6451.CVTCompoundDynamicAnalysis)

        @property
        def cvt_pulley_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6452.CVTPulleyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6452,
            )

            return self._parent._cast(_6452.CVTPulleyCompoundDynamicAnalysis)

        @property
        def cycloidal_assembly_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6453.CycloidalAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6453,
            )

            return self._parent._cast(_6453.CycloidalAssemblyCompoundDynamicAnalysis)

        @property
        def cycloidal_disc_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6455.CycloidalDiscCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6455,
            )

            return self._parent._cast(_6455.CycloidalDiscCompoundDynamicAnalysis)

        @property
        def cylindrical_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6457.CylindricalGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6457,
            )

            return self._parent._cast(_6457.CylindricalGearCompoundDynamicAnalysis)

        @property
        def cylindrical_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6459.CylindricalGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6459,
            )

            return self._parent._cast(_6459.CylindricalGearSetCompoundDynamicAnalysis)

        @property
        def cylindrical_planet_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6460.CylindricalPlanetGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6460,
            )

            return self._parent._cast(
                _6460.CylindricalPlanetGearCompoundDynamicAnalysis
            )

        @property
        def datum_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6461.DatumCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6461,
            )

            return self._parent._cast(_6461.DatumCompoundDynamicAnalysis)

        @property
        def external_cad_model_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6462.ExternalCADModelCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6462,
            )

            return self._parent._cast(_6462.ExternalCADModelCompoundDynamicAnalysis)

        @property
        def face_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6463.FaceGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6463,
            )

            return self._parent._cast(_6463.FaceGearCompoundDynamicAnalysis)

        @property
        def face_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6465.FaceGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6465,
            )

            return self._parent._cast(_6465.FaceGearSetCompoundDynamicAnalysis)

        @property
        def fe_part_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6466.FEPartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6466,
            )

            return self._parent._cast(_6466.FEPartCompoundDynamicAnalysis)

        @property
        def flexible_pin_assembly_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6467.FlexiblePinAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6467,
            )

            return self._parent._cast(_6467.FlexiblePinAssemblyCompoundDynamicAnalysis)

        @property
        def gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6468.GearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6468,
            )

            return self._parent._cast(_6468.GearCompoundDynamicAnalysis)

        @property
        def gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6470.GearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6470,
            )

            return self._parent._cast(_6470.GearSetCompoundDynamicAnalysis)

        @property
        def guide_dxf_model_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6471.GuideDxfModelCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6471,
            )

            return self._parent._cast(_6471.GuideDxfModelCompoundDynamicAnalysis)

        @property
        def hypoid_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6472.HypoidGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6472,
            )

            return self._parent._cast(_6472.HypoidGearCompoundDynamicAnalysis)

        @property
        def hypoid_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6474.HypoidGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6474,
            )

            return self._parent._cast(_6474.HypoidGearSetCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6476.KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6476,
            )

            return self._parent._cast(
                _6476.KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6478.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6478,
            )

            return self._parent._cast(
                _6478.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6479.KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6479,
            )

            return self._parent._cast(
                _6479.KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6481.KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6481,
            )

            return self._parent._cast(
                _6481.KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6482.KlingelnbergCycloPalloidSpiralBevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6482,
            )

            return self._parent._cast(
                _6482.KlingelnbergCycloPalloidSpiralBevelGearCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6484.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6484,
            )

            return self._parent._cast(
                _6484.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis
            )

        @property
        def mass_disc_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6485.MassDiscCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6485,
            )

            return self._parent._cast(_6485.MassDiscCompoundDynamicAnalysis)

        @property
        def measurement_component_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6486.MeasurementComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6486,
            )

            return self._parent._cast(_6486.MeasurementComponentCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6487.MountableComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6487,
            )

            return self._parent._cast(_6487.MountableComponentCompoundDynamicAnalysis)

        @property
        def oil_seal_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6488.OilSealCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6488,
            )

            return self._parent._cast(_6488.OilSealCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6489.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6489,
            )

            return self._parent._cast(_6489.PartCompoundDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6490.PartToPartShearCouplingCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6490,
            )

            return self._parent._cast(
                _6490.PartToPartShearCouplingCompoundDynamicAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6492.PartToPartShearCouplingHalfCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6492,
            )

            return self._parent._cast(
                _6492.PartToPartShearCouplingHalfCompoundDynamicAnalysis
            )

        @property
        def planetary_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6494.PlanetaryGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6494,
            )

            return self._parent._cast(_6494.PlanetaryGearSetCompoundDynamicAnalysis)

        @property
        def planet_carrier_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6495.PlanetCarrierCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6495,
            )

            return self._parent._cast(_6495.PlanetCarrierCompoundDynamicAnalysis)

        @property
        def point_load_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6496.PointLoadCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6496,
            )

            return self._parent._cast(_6496.PointLoadCompoundDynamicAnalysis)

        @property
        def power_load_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6497.PowerLoadCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6497,
            )

            return self._parent._cast(_6497.PowerLoadCompoundDynamicAnalysis)

        @property
        def pulley_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6498.PulleyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6498,
            )

            return self._parent._cast(_6498.PulleyCompoundDynamicAnalysis)

        @property
        def ring_pins_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6499.RingPinsCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6499,
            )

            return self._parent._cast(_6499.RingPinsCompoundDynamicAnalysis)

        @property
        def rolling_ring_assembly_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6501.RollingRingAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6501,
            )

            return self._parent._cast(_6501.RollingRingAssemblyCompoundDynamicAnalysis)

        @property
        def rolling_ring_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6502.RollingRingCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6502,
            )

            return self._parent._cast(_6502.RollingRingCompoundDynamicAnalysis)

        @property
        def root_assembly_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6504.RootAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6504,
            )

            return self._parent._cast(_6504.RootAssemblyCompoundDynamicAnalysis)

        @property
        def shaft_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6505.ShaftCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6505,
            )

            return self._parent._cast(_6505.ShaftCompoundDynamicAnalysis)

        @property
        def shaft_hub_connection_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6506.ShaftHubConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6506,
            )

            return self._parent._cast(_6506.ShaftHubConnectionCompoundDynamicAnalysis)

        @property
        def specialised_assembly_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6508.SpecialisedAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6508,
            )

            return self._parent._cast(_6508.SpecialisedAssemblyCompoundDynamicAnalysis)

        @property
        def spiral_bevel_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6509.SpiralBevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6509,
            )

            return self._parent._cast(_6509.SpiralBevelGearCompoundDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6511.SpiralBevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6511,
            )

            return self._parent._cast(_6511.SpiralBevelGearSetCompoundDynamicAnalysis)

        @property
        def spring_damper_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6512.SpringDamperCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6512,
            )

            return self._parent._cast(_6512.SpringDamperCompoundDynamicAnalysis)

        @property
        def spring_damper_half_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6514.SpringDamperHalfCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6514,
            )

            return self._parent._cast(_6514.SpringDamperHalfCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6515.StraightBevelDiffGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6515,
            )

            return self._parent._cast(
                _6515.StraightBevelDiffGearCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6517.StraightBevelDiffGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6517,
            )

            return self._parent._cast(
                _6517.StraightBevelDiffGearSetCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6518.StraightBevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6518,
            )

            return self._parent._cast(_6518.StraightBevelGearCompoundDynamicAnalysis)

        @property
        def straight_bevel_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6520.StraightBevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6520,
            )

            return self._parent._cast(_6520.StraightBevelGearSetCompoundDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6521.StraightBevelPlanetGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6521,
            )

            return self._parent._cast(
                _6521.StraightBevelPlanetGearCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6522.StraightBevelSunGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6522,
            )

            return self._parent._cast(_6522.StraightBevelSunGearCompoundDynamicAnalysis)

        @property
        def synchroniser_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6523.SynchroniserCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6523,
            )

            return self._parent._cast(_6523.SynchroniserCompoundDynamicAnalysis)

        @property
        def synchroniser_half_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6524.SynchroniserHalfCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6524,
            )

            return self._parent._cast(_6524.SynchroniserHalfCompoundDynamicAnalysis)

        @property
        def synchroniser_part_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6525.SynchroniserPartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6525,
            )

            return self._parent._cast(_6525.SynchroniserPartCompoundDynamicAnalysis)

        @property
        def synchroniser_sleeve_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6526.SynchroniserSleeveCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6526,
            )

            return self._parent._cast(_6526.SynchroniserSleeveCompoundDynamicAnalysis)

        @property
        def torque_converter_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6527.TorqueConverterCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6527,
            )

            return self._parent._cast(_6527.TorqueConverterCompoundDynamicAnalysis)

        @property
        def torque_converter_pump_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6529.TorqueConverterPumpCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6529,
            )

            return self._parent._cast(_6529.TorqueConverterPumpCompoundDynamicAnalysis)

        @property
        def torque_converter_turbine_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6530.TorqueConverterTurbineCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6530,
            )

            return self._parent._cast(
                _6530.TorqueConverterTurbineCompoundDynamicAnalysis
            )

        @property
        def unbalanced_mass_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6531.UnbalancedMassCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6531,
            )

            return self._parent._cast(_6531.UnbalancedMassCompoundDynamicAnalysis)

        @property
        def virtual_component_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6532.VirtualComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6532,
            )

            return self._parent._cast(_6532.VirtualComponentCompoundDynamicAnalysis)

        @property
        def worm_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6533.WormGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6533,
            )

            return self._parent._cast(_6533.WormGearCompoundDynamicAnalysis)

        @property
        def worm_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6535.WormGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6535,
            )

            return self._parent._cast(_6535.WormGearSetCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6536.ZerolBevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6536,
            )

            return self._parent._cast(_6536.ZerolBevelGearCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6538.ZerolBevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6538,
            )

            return self._parent._cast(_6538.ZerolBevelGearSetCompoundDynamicAnalysis)

        @property
        def abstract_assembly_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6677.AbstractAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6677,
            )

            return self._parent._cast(
                _6677.AbstractAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_shaft_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6678.AbstractShaftCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6678,
            )

            return self._parent._cast(_6678.AbstractShaftCompoundCriticalSpeedAnalysis)

        @property
        def abstract_shaft_or_housing_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6679.AbstractShaftOrHousingCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6679,
            )

            return self._parent._cast(
                _6679.AbstractShaftOrHousingCompoundCriticalSpeedAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6681.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6681,
            )

            return self._parent._cast(
                _6681.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6683.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6683,
            )

            return self._parent._cast(
                _6683.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def assembly_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6684.AssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6684,
            )

            return self._parent._cast(_6684.AssemblyCompoundCriticalSpeedAnalysis)

        @property
        def bearing_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6685.BearingCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6685,
            )

            return self._parent._cast(_6685.BearingCompoundCriticalSpeedAnalysis)

        @property
        def belt_drive_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6687.BeltDriveCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6687,
            )

            return self._parent._cast(_6687.BeltDriveCompoundCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6688.BevelDifferentialGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6688,
            )

            return self._parent._cast(
                _6688.BevelDifferentialGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6690.BevelDifferentialGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6690,
            )

            return self._parent._cast(
                _6690.BevelDifferentialGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6691.BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6691,
            )

            return self._parent._cast(
                _6691.BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6692.BevelDifferentialSunGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6692,
            )

            return self._parent._cast(
                _6692.BevelDifferentialSunGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6693.BevelGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6693,
            )

            return self._parent._cast(_6693.BevelGearCompoundCriticalSpeedAnalysis)

        @property
        def bevel_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6695.BevelGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6695,
            )

            return self._parent._cast(_6695.BevelGearSetCompoundCriticalSpeedAnalysis)

        @property
        def bolt_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6696.BoltCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6696,
            )

            return self._parent._cast(_6696.BoltCompoundCriticalSpeedAnalysis)

        @property
        def bolted_joint_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6697.BoltedJointCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6697,
            )

            return self._parent._cast(_6697.BoltedJointCompoundCriticalSpeedAnalysis)

        @property
        def clutch_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6698.ClutchCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6698,
            )

            return self._parent._cast(_6698.ClutchCompoundCriticalSpeedAnalysis)

        @property
        def clutch_half_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6700.ClutchHalfCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6700,
            )

            return self._parent._cast(_6700.ClutchHalfCompoundCriticalSpeedAnalysis)

        @property
        def component_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6702.ComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6702,
            )

            return self._parent._cast(_6702.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def concept_coupling_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6703.ConceptCouplingCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6703,
            )

            return self._parent._cast(
                _6703.ConceptCouplingCompoundCriticalSpeedAnalysis
            )

        @property
        def concept_coupling_half_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6705.ConceptCouplingHalfCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6705,
            )

            return self._parent._cast(
                _6705.ConceptCouplingHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def concept_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6706.ConceptGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6706,
            )

            return self._parent._cast(_6706.ConceptGearCompoundCriticalSpeedAnalysis)

        @property
        def concept_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6708.ConceptGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6708,
            )

            return self._parent._cast(_6708.ConceptGearSetCompoundCriticalSpeedAnalysis)

        @property
        def conical_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6709.ConicalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6709,
            )

            return self._parent._cast(_6709.ConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def conical_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6711.ConicalGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6711,
            )

            return self._parent._cast(_6711.ConicalGearSetCompoundCriticalSpeedAnalysis)

        @property
        def connector_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6713.ConnectorCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6713,
            )

            return self._parent._cast(_6713.ConnectorCompoundCriticalSpeedAnalysis)

        @property
        def coupling_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6714.CouplingCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6714,
            )

            return self._parent._cast(_6714.CouplingCompoundCriticalSpeedAnalysis)

        @property
        def coupling_half_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6716.CouplingHalfCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6716,
            )

            return self._parent._cast(_6716.CouplingHalfCompoundCriticalSpeedAnalysis)

        @property
        def cvt_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6718.CVTCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6718,
            )

            return self._parent._cast(_6718.CVTCompoundCriticalSpeedAnalysis)

        @property
        def cvt_pulley_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6719.CVTPulleyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6719,
            )

            return self._parent._cast(_6719.CVTPulleyCompoundCriticalSpeedAnalysis)

        @property
        def cycloidal_assembly_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6720.CycloidalAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6720,
            )

            return self._parent._cast(
                _6720.CycloidalAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def cycloidal_disc_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6722.CycloidalDiscCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6722,
            )

            return self._parent._cast(_6722.CycloidalDiscCompoundCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6724.CylindricalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6724,
            )

            return self._parent._cast(
                _6724.CylindricalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def cylindrical_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6726.CylindricalGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6726,
            )

            return self._parent._cast(
                _6726.CylindricalGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def cylindrical_planet_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6727.CylindricalPlanetGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6727,
            )

            return self._parent._cast(
                _6727.CylindricalPlanetGearCompoundCriticalSpeedAnalysis
            )

        @property
        def datum_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6728.DatumCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6728,
            )

            return self._parent._cast(_6728.DatumCompoundCriticalSpeedAnalysis)

        @property
        def external_cad_model_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6729.ExternalCADModelCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6729,
            )

            return self._parent._cast(
                _6729.ExternalCADModelCompoundCriticalSpeedAnalysis
            )

        @property
        def face_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6730.FaceGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6730,
            )

            return self._parent._cast(_6730.FaceGearCompoundCriticalSpeedAnalysis)

        @property
        def face_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6732.FaceGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6732,
            )

            return self._parent._cast(_6732.FaceGearSetCompoundCriticalSpeedAnalysis)

        @property
        def fe_part_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6733.FEPartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6733,
            )

            return self._parent._cast(_6733.FEPartCompoundCriticalSpeedAnalysis)

        @property
        def flexible_pin_assembly_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6734.FlexiblePinAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6734,
            )

            return self._parent._cast(
                _6734.FlexiblePinAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6735.GearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6735,
            )

            return self._parent._cast(_6735.GearCompoundCriticalSpeedAnalysis)

        @property
        def gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6737.GearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6737,
            )

            return self._parent._cast(_6737.GearSetCompoundCriticalSpeedAnalysis)

        @property
        def guide_dxf_model_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6738.GuideDxfModelCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6738,
            )

            return self._parent._cast(_6738.GuideDxfModelCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6739.HypoidGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6739,
            )

            return self._parent._cast(_6739.HypoidGearCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6741.HypoidGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6741,
            )

            return self._parent._cast(_6741.HypoidGearSetCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6743.KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6743,
            )

            return self._parent._cast(
                _6743.KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_6745.KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6745,
            )

            return self._parent._cast(
                _6745.KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6746.KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6746,
            )

            return self._parent._cast(
                _6746.KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6748.KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6748,
            )

            return self._parent._cast(
                _6748.KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_6749.KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6749,
            )

            return self._parent._cast(
                _6749.KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6751.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6751,
            )

            return self._parent._cast(
                _6751.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def mass_disc_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6752.MassDiscCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6752,
            )

            return self._parent._cast(_6752.MassDiscCompoundCriticalSpeedAnalysis)

        @property
        def measurement_component_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6753.MeasurementComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6753,
            )

            return self._parent._cast(
                _6753.MeasurementComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6754.MountableComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6754,
            )

            return self._parent._cast(
                _6754.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def oil_seal_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6755.OilSealCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6755,
            )

            return self._parent._cast(_6755.OilSealCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6756.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6756,
            )

            return self._parent._cast(_6756.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6757.PartToPartShearCouplingCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6757,
            )

            return self._parent._cast(
                _6757.PartToPartShearCouplingCompoundCriticalSpeedAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6759.PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6759,
            )

            return self._parent._cast(
                _6759.PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def planetary_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6761.PlanetaryGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6761,
            )

            return self._parent._cast(
                _6761.PlanetaryGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def planet_carrier_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6762.PlanetCarrierCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6762,
            )

            return self._parent._cast(_6762.PlanetCarrierCompoundCriticalSpeedAnalysis)

        @property
        def point_load_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6763.PointLoadCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6763,
            )

            return self._parent._cast(_6763.PointLoadCompoundCriticalSpeedAnalysis)

        @property
        def power_load_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6764.PowerLoadCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6764,
            )

            return self._parent._cast(_6764.PowerLoadCompoundCriticalSpeedAnalysis)

        @property
        def pulley_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6765.PulleyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6765,
            )

            return self._parent._cast(_6765.PulleyCompoundCriticalSpeedAnalysis)

        @property
        def ring_pins_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6766.RingPinsCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6766,
            )

            return self._parent._cast(_6766.RingPinsCompoundCriticalSpeedAnalysis)

        @property
        def rolling_ring_assembly_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6768.RollingRingAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6768,
            )

            return self._parent._cast(
                _6768.RollingRingAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def rolling_ring_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6769.RollingRingCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6769,
            )

            return self._parent._cast(_6769.RollingRingCompoundCriticalSpeedAnalysis)

        @property
        def root_assembly_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6771.RootAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6771,
            )

            return self._parent._cast(_6771.RootAssemblyCompoundCriticalSpeedAnalysis)

        @property
        def shaft_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6772.ShaftCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6772,
            )

            return self._parent._cast(_6772.ShaftCompoundCriticalSpeedAnalysis)

        @property
        def shaft_hub_connection_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6773.ShaftHubConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6773,
            )

            return self._parent._cast(
                _6773.ShaftHubConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def specialised_assembly_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6775.SpecialisedAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6775,
            )

            return self._parent._cast(
                _6775.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6776.SpiralBevelGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6776,
            )

            return self._parent._cast(
                _6776.SpiralBevelGearCompoundCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6778.SpiralBevelGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6778,
            )

            return self._parent._cast(
                _6778.SpiralBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def spring_damper_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6779.SpringDamperCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6779,
            )

            return self._parent._cast(_6779.SpringDamperCompoundCriticalSpeedAnalysis)

        @property
        def spring_damper_half_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6781.SpringDamperHalfCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6781,
            )

            return self._parent._cast(
                _6781.SpringDamperHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6782.StraightBevelDiffGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6782,
            )

            return self._parent._cast(
                _6782.StraightBevelDiffGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6784.StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6784,
            )

            return self._parent._cast(
                _6784.StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6785.StraightBevelGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6785,
            )

            return self._parent._cast(
                _6785.StraightBevelGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6787.StraightBevelGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6787,
            )

            return self._parent._cast(
                _6787.StraightBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6788.StraightBevelPlanetGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6788,
            )

            return self._parent._cast(
                _6788.StraightBevelPlanetGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6789.StraightBevelSunGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6789,
            )

            return self._parent._cast(
                _6789.StraightBevelSunGearCompoundCriticalSpeedAnalysis
            )

        @property
        def synchroniser_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6790.SynchroniserCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6790,
            )

            return self._parent._cast(_6790.SynchroniserCompoundCriticalSpeedAnalysis)

        @property
        def synchroniser_half_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6791.SynchroniserHalfCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6791,
            )

            return self._parent._cast(
                _6791.SynchroniserHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def synchroniser_part_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6792.SynchroniserPartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6792,
            )

            return self._parent._cast(
                _6792.SynchroniserPartCompoundCriticalSpeedAnalysis
            )

        @property
        def synchroniser_sleeve_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6793.SynchroniserSleeveCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6793,
            )

            return self._parent._cast(
                _6793.SynchroniserSleeveCompoundCriticalSpeedAnalysis
            )

        @property
        def torque_converter_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6794.TorqueConverterCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6794,
            )

            return self._parent._cast(
                _6794.TorqueConverterCompoundCriticalSpeedAnalysis
            )

        @property
        def torque_converter_pump_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6796.TorqueConverterPumpCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6796,
            )

            return self._parent._cast(
                _6796.TorqueConverterPumpCompoundCriticalSpeedAnalysis
            )

        @property
        def torque_converter_turbine_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6797.TorqueConverterTurbineCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6797,
            )

            return self._parent._cast(
                _6797.TorqueConverterTurbineCompoundCriticalSpeedAnalysis
            )

        @property
        def unbalanced_mass_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6798.UnbalancedMassCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6798,
            )

            return self._parent._cast(_6798.UnbalancedMassCompoundCriticalSpeedAnalysis)

        @property
        def virtual_component_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6799.VirtualComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6799,
            )

            return self._parent._cast(
                _6799.VirtualComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def worm_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6800.WormGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6800,
            )

            return self._parent._cast(_6800.WormGearCompoundCriticalSpeedAnalysis)

        @property
        def worm_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6802.WormGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6802,
            )

            return self._parent._cast(_6802.WormGearSetCompoundCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6803.ZerolBevelGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6803,
            )

            return self._parent._cast(_6803.ZerolBevelGearCompoundCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_6805.ZerolBevelGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6805,
            )

            return self._parent._cast(
                _6805.ZerolBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7143.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7143,
            )

            return self._parent._cast(
                _7143.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7144.AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7144,
            )

            return self._parent._cast(
                _7144.AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_or_housing_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7145.AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7145,
            )

            return self._parent._cast(
                _7145.AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7147.AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7147,
            )

            return self._parent._cast(
                _7147.AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7149.AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7149,
            )

            return self._parent._cast(
                _7149.AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7150.AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7150,
            )

            return self._parent._cast(
                _7150.AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bearing_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7151.BearingCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7151,
            )

            return self._parent._cast(
                _7151.BearingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def belt_drive_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7153.BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7153,
            )

            return self._parent._cast(
                _7153.BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7154.BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7154,
            )

            return self._parent._cast(
                _7154.BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7156.BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7156,
            )

            return self._parent._cast(
                _7156.BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7157.BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7157,
            )

            return self._parent._cast(
                _7157.BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_sun_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7158.BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7158,
            )

            return self._parent._cast(
                _7158.BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7159.BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7159,
            )

            return self._parent._cast(
                _7159.BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7161.BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7161,
            )

            return self._parent._cast(
                _7161.BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bolt_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7162.BoltCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7162,
            )

            return self._parent._cast(
                _7162.BoltCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bolted_joint_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7163.BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7163,
            )

            return self._parent._cast(
                _7163.BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7164.ClutchCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7164,
            )

            return self._parent._cast(
                _7164.ClutchCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7166.ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7166,
            )

            return self._parent._cast(
                _7166.ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7168.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7168,
            )

            return self._parent._cast(
                _7168.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7169.ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7169,
            )

            return self._parent._cast(
                _7169.ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_7171.ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7171,
            )

            return self._parent._cast(
                _7171.ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7172.ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7172,
            )

            return self._parent._cast(
                _7172.ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7174.ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7174,
            )

            return self._parent._cast(
                _7174.ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7175.ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7175,
            )

            return self._parent._cast(
                _7175.ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7177.ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7177,
            )

            return self._parent._cast(
                _7177.ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connector_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7179.ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7179,
            )

            return self._parent._cast(
                _7179.ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7180.CouplingCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7180,
            )

            return self._parent._cast(
                _7180.CouplingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7182.CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7182,
            )

            return self._parent._cast(
                _7182.CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7184.CVTCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7184,
            )

            return self._parent._cast(
                _7184.CVTCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_pulley_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7185.CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7185,
            )

            return self._parent._cast(
                _7185.CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7186.CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7186,
            )

            return self._parent._cast(
                _7186.CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7188.CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7188,
            )

            return self._parent._cast(
                _7188.CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7190.CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7190,
            )

            return self._parent._cast(
                _7190.CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_7192.CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7192,
            )

            return self._parent._cast(
                _7192.CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7193.CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7193,
            )

            return self._parent._cast(
                _7193.CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def datum_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7194.DatumCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7194,
            )

            return self._parent._cast(
                _7194.DatumCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def external_cad_model_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7195.ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7195,
            )

            return self._parent._cast(
                _7195.ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7196.FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7196,
            )

            return self._parent._cast(
                _7196.FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7198.FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7198,
            )

            return self._parent._cast(
                _7198.FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def fe_part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7199.FEPartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7199,
            )

            return self._parent._cast(
                _7199.FEPartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def flexible_pin_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_7200.FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7200,
            )

            return self._parent._cast(
                _7200.FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7201.GearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7201,
            )

            return self._parent._cast(
                _7201.GearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7203.GearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7203,
            )

            return self._parent._cast(
                _7203.GearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def guide_dxf_model_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7204.GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7204,
            )

            return self._parent._cast(
                _7204.GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7205.HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7205,
            )

            return self._parent._cast(
                _7205.HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7207.HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7207,
            )

            return self._parent._cast(
                _7207.HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7209.KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7209,
            )

            return self._parent._cast(
                _7209.KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7211.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7211,
            )

            return self._parent._cast(
                _7211.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7212.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7212,
            )

            return self._parent._cast(
                _7212.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7214.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7214,
            )

            return self._parent._cast(
                _7214.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7215.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7215,
            )

            return self._parent._cast(
                _7215.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7217.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7217,
            )

            return self._parent._cast(
                _7217.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mass_disc_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7218.MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7218,
            )

            return self._parent._cast(
                _7218.MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def measurement_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7219.MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7219,
            )

            return self._parent._cast(
                _7219.MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_7220.MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7220,
            )

            return self._parent._cast(
                _7220.MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def oil_seal_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7221.OilSealCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7221,
            )

            return self._parent._cast(
                _7221.OilSealCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7222.PartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7222,
            )

            return self._parent._cast(
                _7222.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7223.PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7223,
            )

            return self._parent._cast(
                _7223.PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7225.PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7225,
            )

            return self._parent._cast(
                _7225.PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planetary_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7227.PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7227,
            )

            return self._parent._cast(
                _7227.PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planet_carrier_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7228.PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7228,
            )

            return self._parent._cast(
                _7228.PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def point_load_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7229.PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7229,
            )

            return self._parent._cast(
                _7229.PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def power_load_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7230.PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7230,
            )

            return self._parent._cast(
                _7230.PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def pulley_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7231.PulleyCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7231,
            )

            return self._parent._cast(
                _7231.PulleyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def ring_pins_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7232.RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7232,
            )

            return self._parent._cast(
                _7232.RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_7234.RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7234,
            )

            return self._parent._cast(
                _7234.RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7235.RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7235,
            )

            return self._parent._cast(
                _7235.RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def root_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7237.RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7237,
            )

            return self._parent._cast(
                _7237.RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7238.ShaftCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7238,
            )

            return self._parent._cast(
                _7238.ShaftCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_hub_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_7239.ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7239,
            )

            return self._parent._cast(
                _7239.ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def specialised_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_7241.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7241,
            )

            return self._parent._cast(
                _7241.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7242.SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7242,
            )

            return self._parent._cast(
                _7242.SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_7244.SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7244,
            )

            return self._parent._cast(
                _7244.SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7245.SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7245,
            )

            return self._parent._cast(
                _7245.SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7247.SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7247,
            )

            return self._parent._cast(
                _7247.SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7248.StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7248,
            )

            return self._parent._cast(
                _7248.StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7250.StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7250,
            )

            return self._parent._cast(
                _7250.StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7251.StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7251,
            )

            return self._parent._cast(
                _7251.StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7253.StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7253,
            )

            return self._parent._cast(
                _7253.StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7254.StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7254,
            )

            return self._parent._cast(
                _7254.StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_sun_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7255.StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7255,
            )

            return self._parent._cast(
                _7255.StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7256.SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7256,
            )

            return self._parent._cast(
                _7256.SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7257.SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7257,
            )

            return self._parent._cast(
                _7257.SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7258.SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7258,
            )

            return self._parent._cast(
                _7258.SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_sleeve_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_7259.SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7259,
            )

            return self._parent._cast(
                _7259.SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7260.TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7260,
            )

            return self._parent._cast(
                _7260.TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_pump_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_7262.TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7262,
            )

            return self._parent._cast(
                _7262.TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_turbine_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7263.TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7263,
            )

            return self._parent._cast(
                _7263.TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def unbalanced_mass_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7264.UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7264,
            )

            return self._parent._cast(
                _7264.UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def virtual_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7265.VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7265,
            )

            return self._parent._cast(
                _7265.VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7266.WormGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7266,
            )

            return self._parent._cast(
                _7266.WormGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7268.WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7268,
            )

            return self._parent._cast(
                _7268.WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7269.ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7269,
            )

            return self._parent._cast(
                _7269.ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7271.ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7271,
            )

            return self._parent._cast(
                _7271.ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7408.AbstractAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7408,
            )

            return self._parent._cast(
                _7408.AbstractAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_shaft_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7409.AbstractShaftCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7409,
            )

            return self._parent._cast(
                _7409.AbstractShaftCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_shaft_or_housing_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7410.AbstractShaftOrHousingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7410,
            )

            return self._parent._cast(
                _7410.AbstractShaftOrHousingCompoundAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7412.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7412,
            )

            return self._parent._cast(
                _7412.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7414.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7414,
            )

            return self._parent._cast(
                _7414.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def assembly_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7415.AssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7415,
            )

            return self._parent._cast(_7415.AssemblyCompoundAdvancedSystemDeflection)

        @property
        def bearing_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7416.BearingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7416,
            )

            return self._parent._cast(_7416.BearingCompoundAdvancedSystemDeflection)

        @property
        def belt_drive_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7418.BeltDriveCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7418,
            )

            return self._parent._cast(_7418.BeltDriveCompoundAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7419.BevelDifferentialGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7419,
            )

            return self._parent._cast(
                _7419.BevelDifferentialGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7421.BevelDifferentialGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7421,
            )

            return self._parent._cast(
                _7421.BevelDifferentialGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7422.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7422,
            )

            return self._parent._cast(
                _7422.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7423.BevelDifferentialSunGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7423,
            )

            return self._parent._cast(
                _7423.BevelDifferentialSunGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7424.BevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7424,
            )

            return self._parent._cast(_7424.BevelGearCompoundAdvancedSystemDeflection)

        @property
        def bevel_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7426.BevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7426,
            )

            return self._parent._cast(
                _7426.BevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def bolt_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7427.BoltCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7427,
            )

            return self._parent._cast(_7427.BoltCompoundAdvancedSystemDeflection)

        @property
        def bolted_joint_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7428.BoltedJointCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7428,
            )

            return self._parent._cast(_7428.BoltedJointCompoundAdvancedSystemDeflection)

        @property
        def clutch_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7429.ClutchCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7429,
            )

            return self._parent._cast(_7429.ClutchCompoundAdvancedSystemDeflection)

        @property
        def clutch_half_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7431.ClutchHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7431,
            )

            return self._parent._cast(_7431.ClutchHalfCompoundAdvancedSystemDeflection)

        @property
        def component_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7433.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7433,
            )

            return self._parent._cast(_7433.ComponentCompoundAdvancedSystemDeflection)

        @property
        def concept_coupling_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7434.ConceptCouplingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7434,
            )

            return self._parent._cast(
                _7434.ConceptCouplingCompoundAdvancedSystemDeflection
            )

        @property
        def concept_coupling_half_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7436.ConceptCouplingHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7436,
            )

            return self._parent._cast(
                _7436.ConceptCouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def concept_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7437.ConceptGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7437,
            )

            return self._parent._cast(_7437.ConceptGearCompoundAdvancedSystemDeflection)

        @property
        def concept_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7439.ConceptGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7439,
            )

            return self._parent._cast(
                _7439.ConceptGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7440.ConicalGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7440,
            )

            return self._parent._cast(_7440.ConicalGearCompoundAdvancedSystemDeflection)

        @property
        def conical_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7442.ConicalGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7442,
            )

            return self._parent._cast(
                _7442.ConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def connector_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7444.ConnectorCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7444,
            )

            return self._parent._cast(_7444.ConnectorCompoundAdvancedSystemDeflection)

        @property
        def coupling_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7445.CouplingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7445,
            )

            return self._parent._cast(_7445.CouplingCompoundAdvancedSystemDeflection)

        @property
        def coupling_half_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7447.CouplingHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7447,
            )

            return self._parent._cast(
                _7447.CouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def cvt_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7449.CVTCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7449,
            )

            return self._parent._cast(_7449.CVTCompoundAdvancedSystemDeflection)

        @property
        def cvt_pulley_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7450.CVTPulleyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7450,
            )

            return self._parent._cast(_7450.CVTPulleyCompoundAdvancedSystemDeflection)

        @property
        def cycloidal_assembly_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7451.CycloidalAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7451,
            )

            return self._parent._cast(
                _7451.CycloidalAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def cycloidal_disc_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7453.CycloidalDiscCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7453,
            )

            return self._parent._cast(
                _7453.CycloidalDiscCompoundAdvancedSystemDeflection
            )

        @property
        def cylindrical_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7455.CylindricalGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7455,
            )

            return self._parent._cast(
                _7455.CylindricalGearCompoundAdvancedSystemDeflection
            )

        @property
        def cylindrical_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7457.CylindricalGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7457,
            )

            return self._parent._cast(
                _7457.CylindricalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def cylindrical_planet_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7458.CylindricalPlanetGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7458,
            )

            return self._parent._cast(
                _7458.CylindricalPlanetGearCompoundAdvancedSystemDeflection
            )

        @property
        def datum_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7459.DatumCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7459,
            )

            return self._parent._cast(_7459.DatumCompoundAdvancedSystemDeflection)

        @property
        def external_cad_model_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7460.ExternalCADModelCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7460,
            )

            return self._parent._cast(
                _7460.ExternalCADModelCompoundAdvancedSystemDeflection
            )

        @property
        def face_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7461.FaceGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7461,
            )

            return self._parent._cast(_7461.FaceGearCompoundAdvancedSystemDeflection)

        @property
        def face_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7463.FaceGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7463,
            )

            return self._parent._cast(_7463.FaceGearSetCompoundAdvancedSystemDeflection)

        @property
        def fe_part_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7464.FEPartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7464,
            )

            return self._parent._cast(_7464.FEPartCompoundAdvancedSystemDeflection)

        @property
        def flexible_pin_assembly_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7465.FlexiblePinAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7465,
            )

            return self._parent._cast(
                _7465.FlexiblePinAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7466.GearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7466,
            )

            return self._parent._cast(_7466.GearCompoundAdvancedSystemDeflection)

        @property
        def gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7468.GearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7468,
            )

            return self._parent._cast(_7468.GearSetCompoundAdvancedSystemDeflection)

        @property
        def guide_dxf_model_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7469.GuideDxfModelCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7469,
            )

            return self._parent._cast(
                _7469.GuideDxfModelCompoundAdvancedSystemDeflection
            )

        @property
        def hypoid_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7470.HypoidGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7470,
            )

            return self._parent._cast(_7470.HypoidGearCompoundAdvancedSystemDeflection)

        @property
        def hypoid_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7472.HypoidGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7472,
            )

            return self._parent._cast(
                _7472.HypoidGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> (
            "_7474.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection"
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7474,
            )

            return self._parent._cast(
                _7474.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7476.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7476,
            )

            return self._parent._cast(
                _7476.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7477.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7477,
            )

            return self._parent._cast(
                _7477.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7479.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7479,
            )

            return self._parent._cast(
                _7479.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7480.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7480,
            )

            return self._parent._cast(
                _7480.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7482.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7482,
            )

            return self._parent._cast(
                _7482.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def mass_disc_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7483.MassDiscCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7483,
            )

            return self._parent._cast(_7483.MassDiscCompoundAdvancedSystemDeflection)

        @property
        def measurement_component_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7484.MeasurementComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7484,
            )

            return self._parent._cast(
                _7484.MeasurementComponentCompoundAdvancedSystemDeflection
            )

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7485.MountableComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7485,
            )

            return self._parent._cast(
                _7485.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def oil_seal_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7486.OilSealCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7486,
            )

            return self._parent._cast(_7486.OilSealCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7487.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7487,
            )

            return self._parent._cast(_7487.PartCompoundAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7488.PartToPartShearCouplingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7488,
            )

            return self._parent._cast(
                _7488.PartToPartShearCouplingCompoundAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_half_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7490.PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7490,
            )

            return self._parent._cast(
                _7490.PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def planetary_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7492.PlanetaryGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7492,
            )

            return self._parent._cast(
                _7492.PlanetaryGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def planet_carrier_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7493.PlanetCarrierCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7493,
            )

            return self._parent._cast(
                _7493.PlanetCarrierCompoundAdvancedSystemDeflection
            )

        @property
        def point_load_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7494.PointLoadCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7494,
            )

            return self._parent._cast(_7494.PointLoadCompoundAdvancedSystemDeflection)

        @property
        def power_load_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7495.PowerLoadCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7495,
            )

            return self._parent._cast(_7495.PowerLoadCompoundAdvancedSystemDeflection)

        @property
        def pulley_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7496.PulleyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7496,
            )

            return self._parent._cast(_7496.PulleyCompoundAdvancedSystemDeflection)

        @property
        def ring_pins_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7497.RingPinsCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7497,
            )

            return self._parent._cast(_7497.RingPinsCompoundAdvancedSystemDeflection)

        @property
        def rolling_ring_assembly_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7499.RollingRingAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7499,
            )

            return self._parent._cast(
                _7499.RollingRingAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def rolling_ring_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7500.RollingRingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7500,
            )

            return self._parent._cast(_7500.RollingRingCompoundAdvancedSystemDeflection)

        @property
        def root_assembly_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7502.RootAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7502,
            )

            return self._parent._cast(
                _7502.RootAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def shaft_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7503.ShaftCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7503,
            )

            return self._parent._cast(_7503.ShaftCompoundAdvancedSystemDeflection)

        @property
        def shaft_hub_connection_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7504.ShaftHubConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7504,
            )

            return self._parent._cast(
                _7504.ShaftHubConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def specialised_assembly_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7506.SpecialisedAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7506,
            )

            return self._parent._cast(
                _7506.SpecialisedAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7507.SpiralBevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7507,
            )

            return self._parent._cast(
                _7507.SpiralBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7509.SpiralBevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7509,
            )

            return self._parent._cast(
                _7509.SpiralBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def spring_damper_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7510.SpringDamperCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7510,
            )

            return self._parent._cast(
                _7510.SpringDamperCompoundAdvancedSystemDeflection
            )

        @property
        def spring_damper_half_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7512.SpringDamperHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7512,
            )

            return self._parent._cast(
                _7512.SpringDamperHalfCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7513.StraightBevelDiffGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7513,
            )

            return self._parent._cast(
                _7513.StraightBevelDiffGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7515.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7515,
            )

            return self._parent._cast(
                _7515.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7516.StraightBevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7516,
            )

            return self._parent._cast(
                _7516.StraightBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7518.StraightBevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7518,
            )

            return self._parent._cast(
                _7518.StraightBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_planet_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7519.StraightBevelPlanetGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7519,
            )

            return self._parent._cast(
                _7519.StraightBevelPlanetGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7520.StraightBevelSunGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7520,
            )

            return self._parent._cast(
                _7520.StraightBevelSunGearCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7521.SynchroniserCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7521,
            )

            return self._parent._cast(
                _7521.SynchroniserCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_half_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7522.SynchroniserHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7522,
            )

            return self._parent._cast(
                _7522.SynchroniserHalfCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_part_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7523.SynchroniserPartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7523,
            )

            return self._parent._cast(
                _7523.SynchroniserPartCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_sleeve_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7524.SynchroniserSleeveCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7524,
            )

            return self._parent._cast(
                _7524.SynchroniserSleeveCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7525.TorqueConverterCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7525,
            )

            return self._parent._cast(
                _7525.TorqueConverterCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_pump_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7527.TorqueConverterPumpCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7527,
            )

            return self._parent._cast(
                _7527.TorqueConverterPumpCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_turbine_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7528.TorqueConverterTurbineCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7528,
            )

            return self._parent._cast(
                _7528.TorqueConverterTurbineCompoundAdvancedSystemDeflection
            )

        @property
        def unbalanced_mass_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7529.UnbalancedMassCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7529,
            )

            return self._parent._cast(
                _7529.UnbalancedMassCompoundAdvancedSystemDeflection
            )

        @property
        def virtual_component_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7530.VirtualComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7530,
            )

            return self._parent._cast(
                _7530.VirtualComponentCompoundAdvancedSystemDeflection
            )

        @property
        def worm_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7531.WormGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7531,
            )

            return self._parent._cast(_7531.WormGearCompoundAdvancedSystemDeflection)

        @property
        def worm_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7533.WormGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7533,
            )

            return self._parent._cast(_7533.WormGearSetCompoundAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7534.ZerolBevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7534,
            )

            return self._parent._cast(
                _7534.ZerolBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "_7536.ZerolBevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7536,
            )

            return self._parent._cast(
                _7536.ZerolBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def part_compound_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "PartCompoundAnalysis":
            return self._parent

        def __getattr__(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartCompoundAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def two_d_drawing(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TwoDDrawing

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "PartCompoundAnalysis._Cast_PartCompoundAnalysis":
        return self._Cast_PartCompoundAnalysis(self)
