Reference:

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "x": [1, 2, 3, 4, 5],
    "y": [2, 4, 1, 3, 5]
})

plt.scatter(df["x"], df["y"])
plt.show()
