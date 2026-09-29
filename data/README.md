# Data

This repository does not redistribute the raw Victoria SCATS traffic-signal volume data or the large processed datasets generated during the study.

## Raw data

Download the source data from the Victoria Department of Transport and Planning DataVic dataset:

https://discover.data.vic.gov.au/dataset/traffic-signal-volume-data

The study uses data from **2026-01-01 through 2026-08-30** at 15-minute resolution.

Place the downloaded monthly ZIP archives in:

```text
data/raw/
```

The notebooks expect the raw source archives to be available in this directory when running the complete workflow from NB1.

## Processed data

Processed datasets and model-ready files are generated sequentially by the notebooks and written under `outputs/`.

Because several processed Parquet files are large, they are not stored in the Git repository. The processed datasets used in the manuscript analysis are **available from the corresponding author upon reasonable request**.

For internal review and reproducibility checking, the corresponding author can provide a processed-data package containing the model-ready dataset, detector mapping, failure-run library, monthly clean 15-minute files, and split/manifest files required to reproduce the main experiments.

## Notebook dependencies

- NB1 reads the raw monthly source archives.
- NB2 reads the raw archives and creates the detector-selection and 15-minute modeling datasets.
- NB3 reads NB2 outputs and creates forecasting datasets, trained models, predictions, tables, and figures.
- NB4 reads NB3 outputs and creates robustness/failure-injection artifacts.
- NB5 reads NB3 and NB4 outputs and creates failure-aware mitigation artifacts.
- NB6 reads outputs from NB2–NB5 and creates the practical missing-input baseline benchmark.

Do not commit private data, credentials, personal Google Drive paths, or large raw/processed data files to the Git repository.
