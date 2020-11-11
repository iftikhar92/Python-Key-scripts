# Import necessarily libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load data
# titanic = sns.load_dataset("titanic")
titanic = pd.read_csv('billing1.csv')
#print (titanic)
# Set up a factorplot
#print (titanic)
#g = sns.factorplot("smoker", "total_bill", "sex", data=titanic, kind="bar", palette="muted", legend=False)
#sns.factorplot()

g = sns.factorplot("total_bill", "smoker", data=titanic, kind="bar", palette="muted", legend=False)
sns.factorplot()
# Show plot
plt.show()