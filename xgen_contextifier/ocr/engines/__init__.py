# xgen_contextifier/ocr/engines/__init__.py
"""
OCR Engine Implementations

Each engine implements BaseOCREngine.build_message_content()
for its specific provider's message format.
"""

from xgen_contextifier.ocr.engines.openai_engine import OpenAIOCREngine
from xgen_contextifier.ocr.engines.anthropic_engine import AnthropicOCREngine
from xgen_contextifier.ocr.engines.gemini_engine import GeminiOCREngine
from xgen_contextifier.ocr.engines.bedrock_engine import BedrockOCREngine
from xgen_contextifier.ocr.engines.vllm_engine import VLLMOCREngine
from xgen_contextifier.ocr.engines.tesseract_engine import TesseractOCREngine

__all__ = [
    "OpenAIOCREngine",
    "AnthropicOCREngine",
    "GeminiOCREngine",
    "BedrockOCREngine",
    "VLLMOCREngine",
    "TesseractOCREngine",
]
