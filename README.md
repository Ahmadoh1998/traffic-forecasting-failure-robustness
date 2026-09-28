# Beyond Clean-Data Accuracy: Quantifying Failure Propagation and Improving Robustness in Short-Term Traffic Forecasting

This repository contains the reproducibility materials associated with the manuscript:

**“Beyond Clean-Data Accuracy: Quantifying Failure Propagation and Improving Robustness in Short-Term Traffic Forecasting.”**

The study evaluates 15-minute short-term traffic-volume forecasting under both clean-data and detector-failure conditions. It investigates how detector outages and unavailable lagged observations propagate through the forecasting pipeline and compares conventional clean-data forecasting, failure-aware mitigation, and practical missing-input baselines.

## Repository Structure

```text
traffic-forecasting-failure-robustness/
├── README.md
├── requirements.txt
├── CITATION.cff
├── LICENSE
├── notebooks/
│   ├── NB1_Data_Inspection_and_Quality_Audit.ipynb
│   ├── NB2_Detector_Selection_and_Modeling_Sample.ipynb
│   ├── NB3_Clean_Condition_Forecasting.ipynb
│   ├── NB4_Robustness_and_Failure_Injection.ipynb
│   ├── NB5_Failure_Aware_Mitigation.ipynb
│   └── NB6_Practical_Missing_Input_Baselines.ipynb
├── data/
│   └── README.md
└── outputs/
    ├── figures/
    └── tables/
```

The repository is being prepared so that the complete workflow can be followed in the order **NB1 → NB6**.

## Notebook Workflow

### NB1 — Data Inspection and Quality Audit
Performs the initial inspection and quality assessment of the Victoria SCATS traffic-signal volume data, including schema checks, missing values, duplicate records, detector alarms, zero/negative observations, and interval-versus-daily consistency checks.

### NB2 — Detector Selection and Modeling Sample
Constructs the eligible detector pool and modeling sample by applying stability, activity, completeness, regional coverage, traffic-volume, and alarm-exposure criteria.

### NB3 — Clean-Condition Forecasting
Develops and evaluates the clean-data forecasting models for 15-minute traffic-volume prediction, including persistence, seasonal-naive, LightGBM, and XGBoost benchmarks.

### NB4 — Robustness and Failure Injection
Quantifies how detector failures and missing lagged inputs affect downstream forecasts. It includes real failure-run analysis, blackout amplification, and controlled failure-injection experiments.

### NB5 — Failure-Aware Mitigation
Evaluates failure-aware mitigation strategies using controlled validation experiments and compares their performance with the degraded clean-model response.

### NB6 — Practical Missing-Input Baselines
Evaluates operationally simple missing-input baselines, including previous-day substitution, previous-week substitution, and seasonal-naive fallback where applicable.

## Data Source

The raw traffic data are obtained from the **Victoria Department of Transport and Planning — Traffic Signal Volume Data** dataset:

https://discover.data.vic.gov.au/dataset/traffic-signal-volume-data

The dataset provides traffic volumes for individual SCATS traffic-loop detectors aggregated at 15-minute intervals.

For this study, data covering **January 1, 2026 through August 30, 2026** were used.

**Accessed:** 28 September 2026.

The original source data are not duplicated in this repository. Users should obtain the relevant source files directly from the official DataVic dataset page.

## Reproducibility Data

Processed files required to reproduce the reported experiments will be documented in `data/README.md`.

Large reproducibility files that are unsuitable for normal Git tracking will be distributed separately through a versioned repository release or another archival location. The permanent link will be added here once the reproducibility package is finalized.

## Recommended Execution Order

```text
NB1
 ↓
NB2
 ↓
NB3
 ↓
NB4
 ↓
NB5
 ↓
NB6
```

Later notebooks depend on processed datasets, predictions, or outputs produced by earlier stages.

## Running the Notebooks

The analyses were developed using **Google Colab**.

Before running the notebooks:

1. Obtain the required raw or processed data.
2. Install the required Python packages.
3. Set the project root/data paths at the beginning of each notebook.
4. Run the notebooks sequentially from NB1 through NB6 unless starting from a provided processed-data checkpoint.

Author-specific absolute Google Drive paths should not be used in the released notebooks. A single editable project root with relative subpaths is recommended, for example:

```python
from pathlib import Path

PROJECT_ROOT = Path("/content/traffic-forecasting-failure-robustness")
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
```

Users working in Google Drive can change only `PROJECT_ROOT` while keeping the internal folder structure unchanged.

## Python Environment

The final software environment will be documented in `requirements.txt` with pinned package versions.

The workflow uses common scientific Python libraries together with packages required for:

- numerical and tabular data processing;
- machine learning;
- LightGBM;
- XGBoost;
- Parquet file I/O;
- model evaluation; and
- figure generation.

The environment can then be installed with:

```bash
pip install -r requirements.txt
```

## Reproducibility Notes

Before the repository is released publicly, the notebooks will be checked to ensure that:

- all required input files are documented;
- author-specific local paths are removed;
- no credentials, tokens, or private links are present;
- random seeds are documented where applicable;
- package versions are recorded;
- outputs use clear and reproducible filenames; and
- the notebook sequence and dependencies are explicit.

## Code Availability

The analysis code associated with the manuscript is maintained in this repository:

https://github.com/Ahmadoh1998/traffic-forecasting-failure-robustness

The repository will contain the six analysis notebooks, execution instructions, software-environment information, and links to the required data resources.

## Data Availability

The raw traffic-volume data are publicly available from the Victoria Department of Transport and Planning through the DataVic **Traffic Signal Volume Data** dataset:

https://discover.data.vic.gov.au/dataset/traffic-signal-volume-data

Processed reproducibility files required for the manuscript experiments will be linked here after the reproducibility package is finalized.

## Citation

A machine-readable `CITATION.cff` file will be added after the manuscript author list and publication metadata are finalized.

## License

The analysis code in this repository is released under the MIT License.

The original Victoria traffic data remain subject to the terms and conditions specified by the data provider.

## Contact

For questions related to the code or reproducibility materials, please use the repository's GitHub Issues page after the repository is made public.
