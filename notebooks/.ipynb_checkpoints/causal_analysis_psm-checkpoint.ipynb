{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c353f110-2dbc-4cbd-813b-c44575abdcc7",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'sklearn'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mModuleNotFoundError\u001b[39m                       Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[1]\u001b[39m\u001b[32m, line 2\u001b[39m\n\u001b[32m      1\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mpandas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mpd\u001b[39;00m\n\u001b[32m----> \u001b[39m\u001b[32m2\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01msklearn\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mlinear_model\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m LogisticRegression\n\u001b[32m      3\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01msklearn\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mneighbors\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m NearestNeighbors\n\u001b[32m      5\u001b[39m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34mrun_causal_analysis\u001b[39m(data_path):\n\u001b[32m      6\u001b[39m     \u001b[38;5;66;03m# Load dataset\u001b[39;00m\n",
      "\u001b[31mModuleNotFoundError\u001b[39m: No module named 'sklearn'"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.neighbors import NearestNeighbors\n",
    "\n",
    "def run_causal_analysis(data_path):\n",
    "    # Load dataset\n",
    "    df = pd.read_csv(data_path, low_memory=False)\n",
    "    df = df.drop(columns=[col for col in df.columns if \"Unnamed\" in col])\n",
    "    df[\"morbidity_index\"] = pd.to_numeric(df[\"morbidity_index\"], errors=\"coerce\")\n",
    "    df = df.dropna(subset=[\"churn_rate\", \"treatment_flag\", \"zusatzbeitrag\", \"morbidity_index\", \"insured_lag\", \"marktanteil versicherte\"])\n",
    "\n",
    "    # Propensity Score Estimation\n",
    "    X_psm = df[[\"zusatzbeitrag\", \"morbidity_index\", \"insured_lag\", \"marktanteil versicherte\"]]\n",
    "    y_psm = df[\"treatment_flag\"].astype(int)\n",
    "\n",
    "    logit = LogisticRegression(max_iter=1000)\n",
    "    logit.fit(X_psm, y_psm)\n",
    "    df[\"propensity_score\"] = logit.predict_proba(X_psm)[:, 1]\n",
    "    df[\"treatment\"] = y_psm\n",
    "\n",
    "    # Matching\n",
    "    treated = df[df[\"treatment\"] == 1]\n",
    "    control = df[df[\"treatment\"] == 0]\n",
    "    nn = NearestNeighbors(n_neighbors=1)\n",
    "    nn.fit(control[[\"propensity_score\"]])\n",
    "    _, indices = nn.kneighbors(treated[[\"propensity_score\"]])\n",
    "    matched_control = control.iloc[indices.flatten()].reset_index(drop=True)\n",
    "    matched_treated = treated.reset_index(drop=True)\n",
    "\n",
    "    # Average Treatment Effect (ATE)\n",
    "    ate = matched_treated[\"churn_rate\"].mean() - matched_control[\"churn_rate\"].mean()\n",
    "    print(\"ATE (Average Treatment Effect):\", round(ate, 6))\n",
    "    return ate\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    data_path = \"../data/processed/merged_panel_clean_data.csv\"\n",
    "    run_causal_analysis(data_path)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1a8b0460-3593-4daa-8ee1-7d9931c58354",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
