# A weather station records 24 hourly temperatures and should calculate the average, find max and min and convert readings fron celsius to frhrenheit.
# mathematical formular for convertion is F = 1.8C. + 32 
# Example 1
import numpy as np
temperatures_c = np.array([18,20, 22, 24, 26])
mean_temp = np.mean(temperatures_c)
min_temp = np.min(temperatures_c)
max_temp = np.max(temperatures_c)
temperatures_f =1.8 * temperatures_c + 32

print("Average", mean_temp)
print("Minimum", min_temp)
print("Maximum", max_temp)
print("Temperatures in Fahrenheit", temperatures_f)

# A hospital records the heart rates of five patients.
# Example 2
import numpy as np
heart_rates = np.array([72,85,90,68,105])
mean_heart_rate = np.mean(heart_rates)
min_heart_rate = np.min(heart_rates)
max_heart_rate =np.max(heart_rates)
sum_heart_rate = np.sum(heart_rates)

print("Average Heart Rate:", mean_heart_rate)
print("Minimum Heart Rate:", min_heart_rate)
print("Maximum Heart Rate:", max_heart_rate)
print("Sum of Heart Rates:", sum_heart_rate)