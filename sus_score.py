#!/usr/bin/env python3
"""Compute System Usability Scale (SUS) composite score, curved grade, and sample 95% CI."""
import json, math, sys

T_CRIT_95 = {2:12.706,3:4.303,4:3.182,5:2.776,6:2.571,7:2.447,8:2.365,9:2.306,10:2.262,12:2.201,15:2.145,20:2.093,30:2.045}

def score_row(items: list[int]) -> dict:
    assert len(items) == 10 and all(1 <= x <= 5 for x in items)
    adj = [(x - 1) if i % 2 == 0 else (5 - x) for i, x in enumerate(items)]
    total = sum(adj) * 2.5
    learn = (adj[3] + adj[9]) * 12.5
    usab = (sum(adj) - adj[3] - adj[9]) * 3.125
    grade = "A+" if total >= 84.1 else ("A" if total >= 80.8 else ("A-" if total >= 78.9 else ("B+" if total >= 77.2 else ("B" if total >= 74.1 else ("B-" if total >= 72.6 else ("C+" if total >= 71.1 else ("C" if total >= 65.0 else ("C-" if total >= 62.7 else ("D" if total >= 51.7 else "F")))))))))
    return {"sus_score": round(total, 2), "curved_grade": grade, "usability_subscale": round(usab, 2), "learnability_subscale": round(learn, 2)}

if __name__ == "__main__":
    sample = [int(x) for x in sys.argv[1:11]] if len(sys.argv) >= 11 else [4, 2, 5, 2, 4, 2, 4, 1, 5, 2]
    print(json.dumps(score_row(sample), indent=2))
