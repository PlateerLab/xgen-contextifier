# xgen_contextifier/pipeline/__init__.py
"""
Pipeline — Processing Pipeline Components

The pipeline defines the strict 5-stage contract that EVERY handler must follow:

    ┌─────────────┐    ┌──────────────┐    ┌───────────────────┐    ┌──────────────────┐    ┌───────────────┐
    │  Converter   │───▶│ Preprocessor │───▶│ MetadataExtractor │───▶│ ContentExtractor │───▶│ Postprocessor │
    │ (binary→obj) │    │ (clean/xform)│    │  (doc properties) │    │ (text/img/tbl/ch) │    │ (assemble)    │
    └─────────────┘    └──────────────┘    └───────────────────┘    └──────────────────┘    └───────────────┘

Key invariants:
- All stages are REQUIRED (use Null implementations for no-ops)
- Each stage has exactly ONE abstract method to implement
- Input/output types are standardized via types.py
- Stages are stateless — all state flows through the data
- Every stage supports validate() for input checking

Exports:
    Abstract bases:
        BaseConverter, BasePreprocessor, BaseMetadataExtractor,
        BaseContentExtractor, BasePostprocessor

    Null implementations (for optional stages):
        NullConverter, NullPreprocessor, NullMetadataExtractor,
        NullContentExtractor, NullPostprocessor

    Data types (re-exported from types):
        PreprocessedData, DocumentMetadata, ExtractionResult
"""

from xgen_contextifier.pipeline.converter import BaseConverter, NullConverter
from xgen_contextifier.pipeline.preprocessor import BasePreprocessor, NullPreprocessor
from xgen_contextifier.pipeline.metadata_extractor import (
    BaseMetadataExtractor,
    NullMetadataExtractor,
)
from xgen_contextifier.pipeline.content_extractor import (
    BaseContentExtractor,
    NullContentExtractor,
)
from xgen_contextifier.pipeline.postprocessor import (
    BasePostprocessor,
    NullPostprocessor,
)

__all__ = [
    # Abstract bases
    "BaseConverter",
    "BasePreprocessor",
    "BaseMetadataExtractor",
    "BaseContentExtractor",
    "BasePostprocessor",
    # Null implementations
    "NullConverter",
    "NullPreprocessor",
    "NullMetadataExtractor",
    "NullContentExtractor",
    "NullPostprocessor",
]
