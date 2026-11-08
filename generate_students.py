import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
n = 1000

ability = rng.normal(0, 1, n)
engagement = 0.3 * ability + rng.normal(0, 0.95, n)

prior_gpa = np.clip(2.9 + 0.55 * ability + rng.normal(0, 0.3, n), 0, 4)
print(prior_gpa[:5].round(2), prior_gpa.min().round(2), prior_gpa.max().round(2)) 

attendance_rate = np.clip(0.82 + 0.07 * engagement + rng.normal(0, 0.07, n), 0.2, 1.0)
print(attendance_rate[:5].round(2), attendance_rate.min().round(2), attendance_rate.max().round(2))

missed_assignments = rng.poisson(np.exp(0.9 - 0.45 * engagement))
print(missed_assignments[:5], missed_assignments.min(), missed_assignments.max())

midterm_avg = np.clip(72 + 8 * ability + 4 * engagement + rng.normal(0, 8, n), 20, 100)
lms_logins = rng.poisson(np.exp(1.9 + 0.25 * engagement))

life_shock = rng.normal(0, 1, n)
perf = 0.9 * ability + 0.8 * engagement + 0.4 * life_shock + rng.normal(0, 0.6, n)

outcome_final_gpa = np.clip(2.9 + 0.5 * perf, 0, 4)
outcome_courses_failed = rng.poisson(np.exp(-2.2 - 0.9 * perf))
outcome_at_risk = ((outcome_final_gpa < 2.0) | (outcome_courses_failed >= 1)).astype(int)

print(outcome_at_risk.mean().round(3))
print(midterm_avg[:5].round(1), midterm_avg.min().round(1), midterm_avg.max().round(1))
print(lms_logins[:5], lms_logins.min(), lms_logins.max())

print(ability.mean().round(2), ability.std().round(2))
print(engagement.mean().round(2), engagement.std().round(2))
print(np.corrcoef(ability, engagement)[0, 1].round(2))

df = pd. DataFrame ({
    "student_id": [f"S{i:04}" for i in range(1,n+1)],
    "prior_gpa": prior_gpa.round(2),
    "attendance_rate": attendance_rate.round(3),
    "missed_assignments": missed_assignments,
    "midterm_avg": midterm_avg.round(1),
    "lms_logins_per_week": lms_logins,
    "outcome_final_gpa": outcome_final_gpa.round(2),
    "outcome_courses_failed": outcome_courses_failed,
    "outcome_at_risk": outcome_at_risk,
})

print(df.head())
print(df.corr(numeric_only=True)["outcome_at_risk"].round(2))

df.to_csv("students.csv", index=False)
print("Saved", len(df), "students")
print("At-risk rate:", df["outcome_at_risk"].mean().round(3))