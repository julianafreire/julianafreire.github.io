---
title: "Magneto: Combining Small and Large Language Models for Schema Matching"
collection: "publications"
generated_by: "scripts/generate_publications.py"
permalink: "/publication/2025-04-01-magneto-combining-small-and-large-language-models-for-schema-matching"
date: "2025-04-01"
venue: "Proceedings of the VLDB Endowment"
citation: "Yurong Liu, Eduardo H. M. Pena, Aécio Santos, Eden Wu, and Juliana Freire \"Magneto: Combining Small and Large Language Models for Schema Matching.\" Proceedings of the VLDB Endowment 2025"
bibtex_key: "liu_magneto_2025"
excerpt: "Recent advances in language models (LMs) open new opportunities for schema matching (SM). Recent approaches have shown their potential and key limitations: while small LMs (SLMs) require costly, difficult-to-obtain training data, large LMs (LLMs) demand significant computational resources and face context window constraints. We present Magneto, a cost-effective and accurate solution for SM that combines the advantages of SLMs and LLMs to address their limitations. By structuring the SM pipeline in two phases, retrieval and reranking, Magneto can use computationally efficient SLM-based strategies to derive candidate matches which can then be reranked by LLMs, thus making it possible to reduce runtime while improving matching accuracy. We propose (1) a self-supervised approach to fine-tune SLMs which uses LLMs to generate syntactically diverse training data, and (2) prompting strategies that are effective for reranking. We also introduce a new benchmark, developed in collaboration with domain experts, which includes real biomedical datasets and presents new challenges for SM methods. Through a detailed experimental evaluation, using both our new and existing benchmarks, we show that Magneto is scalable and attains high accuracy for datasets from different domains."
paperurl: "https://dl.acm.org/doi/10.14778/3742728.3742757"
---

[View publication](https://dl.acm.org/doi/10.14778/3742728.3742757)
