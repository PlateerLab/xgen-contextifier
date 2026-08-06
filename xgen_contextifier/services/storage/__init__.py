# xgen_contextifier/services/storage/__init__.py
"""
Storage — Pluggable Storage Backends

Provides a common interface for persisting files (images, etc.)
to local filesystem or cloud storage.
"""

from xgen_contextifier.services.storage.base import BaseStorageBackend
from xgen_contextifier.services.storage.local import LocalStorageBackend

__all__ = [
    "BaseStorageBackend",
    "LocalStorageBackend",
]
