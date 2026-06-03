import os
from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier

app = Flask(__name__)

# ── Load dataset and train models when the app starts ──────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "data", "college_mental_health.csv")
df = pd.read_csv(csv_path)

features = [
    'Daily_Activity_Pattern', 'Study_Hours', 'Sleep_Schedules', 'Class_Attendance',
    'Heart_Rate', 'Sleep_Quality', 'Step_Count', 'Messaging_Frequency',
    'Social_Media_Activity', 'Club_Event_Participation'
]

X = df[features]
y_reg = df['Stress_Levels']
y_clf = df['Mental_Health_Risk']

X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X, y_reg, test_size=0.2, random_state=42)
X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(X, y_clf, test_size=0.2, random_state=42)

regressor = RandomForestRegressor(n_estimators=200, random_state=42).fit(X_train_r, y_train_r)
classifier = RandomForestClassifier(n_estimators=200, random_state=42).fit(X_train_c, y_train_c)


# ── Anxiety & Depression derived from Stress ───────────────────────────
def compute_from_stress(stress_value):
    """Derive anxiety and depression proxies from a predicted stress score."""
    anxiety = min(100, max(0, stress_value * 1.2))
    depression = min(100, max(0, stress_value ** 1.1))
    return round(anxiety, 2), round(depression, 2)


@app.route("/", methods=["GET", "POST"])
def index():
    stress_pred = None
    risk_pred = None
    anxiety = None
    depression = None
    causes = []
    precautions = []

    if request.method == "POST":
        f = {k: float(request.form[k]) for k in features}
        X_vec = np.array([f[c] for c in features]).reshape(1, -1)

        # Stress prediction
        stress_pred = round(regressor.predict(X_vec)[0], 2)

        # Risk prediction
        risk_pred = classifier.predict(X_vec)[0]

        # Anxiety & Depression derived from Stress
        anxiety, depression = compute_from_stress(stress_pred)

        # Causes & precautions
        if f['Sleep_Quality'] < 4:
            causes.append("Poor sleep quality may be increasing stress.")
        if f['Heart_Rate'] > 85:
            causes.append("Elevated heart rate suggests high physiological arousal.")
        if f['Step_Count'] < 5000:
            causes.append("Low physical activity can worsen mood and energy levels.")
        if f['Social_Media_Activity'] > 7:
            causes.append("High social media use may correlate with increased anxiety.")
        if f['Study_Hours'] > 8:
            causes.append("Excessive study hours without breaks may contribute to burnout.")
        if f['Class_Attendance'] < 50:
            causes.append("Low class attendance may indicate disengagement or avoidance.")

        precautions = [
            "Improve sleep hygiene and maintain consistent sleep schedules.",
            "Add 20–30 minutes of daily physical activity.",
            "Limit late-night social media use.",
            "Practice relaxation techniques like deep breathing or mindfulness.",
            "Maintain a balanced routine between study, rest, and social time.",
        ]

    return render_template(
        "index.html",
        stress=stress_pred,
        risk=risk_pred,
        anxiety=anxiety,
        depression=depression,
        causes=causes,
        precautions=precautions,
    )


if __name__ == "__main__":
    app.run(debug=True)
