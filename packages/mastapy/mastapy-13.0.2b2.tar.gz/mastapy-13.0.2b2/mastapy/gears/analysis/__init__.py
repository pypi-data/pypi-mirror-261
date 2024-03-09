"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1216 import AbstractGearAnalysis
    from ._1217 import AbstractGearMeshAnalysis
    from ._1218 import AbstractGearSetAnalysis
    from ._1219 import GearDesignAnalysis
    from ._1220 import GearImplementationAnalysis
    from ._1221 import GearImplementationAnalysisDutyCycle
    from ._1222 import GearImplementationDetail
    from ._1223 import GearMeshDesignAnalysis
    from ._1224 import GearMeshImplementationAnalysis
    from ._1225 import GearMeshImplementationAnalysisDutyCycle
    from ._1226 import GearMeshImplementationDetail
    from ._1227 import GearSetDesignAnalysis
    from ._1228 import GearSetGroupDutyCycle
    from ._1229 import GearSetImplementationAnalysis
    from ._1230 import GearSetImplementationAnalysisAbstract
    from ._1231 import GearSetImplementationAnalysisDutyCycle
    from ._1232 import GearSetImplementationDetail
else:
    import_structure = {
        "_1216": ["AbstractGearAnalysis"],
        "_1217": ["AbstractGearMeshAnalysis"],
        "_1218": ["AbstractGearSetAnalysis"],
        "_1219": ["GearDesignAnalysis"],
        "_1220": ["GearImplementationAnalysis"],
        "_1221": ["GearImplementationAnalysisDutyCycle"],
        "_1222": ["GearImplementationDetail"],
        "_1223": ["GearMeshDesignAnalysis"],
        "_1224": ["GearMeshImplementationAnalysis"],
        "_1225": ["GearMeshImplementationAnalysisDutyCycle"],
        "_1226": ["GearMeshImplementationDetail"],
        "_1227": ["GearSetDesignAnalysis"],
        "_1228": ["GearSetGroupDutyCycle"],
        "_1229": ["GearSetImplementationAnalysis"],
        "_1230": ["GearSetImplementationAnalysisAbstract"],
        "_1231": ["GearSetImplementationAnalysisDutyCycle"],
        "_1232": ["GearSetImplementationDetail"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractGearAnalysis",
    "AbstractGearMeshAnalysis",
    "AbstractGearSetAnalysis",
    "GearDesignAnalysis",
    "GearImplementationAnalysis",
    "GearImplementationAnalysisDutyCycle",
    "GearImplementationDetail",
    "GearMeshDesignAnalysis",
    "GearMeshImplementationAnalysis",
    "GearMeshImplementationAnalysisDutyCycle",
    "GearMeshImplementationDetail",
    "GearSetDesignAnalysis",
    "GearSetGroupDutyCycle",
    "GearSetImplementationAnalysis",
    "GearSetImplementationAnalysisAbstract",
    "GearSetImplementationAnalysisDutyCycle",
    "GearSetImplementationDetail",
)
