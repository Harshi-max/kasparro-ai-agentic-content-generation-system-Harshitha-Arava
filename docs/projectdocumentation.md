# Project Documentation

Problem Statement:
- Design and implement a modular agentic automation system that takes a small product dataset and automatically generates structured, machine-readable content pages (FAQ, Product Page, Comparison Page).

Solution Overview:
- A small Python-based agent pipeline. Each agent has one responsibility and passes structured data to the next. The system includes reusable content logic blocks, a structured template engine, and outputs JSON pages.

Scopes & Assumptions:
- Input: a single JSON product file (`input/product.json`).
- No external web calls or research — the system only uses the supplied product data and internally defined fictional competitor data for comparison.
- Minimal dependencies: only the Python standard library.

System Design (mandatory):
- Agents:
  - `ParserAgent`: validates & normalizes the input JSON into an internal model.
  - `QuestionGeneratorAgent`: creates at least 15 categorized Q&A items from the product model.
  - `TemplateEngineAgent`: applies structured templates to produce JSON pages.
  - `ComparisonAgent`: produces a fictional competitor and comparison data.
  - `Orchestrator`: coordinates agent message passing and pipeline execution.
- Data flow: Input JSON -> Parser -> Question Generator -> Template Engine (+ Content Blocks) -> Outputs
- Template format: JSON templates define fields and simple block references. The TemplateEngine resolves fields using content blocks or direct mapping.

Optional diagrams:
- The pipeline is a simple linear orchestration with independent worker agents. (No diagram included to keep repo compact.)

Do not include per-file explanations — the repo is small and self-explanatory.
