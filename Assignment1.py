import turtle as t
import random, sys
BASEPYONLY = True
t.Screen()
t.speed('fastest')

# draw axis
t.color('black', '')
t.penup(); t.goto(-400, 0); t.pendown(), t.forward(800), t.stamp()
t.penup(); t.seth(90); t.goto(0, -450); t.pendown(), t.forward(900), t.stamp()

t.resizemode('user')
t.turtlesize(0.3,0.3,1)
t.shape('circle')

# Creating and ploting the data set
t.color('blue','')
nobs = 50
x_list = []
y_list = []
for _ in range(nobs):
    x_data = random.uniform(-200, 200)
    y_data = x_data * 0.5 + 10 + random.uniform(-40, 40)
    x_list.append(x_data)
    y_list.append(y_data)
    t.penup(); t.goto(x_data, y_data); t.stamp()

# Calculate x and y bar
x_mean = sum(x_list)/nobs
y_mean = sum(y_list)/nobs

# Calculate S2x
S2x = 0
for xi in x_list:
    S2x += (xi - x_mean)**2
S2x = S2x * 1/(nobs-1)

# Calculate B1 and B0
index = 0
B1 = 0
for xi in x_list:
    wi = (xi - x_mean)/((nobs-1)*S2x)
    B1 += y_list[index] * wi
    index += 1
B0 = y_mean - B1 * x_mean

# Find the end points of the regression line
pointA = (min(x_list), B0 + B1 * min(x_list))
pointB = (max(x_list), B0 + B1 * max(x_list))

# Draw the line
t.color('red', '')
t.width(width=5)
t.penup(); t.goto(pointA);t.pendown();t.goto(pointB)

# Calculate R^2
rss = 0
tss = 0
index2 = 0
for yi in y_list:
    yi_hat = 10 + x_list[index2] * 0.5
    rss += (yi_hat - y_mean) ** 2
    tss += (yi - y_mean) ** 2
    index2 += 1
R2 = rss/tss

# Round and parse the results to 5 decimal places as in the example
B0 = str(round(B0, 5))
B1 = str(round(B1, 5))
R2 = str(round(R2, 5))

# Printing the information to the screen
t.shapesize(0.001,0.001,0)
t.color('blue', '')
t.penup(); t.goto(10,295); t.pendown()
t.write('truth: Yᵢ = 10 + 0.5xᵢ + eᵢ', font=("Arial", 17, "italic"))

t.penup(); t.goto(10,275); t.pendown()
t.write('fitted: Ŷ = ' + B0 + ' + ' + B1 + 'x', font=("Arial", 17, "italic"))

t.penup(); t.goto(10,255); t.pendown()
t.write('R\u00b2 = ' + R2, font=("Arial", 17, "italic"))

t.done()

#%%
