# linear curve fitting 

import numpy as np

hours = np.array([1, 2, 3, 4, 5])
scores = np.array([45, 50, 58, 65, 72])

coefficients = np.polyfit(hours, scores, 1)

print("Slope:", coefficients[0])
print("Intercept:", coefficients[1])

predicted_score = np.polyval(coefficients, 6)

print("Predicted score:", predicted_score)

#Visualizing the fitted curve 

import numpy as np
import matplotlib.pyplot as plt

hours = np.array([1, 2, 3, 4, 5])
scores = np.array([45, 50, 58, 65, 72])

coefficients = np.polyfit(hours, scores, 2)

predicted_scores = np.polyval(coefficients, hours)

plt.scatter(hours, scores, label="Actual data")
plt.plot(hours, predicted_scores, label="Fitted line")

plt.xlabel("Hours studied")
plt.ylabel("Exam scores")
plt.title("Study Hours vs Exam Scores")

plt.legend()
plt.show()