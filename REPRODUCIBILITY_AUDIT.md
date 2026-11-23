# Saved-model prediction reproducibility audit

## Scope

This audit documents a read-only verification performed in Google Colab using the archived January-July LightGBM and XGBoost models, the August forecasting feature dataset, and saved August predictions. It is **not** a claim that the entire NB1-NB6 workflow was rerun from raw data.

## Inputs

- `outputs/Notebook_3_Output/Models/LightGBM_FINAL_JanJul_1200.txt`
- `outputs/Notebook_3_Output/Models/XGBoost_FINAL_JanJul_624.json`
- `outputs/Notebook_3_Output/Data/Forecasting_Monthly/FORECASTING_2026-08.parquet`
- `outputs/Notebook_3_Output/Data/August_Final_All_Model_Predictions.parquet`

The large artifacts are not committed to this repository; their availability is described in `data/README.md`.

## Verification procedure

1. Load the archived models without retraining.
2. Select forecasting rows with `All_Lags_Available == True`.
3. Validate one-to-one correspondence between saved predictions and forecast features using `Timestamp` and `Detector_Code`.
4. Select 100,000 saved prediction rows with `random_state=42`.
5. Score the nine original features in their saved order using `float32`, and apply nonnegative clipping to match the original postprocessing.
6. Compare saved and reproduced predictions using absolute difference tolerance `1e-4`.

## Observed results

| Check | Result |
|---|---|
| Saved prediction rows | 2,108,544 |
| All-lag-ready forecasting rows | 2,108,544 |
| Matching keys | 2,108,544 |
| Unmatched keys | 0 |
| Compared rows per model | 100,000 |
| LightGBM maximum absolute difference | 2.0724021737805742e-05 |
| LightGBM mean absolute difference | 6.50279560395136e-07 |
| LightGBM rows above 1e-4 | 0 |
| XGBoost maximum absolute difference | 0.0 |
| XGBoost mean absolute difference | 0.0 |
| XGBoost rows above 1e-4 | 0 |

**Result:** Both saved-model prediction checks passed at tolerance `1e-4`.

## Model structure

- LightGBM: 1,200 trees, nine predictors.
- XGBoost: 624 boosting rounds, nine predictors.
- Predictor order: `Detector_Code`, `Interval_Index`, `DayOfWeek`, `IsWeekend`, `Lag_1`, `Lag_2`, `Lag_4`, `Lag_8`, `Lag_96`.
- Saved XGBoost model metadata reports version `3.4.1`.
- LightGBM's model header `version=v4` identifies its model format, **not** necessarily the training library version.

## Colab verification environment (not confirmed original training environment)

- Python 3.13.16
- numpy 2.4.6
- pandas 2.2.3
- pyarrow 23.0.1
- matplotlib 3.10.0
- scipy 1.16.3
- scikit-learn 1.6.1
- lightgbm 4.6.0
- xgboost 3.4.1

These versions describe the successful **verification** runtime. They should not be labeled as the original training environment without further evidence.

## Outstanding reproducibility tasks

- Preserve and document an independently executable NB1-NB6 environment with tested dependency versions.
- Verify availability and provenance of all intermediate datasets, not just model checkpoints.
- Run the full notebook workflow in a fresh environment, comparing produced tables and figures against the manuscript.
- Record input hashes and environment details for the archival release.

No model retraining or source-data modification was performed during the documented prediction audit.
