"""Read-only NB4 input preflight. Run from repository root:
python scripts/check_nb4_inputs.py --root /path/to/traffic-forecasting-failure-robustness
Exit 0: required files and expected Parquet columns are present.
Exit 1: missing input, invalid schema, or unreadable model.
This does not execute NB4 or certify full-workflow reproducibility.
"""
import argparse
import sys
from pathlib import Path

FEATURES = [
    "Detector_Code", "Interval_Index", "DayOfWeek", "IsWeekend",
    "Lag_1", "Lag_2", "Lag_4", "Lag_8", "Lag_96",
]
KEYS = ["Timestamp", "Detector_Code"]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    base = args.root.expanduser().resolve() / "outputs" / "Notebook_3_Output"
    paths = {
        "August forecast features": base / "Data/Forecasting_Monthly/FORECASTING_2026-08.parquet",
        "August saved predictions": base / "Data/August_Final_All_Model_Predictions.parquet",
        "LightGBM model": base / "Models/LightGBM_FINAL_JanJul_1200.txt",
        "XGBoost model": base / "Models/XGBoost_FINAL_JanJul_624.json",
        "Feature configuration": base / "Results/Forecasting_Feature_Configuration.json",
    }
    failures = []
    print("NB4 INPUT PREFLIGHT (READ ONLY)")
    print("Project root:", args.root.expanduser().resolve())
    for label, path in paths.items():
        exists = path.is_file()
        print(f"{'FOUND' if exists else 'MISSING'}: {label}: {path}")
        if not exists:
            failures.append(label)
    try:
        import pyarrow.parquet as pq
        for label, required in [
            ("August forecast features", list(dict.fromkeys(KEYS + FEATURES + ["All_Lags_Available"]))),
            ("August saved predictions", KEYS + ["LightGBM_Prediction", "XGBoost_Prediction"]),
        ]:
            if label in failures:
                continue
            columns = set(pq.ParquetFile(paths[label]).schema.names)
            missing = sorted(set(required) - columns)
            print(f"{label} schema: {'PASS' if not missing else 'FAIL'}")
            if missing:
                print("  Missing columns:", missing)
                failures.append(label + " schema")
    except ImportError:
        print("pyarrow not installed; Parquet schema validation unavailable")
        failures.append("pyarrow")
    except Exception as exc:
        print("Parquet schema check failed:", type(exc).__name__, str(exc))
        failures.append("Parquet schema")
    if not any(x in failures for x in ("LightGBM model", "XGBoost model")):
        try:
            import lightgbm as lgb
            import xgboost as xgb
            lm = lgb.Booster(model_file=str(paths["LightGBM model"]))
            xm = xgb.Booster()
            xm.load_model(str(paths["XGBoost model"]))
            valid = lm.feature_name() == FEATURES and xm.feature_names == FEATURES
            valid = valid and lm.num_trees() == 1200 and xm.num_boosted_rounds() == 624
            print("Saved model structure:", "PASS" if valid else "FAIL")
            if not valid:
                failures.append("model structure")
        except Exception as exc:
            print("Model loading failed:", type(exc).__name__, str(exc))
            failures.append("model loading")
    print("PREFLIGHT:", "PASS" if not failures else "FAIL")
    if failures:
        print("Unresolved:", ", ".join(failures))
    return 1 if failures else 0

if __name__ == "__main__":
    sys.exit(main())
