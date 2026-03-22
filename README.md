---
license: cc-by-sa-4.0
task_categories:
  - text-classification
  - question-answering
language:
  - en
tags:
  - ai
  - machine-learning
  - deep-learning
  - awesome-list
  - ai-tools
  - llm
  - rag
  - agents
  - benchmarks
size_categories:
  - 1K<n<10K
pretty_name: Awesome AI Index
---
# awesome-ai-index

> The definitive Awesome AI Index — weekly-updated archive of tools, models, papers, courses, code, agents, RAG, fine-tuning, and live event concepts for AI engineers & leaders. Daily fresh entries.

[![Stars](https://img.shields.io/github/stars/alpha-one-index/awesome-ai-index?style=social)](https://github.com/alpha-one-index/awesome-ai-index/stargazers)
[![License: CC-BY-SA-4.0](https://img.shields.io/badge/License-CC--BY--SA--4.0-lightgrey.svg)](LICENSE)
[![Weekly Update](https://img.shields.io/badge/updated-weekly-brightgreen)](https://github.com/alpha-one-index/awesome-ai-index/releases)
[![Data Version](https://img.shields.io/badge/data--version-1.0.0-blue)](https://github.com/alpha-one-index/awesome-ai-index/releases/tag/v1.0.0)
[![Validate](https://github.com/alpha-one-index/awesome-ai-index/actions/workflows/validate.yml/badge.svg)](https://github.com/alpha-one-index/awesome-ai-index/actions/workflows/validate.yml)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Dataset-yellow)](https://huggingface.co/datasets/alpha-one-index/awesome-ai-index)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Kaggle](https://img.shields.io/badge/Kaggle-Dataset-blue)](https://www.kaggle.com/datasets/alphaoneindex/ai-vendor-risk-index)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Downloads](https://img.shields.io/github/downloads/alpha-one-index/awesome-ai-index/total)](https://github.com/alpha-one-index/awesome-ai-index/releases)
[![Last Updated](https://img.shields.io/badge/last%20updated-March%202026-blue)](#)

**Download data:** [`ai-index.json`](https://github.com/alpha-one-index/awesome-ai-index/releases/latest/download/ai-index.json) | [`events.csv`](https://github.com/alpha-one-index/awesome-ai-index/releases/latest/download/events.csv)

Machine-readable JSON. No paywalls. Updated every Friday via GitHub Actions.

**Full reports, vendor deep-dives, and premium data:** [alphaoneindex.com](https://alphaoneindex.com) | [AI Vendor Risk Index](https://github.com/alpha-one-index/ai-vendor-risk-index)

---

## Table of Contents

- [What's Inside](#whats-inside)
- [Why This Exists](#why-this-exists)
- [Quick Start](#quick-start)
- [Top Open Models](#top-open-models)
- [Top Proprietary Models](#top-proprietary-models)
- [Agent Frameworks](#agent-frameworks)
- [RAG Frameworks & Tools](#rag-frameworks--tools)
- [Fine-Tuning Tools](#fine-tuning-tools)
- [Inference Optimization](#inference-optimization)
- [Vector Databases](#vector-databases)
- [LLM Orchestration](#llm-orchestration)
- [Prompt Engineering](#prompt-engineering)
- [AI Code Assistants](#ai-code-assistants)
- [AI Image Generation](#ai-image-generation)
- [AI Video Generation](#ai-video-generation)
- [AI Audio & Speech](#ai-audio--speech)
- [AI Search Engines](#ai-search-engines)
- [Evaluation & Benchmarks](#evaluation--benchmarks)
- [Datasets for Training](#datasets-for-training)
- [AI Safety & Alignment](#ai-safety--alignment)
- [AI Ethics & Governance](#ai-ethics--governance)
- [Compliance Frameworks](#compliance-frameworks)
- [MLOps & Model Serving](#mlops--model-serving)
- [Cloud AI Platforms](#cloud-ai-platforms)
- [Edge AI & On-Device](#edge-ai--on-device)
- [AI Hardware](#ai-hardware)
- [Free AI Courses](#free-ai-courses)
- [AI Research Labs](#ai-research-labs)
- [AI Conferences & Events](#ai-conferences--events)
- [Latest Papers (Weekly Updated)](#latest-papers-weekly-updated)
- [Production Tools & APIs](#production-tools--apis)
- [AI for Science](#ai-for-science)
- [AI for Healthcare](#ai-for-healthcare)
- [AI for Finance](#ai-for-finance)
- [AI for Robotics](#ai-for-robotics)
- [Multimodal AI](#multimodal-ai)
- [Vendor Profiles](#vendor-profiles)
- [Use as an API](#use-as-an-api)
- [Academic Citation](#academic-citation)
- [Contributing](#contributing)
- [Related Projects](#related-projects)
- [License](#license)

---

## What's Inside

| Dataset | Records | Format | Updated |
|---------|---------|--------|---------|
| [AI Models](data/models/) | 130+ | JSON | Weekly |
| [Vendors](data/vendors/) | 40+ | JSON | Weekly |
| [Benchmarks](data/benchmarks/) | 12+ | JSON | Monthly |
| [Compliance Frameworks](data/frameworks/) | 7 | JSON | Quarterly |

## Why This Exists

No single open-source repository covers the full AI ecosystem stack:
- **Models** with real benchmark scores (MMLU, GPQA Diamond, HumanEval, SWE-bench)
- **Vendors** with HQ, founding year, licensing, EU AI Act risk tier
- **Benchmarks** with methodology, saturation signals, and citation counts
- **Compliance** mapping (EU AI Act, NIST AI RMF, ISO 42001, NTIA SBOM)

This repo is that missing layer.

## Quick Start

```bash
# Get all models as JSON
curl https://raw.githubusercontent.com/alpha-one-index/awesome-ai-index/main/data/models/models.json

# Get all vendors as JSON
curl https://raw.githubusercontent.com/alpha-one-index/awesome-ai-index/main/data/vendors/vendors.json

# Get benchmarks
curl https://raw.githubusercontent.com/alpha-one-index/awesome-ai-index/main/data/benchmarks/benchmarks.json
```

```python
import requests

# Load all models
models = requests.get(
    "https://raw.githubusercontent.com/alpha-one-index/awesome-ai-index/main/data/models/models.json"
).json()

# Filter open-source models with MMLU > 80
open_models = [m for m in models if m.get("license") != "Proprietary" and m.get("mmlu", 0) > 80]
print(f"Found {len(open_models)} open-source models with MMLU > 80")
```

---

## Top Open Models

<details>
<summary>Click to expand — 30+ open-weight models ranked by performance</summary>

| Model | Vendor | Parameters | MMLU | GPQA Diamond | HumanEval | License | Release |
|-------|--------|-----------|------|-------------|-----------|---------|--------|
| Qwen 3.5 | Alibaba | 72B | 88.4 | 88.4 | 92.1 | Apache-2.0 | 2026-02 |
| DeepSeek R1 | DeepSeek | 671B MoE | 90.8 | 71.5 | 89.2 | MIT | 2025-01 |
| Llama 4 Scout | Meta | 109B MoE | 84.2 | 74.2 | 87.4 | Llama 4 | 2025-04 |
| Llama 4 Maverick | Meta | 400B MoE | 88.3 | 78.5 | 91.1 | Llama 4 | 2025-04 |
| Mistral Large 3 | Mistral AI | 123B | 86.5 | 68.0 | 88.7 | MRL-0.1 | 2025-03 |
| Gemma 3 27B | Google | 27B | 82.1 | 62.4 | 84.5 | Gemma | 2025-03 |
| Command R+ | Cohere | 104B | 81.5 | 58.2 | 79.3 | CC-BY-NC-4.0 | 2024-04 |
| Phi-4 | Microsoft | 14B | 84.8 | 56.1 | 82.6 | MIT | 2024-12 |
| DBRX | Databricks | 132B MoE | 73.7 | 45.2 | 70.1 | Databricks Open | 2024-03 |
| Yi-Lightning | 01.AI | 200B MoE | 82.0 | 55.8 | 80.4 | Apache-2.0 | 2024-11 |
| Falcon-180B | TII | 180B | 70.5 | 38.1 | 65.3 | Falcon-180B TII | 2023-09 |
| Mixtral 8x22B | Mistral AI | 176B MoE | 77.8 | 45.6 | 75.2 | Apache-2.0 | 2024-04 |
| OLMo 2 | AI2 | 32B | 75.4 | 42.1 | 72.8 | Apache-2.0 | 2025-02 |
| StarCoder2 | BigCode | 15B | - | - | 46.3 | BigCode OpenRAIL-M | 2024-02 |
| Jamba 1.5 | AI21 Labs | 398B MoE | 80.2 | 52.4 | 78.1 | Jamba Open | 2024-08 |
| InternLM3 | Shanghai AI Lab | 8B | 77.3 | 48.5 | 76.4 | Apache-2.0 | 2025-01 |
| MAP-Neo | M-A-P | 7B | 58.2 | 32.1 | 45.6 | Apache-2.0 | 2024-05 |
| Sailor2 | Sea AI Lab | 20B | 68.5 | 38.4 | 62.1 | Apache-2.0 | 2024-12 |
| SmolLM2 | HuggingFace | 1.7B | 55.1 | 28.3 | 42.5 | Apache-2.0 | 2024-11 |
| Granite 3.1 | IBM | 8B | 72.8 | 42.1 | 68.4 | Apache-2.0 | 2024-12 |
| Nemotron-4 | NVIDIA | 340B | 78.7 | 50.3 | 76.2 | NVIDIA Open | 2024-06 |
| Grok-1 | xAI | 314B MoE | 73.0 | 40.2 | 63.2 | Apache-2.0 | 2024-03 |
| Solar | Upstage | 10.7B | 66.2 | 35.4 | 58.1 | Apache-2.0 | 2023-12 |
| Baichuan 4 | Baichuan | 70B | 78.5 | 48.2 | 74.3 | Baichuan | 2024-10 |
| Qwen 2.5 Coder | Alibaba | 32B | - | - | 65.9 | Apache-2.0 | 2024-11 |
| CodeLlama | Meta | 70B | - | - | 67.8 | Llama 2 | 2023-08 |
| Arctic | Snowflake | 480B MoE | 67.3 | 36.8 | 64.5 | Apache-2.0 | 2024-04 |
| WizardLM-2 | Microsoft | 8x22B | 75.2 | 44.1 | 73.8 | Llama 2 | 2024-04 |
| Zephyr | HuggingFace | 7B | 61.4 | 32.5 | 55.2 | MIT | 2023-10 |
| TinyLlama | Community | 1.1B | 25.3 | 12.1 | 18.4 | Apache-2.0 | 2024-01 |

> Full dataset: [data/models/models.json](data/models/models.json)

</details>

---

## Top Proprietary Models

<details>
<summary>Click to expand — Leading closed-source models</summary>

| Model | Vendor | Arena Score | MMLU | GPQA Diamond | Context | Pricing (1M tokens) |
|-------|--------|-------------|------|-------------|---------|--------------------|
| Claude Opus 4.6 | Anthropic | 2002 | 91.5 | 91.5 | 200K | $15 / $75 |
| Gemini 3.1 Pro | Google | 1855 | 90.8 | 90.8 | 2M | $1.25 / $5 |
| GPT-5.4 | OpenAI | 1665 | 92.0 | 92.0 | 128K | $5 / $15 |
| Kimi K2.5 | Moonshot AI | 1447 | 87.6 | 87.6 | 128K | $0.80 / $2.40 |
| Claude 3.5 Sonnet | Anthropic | 1285 | 88.7 | 65.0 | 200K | $3 / $15 |
| Gemini 1.5 Pro | Google | 1280 | 86.5 | 59.1 | 2M | $1.25 / $5 |
| GPT-4o | OpenAI | 1248 | 88.7 | 53.6 | 128K | $2.50 / $10 |
| o3-mini | OpenAI | 1300 | 87.2 | 79.7 | 200K | $1.10 / $4.40 |
| Grok 3 | xAI | 1402 | 88.1 | 81.2 | 128K | $3 / $15 |
| Reka Core | Reka | 1185 | 82.4 | 48.5 | 128K | $3 / $15 |

</details>

---

## Agent Frameworks

<details>
<summary>Click to expand — Tools for building autonomous AI agents</summary>

| Framework | Stars | Language | Key Features | License |
|-----------|-------|----------|-------------|--------|
| [LangGraph](https://github.com/langchain-ai/langgraph) | 8.5K+ | Python | Stateful multi-agent workflows, cycles, persistence | MIT |
| [CrewAI](https://github.com/joaomdmoura/crewAI) | 25K+ | Python | Role-based agents, task delegation, tool use | MIT |
| [AutoGen](https://github.com/microsoft/autogen) | 38K+ | Python | Multi-agent conversation, code execution | CC-BY-4.0 |
| [OpenAI Swarm](https://github.com/openai/swarm) | 18K+ | Python | Lightweight multi-agent orchestration | MIT |
| [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 23K+ | C#/Python | Enterprise AI orchestration, plugins | MIT |
| [Haystack](https://github.com/deepset-ai/haystack) | 18K+ | Python | LLM pipelines, RAG, agents | Apache-2.0 |
| [Pydantic AI](https://github.com/pydantic/pydantic-ai) | 8K+ | Python | Type-safe agent framework | MIT |
| [Agno](https://github.com/agno-agi/agno) | 20K+ | Python | Lightweight agent toolkit | Apache-2.0 |
| [Camel](https://github.com/camel-ai/camel) | 6K+ | Python | Communicative agents, role-playing | Apache-2.0 |
| [MetaGPT](https://github.com/geekan/MetaGPT) | 48K+ | Python | Multi-agent meta-programming | MIT |
| [BabyAGI](https://github.com/yoheinakajima/babyagi) | 20K+ | Python | Task-driven autonomous agent | MIT |
| [SuperAGI](https://github.com/TransformerOptimus/SuperAGI) | 16K+ | Python | Open-source AGI framework | MIT |
| [ChatDev](https://github.com/OpenBMB/ChatDev) | 26K+ | Python | Virtual software company agents | Apache-2.0 |
| [Langroid](https://github.com/langroid/langroid) | 3K+ | Python | Multi-agent LLM programming | MIT |
| [Atomic Agents](https://github.com/BrainBlend-AI/atomic-agents) | 2K+ | Python | Modular agent components | MIT |

</details>

---

## RAG Frameworks & Tools

<details>
<summary>Click to expand — Retrieval-Augmented Generation ecosystem</summary>

| Tool | Stars | Focus | Key Features | License |
|------|-------|-------|-------------|--------|
| [LlamaIndex](https://github.com/run-llama/llama_index) | 38K+ | Python | Data connectors, indices, query engines | MIT |
| [LangChain](https://github.com/langchain-ai/langchain) | 100K+ | Python/JS | Chains, agents, RAG pipelines | MIT |
| [Haystack](https://github.com/deepset-ai/haystack) | 18K+ | Python | Production RAG pipelines | Apache-2.0 |
| [RAGFlow](https://github.com/infiniflow/ragflow) | 35K+ | Python | Deep document understanding RAG | Apache-2.0 |
| [Verba](https://github.com/weaviate/Verba) | 6K+ | Python | RAG chatbot with Weaviate | BSD-3 |
| [Embedchain](https://github.com/embedchain/embedchain) | 10K+ | Python | RAG framework for any data source | Apache-2.0 |
| [PrivateGPT](https://github.com/zylon-ai/private-gpt) | 55K+ | Python | Private RAG with local LLMs | Apache-2.0 |
| [Vanna](https://github.com/vanna-ai/vanna) | 12K+ | Python | RAG for SQL databases | MIT |
| [R2R](https://github.com/SciPhi-AI/R2R) | 4K+ | Python | Production-ready RAG engine | MIT |
| [Cognita](https://github.com/truefoundry/cognita) | 4K+ | Python | Open-source RAG framework | Apache-2.0 |
| [FlashRAG](https://github.com/RUC-NLPIR/FlashRAG) | 2K+ | Python | RAG benchmark toolkit | MIT |
| [Canopy](https://github.com/pinecone-io/canopy) | 1K+ | Python | RAG with Pinecone | Apache-2.0 |

</details>

---

## Fine-Tuning Tools

<details>
<summary>Click to expand — Tools for customizing and fine-tuning LLMs</summary>

| Tool | Stars | Focus | License |
|------|-------|-------|---------|
| [Unsloth](https://github.com/unslothai/unsloth) | 25K+ | 2x faster fine-tuning, 80% less memory | Apache-2.0 |
| [Axolotl](https://github.com/OpenAccess-AI-Collective/axolotl) | 8K+ | Multi-GPU fine-tuning framework | Apache-2.0 |
| [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) | 42K+ | Easy fine-tuning for 100+ LLMs | Apache-2.0 |
| [PEFT](https://github.com/huggingface/peft) | 17K+ | Parameter-efficient fine-tuning (LoRA, QLoRA) | Apache-2.0 |
| [TRL](https://github.com/huggingface/trl) | 11K+ | RLHF, DPO, PPO training | Apache-2.0 |
| [Lit-GPT](https://github.com/Lightning-AI/litgpt) | 11K+ | Pretrain, fine-tune, deploy 20+ LLMs | Apache-2.0 |
| [Ludwig](https://github.com/ludwig-ai/ludwig) | 11K+ | Declarative deep learning framework | Apache-2.0 |
| [Mergekit](https://github.com/arcee-ai/mergekit) | 5K+ | Model merging toolkit | LGPL-3.0 |
| [Torchtune](https://github.com/pytorch/torchtune) | 5K+ | PyTorch-native fine-tuning | BSD-3 |
| [Liger Kernel](https://github.com/linkedin/Liger-Kernel) | 4K+ | Efficient Triton kernels for LLM training | BSD-2 |

</details>

---

## Inference Optimization

<details>
<summary>Click to expand — Tools for fast, efficient LLM inference</summary>

| Tool | Stars | Focus | License |
|------|-------|-------|---------|
| [vLLM](https://github.com/vllm-project/vllm) | 42K+ | High-throughput LLM serving with PagedAttention | Apache-2.0 |
| [llama.cpp](https://github.com/ggerganov/llama.cpp) | 75K+ | CPU/GPU inference in C/C++ | MIT |
| [Ollama](https://github.com/ollama/ollama) | 110K+ | Run LLMs locally with one command | MIT |
| [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) | 10K+ | NVIDIA-optimized inference | Apache-2.0 |
| [SGLang](https://github.com/sgl-project/sglang) | 8K+ | Structured generation language for LLMs | Apache-2.0 |
| [ExLlamaV2](https://github.com/turboderp/exllamav2) | 4K+ | Fast GPTQ/EXL2 inference | MIT |
| [MLC LLM](https://github.com/mlc-ai/mlc-llm) | 20K+ | Universal LLM deployment on any device | Apache-2.0 |
| [Text Generation Inference](https://github.com/huggingface/text-generation-inference) | 10K+ | Production LLM serving by HuggingFace | HFOIL-1.0 |
| [LMDeploy](https://github.com/InternLM/lmdeploy) | 5K+ | Efficient LLM deployment toolkit | Apache-2.0 |
| [DeepSpeed-MII](https://github.com/microsoft/DeepSpeed-MII) | 2K+ | Low-latency model inference | Apache-2.0 |
| [PowerInfer](https://github.com/SJTU-IPADS/PowerInfer) | 8K+ | Fast LLM serving on consumer GPUs | Apache-2.0 |
| [GGML](https://github.com/ggerganov/ggml) | 11K+ | Tensor library for ML | MIT |

</details>

---

## Vector Databases

<details>
<summary>Click to expand — Databases optimized for embedding storage and similarity search</summary>

| Database | Stars | Type | Key Features | License |
|----------|-------|------|-------------|--------|
| [Milvus](https://github.com/milvus-io/milvus) | 32K+ | Distributed | GPU-accelerated, hybrid search | Apache-2.0 |
| [Qdrant](https://github.com/qdrant/qdrant) | 22K+ | Cloud-native | Rust-based, filtering, payload | Apache-2.0 |
| [Weaviate](https://github.com/weaviate/weaviate) | 12K+ | Cloud-native | GraphQL API, modules | BSD-3 |
| [ChromaDB](https://github.com/chroma-core/chroma) | 16K+ | Embedded | Simple API, Python-first | Apache-2.0 |
| [Pinecone](https://www.pinecone.io/) | SaaS | Managed | Serverless, hybrid search | Proprietary |
| [pgvector](https://github.com/pgvector/pgvector) | 13K+ | Extension | PostgreSQL vector search | PostgreSQL |
| [LanceDB](https://github.com/lancedb/lancedb) | 5K+ | Embedded | Serverless, multimodal | Apache-2.0 |
| [Vespa](https://github.com/vespa-engine/vespa) | 6K+ | Distributed | Real-time serving, ranking | Apache-2.0 |
| [Marqo](https://github.com/marqo-ai/marqo) | 5K+ | Cloud-native | Tensor search, multimodal | Apache-2.0 |
| [FAISS](https://github.com/facebookresearch/faiss) | 32K+ | Library | GPU-optimized similarity search | MIT |

</details>

---

## LLM Orchestration

<details>
<summary>Click to expand — Frameworks for building LLM applications</summary>

| Tool | Stars | Focus | License |
|------|-------|-------|---------|
| [LangChain](https://github.com/langchain-ai/langchain) | 100K+ | Full-stack LLM application framework | MIT |
| [LlamaIndex](https://github.com/run-llama/llama_index) | 38K+ | Data-aware LLM applications | MIT |
| [DSPy](https://github.com/stanfordnlp/dspy) | 22K+ | Programming (not prompting) LMs | MIT |
| [Guidance](https://github.com/guidance-ai/guidance) | 19K+ | Structured output generation | MIT |
| [Instructor](https://github.com/jxnl/instructor) | 9K+ | Structured data extraction from LLMs | MIT |
| [Outlines](https://github.com/outlines-dev/outlines) | 10K+ | Structured generation for LLMs | Apache-2.0 |
| [Mastra](https://github.com/mastra-ai/mastra) | 10K+ | TypeScript AI framework | MIT |
| [Mirascope](https://github.com/Mirascope/mirascope) | 2K+ | Pythonic LLM toolkit | MIT |
| [LiteLLM](https://github.com/BerriAI/litellm) | 16K+ | Unified API for 100+ LLM providers | MIT |
| [Portkey](https://github.com/Portkey-AI/gateway) | 6K+ | AI gateway for LLM routing | MIT |

</details>

---

## Prompt Engineering

<details>
<summary>Click to expand — Resources and tools for effective prompting</summary>

| Resource | Type | Description |
|----------|------|------------|
| [Prompt Engineering Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) | Guide | Comprehensive prompt engineering techniques |
| [LangChain Hub](https://smith.langchain.com/hub) | Hub | Community prompt templates |
| [OpenAI Cookbook](https://github.com/openai/openai-cookbook) | Examples | Official prompt patterns and recipes |
| [Anthropic Prompt Library](https://docs.anthropic.com/en/prompt-library) | Library | Curated prompt examples for Claude |
| [Chain-of-Thought Hub](https://github.com/FranxYao/chain-of-thought-hub) | Research | CoT reasoning benchmarks |
| [Fabric](https://github.com/danielmiessler/fabric) | Tool | AI-augmented prompt patterns |
| [PromptBench](https://github.com/microsoft/promptbench) | Benchmark | Evaluating prompt robustness |
| [DSPy](https://github.com/stanfordnlp/dspy) | Framework | Programmatic prompt optimization |

</details>

---

## AI Code Assistants

<details>
<summary>Click to expand — AI-powered coding tools</summary>

| Tool | Type | Model | Pricing | Key Features |
|------|------|-------|---------|--------------|
| [GitHub Copilot](https://github.com/features/copilot) | IDE Extension | GPT-4o/Claude | $10-39/mo | Inline completion, chat, workspace |
| [Cursor](https://cursor.sh/) | IDE | Multi-model | $20/mo | Fork of VS Code with AI-native editing |
| [Windsurf](https://codeium.com/windsurf) | IDE | Cascade | $10/mo | Agentic IDE with Flows |
| [Cline](https://github.com/cline/cline) | Extension | Multi-model | Free (OSS) | Autonomous coding agent in VS Code |
| [Aider](https://github.com/paul-gauthier/aider) | CLI | Multi-model | Free (OSS) | AI pair programming in terminal |
| [Continue](https://github.com/continuedev/continue) | Extension | Multi-model | Free (OSS) | Open-source Copilot alternative |
| [Tabnine](https://www.tabnine.com/) | Extension | Custom | $12/mo | Privacy-focused, on-prem option |
| [Amazon Q Developer](https://aws.amazon.com/q/developer/) | IDE/CLI | Amazon | Free tier | AWS-integrated code assistant |
| [Devin](https://devin.ai/) | Agent | Custom | $500/mo | Autonomous software engineer |
| [OpenHands](https://github.com/All-Hands-AI/OpenHands) | Agent | Multi-model | Free (OSS) | Open-source Devin alternative |
| [SWE-agent](https://github.com/princeton-nlp/SWE-agent) | Agent | Multi-model | Free (OSS) | Autonomous bug fixing |
| [Bolt.new](https://bolt.new/) | Web | Multi-model | Freemium | Full-stack app generation |

</details>

---

## AI Image Generation

<details>
<summary>Click to expand — Image generation models and tools</summary>

| Model/Tool | Vendor | Type | License |
|-----------|--------|------|---------|
| [DALL-E 3](https://openai.com/dall-e-3) | OpenAI | API | Proprietary |
| [Midjourney v6](https://www.midjourney.com/) | Midjourney | SaaS | Proprietary |
| [Stable Diffusion 3](https://stability.ai/) | Stability AI | Open | Stability Community |
| [FLUX.1](https://github.com/black-forest-labs/flux) | Black Forest Labs | Open | Apache-2.0 |
| [Imagen 3](https://deepmind.google/technologies/imagen-3/) | Google | API | Proprietary |
| [Ideogram 2.0](https://ideogram.ai/) | Ideogram | SaaS | Proprietary |
| [ComfyUI](https://github.com/comfyanonymous/ComfyUI) | Community | Tool | GPL-3.0 |
| [Automatic1111](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | Community | Tool | AGPL-3.0 |
| [Fooocus](https://github.com/lllyasviel/Fooocus) | Community | Tool | GPL-3.0 |
| [InvokeAI](https://github.com/invoke-ai/InvokeAI) | Community | Tool | Apache-2.0 |

</details>

---

## AI Video Generation

<details>
<summary>Click to expand — Video generation and editing models</summary>

| Model/Tool | Vendor | Type | Key Features |
|-----------|--------|------|--------------|
| [Sora](https://openai.com/sora) | OpenAI | API | Text-to-video, editing |
| [Veo 2](https://deepmind.google/technologies/veo/) | Google | API | 4K video generation |
| [Kling](https://klingai.com/) | Kuaishou | SaaS | Motion brush, lip sync |
| [Runway Gen-3](https://runwayml.com/) | Runway | SaaS | Multi-modal video gen |
| [Pika 2.0](https://pika.art/) | Pika | SaaS | Cinematic video gen |
| [Luma Dream Machine](https://lumalabs.ai/) | Luma AI | SaaS | Fast video generation |
| [CogVideo](https://github.com/THUDM/CogVideo) | Tsinghua | Open | Open-source text-to-video |
| [AnimateDiff](https://github.com/guoyww/AnimateDiff) | Community | Open | Animation from images |
| [Wan](https://github.com/Wan-Video/Wan2.1) | Alibaba | Open | Open-source video model |

</details>

---

## AI Audio & Speech

<details>
<summary>Click to expand — Speech, music, and audio AI tools</summary>

| Tool | Type | Focus | License |
|------|------|-------|---------|
| [Whisper](https://github.com/openai/whisper) | Model | Speech-to-text | MIT |
| [Bark](https://github.com/suno-ai/bark) | Model | Text-to-speech, multilingual | MIT |
| [Coqui TTS](https://github.com/coqui-ai/TTS) | Model | Text-to-speech | MPL-2.0 |
| [Eleven Labs](https://elevenlabs.io/) | SaaS | Voice cloning, TTS | Proprietary |
| [Suno](https://suno.com/) | SaaS | Music generation | Proprietary |
| [Udio](https://www.udio.com/) | SaaS | Music generation | Proprietary |
| [MusicGen](https://github.com/facebookresearch/audiocraft) | Model | Music generation | MIT |
| [Faster Whisper](https://github.com/SYSTRAN/faster-whisper) | Tool | Fast speech recognition | MIT |
| [WhisperX](https://github.com/m-bain/whisperX) | Tool | Whisper with word alignment | BSD-4 |
| [Parler TTS](https://github.com/huggingface/parler-tts) | Model | Controllable TTS | Apache-2.0 |
| [Fish Speech](https://github.com/fishaudio/fish-speech) | Model | Multilingual TTS | CC-BY-NC-SA-4.0 |

</details>

---

## AI Search Engines

<details>
<summary>Click to expand — AI-powered search and answer engines</summary>

| Engine | Type | Key Features |
|--------|------|--------------|
| [Perplexity](https://perplexity.ai/) | SaaS | Citation-backed AI answers, Pro Search |
| [You.com](https://you.com/) | SaaS | AI search with apps and agents |
| [Phind](https://phind.com/) | SaaS | Developer-focused AI search |
| [Tavily](https://tavily.com/) | API | Search API optimized for AI agents |
| [Exa](https://exa.ai/) | API | Neural search API for embeddings |
| [SearXNG](https://github.com/searxng/searxng) | Self-hosted | Privacy-respecting metasearch | 
| [Kagi](https://kagi.com/) | SaaS | Premium ad-free search with AI |
| [Brave Search](https://search.brave.com/) | SaaS | Independent index with AI answers |

</details>

---

## Evaluation & Benchmarks

<details>
<summary>Click to expand — LLM evaluation tools and benchmark suites</summary>

| Benchmark/Tool | Focus | Metrics | Source |
|---------------|-------|---------|--------|
| [MMLU](https://github.com/hendrycks/test) | Knowledge | 57 subjects, 15K questions | Hendrycks et al. |
| [GPQA Diamond](https://arxiv.org/abs/2311.12022) | Expert reasoning | PhD-level science questions | NYU |
| [HumanEval](https://github.com/openai/human-eval) | Code generation | Pass@k on 164 problems | OpenAI |
| [SWE-bench](https://www.swebench.com/) | Real software engineering | GitHub issue resolution | Princeton |
| [Chatbot Arena](https://chat.lmsys.org/) | Human preference | Elo ratings from blind comparisons | LMSYS |
| [MATH](https://github.com/hendrycks/math) | Mathematics | 12.5K competition math problems | Hendrycks et al. |
| [BigBench](https://github.com/google/BIG-bench) | Diverse tasks | 200+ language tasks | Google |
| [MT-Bench](https://github.com/lm-sys/FastChat) | Multi-turn chat | GPT-4 judged conversations | LMSYS |
| [AlpacaEval](https://github.com/tatsu-lab/alpaca_eval) | Instruction following | Win rate vs reference model | Stanford |
| [IFEval](https://arxiv.org/abs/2311.07911) | Instruction following | Verifiable instruction adherence | Google |
| [Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) | Aggregate | Multiple benchmarks combined | HuggingFace |
| [LM Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness) | Framework | 200+ tasks, unified eval | EleutherAI |
| [HELM](https://crfm.stanford.edu/helm/) | Holistic | 42 scenarios, 7 metrics | Stanford |
| [Agentic Benchmarks](https://github.com/SWE-bench) | Agent capability | Real-world task completion | Various |

</details>

---

## Datasets for Training

<details>
<summary>Click to expand — Key datasets for LLM pre-training and fine-tuning</summary>

| Dataset | Size | Focus | License |
|---------|------|-------|---------|
| [FineWeb](https://huggingface.co/datasets/HuggingFaceFW/fineweb) | 15T tokens | Web text, deduplicated | ODC-By |
| [RedPajama v2](https://github.com/togethercomputer/RedPajama-Data) | 30T tokens | Web crawl + curated | Apache-2.0 |
| [The Stack v2](https://huggingface.co/datasets/bigcode/the-stack-v2) | 67.5TB | Source code, 600+ languages | Various |
| [OASST2](https://huggingface.co/datasets/OpenAssistant/oasst2) | 91K convos | Human feedback dialogues | Apache-2.0 |
| [UltraChat](https://github.com/thunlp/UltraChat) | 1.5M convos | Synthetic multi-turn chat | MIT |
| [SlimPajama](https://huggingface.co/datasets/cerebras/SlimPajama-627B) | 627B tokens | Deduplicated RedPajama | Apache-2.0 |
| [Dolma](https://github.com/allenai/dolma) | 3T tokens | Multi-source pretraining | AI2 ImpACT |
| [LMSYS-Chat-1M](https://huggingface.co/datasets/lmsys/lmsys-chat-1m) | 1M convos | Real user LLM conversations | CC-BY-NC-4.0 |
| [OpenHermes 2.5](https://huggingface.co/datasets/teknium/OpenHermes-2.5) | 1M samples | Curated instruction data | CC-BY-4.0 |
| [WildChat](https://huggingface.co/datasets/allenai/WildChat-1M) | 1M convos | Real ChatGPT conversations | AI2 ImpACT |

</details>

---

## AI Safety & Alignment

<details>
<summary>Click to expand — Safety research, red-teaming, and alignment tools</summary>

| Resource | Type | Focus |
|----------|------|-------|
| [Anthropic Research](https://www.anthropic.com/research) | Lab | Constitutional AI, interpretability |
| [ARC Evals](https://evals.alignment.org/) | Evaluations | Dangerous capability assessments |
| [METR](https://metr.org/) | Organization | Model evaluation and threat research |
| [Guardrails AI](https://github.com/guardrails-ai/guardrails) | Tool | Input/output validation for LLMs |
| [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) | Tool | Programmable safety rails |
| [LLM Guard](https://github.com/protectai/llm-guard) | Tool | Security scanning for LLM I/O |
| [Garak](https://github.com/leondz/garak) | Tool | LLM vulnerability scanner |
| [Rebuff](https://github.com/protectai/rebuff) | Tool | Prompt injection detection |
| [HarmBench](https://github.com/centerforaisafety/HarmBench) | Benchmark | Red-teaming evaluation framework |
| [Alignment Forum](https://www.alignmentforum.org/) | Community | AI alignment research discussion |

</details>

---

## AI Ethics & Governance

<details>
<summary>Click to expand — Ethical AI frameworks and governance resources</summary>

| Resource | Organization | Focus |
|----------|-------------|-------|
| [AI Ethics Guidelines](https://www.oecd.org/en/topics/sub-issues/artificial-intelligence.html) | OECD | International AI principles |
| [Responsible AI Practices](https://ai.google/responsibility/) | Google | Industry responsible AI framework |
| [AI Fairness 360](https://github.com/Trusted-AI/AIF360) | IBM | Bias detection and mitigation |
| [Model Cards](https://modelcards.withgoogle.com/) | Google | Model documentation standard |
| [Datasheets for Datasets](https://arxiv.org/abs/1803.09010) | Research | Dataset documentation framework |
| [AI Incident Database](https://incidentdatabase.ai/) | Partnership on AI | Tracking AI failures and harms |
| [NIST AI RMF](https://www.nist.gov/artificial-intelligence) | NIST | US AI risk management framework |
| [EU AI Act](https://artificialintelligenceact.eu/) | European Union | Comprehensive AI regulation |

</details>

---

## Compliance Frameworks

<details>
<summary>Click to expand — Regulatory and compliance frameworks for AI</summary>

| Framework | Jurisdiction | Status | Focus |
|-----------|-------------|--------|-------|
| EU AI Act | European Union | Enforced (2025+) | Risk-based AI regulation |
| NIST AI RMF | United States | Published | AI risk management |
| ISO 42001 | International | Published | AI management systems |
| ISO 23894 | International | Published | AI risk management |
| NTIA SBOM | United States | Published | Software bill of materials |
| OWASP Top 10 for LLMs | International | Published | LLM security risks |
| CycloneDX ML-BOM | International | Published | ML bill of materials |

> Full framework data: [data/frameworks/](data/frameworks/)

</details>

---

## MLOps & Model Serving

<details>
<summary>Click to expand — Tools for deploying and monitoring ML in production</summary>

| Tool | Focus | License |
|------|-------|---------|
| [MLflow](https://github.com/mlflow/mlflow) | Experiment tracking, model registry | Apache-2.0 |
| [Weights & Biases](https://wandb.ai/) | Experiment tracking, hyperparameter sweep | Proprietary |
| [DVC](https://github.com/iterative/dvc) | Data versioning, model management | Apache-2.0 |
| [BentoML](https://github.com/bentoml/BentoML) | Model serving, deployment | Apache-2.0 |
| [Ray Serve](https://github.com/ray-project/ray) | Scalable model serving | Apache-2.0 |
| [Triton Inference Server](https://github.com/triton-inference-server/server) | High-performance model serving | BSD-3 |
| [Seldon Core](https://github.com/SeldonIO/seldon-core) | Kubernetes ML deployment | Apache-2.0 |
| [Evidently AI](https://github.com/evidentlyai/evidently) | ML monitoring, data drift | Apache-2.0 |
| [Great Expectations](https://github.com/great-expectations/great_expectations) | Data quality validation | Apache-2.0 |
| [Prefect](https://github.com/PrefectHQ/prefect) | ML pipeline orchestration | Apache-2.0 |

</details>

---

## Cloud AI Platforms

<details>
<summary>Click to expand — Managed AI/ML cloud services</summary>

| Platform | Provider | Key Services | Model Access |
|----------|----------|-------------|-------------|
| [AWS SageMaker](https://aws.amazon.com/sagemaker/) | Amazon | Training, deployment, pipelines | Bedrock models |
| [Google Vertex AI](https://cloud.google.com/vertex-ai) | Google | AutoML, training, serving | Gemini, PaLM |
| [Azure AI Studio](https://ai.azure.com/) | Microsoft | Fine-tuning, prompt flow | OpenAI, Llama |
| [Hugging Face Inference](https://huggingface.co/inference-api) | HuggingFace | Serverless API, Endpoints | All HF models |
| [Together AI](https://www.together.ai/) | Together | Fine-tuning, inference | Open models |
| [Fireworks AI](https://fireworks.ai/) | Fireworks | Fast inference API | Open models |
| [Groq](https://groq.com/) | Groq | Ultra-fast LPU inference | Open models |
| [Cerebras](https://cerebras.ai/) | Cerebras | Wafer-scale chip inference | Open models |
| [Replicate](https://replicate.com/) | Replicate | Run models via API | 100K+ models |
| [Modal](https://modal.com/) | Modal | Serverless GPU compute | Any model |
| [Lambda Labs](https://lambdalabs.com/) | Lambda | GPU cloud for ML | Any model |

</details>

---

## Edge AI & On-Device

<details>
<summary>Click to expand — Running AI models on edge devices</summary>

| Tool/Framework | Focus | Platforms | License |
|---------------|-------|----------|---------|
| [llama.cpp](https://github.com/ggerganov/llama.cpp) | Local LLM inference | CPU/GPU/Metal | MIT |
| [Ollama](https://github.com/ollama/ollama) | One-command local models | Mac/Linux/Windows | MIT |
| [LM Studio](https://lmstudio.ai/) | Local LLM desktop app | Mac/Windows/Linux | Proprietary |
| [Jan](https://github.com/janhq/jan) | Open-source local AI | Mac/Windows/Linux | AGPL-3.0 |
| [TensorFlow Lite](https://www.tensorflow.org/lite) | Mobile/edge inference | iOS/Android/Embedded | Apache-2.0 |
| [ONNX Runtime](https://github.com/microsoft/onnxruntime) | Cross-platform inference | All platforms | MIT |
| [Core ML](https://developer.apple.com/machine-learning/) | Apple silicon inference | iOS/macOS | Proprietary |
| [MediaPipe](https://github.com/google/mediapipe) | On-device ML pipelines | Mobile/Web/Desktop | Apache-2.0 |
| [MLC LLM](https://github.com/mlc-ai/mlc-llm) | Universal device deployment | iOS/Android/Web | Apache-2.0 |
| [Executorch](https://github.com/pytorch/executorch) | PyTorch mobile deployment | Mobile/embedded | BSD-3 |

</details>

---

## AI Hardware

<details>
<summary>Click to expand — Chips and hardware for AI training and inference</summary>

| Hardware | Vendor | Type | FLOPS (FP16) | Use Case |
|----------|--------|------|-----------|---------|
| H200 SXM | NVIDIA | GPU | 989 TFLOPS | LLM training |
| H100 SXM | NVIDIA | GPU | 989 TFLOPS | LLM training/inference |
| A100 80GB | NVIDIA | GPU | 312 TFLOPS | LLM training |
| MI300X | AMD | GPU | 1307 TFLOPS | LLM training |
| Gaudi 3 | Intel | Accelerator | 1835 TFLOPS | LLM training |
| TPU v5p | Google | TPU | 459 TFLOPS | LLM training |
| Trainium 2 | AWS | Accelerator | N/A | AWS LLM training |
| LPU | Groq | LPU | N/A | Ultra-low latency inference |
| WT-1 | Cerebras | WSE | N/A | Single-chip neural net |
| M3 Ultra | Apple | SoC | 800 GFLOPS | Local inference |
| RTX 4090 | NVIDIA | GPU | 165.2 TFLOPS | Consumer fine-tuning |

</details>

---

## Free AI Courses

<details>
<summary>Click to expand — Free and high-quality AI learning resources</summary>

| Course | Provider | Topics | Format |
|--------|----------|--------|--------|
| [Fast.ai](https://www.fast.ai/) | Fast.ai | Deep learning, LLMs | Video + notebooks |
| [Hugging Face NLP Course](https://huggingface.co/learn/nlp-course) | HuggingFace | Transformers, NLP | Interactive |
| [DeepLearning.AI Short Courses](https://www.deeplearning.ai/short-courses/) | DeepLearning.AI | LLMOps, agents, RAG | Video |
| [Stanford CS224N](https://web.stanford.edu/class/cs224n/) | Stanford | NLP with Deep Learning | Video + slides |
| [Stanford CS229](https://cs229.stanford.edu/) | Stanford | Machine Learning | Video + notes |
| [MIT 6.S191](https://introtodeeplearning.com/) | MIT | Introduction to Deep Learning | Video |
| [Andrej Karpathy's Zero to Hero](https://karpathy.ai/zero-to-hero.html) | Karpathy | Neural networks from scratch | YouTube |
| [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course) | Google | ML fundamentals | Interactive |
| [Practical Deep Learning](https://course.fast.ai/) | Fast.ai | Applied DL for coders | Notebooks |
| [Microsoft AI for Beginners](https://github.com/microsoft/AI-For-Beginners) | Microsoft | AI fundamentals | GitHub |
| [LLM Bootcamp](https://fullstackdeeplearning.com/llm-bootcamp/) | Full Stack DL | Building LLM apps | Video |
| [Prompt Engineering Course](https://github.com/dair-ai/Prompt-Engineering-Guide) | DAIR.AI | Prompt engineering | Guide |

</details>

---

## AI Research Labs

<details>
<summary>Click to expand — Leading AI research organizations</summary>

| Lab | Type | Focus Areas | Notable Work |
|-----|------|------------|-------------|
| [OpenAI](https://openai.com/research/) | Private | AGI, safety, multimodal | GPT-4, DALL-E, Sora |
| [DeepMind](https://deepmind.com/) | Google | Scientific AI, gaming | AlphaFold, Gemini |
| [Anthropic](https://www.anthropic.com/research) | Private | AI safety, interpretability | Claude, Constitutional AI |
| [Meta AI](https://ai.meta.com/) | Corporate | Open models, translation | Llama, SEAMLESS |
| [Microsoft Research](https://www.microsoft.com/en-us/research/research-area/ai/) | Corporate | AGI, safety, applications | Phi, Orca |
| [EleutherAI](https://eleutherai.org/) | Nonprofit | Open LLMs, transparency | GPT-NeoX, Pythia |
| [AI2](https://allenai.org/) | Nonprofit | Scientific AI, commonsense | OLMo, SPDX |
| [Hugging Face](https://huggingface.co/) | Company | Open AI ecosystem | Transformers, datasets |
| [Mistral AI](https://mistral.ai/) | Private | Efficient open models | Mistral, Mixtral |
| [Cohere](https://cohere.com/) | Private | Enterprise NLP | Command, Embed |
| [Stability AI](https://stability.ai/) | Private | Open generative models | Stable Diffusion |
| [BigScience](https://bigscience.huggingface.co/) | Research | Open, multilingual LLMs | BLOOM |
| [LAION](https://laion.ai/) | Nonprofit | Open datasets | LAION-5B, OpenCLIP |

</details>

---

## AI Conferences & Events

<details>
<summary>Click to expand — Key AI conferences and community events</summary>

| Conference | Focus | Frequency | Location |
|-----------|-------|-----------|----------|
| NeurIPS | ML theory, applications | Annual (Dec) | Rotating |
| ICML | Machine learning | Annual (Jul) | Rotating |
| ICLR | Deep learning | Annual (May) | Rotating |
| CVPR | Computer vision | Annual (Jun) | Rotating |
| ACL/EMNLP/NAACL | NLP | Annual | Rotating |
| AAAI | AI breadth | Annual (Feb) | Rotating |
| AI Engineer Summit | LLM engineering | Annual | San Francisco |
| AI for Good | Social impact AI | Annual | Geneva |
| GTC (NVIDIA) | AI infrastructure | Annual | San Jose |
| Google I/O | Google AI | Annual (May) | Mountain View |
| Microsoft Build | Azure/OpenAI | Annual (May) | Seattle |
| AWS re:Invent | AWS AI services | Annual (Dec) | Las Vegas |

</details>

---

## Latest Papers (Weekly Updated)

<details>
<summary>Click to expand — Notable recent arXiv papers (auto-updated weekly)</summary>

### March 2026

| Paper | Authors | Key Contribution | arXiv |
|-------|---------|-----------------|-------|
| Qwen 3.5 Technical Report | Alibaba | 72B model achieving 88.4 GPQA | [2503.xxxxx](https://arxiv.org) |
| DeepSeek-V3 | DeepSeek | MoE scaling, 671B with 37B active | [2412.19437](https://arxiv.org/abs/2412.19437) |
| Llama 4: Open Foundation Models | Meta | Multi-scale MoE, Scout & Maverick | [2504.xxxxx](https://arxiv.org) |
| Scaling LLM Test-Time Compute | Google | Test-time scaling improves reasoning | [2408.03314](https://arxiv.org/abs/2408.03314) |
| Constitutional AI | Anthropic | RLHF with AI feedback | [2212.08073](https://arxiv.org/abs/2212.08073) |
| Attention Is All You Need | Google | Original transformer paper | [1706.03762](https://arxiv.org/abs/1706.03762) |
| LoRA: Low-Rank Adaptation | Microsoft | Parameter-efficient fine-tuning | [2106.09685](https://arxiv.org/abs/2106.09685) |
| RLHF: Training LMs from Human Feedback | OpenAI | RLHF methodology | [2203.02155](https://arxiv.org/abs/2203.02155) |
| Chain-of-Thought Prompting | Google | CoT reasoning in LLMs | [2201.11903](https://arxiv.org/abs/2201.11903) |
| Retrieval-Augmented Generation | Meta | RAG for knowledge-intensive tasks | [2005.11401](https://arxiv.org/abs/2005.11401) |

> This section is auto-updated weekly via GitHub Actions.

</details>

---

## Production Tools & APIs

<details>
<summary>Click to expand — APIs and platforms for AI in production</summary>

| API/Platform | Provider | Focus | Pricing |
|-------------|----------|-------|---------|
| [OpenAI API](https://platform.openai.com/) | OpenAI | GPT-4, embeddings, DALL-E | Pay-per-token |
| [Anthropic API](https://www.anthropic.com/api) | Anthropic | Claude models | Pay-per-token |
| [Google AI API](https://ai.google.dev/) | Google | Gemini, embeddings | Free tier + pay-per-token |
| [Cohere API](https://cohere.com/) | Cohere | Command, Embed, Rerank | Free tier + pay-per-token |
| [Mistral API](https://mistral.ai/api/) | Mistral | Mistral, Codestral | Pay-per-token |
| [Hugging Face API](https://huggingface.co/inference-api) | HuggingFace | 100K+ models | Free + Serverless |
| [xAI API](https://x.ai/api) | xAI | Grok models | Pay-per-token |
| [Together AI](https://api.together.xyz/) | Together | Open models | Pay-per-token |
| [Groq API](https://console.groq.com/) | Groq | Ultra-fast inference | Free tier |
| [Replicate API](https://replicate.com/docs) | Replicate | 100K+ models | Pay-per-compute |
| [Stability AI API](https://stability.ai/api) | Stability | Image/video generation | Pay-per-gen |

</details>

---

## Multimodal AI

<details>
<summary>Click to expand — Models and tools handling multiple modalities</summary>

| Model | Modalities | Vendor | License |
|-------|-----------|--------|--------|
| GPT-4V / GPT-4o | Text, Image, Audio | OpenAI | Proprietary |
| Gemini 3.1 Ultra | Text, Image, Audio, Video, Code | Google | Proprietary |
| Claude 3 Opus | Text, Image | Anthropic | Proprietary |
| LLaVA-1.6 | Text, Image | Community | Apache-2.0 |
| Qwen-VL | Text, Image, Video | Alibaba | Apache-2.0 |
| Phi-3 Vision | Text, Image | Microsoft | MIT |
| InternVL2 | Text, Image, Video | Shanghai AI Lab | MIT |
| PaliGemma 2 | Text, Image | Google | Gemma |
| CogVLM2 | Text, Image | Tsinghua | Apache-2.0 |
| Idefics3 | Text, Image | HuggingFace | Apache-2.0 |
| Pixtral | Text, Image | Mistral | Apache-2.0 |

</details>

---

## AI for Science

<details>
<summary>Click to expand — AI models and tools for scientific research</summary>

| Tool | Field | Description | License |
|------|-------|-------------|--------|
| [AlphaFold 3](https://github.com/google-deepmind/alphafold3) | Biology | Protein & molecular structure prediction | CC-BY-NC-SA-4.0 |
| [ESMFold](https://github.com/facebookresearch/esm) | Biology | Meta's protein structure prediction | MIT |
| [OpenFold](https://github.com/aqlaboratory/openfold) | Biology | Open-source AlphaFold | Apache-2.0 |
| [NVIDIA BioNeMo](https://www.nvidia.com/en-us/clara/bionemo/) | Biology | Drug discovery foundation models | Proprietary |
| [MatterSim](https://github.com/microsoft/mattersim) | Materials | Universal ML potential for materials | MIT |
| [ClimaX](https://github.com/microsoft/ClimaX) | Climate | Foundation model for weather/climate | MIT |
| [FourCastNet](https://github.com/NVlabs/FourCastNet) | Climate | Fast AI weather forecasting | BSD-3 |
| [GNoME](https://deepmind.google/discover/blog/millions-of-new-materials-discovered-with-deep-learning/) | Materials | DeepMind materials discovery | Research |
| [ChemBERTa](https://github.com/seyonechithrananda/bert-loves-chemistry) | Chemistry | SMILES-based molecular transformers | MIT |

</details>

---

## AI for Healthcare

<details>
<summary>Click to expand — Medical and clinical AI applications</summary>

| Tool | Focus | Organization | Notes |
|------|-------|-------------|-------|
| [Med-PaLM 2](https://ai.google/discover/med-palm/) | Medical QA | Google | Passes USMLE |
| [BioMedGPT](https://github.com/PharMolix/OpenBioMed) | Biomedical NLP | Community | Apache-2.0 |
| [ClinicalBERT](https://github.com/kexinhuang12345/clinicalBERT) | Clinical notes | Research | Apache-2.0 |
| [PathAI](https://www.pathai.com/) | Pathology | PathAI | Proprietary |
| [Paige AI](https://paige.ai/) | Oncology pathology | Paige | FDA-cleared |
| [Tempus](https://www.tempus.com/) | Precision oncology | Tempus | Proprietary |
| [Insilico Medicine](https://insilico.com/) | Drug discovery | Insilico | Proprietary |

</details>

---

## AI for Finance

<details>
<summary>Click to expand — AI tools for financial services</summary>

| Tool | Focus | Notes |
|------|-------|-------|
| [FinBERT](https://github.com/ProsusAI/finBERT) | Financial sentiment | Fine-tuned BERT for finance |
| [BloombergGPT](https://arxiv.org/abs/2303.17564) | Finance NLP | 50B finance-trained LLM |
| [FinGPT](https://github.com/AI4Finance-Foundation/FinGPT) | Finance agent | Open-source financial LLMs |
| [NLP4Finance](https://github.com/AI4Finance-Foundation) | Various | AI for finance research org |
| [Numerai](https://numer.ai/) | Stock prediction | Tournament-based ML hedge fund |

</details>

---

## AI for Robotics

<details>
<summary>Click to expand — Foundation models and tools for robotics</summary>

| Tool | Focus | Organization | License |
|------|-------|-------------|--------|
| [RT-2](https://robotics-transformer2.github.io/) | Vision-language-action | Google DeepMind | Research |
| [OpenVLA](https://github.com/openvla/openvla) | Open vision-language-action | Stanford | MIT |
| [Octo](https://github.com/octo-models/octo) | Generalist robot policy | Berkeley | Apache-2.0 |
| [Isaac ROS](https://github.com/NVIDIA-ISAAC-ROS) | ROS2 GPU acceleration | NVIDIA | NVIDIA Isaac |
| [LeRobot](https://github.com/huggingface/lerobot) | Learning for robots | HuggingFace | Apache-2.0 |
| [Genesis](https://github.com/Genesis-Embodied-AI/Genesis) | Physics simulation | Community | Apache-2.0 |

</details>

---

## Vendor Profiles

<details>
<summary>Click to expand — AI vendor ecosystem overview (40+ vendors tracked)</summary>

| Vendor | HQ | Founded | EU AI Act Tier | Key Models | Licensing |
|--------|-----|---------|----------------|-----------|----------|
| OpenAI | San Francisco, CA | 2015 | High | GPT-4, o3, DALL-E, Sora | Proprietary |
| Anthropic | San Francisco, CA | 2021 | High | Claude 3.5/4 | Proprietary |
| Google DeepMind | London, UK | 1988/2014 | High | Gemini, Veo, AlphaFold | Proprietary/Open |
| Meta AI | Menlo Park, CA | 2003 | High | Llama 4, SeamlessM4T | Llama License |
| Microsoft | Redmond, WA | 1975 | High | Phi, Copilot (OpenAI) | Mixed |
| Mistral AI | Paris, France | 2023 | Limited | Mistral, Mixtral, Codestral | Apache-2.0/MRL |
| Cohere | Toronto, Canada | 2019 | Limited | Command, Embed, Rerank | Proprietary |
| AI21 Labs | Tel Aviv, Israel | 2017 | Limited | Jamba, Jurassic | Jamba Open |
| xAI | San Francisco, CA | 2023 | High | Grok 3 | Proprietary |
| DeepSeek | Hangzhou, China | 2023 | High | DeepSeek-V3, R1 | MIT |
| Alibaba | Hangzhou, China | 1999 | High | Qwen 3.5 | Apache-2.0 |
| Moonshot AI | Beijing, China | 2023 | Limited | Kimi K2.5 | Proprietary |
| Hugging Face | New York, NY | 2016 | N/A | Hub, Transformers | Apache-2.0 |
| Stability AI | London, UK | 2019 | High | Stable Diffusion | Various |
| Midjourney | San Francisco, CA | 2021 | High | Midjourney v6 | Proprietary |

> Full vendor database: [data/vendors/vendors.json](data/vendors/vendors.json)

</details>

---

## Use as an API

All data files are accessible as raw GitHub URLs. Use them as live endpoints:

```python
import requests

BASE = "https://raw.githubusercontent.com/alpha-one-index/awesome-ai-index/main/data"

# Models
models = requests.get(f"{BASE}/models/models.json").json()

# Vendors
vendors = requests.get(f"{BASE}/vendors/vendors.json").json()

# Benchmarks
benchmarks = requests.get(f"{BASE}/benchmarks/benchmarks.json").json()

# Filter open-source models with MMLU > 80
open_models = [
    m for m in models
    if m.get("license") != "Proprietary" and m.get("mmlu", 0) > 80
]
print(f"Found {len(open_models)} qualifying models")
```

---

## Dataset Highlights

### Top Models by Chatbot Arena (March 2026)

| Rank | Model | Vendor | Arena Score | GPQA Diamond | License |
|------|-------|--------|-------------|--------------|--------|
| 1 | Claude Opus 4.6 | Anthropic | 2002 | 91.5 | Proprietary |
| 2 | Gemini 3.1 Pro | Google | 1855 | 90.8 | Proprietary |
| 3 | GPT-5.4 | OpenAI | 1665 | 92.0 | Proprietary |
| 4 | Kimi K2.5 | Moonshot AI | 1447 | 87.6 | Proprietary |
| 5 | Qwen 3.5 | Alibaba | 1443 | 88.4 | Apache-2.0 |
| 6 | DeepSeek R1 | DeepSeek | 1398 | 71.5 | MIT |
| 7 | Llama 4 Scout | Meta | 1320 | 74.2 | Llama 4 |
| 8 | Mistral Large 3 | Mistral AI | 1414 | 68.0 | MRL-0.1 |

> Full dataset with 130+ models: [data/models/models.json](data/models/models.json)

---

## Academic Citation

```bibtex
@dataset{awesome_ai_index_2026,
  title     = {awesome-ai-index: The Definitive Open-Source AI Ecosystem Database},
  author    = {Alpha One Index},
  year      = 2026,
  publisher = {GitHub},
  url       = {https://github.com/alpha-one-index/awesome-ai-index},
  license   = {CC-BY-SA-4.0}
}
```

See also: [CITATION.cff](CITATION.cff)

---

## Schema & Methodology

- [data/schemas/schema.json](data/schemas/schema.json) — Full JSON Schema for validation
- [METHODOLOGY.md](METHODOLOGY.md) — Data collection and scoring methodology
- [ROADMAP.md](ROADMAP.md) — Quarterly roadmap and milestones

---

## Contributing

All contributions welcome! Especially:

- **Vendors**: Self-submit via [Issue: Add Vendor](https://github.com/alpha-one-index/awesome-ai-index/issues/new?template=add-vendor.yml)
- **Models**: New models or updated benchmarks via [Issue: Add Model](https://github.com/alpha-one-index/awesome-ai-index/issues/new?template=add-model.yml)
- **Data corrections**: [Issue: Data Correction](https://github.com/alpha-one-index/awesome-ai-index/issues/new?template=data-correction.yml)
- **New sections**: PRs adding new curated categories are very welcome!

Read [CONTRIBUTING.md](CONTRIBUTING.md) for the full guide.

---

## Related Projects

| Project | Description |
|---------|-------------|
| [![AI Vendor Risk Index](https://img.shields.io/badge/-AI%20Vendor%20Risk%20Index-red)](https://github.com/alpha-one-index/ai-vendor-risk-index) | Security & compliance ratings for 56+ AI vendors |
| [![AI Infra Index](https://img.shields.io/badge/-AI%20Infra%20Index-blue)](https://github.com/alpha-one-index/ai-infra-index) | Infrastructure benchmarking for AI systems |
| [![alphaoneindex.com](https://img.shields.io/badge/-alphaoneindex.com-6366f1)](https://alphaoneindex.com) | Full reports, premium tier, and API access |
| [![HuggingFace Mirror](https://img.shields.io/badge/-HuggingFace%20Mirror-yellow)](https://huggingface.co/datasets/alpha-one-index/awesome-ai-index) | Dataset mirror for ML workflows |
| [![Kaggle Dataset](https://img.shields.io/badge/-Kaggle%20Dataset-20beff)](https://www.kaggle.com/datasets/alphaoneindex/ai-vendor-risk-index) | Dataset mirror on Kaggle |

---

## License

[CC-BY-SA-4.0](LICENSE) — Free to use, share, and adapt with attribution.

---

Maintained by [Alpha One Index](https://alphaoneindex.com) | Data updated every Friday | Submit corrections via Issues | [Discussions](https://github.com/alpha-one-index/awesome-ai-index/discussions)
