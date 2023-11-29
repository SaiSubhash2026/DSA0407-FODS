import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import ttest_ind

# Sample data for the control and treatment groups
np.random.seed(42)  # For reproducibility
control_data = np.random.normal(loc=50, scale=10, size=100)
treatment_data = np.random.normal(loc=55, scale=10, size=100)

# Visualize the data using a box plot
plt.boxplot([control_data, treatment_data], labels=['Control', 'Treatment'])
plt.title('Box Plot of Control and Treatment Groups')
plt.ylabel('Measurement')
plt.show()

# Perform independent t-test for hypothesis testing
t_statistic, p_value = ttest_ind(control_data, treatment_data)

# Display the results
print("T-Statistic:", t_statistic)
print("P-Value:", p_value)

# Determine statistical significance
alpha = 0.05
if p_value < alpha:
    print("The difference is statistically significant. Reject the null hypothesis.")
else:
    print("The difference is not statistically significant. Fail to reject the null hypothesis.")
