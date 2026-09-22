---
title: "ArcheType: A Novel Framework for Open-Source Column Type Annotation Using Large Language Models"
collection: "publications"
generated_by: "scripts/generate_publications.py"
permalink: "/publication/2024-05-01-archetype-a-novel-framework-for-open-source-column-type-annotation-using-large-language-models"
date: "2024-05-01"
venue: "Proceedings of the VLDB Endowment"
citation: "Benjamin Feuer, Yurong Liu, Chinmay Hegde, and Juliana Freire \"ArcheType: A Novel Framework for Open-Source Column Type Annotation Using Large Language Models.\" Proceedings of the VLDB Endowment 2024"
bibtex_key: "feuer_archetype_2024"
excerpt: "Existing deep-learning approaches to semantic column type annotation (CTA) have important shortcomings: they rely on semantic types which are fixed at training time; require a large number of training samples per type; incur high run-time inference costs; and their performance can degrade when evaluated on novel datasets, even when types remain constant. Large language models have exhibited strong zero-shot classification performance on a wide range of tasks and in this paper we explore their use for CTA. We introduce ArcheType, a simple, practical method for context sampling, prompt serialization, model querying, and label remapping, which enables large language models to solve CTA problems in a fully zero-shot manner. We ablate each component of our method separately, and establish that improvements to context sampling and label remapping provide the most consistent gains. ArcheType establishes a new state-of-the-art performance on zero-shot CTA benchmarks (including three new domain-specific benchmarks which we release along with this paper), and when used in conjunction with classical CTA techniques, it outperforms a SOTA DoDuo model on the fine-tuned SOTAB benchmark."
paperurl: "https://dl.acm.org/doi/10.14778/3665844.3665857"
---

[View publication](https://dl.acm.org/doi/10.14778/3665844.3665857)
