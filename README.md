# Student Success Predictor

A data platform that helps advisors identify students who may be heading
toward academic difficulty early in the term, explains why, and suggests
a supportive next step.

> Prototype built on **synthetic data**. Metrics demonstrate the pipeline,
> not real-world predictive accuracy.

## Outcome definition
A student is **at risk** if they finish the term with a GPA below 2.0
or fail at least one course. Predictions use only data available by
**week 6** of the term.

## Data
`generate_students.py` creates 1,000 fictional students. Hidden traits
(ability, engagement, life events) drive both the visible features and
the outcome, so the data is noisy like real life.

- Features (known by week 6): prior GPA, attendance, missed assignments,
  midterm average, LMS logins
- Outcome columns (prefixed `outcome_`) are known only at end of term and
  are never used as model inputs, to prevent data leakage.

## Run it
    pip install -r requirements.txt
    python generate_students.py

## Planned stack
Python, pandas, scikit-learn, Snowflake, Dagster, Streamlit / Power BI

## Status
Week 1: synthetic dataset complete.