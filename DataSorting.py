# Sort homelessness by individuals
import pandas as pd
homelessness_ind = homelessness.sort_values(["individuals"],ascending=[True])

# Print the top few rows
print(homelessness_ind.head())
