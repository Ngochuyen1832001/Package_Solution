import pandas as pd
# Create DataFrame1
dataFrame1 = pd.DataFrame(
   {
      "Car": ['BMW', 'Lexus', 'Audi', 'Mustang', 'Bentley', 'Jaguar'],"Units": [100, 150, 110, 80, 110, 90]
   }
)
print"DataFrame1 ...\n",dataFrame1

# Create DataFrame2
dataFrame2 = pd.DataFrame(
   {
      "Car": ['BMW', 'Lexus', 'Audi', 'Mustang', 'Mercedes', 'Jaguar'],"Reg_Price": [7000, 1500, 5000, 8000, 9000, 6000]

   }
)
print"\nDataFrame2 ...\n",dataFrame2

# merge DataFrames
mergedRes = pd.merge(dataFrame1, dataFrame2)
print"\nMerged data frame...\n", mergedRes
