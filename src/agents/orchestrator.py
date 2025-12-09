
from dataclasses import dataclass
from typing import Dict, Any
import os

from .parser_agent import ParserAgent
from .question_generator_agent import QuestionGeneratorAgent
from .template_engine_agent import TemplateEngineAgent
from .compare_agent import ComparisonAgent


@dataclass
class Orchestrator:
    def __init__(self):
        self.parser = ParserAgent()
        self.qgen = QuestionGeneratorAgent()
        self.templ = TemplateEngineAgent()
        self.comparer = ComparisonAgent()

    def run(self, raw_product: Dict[str, Any]) -> Dict[str, Any]:
        # 1. Parse
        product = self.parser.parse(raw_product)

        # 2. Generate questions
        faqs = self.qgen.generate(product)

        # 3. Create competitor
        competitor = self.comparer.make_competitor(product)

        # 4. Render templates
        base = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        tpl_dir = os.path.join(base, 'templates')

        # product page
        prod_tpl = os.path.join(tpl_dir, 'product_template.json')
        product_page = self.templ.render(prod_tpl, product)

        # faq page
        faq_tpl = os.path.join(tpl_dir, 'faq_template.json')
        # include product_name in context for static replacement
        faq_context = dict(product)
        faq_context['product_name'] = product.get('product_name')
        faq_page = self.templ.render(faq_tpl, faq_context)
        faq_page['questions'] = faqs

        # comparison page
        comp_tpl = os.path.join(tpl_dir, 'comparison_template.json')
        comp_context = {'product': product, 'competitor': competitor}
        comparison_page = self.templ.render(comp_tpl, comp_context)
        comparison_page['product'] = product
        comparison_page['competitor'] = competitor

        return {
            'faq': faq_page,
            'product_page': product_page,
            'comparison_page': comparison_page
        }
