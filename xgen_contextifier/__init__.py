# xgen_contextifier/__init__.py
"""
Contextifier v2 — Unified Document Processing Library

A complete rewrite with strict interface contracts, unified pipeline,
and consistent processing across all file formats.

Architecture:
    DocumentProcessor (entry point)
      └── Handler (per format: PDF, DOCX, PPT, Excel, ...)
            └── Pipeline stages (convert → preprocess → extract → postprocess)
                  ├── Converter: binary → format object
                  ├── Preprocessor: clean/transform
                  ├── ContentExtractor: text, images, tables, charts
                  ├── MetadataExtractor: document metadata
                  └── Postprocessor: final assembly & cleanup
      └── Services (shared, injected)
            ├── ImageService: image save/tag generation
            ├── TagService: page/slide/sheet/chart tags
            ├── TableService: table formatting (HTML/MD/Text)
            ├── MetadataService: metadata formatting
            └── StorageBackend: local/cloud file storage
      └── TextChunker (chunking subsystem)
      └── OCR (optional vision-based extraction)

Usage:
    from xgen_contextifier import DocumentProcessor, open_raw

    # AI-friendly view (lightweight, normalized)
    processor = DocumentProcessor()
    text = processor.extract_text("document.pdf")
    chunks = processor.extract_chunks("document.pdf", chunk_size=1000)

    # Raw view (lossless, addressable, WRITABLE — xlsx/docx/pptx)
    raw = open_raw("report.xlsx")
    raw.sheets["Sales"].set_cell("B3", 142)
    raw.save("report-edited.xlsx")     # untouched parts stay byte-identical
"""

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("xgen_contextifier")
except PackageNotFoundError:
    __version__ = "0.0.0-dev"

from xgen_contextifier.document_processor import DocumentProcessor, ChunkResult
from xgen_contextifier.config import ProcessingConfig, ChunkingConfig
from xgen_contextifier.types import ExtractionResult, FileContext, Chunk, ChunkMetadata
from xgen_contextifier.chunking.chunker import TextChunker
from xgen_contextifier.errors import ContextifierError, UnsupportedFormatError
from xgen_contextifier.raw import open_raw
from xgen_contextifier.async_processor import AsyncDocumentProcessor
from xgen_contextifier.cached_processor import CachedDocumentProcessor

__all__ = [
    "__version__",
    # Core
    "DocumentProcessor",
    "AsyncDocumentProcessor",
    "CachedDocumentProcessor",
    "ChunkResult",
    # Config
    "ProcessingConfig",
    "ChunkingConfig",
    # Types
    "ExtractionResult",
    "FileContext",
    "Chunk",
    "ChunkMetadata",
    # Chunking
    "TextChunker",
    # Raw (lossless, writable) access
    "open_raw",
    # Errors
    "ContextifierError",
    "UnsupportedFormatError",
]
