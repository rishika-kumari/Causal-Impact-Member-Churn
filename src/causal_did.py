{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "70836891-b4cb-474d-9e97-4d4760440da8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: linearmodels in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (6.1)\n",
      "Requirement already satisfied: numpy<3,>=1.22.3 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from linearmodels) (2.2.6)\n",
      "Requirement already satisfied: pandas>=1.4.0 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from linearmodels) (2.2.3)\n",
      "Requirement already satisfied: scipy>=1.8.0 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from linearmodels) (1.16.0)\n",
      "Requirement already satisfied: statsmodels>=0.13.0 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from linearmodels) (0.14.4)\n",
      "Requirement already satisfied: mypy-extensions>=0.4 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from linearmodels) (1.1.0)\n",
      "Requirement already satisfied: Cython>=3.0.10 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from linearmodels) (3.1.2)\n",
      "Requirement already satisfied: pyhdfe>=0.1 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from linearmodels) (0.2.0)\n",
      "Requirement already satisfied: formulaic>=1.0.0 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from linearmodels) (1.1.1)\n",
      "Requirement already satisfied: setuptools-scm<9.0.0,>=8.0.0 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from setuptools-scm[toml]<9.0.0,>=8.0.0->linearmodels) (8.3.1)\n",
      "Requirement already satisfied: packaging>=20 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from setuptools-scm<9.0.0,>=8.0.0->setuptools-scm[toml]<9.0.0,>=8.0.0->linearmodels) (25.0)\n",
      "Requirement already satisfied: setuptools in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from setuptools-scm<9.0.0,>=8.0.0->setuptools-scm[toml]<9.0.0,>=8.0.0->linearmodels) (80.8.0)\n",
      "Requirement already satisfied: interface-meta>=1.2.0 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from formulaic>=1.0.0->linearmodels) (1.3.0)\n",
      "Requirement already satisfied: typing-extensions>=4.2.0 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from formulaic>=1.0.0->linearmodels) (4.13.2)\n",
      "Requirement already satisfied: wrapt>=1.17.0rc1 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from formulaic>=1.0.0->linearmodels) (1.17.2)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from pandas>=1.4.0->linearmodels) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from pandas>=1.4.0->linearmodels) (2025.2)\n",
      "Requirement already satisfied: tzdata>=2022.7 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from pandas>=1.4.0->linearmodels) (2025.2)\n",
      "Requirement already satisfied: six>=1.5 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from python-dateutil>=2.8.2->pandas>=1.4.0->linearmodels) (1.17.0)\n",
      "Requirement already satisfied: patsy>=0.5.6 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from statsmodels>=0.13.0->linearmodels) (1.0.1)\n"
     ]
    }
   ],
   "source": [
    "!pip install linearmodels"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f1c45468-403e-47d8-ad7f-d073fd4ab37c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[31mERROR: Ignored the following yanked versions: 1.14.0rc1\u001b[0m\u001b[31m\n",
      "\u001b[0m\u001b[31mERROR: Ignored the following versions that require a different python version: 1.10.0 Requires-Python <3.12,>=3.8; 1.10.0rc1 Requires-Python <3.12,>=3.8; 1.10.0rc2 Requires-Python <3.12,>=3.8; 1.10.1 Requires-Python <3.12,>=3.8; 1.11.0 Requires-Python <3.13,>=3.9; 1.11.0rc1 Requires-Python <3.13,>=3.9; 1.11.0rc2 Requires-Python <3.13,>=3.9; 1.11.1 Requires-Python <3.13,>=3.9; 1.11.2 Requires-Python <3.13,>=3.9; 1.11.3 Requires-Python <3.13,>=3.9; 1.6.2 Requires-Python >=3.7,<3.10; 1.6.3 Requires-Python >=3.7,<3.10; 1.7.0 Requires-Python >=3.7,<3.10; 1.7.1 Requires-Python >=3.7,<3.10; 1.7.2 Requires-Python >=3.7,<3.11; 1.7.3 Requires-Python >=3.7,<3.11; 1.8.0 Requires-Python >=3.8,<3.11; 1.8.0rc1 Requires-Python >=3.8,<3.11; 1.8.0rc2 Requires-Python >=3.8,<3.11; 1.8.0rc3 Requires-Python >=3.8,<3.11; 1.8.0rc4 Requires-Python >=3.8,<3.11; 1.8.1 Requires-Python >=3.8,<3.11; 1.9.0 Requires-Python >=3.8,<3.12; 1.9.0rc1 Requires-Python >=3.8,<3.12; 1.9.0rc2 Requires-Python >=3.8,<3.12; 1.9.0rc3 Requires-Python >=3.8,<3.12; 1.9.1 Requires-Python >=3.8,<3.12\u001b[0m\u001b[31m\n",
      "\u001b[0m\u001b[31mERROR: Could not find a version that satisfies the requirement scipy==1.10.1 (from versions: 0.8.0, 0.9.0, 0.10.0, 0.10.1, 0.11.0, 0.12.0, 0.12.1, 0.13.0, 0.13.1, 0.13.2, 0.13.3, 0.14.0, 0.14.1, 0.15.0, 0.15.1, 0.16.0, 0.16.1, 0.17.0, 0.17.1, 0.18.0, 0.18.1, 0.19.0, 0.19.1, 1.0.0, 1.0.1, 1.1.0, 1.2.0, 1.2.1, 1.2.2, 1.2.3, 1.3.0, 1.3.1, 1.3.2, 1.3.3, 1.4.0, 1.4.1, 1.5.0, 1.5.1, 1.5.2, 1.5.3, 1.5.4, 1.6.0, 1.6.1, 1.9.2, 1.9.3, 1.11.4, 1.12.0rc1, 1.12.0rc2, 1.12.0, 1.13.0rc1, 1.13.0, 1.13.1, 1.14.0rc2, 1.14.0, 1.14.1, 1.15.0rc1, 1.15.0rc2, 1.15.0, 1.15.1, 1.15.2, 1.15.3, 1.16.0rc1, 1.16.0rc2, 1.16.0)\u001b[0m\u001b[31m\n",
      "\u001b[0m\u001b[31mERROR: No matching distribution found for scipy==1.10.1\u001b[0m\u001b[31m\n",
      "\u001b[0mNote: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install scipy==1.10.1 statsmodels==0.13.5\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "5210efb0-700e-4e6c-b996-74d95b1f6a25",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/var/folders/kk/mr4t4jss0v3fbs24nvk11mdh0000gn/T/ipykernel_1751/58881669.py:2: DtypeWarning: Columns (14) have mixed types. Specify dtype option on import or set low_memory=False.\n",
      "  df = pd.read_csv(\"../data/processed/merged_panel_clean_data.csv\")\n"
     ]
    },
    {
     "ename": "ImportError",
     "evalue": "cannot import name '_lazywhere' from 'scipy._lib._util' (/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/scipy/_lib/_util.py)",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mImportError\u001b[39m                               Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[19]\u001b[39m\u001b[32m, line 35\u001b[39m\n\u001b[32m     24\u001b[39m df_model = df.dropna(subset=[\u001b[33m\"\u001b[39m\u001b[33mchurn_rate\u001b[39m\u001b[33m\"\u001b[39m, \u001b[33m\"\u001b[39m\u001b[33mtreatment_flag\u001b[39m\u001b[33m\"\u001b[39m, \u001b[33m\"\u001b[39m\u001b[33mpost\u001b[39m\u001b[33m\"\u001b[39m, \u001b[33m\"\u001b[39m\u001b[33mmorbidity_index\u001b[39m\u001b[33m\"\u001b[39m, \u001b[33m\"\u001b[39m\u001b[33mzusatzbeitrag_lag\u001b[39m\u001b[33m\"\u001b[39m])\n\u001b[32m     26\u001b[39m \u001b[38;5;66;03m# # Fit OLS model with interaction\u001b[39;00m\n\u001b[32m     27\u001b[39m \u001b[38;5;66;03m# did_model = smf.ols(\u001b[39;00m\n\u001b[32m     28\u001b[39m \u001b[38;5;66;03m#     formula=\"churn_rate ~ treatment_flag * post + morbidity_index + zusatzbeitrag_lag\",\u001b[39;00m\n\u001b[32m   (...)\u001b[39m\u001b[32m     32\u001b[39m \u001b[38;5;66;03m# # Show results\u001b[39;00m\n\u001b[32m     33\u001b[39m \u001b[38;5;66;03m# print(did_model.summary())\u001b[39;00m\n\u001b[32m---> \u001b[39m\u001b[32m35\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mstatsmodels\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mformula\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mapi\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01msmf\u001b[39;00m\n\u001b[32m     37\u001b[39m did_model = smf.ols(\n\u001b[32m     38\u001b[39m     formula=\u001b[33m\"\u001b[39m\u001b[33mchurn_rate ~ treatment_flag * post + morbidity_index + zusatzbeitrag_lag\u001b[39m\u001b[33m\"\u001b[39m,\n\u001b[32m     39\u001b[39m     data=df_model\n\u001b[32m     40\u001b[39m ).fit()\n\u001b[32m     42\u001b[39m \u001b[38;5;28mprint\u001b[39m(did_model.summary())\n",
      "\u001b[36mFile \u001b[39m\u001b[32m/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/statsmodels/formula/api.py:2\u001b[39m\n\u001b[32m      1\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mstatsmodels\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mregression\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mlinear_model\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mlm_\u001b[39;00m\n\u001b[32m----> \u001b[39m\u001b[32m2\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mstatsmodels\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mdiscrete\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mdiscrete_model\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mdm_\u001b[39;00m\n\u001b[32m      3\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mstatsmodels\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mdiscrete\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mconditional_models\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mdcm_\u001b[39;00m\n\u001b[32m      4\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mstatsmodels\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mregression\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mmixed_linear_model\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mmlm_\u001b[39;00m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/statsmodels/discrete/discrete_model.py:38\u001b[39m\n\u001b[32m     36\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mstatsmodels\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mbase\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01m_parameter_inference\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mpinfer\u001b[39;00m\n\u001b[32m     37\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mstatsmodels\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mbase\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m _prediction_inference \u001b[38;5;28;01mas\u001b[39;00m pred\n\u001b[32m---> \u001b[39m\u001b[32m38\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mstatsmodels\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mdistributions\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m genpoisson_p\n\u001b[32m     39\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mstatsmodels\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mregression\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mlinear_model\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mlm\u001b[39;00m\n\u001b[32m     40\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mstatsmodels\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mtools\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m data \u001b[38;5;28;01mas\u001b[39;00m data_tools, tools\n",
      "\u001b[36mFile \u001b[39m\u001b[32m/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/statsmodels/distributions/__init__.py:7\u001b[39m\n\u001b[32m      2\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01m.\u001b[39;00m\u001b[34;01mempirical_distribution\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m (\n\u001b[32m      3\u001b[39m     ECDF, ECDFDiscrete, monotone_fn_inverter, StepFunction\n\u001b[32m      4\u001b[39m     )\n\u001b[32m      5\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01m.\u001b[39;00m\u001b[34;01medgeworth\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m ExpandedNormal\n\u001b[32m----> \u001b[39m\u001b[32m7\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01m.\u001b[39;00m\u001b[34;01mdiscrete\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m (\n\u001b[32m      8\u001b[39m     genpoisson_p, zipoisson, zigenpoisson, zinegbin,\n\u001b[32m      9\u001b[39m     )\n\u001b[32m     11\u001b[39m __all__ = [\n\u001b[32m     12\u001b[39m     \u001b[33m'\u001b[39m\u001b[33mECDF\u001b[39m\u001b[33m'\u001b[39m,\n\u001b[32m     13\u001b[39m     \u001b[33m'\u001b[39m\u001b[33mECDFDiscrete\u001b[39m\u001b[33m'\u001b[39m,\n\u001b[32m   (...)\u001b[39m\u001b[32m     21\u001b[39m     \u001b[33m'\u001b[39m\u001b[33mzipoisson\u001b[39m\u001b[33m'\u001b[39m\n\u001b[32m     22\u001b[39m     ]\n\u001b[32m     24\u001b[39m test = PytestTester()\n",
      "\u001b[36mFile \u001b[39m\u001b[32m/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/statsmodels/distributions/discrete.py:5\u001b[39m\n\u001b[32m      3\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mscipy\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mstats\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m rv_discrete, poisson, nbinom\n\u001b[32m      4\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mscipy\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mspecial\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m gammaln\n\u001b[32m----> \u001b[39m\u001b[32m5\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mscipy\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01m_lib\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01m_util\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m _lazywhere\n\u001b[32m      7\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mstatsmodels\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mbase\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mmodel\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m GenericLikelihoodModel\n\u001b[32m     10\u001b[39m \u001b[38;5;28;01mclass\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mgenpoisson_p_gen\u001b[39;00m(rv_discrete):\n",
      "\u001b[31mImportError\u001b[39m: cannot import name '_lazywhere' from 'scipy._lib._util' (/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/scipy/_lib/_util.py)"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "df = pd.read_csv(\"../data/processed/merged_panel_clean_data.csv\")\n",
    "# import pandas as pd\n",
    "\n",
    "# # Load cleaned panel\n",
    "# df = pd.read_csv(\"merged_panel_clean_data.csv\")\n",
    "\n",
    "# Create a combined time identifier\n",
    "df[\"zeit\"] = df[\"jahr\"].astype(str) + \"Q\" + df[\"quartal\"].astype(str)\n",
    "df[\"zeit\"] = df[\"zeit\"].astype(\"category\")\n",
    "\n",
    "# Optional: define post-treatment indicator (cumulative)\n",
    "df[\"post\"] = df.groupby(\"kasse_clean\")[\"treatment_flag\"].transform(lambda x: x.cumsum() > 0)\n",
    "\n",
    "# print(df.columns.tolist())\n",
    "# import statsmodels.formula.api as smf\n",
    "\n",
    "df[\"treatment_flag\"] = df[\"treatment_flag\"].astype(int)\n",
    "df[\"post\"] = df[\"post\"].astype(int)\n",
    "df[\"churn_rate\"] = pd.to_numeric(df[\"churn_rate\"], errors=\"coerce\")\n",
    "df[\"morbidity_index\"] = pd.to_numeric(df[\"morbidity_index\"], errors=\"coerce\")\n",
    "df[\"zusatzbeitrag_lag\"] = pd.to_numeric(df[\"zusatzbeitrag_lag\"], errors=\"coerce\")\n",
    "\n",
    "df_model = df.dropna(subset=[\"churn_rate\", \"treatment_flag\", \"post\", \"morbidity_index\", \"zusatzbeitrag_lag\"])\n",
    "\n",
    "# # Fit OLS model with interaction\n",
    "# did_model = smf.ols(\n",
    "#     formula=\"churn_rate ~ treatment_flag * post + morbidity_index + zusatzbeitrag_lag\",\n",
    "#     data=df\n",
    "# ).fit()\n",
    "\n",
    "# # Show results\n",
    "# print(did_model.summary())\n",
    "\n",
    "import statsmodels.formula.api as smf\n",
    "\n",
    "did_model = smf.ols(\n",
    "    formula=\"churn_rate ~ treatment_flag * post + morbidity_index + zusatzbeitrag_lag\",\n",
    "    data=df_model\n",
    ").fit()\n",
    "\n",
    "print(did_model.summary())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "13715c7b-2908-427a-ae40-0047bf40ca6f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting statsmodels\n",
      "  Downloading statsmodels-0.14.4-cp313-cp313-macosx_11_0_arm64.whl.metadata (9.2 kB)\n",
      "Collecting linearmodels\n",
      "  Downloading linearmodels-6.1-cp313-cp313-macosx_11_0_arm64.whl.metadata (7.9 kB)\n",
      "Requirement already satisfied: numpy<3,>=1.22.3 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from statsmodels) (2.2.6)\n",
      "Collecting scipy!=1.9.2,>=1.8 (from statsmodels)\n",
      "  Downloading scipy-1.16.0-cp313-cp313-macosx_14_0_arm64.whl.metadata (61 kB)\n",
      "Requirement already satisfied: pandas!=2.1.0,>=1.4 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from statsmodels) (2.2.3)\n",
      "Collecting patsy>=0.5.6 (from statsmodels)\n",
      "  Downloading patsy-1.0.1-py2.py3-none-any.whl.metadata (3.3 kB)\n",
      "Requirement already satisfied: packaging>=21.3 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from statsmodels) (25.0)\n",
      "Collecting mypy-extensions>=0.4 (from linearmodels)\n",
      "  Downloading mypy_extensions-1.1.0-py3-none-any.whl.metadata (1.1 kB)\n",
      "Collecting Cython>=3.0.10 (from linearmodels)\n",
      "  Downloading cython-3.1.2-cp313-cp313-macosx_11_0_arm64.whl.metadata (5.9 kB)\n",
      "Collecting pyhdfe>=0.1 (from linearmodels)\n",
      "  Downloading pyhdfe-0.2.0-py3-none-any.whl.metadata (4.0 kB)\n",
      "Collecting formulaic>=1.0.0 (from linearmodels)\n",
      "  Downloading formulaic-1.1.1-py3-none-any.whl.metadata (6.9 kB)\n",
      "Collecting setuptools-scm<9.0.0,>=8.0.0 (from setuptools-scm[toml]<9.0.0,>=8.0.0->linearmodels)\n",
      "  Downloading setuptools_scm-8.3.1-py3-none-any.whl.metadata (7.0 kB)\n",
      "Requirement already satisfied: setuptools in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from setuptools-scm<9.0.0,>=8.0.0->setuptools-scm[toml]<9.0.0,>=8.0.0->linearmodels) (80.8.0)\n",
      "Collecting interface-meta>=1.2.0 (from formulaic>=1.0.0->linearmodels)\n",
      "  Downloading interface_meta-1.3.0-py3-none-any.whl.metadata (6.7 kB)\n",
      "Requirement already satisfied: typing-extensions>=4.2.0 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from formulaic>=1.0.0->linearmodels) (4.13.2)\n",
      "Collecting wrapt>=1.17.0rc1 (from formulaic>=1.0.0->linearmodels)\n",
      "  Downloading wrapt-1.17.2-cp313-cp313-macosx_11_0_arm64.whl.metadata (6.4 kB)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from pandas!=2.1.0,>=1.4->statsmodels) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from pandas!=2.1.0,>=1.4->statsmodels) (2025.2)\n",
      "Requirement already satisfied: tzdata>=2022.7 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from pandas!=2.1.0,>=1.4->statsmodels) (2025.2)\n",
      "Requirement already satisfied: six>=1.5 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from python-dateutil>=2.8.2->pandas!=2.1.0,>=1.4->statsmodels) (1.17.0)\n",
      "Downloading statsmodels-0.14.4-cp313-cp313-macosx_11_0_arm64.whl (9.9 MB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m9.9/9.9 MB\u001b[0m \u001b[31m23.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m00:01\u001b[0m00:01\u001b[0m\n",
      "\u001b[?25hDownloading linearmodels-6.1-cp313-cp313-macosx_11_0_arm64.whl (1.7 MB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.7/1.7 MB\u001b[0m \u001b[31m19.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hDownloading setuptools_scm-8.3.1-py3-none-any.whl (43 kB)\n",
      "Downloading cython-3.1.2-cp313-cp313-macosx_11_0_arm64.whl (2.8 MB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m2.8/2.8 MB\u001b[0m \u001b[31m22.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hDownloading formulaic-1.1.1-py3-none-any.whl (115 kB)\n",
      "Downloading interface_meta-1.3.0-py3-none-any.whl (14 kB)\n",
      "Downloading mypy_extensions-1.1.0-py3-none-any.whl (5.0 kB)\n",
      "Downloading patsy-1.0.1-py2.py3-none-any.whl (232 kB)\n",
      "Downloading pyhdfe-0.2.0-py3-none-any.whl (19 kB)\n",
      "Downloading scipy-1.16.0-cp313-cp313-macosx_14_0_arm64.whl (20.7 MB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m20.7/20.7 MB\u001b[0m \u001b[31m24.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m00:01\u001b[0m00:01\u001b[0m\n",
      "\u001b[?25hDownloading wrapt-1.17.2-cp313-cp313-macosx_11_0_arm64.whl (38 kB)\n",
      "Installing collected packages: wrapt, setuptools-scm, scipy, patsy, mypy-extensions, interface-meta, Cython, pyhdfe, statsmodels, formulaic, linearmodels\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m11/11\u001b[0m [linearmodels][0m [linearmodels]\n",
      "\u001b[1A\u001b[2KSuccessfully installed Cython-3.1.2 formulaic-1.1.1 interface-meta-1.3.0 linearmodels-6.1 mypy-extensions-1.1.0 patsy-1.0.1 pyhdfe-0.2.0 scipy-1.16.0 setuptools-scm-8.3.1 statsmodels-0.14.4 wrapt-1.17.2\n"
     ]
    },
    {
     "ename": "ImportError",
     "evalue": "cannot import name '_lazywhere' from 'scipy._lib._util' (/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/scipy/_lib/_util.py)",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mImportError\u001b[39m                               Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 4\u001b[39m\n\u001b[32m      1\u001b[39m get_ipython().system(\u001b[33m'\u001b[39m\u001b[33mpip install statsmodels linearmodels\u001b[39m\u001b[33m'\u001b[39m)\n\u001b[32m      3\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mpandas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mpd\u001b[39;00m\n\u001b[32m----> \u001b[39m\u001b[32m4\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mstatsmodels\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mformula\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mapi\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01msmf\u001b[39;00m\n\u001b[32m      5\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mlinearmodels\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mpanel\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m PanelOLS\n\u001b[32m      7\u001b[39m \u001b[38;5;66;03m# Load cleaned panel data\u001b[39;00m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/statsmodels/formula/api.py:2\u001b[39m\n\u001b[32m      1\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mstatsmodels\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mregression\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mlinear_model\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mlm_\u001b[39;00m\n\u001b[32m----> \u001b[39m\u001b[32m2\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mstatsmodels\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mdiscrete\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mdiscrete_model\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mdm_\u001b[39;00m\n\u001b[32m      3\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mstatsmodels\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mdiscrete\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mconditional_models\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mdcm_\u001b[39;00m\n\u001b[32m      4\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mstatsmodels\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mregression\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mmixed_linear_model\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mmlm_\u001b[39;00m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/statsmodels/discrete/discrete_model.py:38\u001b[39m\n\u001b[32m     36\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mstatsmodels\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mbase\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01m_parameter_inference\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mpinfer\u001b[39;00m\n\u001b[32m     37\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mstatsmodels\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mbase\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m _prediction_inference \u001b[38;5;28;01mas\u001b[39;00m pred\n\u001b[32m---> \u001b[39m\u001b[32m38\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mstatsmodels\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mdistributions\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m genpoisson_p\n\u001b[32m     39\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mstatsmodels\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mregression\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mlinear_model\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mlm\u001b[39;00m\n\u001b[32m     40\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mstatsmodels\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mtools\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m data \u001b[38;5;28;01mas\u001b[39;00m data_tools, tools\n",
      "\u001b[36mFile \u001b[39m\u001b[32m/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/statsmodels/distributions/__init__.py:7\u001b[39m\n\u001b[32m      2\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01m.\u001b[39;00m\u001b[34;01mempirical_distribution\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m (\n\u001b[32m      3\u001b[39m     ECDF, ECDFDiscrete, monotone_fn_inverter, StepFunction\n\u001b[32m      4\u001b[39m     )\n\u001b[32m      5\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01m.\u001b[39;00m\u001b[34;01medgeworth\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m ExpandedNormal\n\u001b[32m----> \u001b[39m\u001b[32m7\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01m.\u001b[39;00m\u001b[34;01mdiscrete\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m (\n\u001b[32m      8\u001b[39m     genpoisson_p, zipoisson, zigenpoisson, zinegbin,\n\u001b[32m      9\u001b[39m     )\n\u001b[32m     11\u001b[39m __all__ = [\n\u001b[32m     12\u001b[39m     \u001b[33m'\u001b[39m\u001b[33mECDF\u001b[39m\u001b[33m'\u001b[39m,\n\u001b[32m     13\u001b[39m     \u001b[33m'\u001b[39m\u001b[33mECDFDiscrete\u001b[39m\u001b[33m'\u001b[39m,\n\u001b[32m   (...)\u001b[39m\u001b[32m     21\u001b[39m     \u001b[33m'\u001b[39m\u001b[33mzipoisson\u001b[39m\u001b[33m'\u001b[39m\n\u001b[32m     22\u001b[39m     ]\n\u001b[32m     24\u001b[39m test = PytestTester()\n",
      "\u001b[36mFile \u001b[39m\u001b[32m/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/statsmodels/distributions/discrete.py:5\u001b[39m\n\u001b[32m      3\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mscipy\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mstats\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m rv_discrete, poisson, nbinom\n\u001b[32m      4\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mscipy\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mspecial\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m gammaln\n\u001b[32m----> \u001b[39m\u001b[32m5\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mscipy\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01m_lib\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01m_util\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m _lazywhere\n\u001b[32m      7\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mstatsmodels\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mbase\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mmodel\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m GenericLikelihoodModel\n\u001b[32m     10\u001b[39m \u001b[38;5;28;01mclass\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mgenpoisson_p_gen\u001b[39;00m(rv_discrete):\n",
      "\u001b[31mImportError\u001b[39m: cannot import name '_lazywhere' from 'scipy._lib._util' (/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/scipy/_lib/_util.py)"
     ]
    }
   ],
   "source": [
    "!pip install statsmodels linearmodels\n",
    "\n",
    "import pandas as pd\n",
    "import statsmodels.formula.api as smf\n",
    "from linearmodels.panel import PanelOLS\n",
    "\n",
    "# Load cleaned panel data\n",
    "df = pd.read_csv(\"data/processed/merged_panel_clean_data.csv\")\n",
    "\n",
    "# Create a combined time identifier\n",
    "df[\"zeit\"] = df[\"jahr\"].astype(str) + \"Q\" + df[\"quartal\"].astype(str)\n",
    "df[\"zeit\"] = df[\"zeit\"].astype(\"category\")\n",
    "\n",
    "# Define post-treatment indicator (cumulative)\n",
    "df[\"post\"] = df.groupby(\"kasse_clean\")[\"treatment_flag\"].transform(lambda x: x.cumsum() > 0)\n",
    "\n",
    "# Ensure correct data types\n",
    "df[\"treatment_flag\"] = df[\"treatment_flag\"].astype(int)\n",
    "df[\"post\"] = df[\"post\"].astype(int)\n",
    "df[\"churn_rate\"] = pd.to_numeric(df[\"churn_rate\"], errors=\"coerce\")\n",
    "df[\"morbidity_index\"] = pd.to_numeric(df[\"morbidity_index\"], errors=\"coerce\")\n",
    "df[\"zusatzbeitrag_lag\"] = pd.to_numeric(df[\"zusatzbeitrag_lag\"], errors=\"coerce\")\n",
    "\n",
    "# Drop rows with missing data in relevant columns\n",
    "df_model = df.dropna(subset=[\"churn_rate\", \"treatment_flag\", \"post\", \"morbidity_index\", \"zusatzbeitrag_lag\"])\n",
    "\n",
    "# Fit Difference-in-Differences OLS model\n",
    "ols_model = smf.ols(\n",
    "    formula=\"churn_rate ~ treatment_flag * post + morbidity_index + zusatzbeitrag_lag\",\n",
    "    data=df_model\n",
    ").fit()\n",
    "\n",
    "def run_ols_did():\n",
    "    print(\"OLS DiD Results:\")\n",
    "    print(ols_model.summary())\n",
    "\n",
    "# Prepare panel data for fixed-effects model\n",
    "df[\"zeit_dt\"] = pd.PeriodIndex(df[\"zeit\"].astype(str), freq=\"Q\").to_timestamp()\n",
    "df[\"kasse_clean\"] = df[\"kasse_clean\"].astype(str)\n",
    "df_panel = df.set_index([\"kasse_clean\", \"zeit_dt\"])\n",
    "\n",
    "# Fit fixed-effects panel model\n",
    "fe_model = PanelOLS.from_formula(\n",
    "    formula=\"churn_rate ~ treatment_flag + morbidity_index + zusatzbeitrag_lag + EntityEffects + TimeEffects\",\n",
    "    data=df_panel\n",
    ")\n",
    "\n",
    "fe_results = fe_model.fit()\n",
    "\n",
    "def run_fe_did():\n",
    "    print(\"Fixed Effects DiD Results:\")\n",
    "    print(fe_results.summary)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "75a4a166-a236-422a-a7d8-b6226d7b80e0",
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
