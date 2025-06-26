{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4ec957f7-98bd-416d-84b7-e1cb581d36ad",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "df = pd.read_csv(\"../../data/processed/merged_panel_clean_data.csv\")\n",
    "\n",
    "# ▶️ Competitor contribution stats\n",
    "df[\"avg_competitor_rate\"] = df.groupby([\"jahr\", \"quartal\"])[\"zusatzbeitrag\"].transform(\"mean\")\n",
    "df[\"gap_to_competitor\"] = df[\"zusatzbeitrag\"] - df[\"avg_competitor_rate\"]\n",
    "\n",
    "def plot_competitor_influence():\n",
    "    sns.scatterplot(data=df, x=\"avg_competitor_rate\", y=\"churn_rate\")\n",
    "    plt.title(\"Churn vs. Competitor Average Contribution\")\n",
    "    plt.show()\n",
    "\n",
    "    sns.scatterplot(data=df, x=\"gap_to_competitor\", y=\"churn_rate\")\n",
    "    plt.title(\"Churn vs. Gap to Market Average\")\n",
    "    plt.axvline(0, color=\"red\", linestyle=\"--\")\n",
    "    plt.show()\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    plot_competitor_influence()\n"
   ]
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
