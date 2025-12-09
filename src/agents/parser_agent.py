"""ParserAgent: normalize and validate the incoming product JSON."""
from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class ParserAgent:
    def parse(self, raw: Dict[str, Any]) -> Dict[str, Any]:
        # Normalize keys and ensure types
        model = {
            "product_name": raw.get("product_name") or raw.get("Product Name"),
            "concentration": raw.get("concentration"),
            "skin_type": raw.get("skin_type"),
            "key_ingredients": raw.get("key_ingredients") or raw.get("Key Ingredients", []),
            "benefits": raw.get("benefits") or raw.get("Benefits", []),
            "how_to_use": raw.get("how_to_use") or raw.get("How to Use"),
            "side_effects": raw.get("side_effects") or raw.get("Side Effects"),
            "price": raw.get("price") or raw.get("Price"),
        }
        # Basic cleaning
        if isinstance(model["key_ingredients"], str):
            model["key_ingredients"] = [x.strip() for x in model["key_ingredients"].split(",")]
        return model
