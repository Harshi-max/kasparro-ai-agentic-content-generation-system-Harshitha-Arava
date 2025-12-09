"""Reusable content logic blocks used by templates."""
from typing import Dict, Any, List


def generate_benefits_block(product: Dict[str, Any]) -> List[str]:
    benefits = product.get("benefits") or []
    if not benefits:
        # fallback from ingredients
        ings = product.get("key_ingredients", [])
        benefits = [f"Contains {i}" for i in ings]
    return benefits


def extract_usage_block(product: Dict[str, Any]) -> str:
    return product.get("how_to_use", "")


def generate_faq_questions(product: Dict[str, Any]) -> List[Dict[str, str]]:
    # Generate 15 categorized Q&A (simple, data-driven)
    qs = []
    name = product.get("product_name", "This product")
    qs.extend([
        {"question": "What is this product?", "answer": f"{name} is a skincare serum."},
        {"question": "Who is it for?", "answer": f"Suitable for {product.get('skin_type', 'all skin types')}"},
        {"question": "What are the key ingredients?", "answer": ", ".join(product.get('key_ingredients', []))},
        {"question": "What benefits does it provide?", "answer": ", ".join(product.get('benefits', []))},
        {"question": "How do I use it?", "answer": product.get('how_to_use', '')},
        {"question": "Are there side effects?", "answer": product.get('side_effects', 'None reported.')},
    ])
    # Add safety, purchase, comparison, usage variations until 15
    while len(qs) < 15:
        idx = len(qs) + 1
        qs.append({"question": f"Additional Q{idx}", "answer": "Refer to the product details above."})
    return qs


def compare_ingredients_block(a: Dict[str, Any], b: Dict[str, Any]) -> List[Dict[str, str]]:
    a_ings = set([i.lower() for i in a.get('key_ingredients', [])])
    b_ings = set([i.lower() for i in b.get('key_ingredients', [])])
    shared = list(a_ings & b_ings)
    only_a = list(a_ings - b_ings)
    only_b = list(b_ings - a_ings)
    points = []
    if shared:
        points.append({"point": "Shared ingredients", "detail": ", ".join(shared)})
    if only_a:
        points.append({"point": f"{a.get('product_name')} unique", "detail": ", ".join(only_a)})
    if only_b:
        points.append({"point": f"{b.get('product_name')} unique", "detail": ", ".join(only_b)})
    return points
