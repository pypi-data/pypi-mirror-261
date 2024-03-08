# LeafletSC

LeafletSC is a binomial mixture model designed for the analysis of alternative splicing events in single-cell RNA sequencing data. The model facilitates understanding and quantifying splicing variability at the single-cell level. Below is the graphical model representation:

<p align="center">
  <img src="https://github.com/daklab/Leaflet/assets/23510936/3e147ba5-7ee8-47ae-b84c-5e99e0551acf" width="500">
</p>

## Compatibility with sequencing platforms 
LeafletSC supports analysis from the following single-cell RNA sequencing platforms:
- Smart-Seq2 
- Split-seq
- 10X 

## Getting Started

LeafletSC is implemented in Python and requires Python version 3.9 or higher. You can easily install LeafletSC via PyPI using the following command:

```bash
pip install LeafletSC
```

Please also make sure you have regtools installed. Prior to using LeafletSC, please run regtools on your single-cell BAM files. Here is an example of what this might look like in a Snakefile:

```Snakemake
{params.regtools_path} junctions extract -a 6 -m 50 -M 500000 {input.bam_use} -o {output.juncs} -s XS -b {output.barcodes}
# Combine junctions and cell barcodes
paste --delimiters='\t' {output.juncs} {output.barcodes} > {output.juncswbarcodes}
```

Once you have your junction files, you can try out the mixture model tutorial under [Tutorials](Tutorials/run_binomial_mixture_model.ipynb)

## Capabilities
With LeafletSC, you can:

- Infer cell states influenced by alternative splicing and identify significant splice junctions.
- Conduct differential splicing analysis between specific cell groups if cell identities are known.
- Generate synthetic alternative splicing datasets for robust analysis testing.

## If you use Leaflet, please cite our [paper](https://www.biorxiv.org/content/10.1101/2023.10.17.562774v1)

```
@unpublished{Isaev2023-bf,
  title    = "Investigating RNA splicing as a source of cellular diversity using a binomial mixture model",
  author   = "Isaev, Keren and Knowles, David A",
  journal  = "bioRxiv",
  pages    = "2023.10.17.562774",
  month    = oct,
  year     = 2023,
  language = "en"
}
```

### To-do: 

1. Add documentation and some tests for how to run the simulation code 
2. Add 10X/split-seq mode in addition to smart-seq2
3. Extend framework to seurat/scanpy anndata objects
4. Add notes on generative model and inference method