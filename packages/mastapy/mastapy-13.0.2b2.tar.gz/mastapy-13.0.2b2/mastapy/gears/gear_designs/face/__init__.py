"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._990 import FaceGearDesign
    from ._991 import FaceGearDiameterFaceWidthSpecificationMethod
    from ._992 import FaceGearMeshDesign
    from ._993 import FaceGearMeshMicroGeometry
    from ._994 import FaceGearMicroGeometry
    from ._995 import FaceGearPinionDesign
    from ._996 import FaceGearSetDesign
    from ._997 import FaceGearSetMicroGeometry
    from ._998 import FaceGearWheelDesign
else:
    import_structure = {
        "_990": ["FaceGearDesign"],
        "_991": ["FaceGearDiameterFaceWidthSpecificationMethod"],
        "_992": ["FaceGearMeshDesign"],
        "_993": ["FaceGearMeshMicroGeometry"],
        "_994": ["FaceGearMicroGeometry"],
        "_995": ["FaceGearPinionDesign"],
        "_996": ["FaceGearSetDesign"],
        "_997": ["FaceGearSetMicroGeometry"],
        "_998": ["FaceGearWheelDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "FaceGearDesign",
    "FaceGearDiameterFaceWidthSpecificationMethod",
    "FaceGearMeshDesign",
    "FaceGearMeshMicroGeometry",
    "FaceGearMicroGeometry",
    "FaceGearPinionDesign",
    "FaceGearSetDesign",
    "FaceGearSetMicroGeometry",
    "FaceGearWheelDesign",
)
