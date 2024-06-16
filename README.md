# DS-in-Finance
## Project 1
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

## Project 2
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

## Project 3
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
