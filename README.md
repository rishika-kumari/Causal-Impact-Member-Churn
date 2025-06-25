# Causal-Impact-Member-Churn
Data Science project

Topic 1: Causal Impact of Contributions on Member Churn
Goal: Causal Effect on Additional Contribution Rate on Member Churn in Statutory Health
Insurance Funds
Project Description:
Since 2016, statutory health insurance funds in Germany have levied additional contributions on top
of the average rate to balance the gap between income and expenditure. The frequency of such
increases has risen significantly in recent years. Whenever a fund raises its contributions, insured
individuals have the right to terminate their membership and switch to a different fund within four
weeks. This project investigates the causal effect of additional contributions on member churn,
testing the hypothesis that these financial changes are a key driver of fund switching. It also explores
whether the timing and scale of competitor fund increases reduce the likelihood of individual churn.
By applying causal inference techniques, the aim is to go beyond predictive modeling to understand
the actual drivers of churn and inform strategic decisions on setting contribution levels.
Research Questions:
▪ What is the causal impact of a fund’s additional contribution increase on its membership levels?
▪ To what extent do competitor fund contributions influence switching behavior?
▪ Can causal inference uncover insights that predictive models overlook?Tasks:
▪ Preprocess and integrate data on contributions, membership, and morbidity indicators from insurance funds.
▪ Conduct exploratory data analysis to understand trends and potential confounders.
▪ Apply causal inference methods to estimate treatment effects.
▪ Validate model assumptions and test robustness of results using falsification strategies.
▪ Build a predictive model estimating member churn based on own and competitor contribution decisions.
▪ Develop an interactive prototype to compare causal effects and predictive outputs across funds and time periods.
Expected Outcome:
▪ A causal analysis pipeline that quantifies how contribution changes affect member churn.
▪ A predictive model estimating member churn based on contribution decisions (excluding deceased individuals) to
benchmark against causal models.
▪ A web interface dashboard displaying both causal estimates and predictive churn outcomes for different funds.
Data:
▪ Additional contribution rates from >100 statutory health insurance funds (2016–2025), biannual (quarterly granularity if
available).
▪ Number of insured individuals per fund as of Jan 1 each year (quarterly granularity if available).
▪ If desired: revenue from the additional contribution per insured person per health insurance fund per year
▪ Risk factor (morbidity) as a proxy for the insured structure per health insurance fund from 2019-2025 and the number of
deceased insured people.  THis is the project description and attached the data provided. Could you explain every bit of details to be done for the completion of project and step by step to follow with the attached data
