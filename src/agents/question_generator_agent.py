"""Generates categorized questions/answers from product model."""
from dataclasses import dataclass
from typing import Dict, Any, List


@dataclass
class QuestionGeneratorAgent:
    def generate(self, product: Dict[str, Any]) -> List[Dict[str, str]]:
        # Delegates to content block for simple deterministic generation
        from ..content_blocks import generate_faq_questions

        return generate_faq_questions(product)
