# System Usability Scale (SUS) Psychometric & Confidence Interval Calculator

Zero-dependency Python CLI implementing Brooke's (1986) alternating 10-item System Usability Scale equation, Lewis & Sauro's Usability (`8`-item) vs. Learnability (`Q4 + Q10`) subscales, and Sauro-Lewis curved letter grades (`A+` through `F` anchored at the `68.0` 50th-percentile benchmark).

Run interactive single-user scoring or multi-participant CSV/TSV batch confidence intervals in the browser at **[SUS Calculator](https://suscalculator.wiki/)**:
- **Single-User SUS Score & Curved Grade Calculator**: https://suscalculator.wiki/
- **Batch CSV Mean, SD & Student's `t` 95% CI Studio**: https://suscalculator.wiki/batch-csv-calculator/
- **SUS Sample Size & 2-Item UMUX-Lite Converter**: https://suscalculator.wiki/sample-size-and-umux-lite/

## Usage

```bash
python3 sus_score.py 4 2 5 2 4 2 4 1 5 2
```

## License
MIT
