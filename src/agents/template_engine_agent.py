"""A minimal template engine: resolves template fields via mapping or content blocks."""
import json
from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class TemplateEngineAgent:
    def render(self, template_path: str, context: Dict[str, Any]) -> Dict[str, Any]:
        with open(template_path, 'r', encoding='utf-8') as f:
            tpl = json.load(f)

        out = {"type": tpl.get('type')}
        for field in tpl.get('fields', []):
            name = field['name']
            source = field.get('source')
            if source == 'static':
                val = field.get('value', '').replace('{{product_name}}', context.get('product_name', ''))
            elif source == 'map':
                path = field.get('path')
                # support top-level mapping only for this minimal engine
                val = context.get(path) if isinstance(context.get(path), (list, dict, str)) else context.get(path)
            elif source == 'block':
                # call block function in content_blocks
                block = field.get('block')
                from ..content_blocks import generate_benefits_block, extract_usage_block, generate_faq_questions, compare_ingredients_block
                if block == 'generate_benefits_block':
                    val = generate_benefits_block(context)
                elif block == 'extract_usage_block':
                    val = extract_usage_block(context)
                elif block == 'generate_faq_questions':
                    val = generate_faq_questions(context)
                elif block == 'compare_ingredients_block':
                    # comparison expects two product dicts in context
                    val = compare_ingredients_block(context.get('product'), context.get('competitor'))
                else:
                    val = None
            else:
                val = None
            out[name] = val
        return out
