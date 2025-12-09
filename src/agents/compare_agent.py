
from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class ComparisonAgent:
    def make_competitor(self, product: Dict[str, Any]) -> Dict[str, Any]:
        competitor = {
            "product_name": f"{product.get('product_name', 'Comp')} - Alternative",
            "key_ingredients": product.get('key_ingredients', [])[:1] + ["Niacinamide"],
            "benefits": ["Brightening", "Hydration"],
            "price": "₹799"
        }
        return competitor
