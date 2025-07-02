# Causal Impact of Additional Contributions on Member Churn

This repository investigates the causal and predictive relationship between **additional contributions** in German statutory health insurance funds and the **churn behavior of members**.

## 📊 Project Objectives

1. **Causal Inference**  
   Estimate the effect of contribution rate increases on member churn using:
   - **Difference-in-Differences (DiD)**
   - **Propensity Score Matching (PSM)**

2. **Predictive Modeling**  
   Build a machine learning model (Neural Network) to forecast churn based on fund characteristics.

3. **Comparative Analysis**  
   Compare insights gained from causal vs predictive models to inform decision-making.

---

## 🚀 Quick-start

### 1. Clone and create a virtual environment

```bash
git clone https://github.com/your-org/causal-churn.git
cd causal-churn
python -m venv .venv
source .venv/bin/activate           # PowerShell: .venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```bash
pip install --upgrade pip wheel
pip install -r requirements.txt
```

> **Note**  
> `requirements.txt` pins **SciPy < 1.11** to keep it compatible with `statsmodels 0.14.x`.  
> If you need the newest SciPy, install the dev build of statsmodels instead (see the comment at the bottom of the file).

---

### 3. Add data (optional)

Place the raw Excel files in `data/`:

```bash
 ├─ matched_sample.xlsx
 ├─ nn_prediction_results.xlsx
 ├─ causal_results.xlsx
 └─ did_results.xlsx
```

If the files are missing the app falls back to a small synthetic dataset, so you can still test the UI.

### 4. Run the Dash dashboard

```bash
python app/app.py
Then open http://127.0.0.1:8060 in your browser.
```

### 📂 Repository structure

```bash
├─ app/               # Dash application
│   └─ app.py
├─ data/              # raw & processed data
├─ notebooks/         # exploratory work
├─ requirements.txt   # Python dependencies
└─ README.md
```
