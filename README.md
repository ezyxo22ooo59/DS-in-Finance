# DS-in-Finance

This Python project utilizes the turtle graphics library to visually demonstrate a simple linear regression model. Below is a summary of the code:

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
