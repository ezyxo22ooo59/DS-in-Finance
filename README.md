# DS in Finance and Insurance

## Final Projecct: Comprehensive Housing Price Prediction in Daegu Using Machine Learning Models Summary

(See detail in project report)

### Introduction
The primary objective of this project was to analyze and predict apartment prices in Daegu, South Korea, over a decade (2007-2017). With economic and population growth, the fluctuation in housing prices has become a significant concern. The dataset comprises 1.4 million observations with 29 potential factors influencing housing prices.

### Data Import and Structure
The dataset was loaded into Python using the read.csv() function and analyzed for structure and dimensions. It contained 5891 observations and 30 variables, including integers, objects, and floats. The variables ranged from sale prices and construction year to the number of nearby facilities and the type of heating system.

### Data Cleaning and Feature Selection
Initial analysis showed no missing values in the dataset. Categorical variables were converted to numerical values for analysis. A heat map was used to visualize correlations, identifying key features such as apartment size and nearby facilities that significantly influence housing prices.

### Model Development
The project employed various machine learning models to predict housing prices, including:
- Linear Regression: Initial attempts with linear regression revealed a high RMSE, suggesting the presence of outliers.
- Outlier Analysis: Outliers were identified and removed, slightly improving the RMSE.
- Feature Importance: Analysis indicated that some features, like the number of elevators and parking spaces, had high coefficients due to correlations with other variables.

### Optimization and Comparison of Models
Further optimization was done using the Gradient Boosting Regressor, significantly improving model performance. The following models were developed and compared based on RMSE and R² values:
- Linear Regression: Had the highest RMSE.
- K-Nearest Neighbors (KNN): Performed better than linear regression.
- Lasso Regression and Ridge Regression: Showed similar performance to linear regression.
- Decision Tree and Random Forest: These non-linear models outperformed the others, with lower RMSE and higher R² values.

### Final Results 
The decision tree and random forest models were found to be the most effective, providing the best balance between accuracy and complexity. Feature importance analysis revealed that apartment size, year sold, year built, and nearby facilities were the most influential factors in determining housing prices.

### Conclusion
This project successfully demonstrated a comprehensive approach to housing price prediction using various machine learning models. The findings provide valuable insights into the factors affecting housing prices and the effectiveness of different predictive models. The methodology and code can be adapted for similar analyses in other regions or with other datasets, making it a versatile tool for real estate analytics.

## Other Class Project

## Unit 1
This project utilizes the turtle graphics library to visually demonstrate a simple linear regression model. Below is a summary of the code:

1. Setup and Axis Drawing:
- The project initializes the turtle graphics screen and sets the drawing speed to 'fastest'.
- It draws the X and Y axes using black lines.

2. Creating and Plotting the Data Set:
- The turtle's shape is set to a small circle.
- 50 random data points (nobs = 50) are generated. Each x_data point is randomly selected from a uniform distribution between -200 and 200. The corresponding y_data point is calculated using the formula y=0.5×x+10 plus some random noise.
- These points are plotted on the screen with blue stamps.

3. Calculating Regression Parameters:
- The means of the x_list and y_list are computed.
- The variance 𝑆𝑥^2 of the x_list is calculated.
- The regression coefficients 
𝐵1 (slope) and 𝐵0 (intercept) are computed using the least squares method.

4. Drawing the Regression Line:
- The endpoints of the regression line are calculated based on the minimum and maximum x_data.
- The regression line is drawn in red.

5. Calculating and Displaying R Square Value:
- The project computes the total sum of squares (TSS) and the regression sum of squares (RSS) to determine the coefficient of determination, R square.
- The regression equation and R square value are displayed on the screen using turtle writing.

6. Displaying Information:
- The true model equation, fitted regression equation, and R square value are printed on the screen.

At last, the turtle graphics window is closed using t.done().

## Unit 2
This project analyzes the distribution of gaps between occurrences of a specific number in the New York Lottery winning numbers dataset. Below is a summary of the code:

1. Read the CSV File:
- The project reads a CSV file named Lottery_NY_Lotto_Winning_Numbers.csv using the pandas library.
- The data is stored in a DataFrame named df.

