# Multi-Omics Computational Tools & Reference Guide 🧬📊

[![Domain](https://img.shields.io/badge/Domain-Bioinformatics-00f0ff?style=flat-square)](https://github.com/YuliaNuzhnenko)
[![Category](https://img.shields.io/badge/Type-Curated%20Resource%20Catalog-purple?style=flat-square)](#)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)

A curated scientific reference directory and catalog of open-source software, analytical tools, benchmark datasets, and foundational research papers spanning **Bulk RNA-Seq, Single-Cell Genomics, Spatial Transcriptomics, Structural Biology, Epigenomics, Metagenomics, and AI-Driven Drug Discovery**.

> [!NOTE]
> **Reference Directory Notice**: This repository is a curated scientific reference guide and resource catalog of open-source tools, not an executable codebase. All links point directly to the official documentation and original repositories of each respective project.

---

## 📑 Table of Contents
- [Catalog Audit \& Link Validation](#-catalog-audit--link-validation)
- [Bulk RNA-Seq \& Transcriptomics](#bulk-rna-seq--transcriptomics)
- [Single-Cell \& Spatial Omics](#single-cell--spatial-omics)
- [Multi-Omics Factor Integration](#multi-omics-factor-integration)
- [Structural Biology \& AI Drug Discovery](#structural-biology--ai-drug-discovery)
- [Genomics \& Variant Calling](#genomics--variant-calling)
- [Metagenomics \& 16S Microbiome](#metagenomics--16s-microbiome)
- [Workflow Engines \& HPC Cloud Platforms](#workflow-engines--hpc-cloud-platforms)
- [License](#-license)

---

## 🛠 Catalog Audit & Link Validation

Run `python scripts/validate_links.py` to audit directory links and Markdown formatting:

```text
==================================================
 Multi-Omics Resource Link & Catalog Validator
==================================================
Parsed 30 curated scientific resource links in catalog.
Catalog Audit Status: 100% of links properly structured (30 links validated).
```

---

## Bulk RNA-Seq & Transcriptomics

| Tool / Framework | Language / Engine | Primary Application | Link / Reference |
| :--- | :--- | :--- | :--- |
| **DESeq2** | R / Bioconductor | Differential gene expression analysis based on negative binomial distribution | [Bioconductor](https://bioconductor.org/packages/DESeq2/) |
| **limma-voom** | R / Bioconductor | Linear modeling for RNA-seq and microarray gene expression | [Bioconductor](https://bioconductor.org/packages/limma/) |
| **STAR** | C++ | Ultra-fast universal RNA-seq read aligner | [GitHub](https://github.com/alexdobin/STAR) |
| **Salmon** | C++ / Rust | Fast transcript quantification from RNA-seq reads using quasi-mapping | [GitHub](https://github.com/COMBINE-lab/salmon) |
| **fgsea** | R / Bioconductor | Fast Gene Set Enrichment Analysis algorithm | [Bioconductor](https://bioconductor.org/packages/fgsea/) |

---

## Single-Cell & Spatial Omics

| Tool / Framework | Language | Primary Application | Link / Reference |
| :--- | :--- | :--- | :--- |
| **Scanpy** | Python | Scalable single-cell gene expression analysis, clustering, and trajectory inference | [Documentation](https://scanpy.readthedocs.io/) |
| **Seurat (v5)** | R | Toolkit for single-cell genomics, multimodal integration, and spatial transcriptomics | [Documentation](https://satijalab.org/seurat/) |
| **Harmony** | C++ / R / Python | Fast and flexible batch-effect correction for single-cell datasets | [GitHub](https://github.com/immunogenomics/harmony) |
| **Squidpy** | Python | Spatial single-cell analysis and graph-based cellular neighborhood mapping | [Documentation](https://squidpy.readthedocs.io/) |
| **CellPhoneDB** | Python | Public repository of ligands, receptors, and cell-cell communication analysis | [GitHub](https://github.com/venturalab/CellphoneDB) |

---

## Multi-Omics Factor Integration

| Tool / Framework | Input Modalities | Methodology | Reference |
| :--- | :--- | :--- | :--- |
| **MOFA2** | Transcriptomics, Proteomics, Methylation | Multi-Omics Factor Analysis using Bayesian matrix factorization | [MOFA2 Docs](https://biofam.github.io/MOFA2/) |
| **mixOmics** | Transcriptomics, Metabolomics, Microbiome | Multivariate statistical methods (PLS, sparse PLS) | [mixOmics](http://mixomics.org/) |
| **snakemake-multiomics** | Genomics, RNA-Seq | Automated multi-omics pipeline orchestration | [Snakemake](https://snakemake.github.io/) |

---

## Structural Biology & AI Drug Discovery

* **[AlphaFold2](https://github.com/google-deepmind/alphafold)** — DeepMind's neural network for predicting 3D protein structures from amino acid sequences.
* **[ESMFold](https://github.com/facebookresearch/esm)** — Meta AI's fast language model for protein structure prediction directly from sequence embeddings.
* **[RDKit](https://www.rdkit.org/)** — Open-source cheminformatics toolkit for molecular descriptor calculation, fingerprinting (ECFP4), and 2D/3D structure rendering.
* **[py3Dmol](https://3dmol.csb.pitt.edu/)** — High-performance WebGL 3D molecular visualization library for Python, Streamlit, and Jupyter Notebooks.
* **[AutoDock Vina](https://vina.scripps.edu/)** — Open-source molecular docking program for drug-target binding affinity estimation.

---

## Genomics & Variant Calling

* **[GATK4](https://gatk.broadinstitute.org/)** — Broad Institute's Genome Analysis Toolkit for germline and somatic variant discovery (HaplotypeCaller, Mutect2).
* **[Ensembl VEP](https://ensembl.org/info/docs/tools/vep/index.html)** — Variant Effect Predictor for annotating functional consequences of SNVs, indels, and structural variants.
* **[BCFtools](https://samtools.github.io/bcftools/)** — Fast utilities for manipulating VCF and BCF variant call files.

---

## Metagenomics & 16S Microbiome

* **[QIIME2](https://qiime2.org/)** — Next-generation microbiome bioinformatics platform for 16S/18S rRNA and ITS amplicon sequencing.
* **[DADA2](https://benjjneb.github.io/dada2/)** — High-resolution amplicon sequence variant (ASV) dereplication and chimera filtering algorithm.
* **[HUMAnN3](https://huttenhower.sph.harvard.edu/humann/)** — Tool for profiling the presence and abundance of microbial metabolic pathways from metagenomic sequencing.

---

## Workflow Engines & HPC Cloud Platforms

* **[Nextflow](https://nextflow.io)** — Data-driven workflow orchestration engine with native Docker, Singularity, SLURM, and AWS Batch integration.
* **[nf-core](https://nf-co.re/)** — Community-curated, peer-reviewed collection of high-quality Nextflow pipelines.
* **[Cromwell / WDL](https://cromwell.readthedocs.io/)** — Workflow Description Language execution engine used extensively by the Broad Institute.

---

## 📄 License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for details.
