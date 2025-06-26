{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "277eb21c-b54b-42c8-8cdc-90ee90386dab",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting scikit-learn\n",
      "  Downloading scikit_learn-1.7.0-cp313-cp313-macosx_12_0_arm64.whl.metadata (31 kB)\n",
      "Requirement already satisfied: numpy>=1.22.0 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from scikit-learn) (2.2.6)\n",
      "Requirement already satisfied: scipy>=1.8.0 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from scikit-learn) (1.16.0)\n",
      "Collecting joblib>=1.2.0 (from scikit-learn)\n",
      "  Downloading joblib-1.5.1-py3-none-any.whl.metadata (5.6 kB)\n",
      "Collecting threadpoolctl>=3.1.0 (from scikit-learn)\n",
      "  Downloading threadpoolctl-3.6.0-py3-none-any.whl.metadata (13 kB)\n",
      "Downloading scikit_learn-1.7.0-cp313-cp313-macosx_12_0_arm64.whl (10.6 MB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m10.6/10.6 MB\u001b[0m \u001b[31m27.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m \u001b[36m0:00:01\u001b[0m\n",
      "\u001b[?25hDownloading joblib-1.5.1-py3-none-any.whl (307 kB)\n",
      "Downloading threadpoolctl-3.6.0-py3-none-any.whl (18 kB)\n",
      "Installing collected packages: threadpoolctl, joblib, scikit-learn\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m3/3\u001b[0m [scikit-learn][0m [scikit-learn]\n",
      "\u001b[1A\u001b[2KSuccessfully installed joblib-1.5.1 scikit-learn-1.7.0 threadpoolctl-3.6.0\n"
     ]
    }
   ],
   "source": [
    "!pip install scikit-learn\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "956c7a64-b756-42d1-80d3-826c95c1a46c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[31mERROR: Could not find a version that satisfies the requirement tensorflow (from versions: none)\u001b[0m\u001b[31m\n",
      "\u001b[0m\u001b[31mERROR: No matching distribution found for tensorflow\u001b[0m\u001b[31m\n",
      "\u001b[0m"
     ]
    }
   ],
   "source": [
    "!pip install tensorflow\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "880dea44-6d59-4504-a163-f1ae22dad296",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'tensorflow'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mModuleNotFoundError\u001b[39m                       Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[1]\u001b[39m\u001b[32m, line 5\u001b[39m\n\u001b[32m      3\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01msklearn\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mpreprocessing\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m StandardScaler\n\u001b[32m      4\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01msklearn\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mmetrics\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m roc_auc_score, f1_score, brier_score_loss\n\u001b[32m----> \u001b[39m\u001b[32m5\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mtensorflow\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mkeras\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mmodels\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m Sequential\n\u001b[32m      6\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mtensorflow\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mkeras\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mlayers\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m Dense\n\u001b[32m      8\u001b[39m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34mrun_predictive_model\u001b[39m(data_path):\n\u001b[32m      9\u001b[39m     \u001b[38;5;66;03m# Load dataset\u001b[39;00m\n",
      "\u001b[31mModuleNotFoundError\u001b[39m: No module named 'tensorflow'"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "from sklearn.metrics import roc_auc_score, f1_score, brier_score_loss\n",
    "from tensorflow.keras.models import Sequential\n",
    "from tensorflow.keras.layers import Dense\n",
    "\n",
    "def run_predictive_model(data_path):\n",
    "    # Load dataset\n",
    "    df = pd.read_csv(\"../data/processed/merged_panel_clean_data.csv\", low_memory=False)\n",
    "    df = df.drop(columns=[col for col in df.columns if \"Unnamed\" in col])\n",
    "    df[\"morbidity_index\"] = pd.to_numeric(df[\"morbidity_index\"], errors=\"coerce\")\n",
    "    df = df.dropna(subset=[\"churn_rate\", \"treatment_flag\", \"zusatzbeitrag\", \"morbidity_index\", \"insured_lag\", \"marktanteil versicherte\"])\n",
    "    X_pred = df[[\"zusatzbeitrag\", \"zusatzbeitrag_avg\", \"morbidity_index\", \"marktanteil versicherte\", \"insured_lag\"]].dropna()\n",
    "    y_pred = df.loc[X_pred.index, \"churn_rate\"]\n",
    "\n",
    "    scaler = StandardScaler()\n",
    "    X_scaled = scaler.fit_transform(X_pred)\n",
    "    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_pred, test_size=0.2, random_state=42)\n",
    "\n",
    "    model = Sequential([\n",
    "        Dense(64, activation='relu', input_shape=(X_train.shape[1],)),\n",
    "        Dense(32, activation='relu'),\n",
    "        Dense(1, activation='sigmoid')\n",
    "    ])\n",
    "    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])\n",
    "    model.fit(X_train, (y_train > 0.05).astype(int), epochs=50, batch_size=32, validation_split=0.2)\n",
    "\n",
    "    y_nn_pred_prob = model.predict(X_test).flatten()\n",
    "    y_test_binary = (y_test > 0.05).astype(int)\n",
    "\n",
    "    print(\"ROC-AUC:\", roc_auc_score(y_test_binary, y_nn_pred_prob))\n",
    "    print(\"F1 Score:\", f1_score(y_test_binary, (y_nn_pred_prob > 0.05).astype(int)))\n",
    "    print(\"Brier Score:\", brier_score_loss(y_test_binary, y_nn_pred_prob))\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    data_path = \"../data/processed/merged_panel_clean_data.csv\"\n",
    "    run_predictive_model(data_path)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c9ffd6ee-8f71-4bfc-8a84-cdeb26adb2a2",
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
