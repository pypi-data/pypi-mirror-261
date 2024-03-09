"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1389 import DetailedRigidConnectorDesign
    from ._1390 import DetailedRigidConnectorHalfDesign
else:
    import_structure = {
        "_1389": ["DetailedRigidConnectorDesign"],
        "_1390": ["DetailedRigidConnectorHalfDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DetailedRigidConnectorDesign",
    "DetailedRigidConnectorHalfDesign",
)
