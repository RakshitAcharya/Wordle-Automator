import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

y = [1,128,790,835,270,78,15]
x = ["one" , "two" ,"three" ,"four" ,"five" , "six" ,"more"]
tups = list(zip(y,x))
df = pd.DataFrame(tups, columns = ["number","value"])

sns.barplot(y = df["number"],
            x = df["value"])

plt.show()
