# Scientific code audit — preliminary static review

Scope: static inspection of the GitHub NB4 code (Steps 12–15), the NB5 workflow structure, and NB6 final August baseline code (Cells 29 and 38–40). This is not a complete line-by-line audit or independent rerun of NB1–NB6.

## Verified code-level observations

1. **Chronological failure design (NB4 Step 12):** pre-August patterns are assigned to August dates with matching day of week, and candidate windows require complete clean baseline predictions from failure onset through failure end plus 24 hours. The implementation draws one event per detector and uses a seeded RNG.
2. **Ground-truth-preserving injection (NB4 Step 13):** for each lag, the historical timestamp is computed as forecast timestamp minus lag offset; only affected lag inputs are assigned NaN. The code computes the absolute difference between `Target_Volume` and `Actual`. A printed diagnostic is not itself a hard assertion; the archived output must be checked for exact matches.
3. **Statistical inference (NB4 Step 15):** event-level MAE differences are bootstrapped with replacement using 10,000 resamples; a one-sided Wilcoxon signed-rank test is applied to nonzero event differences. This is structurally consistent with event-level rather than row-level inference.
4. **Baseline comparison (NB6 Cells 38–40):** previous-day and previous-week imputation are evaluated separately, with availability checks and matched-row comparisons. The code uses one-to-one merge validation in relevant comparisons. Reported B2/B3 error must remain conditional on available rows.
5. **Known study-design limitation:** detector cohort selection used January–August quality summaries. This means August is not a fully independent cohort-selection holdout, although model fitting/tuning is described as pre-August. The manuscript already discloses this limitation.
6. **Saved-model prediction verification:** see `REPRODUCIBILITY_AUDIT.md` for the successful 100,000-row per-model inference check.

## Items not yet independently established

- Exact equality of every printed NB4 ground-truth diagnostic and the source files.
- Full correctness of NB5 augmentation provenance, duplicate exclusion, and all July/August isolation logic.
- Independent reproduction of NB6 event-level B1-vs-R1 significance from raw event-level outputs.
- Full NB1–NB6 execution from raw source data and archived environment.
- Whether the reported 37.25-hour median blackout and 96-fold median amplification are independently reproduced from the isolated-event CSV.

## Interpretation

The inspected implementation contains several appropriate safeguards; no definitive code defect was established in these specific excerpts. This does **not** certify the full scientific workflow. Any future claims of complete reproducibility should be supported by an independent run and comparison of outputs.

No notebooks, models, datasets, or reported results were modified by this audit.
