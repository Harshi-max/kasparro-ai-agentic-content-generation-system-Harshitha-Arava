"""Entry point for the agent pipeline."""
import json
import os
from .agents.orchestrator import Orchestrator


def main():
    base = os.path.dirname(os.path.dirname(__file__))
    input_path = os.path.join(base, "input", "product.json")
    out_dir = os.path.join(base, "output")
    os.makedirs(out_dir, exist_ok=True)

    with open(input_path, "r", encoding="utf-8") as f:
        product = json.load(f)

    orch = Orchestrator()
    outputs = orch.run(product)

    for name, data in outputs.items():
        out_path = os.path.join(out_dir, f"{name}.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Wrote: {out_path}")


if __name__ == "__main__":
    main()