2. Calculate the Raw Distribution of the Gap for a Specific Number:
- The chosen number for analysis is set to 2 (chosenNumber = 2).
- A function distributeGap(num) is defined to calculate the distribution of gaps between occurrences of the chosen number.
- Within the function:
    - An array gap is initialized to store the counts of gaps of different lengths (0 to 10+).
    - The function iterates through each row of the DataFrame to check if the chosen number appears in the 'Winning Numbers' or 'Bonus #' columns.
    - If the chosen number is found, the count of the current gap length is incremented. Gaps longer than 10 are grouped into the 10+ category.
- The result of the gap distribution is stored in the variable result.

3. Calculate the Percentage and Print the Result:
- The project prints the gap distribution along with the percentage of each gap length.
- It prints the header: "number = 2", followed by the column titles "Gap", "count", and "percent".
- For each gap length in the result array, it prints the gap length, the count of occurrences, and the percentage (rounded to four decimal places).

Finally, the project outputs the distribution of gaps for the number 2, showing how frequently different gap lengths occur in the lottery data.

## Unit 3
This project analyzes term life insurance data to explore the relationship between various factors and the policy face value (FACE) using linear regression and transformation techniques. Below is a summary of the project:

1. Reading the CSV File:
- The project reads a CSV file named TermLifeData.csv using the pandas library.
- The data is stored in a DataFrame named df.

2.  Filtering Data:
- The data is filtered to include only rows where the FACE value is greater than or equal to 50,000.
- The filtered data is stored in df_filtered.

3. Box-Cox Transformation:
- The FACE values in the filtered data are transformed using the Box-Cox method to normalize the distribution.
- The transformed values are stored in a new column FACEbc.
- The project creates histograms to visualize the distribution of FACE before and after transformation.

4. Data Preparation:
- The project prepares the data for regression analysis by creating new columns:
    - INCOME is transformed using the natural logarithm.
    - MAR0 is a binary variable indicating whether MARSTAT is 0.
    - MAR2 is a binary variable indicating whether MARSTAT is 2.

5. Linear Regression Analysis:
- The project performs a linear regression analysis to model the relationship between FACEbc and the predictor variables (EDUCATION, NUMHH, INCOME, MAR0, MAR2).
- The intercept and coefficients of the regression model are printed.

6. Regression Diagnostics:
- The project calculates various regression diagnostics including:
    - 𝑅^2(coefficient of determination)
    - Residual standard error (sigma_hat)

7. Statistical Analysis with Statsmodels:
- The project uses the statsmodels library to perform a detailed statistical analysis and ANOVA (Analysis of Variance).
- The summary of the regression model and the ANOVA table are printed.

8. Predictive Analysis:
- The project makes a prediction based on the regression model for a specific set of input values.
- The prediction and the regression coefficients are printed.

## Unit 4
This project performs non-linear regression using gradient descent to fit a model to a dataset containing x and y values. Below is a summary of the project:

1. Reading the CSV File:
- The project reads a CSV file named data.csv using the pandas library.
- The data is stored in a DataFrame named df.
- The x and y values are extracted and converted to float32 type arrays.

2. Initializing Parameters:
- The regression parameters (beta) and their initial update values are initialized to arrays of zeros and 0.1s, respectively.
- A small learning rate (rate) is set to 0.00005.

3. Defining Error and Gradient Calculation Functions:
- calculateE(beta, X, y): Computes the error (sum of squared differences) between the actual y values and the predicted values using the current beta parameters.
- calculateF(beta, X, y): Computes the gradient of the error function with respect to the beta parameters.

4. Gradient Descent Optimization:
- The project iterates 10,000 times to update the beta parameters using gradient descent.
- In each iteration, the current error is appended to the RSS list, the beta parameters are updated, and the gradient is recalculated.

5. Printing Results:
- The smallest loss achieved during the optimization.
- The learning rate used.
- The final estimated beta parameters.
- The number of updates performed.

6. Plotting the Results:
- A scatter plot of the original x and y values.
- A plot of the true function y = 2 * np.sin(0.5*X - 3) + 0.1 * X.
- A plot of the fitted function using the estimated beta parameters.
- A plot of the loss (error) over the number of updates to visualize the convergence of the optimization.
