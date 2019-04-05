import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series(np.random.randn(100))

plt.plot(s)

df = pd.DataFrame()
df['returns'] = s
df['abs_returns'] = np.abs(s)

print(df.head())
plt.show()
