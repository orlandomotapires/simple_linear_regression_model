# Linear Regression Analysis

## Introduction

This repository contains a Python script for performing linear regression analysis on temperature and maleability angular data of metal prototypes. In this README, I'll explain the basic concepts of linear regression, describe the content used in the code, and discuss the results obtained from the analysis.

## Linear Regression Basics

Linear regression is a statistical method used to model the relationship between a dependent variable and one or more independent variables. In its simplest form, known as simple linear regression, there is only one independent variable. The model assumes that the relationship between the variables is linear, meaning it can be represented by a straight line.

The equation for a simple linear regression model is:

Y = b0 + b1*X + ε

Where:
- Y is the dependent variable
- X is the independent variable
- b0 is the intercept
- b1 is the slope
- ε is the error term

The goal of linear regression is to estimate the values of b0 and b1 that minimize the sum of the squared differences between the observed and predicted values of the dependent variable.

## Content Used in the Code

The code in this repository reads data from a file named `data.txt`, where each line contains temperature and maleability angular data for metal prototypes. The data is formatted as follows:

Temperature1 Maleability_Angular1 Maleability_Angular2 Maleability_Angular3
Temperature2 Maleability_Angular1 Maleability_Angular2 Maleability_Angular3

The code performs the following steps:
1. Reads and formats the data.
2. Performs linear regression analysis for each prototype.
3. Plots scatter plots and linear regression lines.
4. Calculates R-squared values, performs hypothesis tests for regression, and estimates malleability at 30°C for each prototype.

## Statistical Functions Used

- **mean(values):** Calculates the mean of a list of values.
- **linear_regression(X, Y):** Calculates the coefficients of the simple linear regression model (b0 and b1) using the least squares method.
- **r_squared(X, Y, b0, b1):** Calculates the coefficient of determination (R^2) for a linear regression model.
- **stats.linregress(X, Y):** Performs a linear regression hypothesis test and provides information about the slope, intercept, correlation coefficient, p-value, and standard error of the estimate.

## Results

The results of the analysis are as follows:

### Prototype A

- **R-squared (R^2):** 0.0087
  - The R-squared value indicates that only approximately 0.87% of the variance in the maleability angular of Prototype A can be explained by changes in temperature. This suggests a very weak relationship between temperature and maleability angular for Prototype A.
- **p-value for Hypothesis Test for Regression:** 0.6949
  - The p-value associated with the hypothesis test for regression is 0.6949, which is greater than the typical significance level of 0.05. This suggests that there is no significant linear relationship between temperature and maleability angular for Prototype A.
- **Estimated Malleability at 30°C:** 6.8245
  - The estimated maleability at 30°C for Prototype A is 6.8245. However, given the weak relationship indicated by the low R-squared value and non-significant p-value, this estimate should be interpreted with caution.

### Prototype B

- **R-squared (R^2):** 0.8251
  - The R-squared value indicates that approximately 82.51% of the variance in the maleability angular of Prototype B can be explained by changes in temperature. This suggests a strong positive relationship between temperature and maleability angular for Prototype B.
- **p-value for Hypothesis Test for Regression:** 0.0000
  - The p-value associated with the hypothesis test for regression is 0.0000, which is less than the typical significance level of 0.05. This indicates that there is a significant linear relationship between temperature and maleability angular for Prototype B.
- **Estimated Malleability at 30°C:** 4.8059
  - The estimated maleability at 30°C for Prototype B is 4.8059. Given the strong relationship indicated by the high R-squared value and significant p-value, this estimate is likely to be more reliable.

### Prototype C
- **R-squared (R^2):** 0.4441
  - The R-squared value indicates that approximately 44.41% of the variance in the maleability angular of Prototype C can be explained by changes in temperature. This suggests a moderate positive relationship between temperature and maleability angular for Prototype C.
- **p-value for Hypothesis Test for Regression:** 0.0013
  - The p-value associated with the hypothesis test for regression is 0.0013, which is less than the typical significance level of 0.05. This indicates that there is a significant linear relationship between temperature and maleability angular for Prototype C.
- **Estimated Malleability at 30°C:** 7.7397
  - The estimated maleability at 30°C for Prototype C is 7.7397. This estimate is subject to the moderate relationship indicated by the R-squared value and significant p-value.

## Conclusion

Linear regression analysis provides insights into the relationship between temperature and maleability angular of metal prototypes. The results obtained from the analysis can be used to make predictions and inform decision-making processes related to metal processing and manufacturing.