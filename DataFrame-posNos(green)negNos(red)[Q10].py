import pandas as pd
import numpy as np


np.random.seed(0)
data = np.random.randn(10, 4)
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])


df.loc[2, 'A'] = np.nan
df.loc[5, 'C'] = np.nan
df.loc[8, 'D'] = np.nan


def highlight_nan(val):
    if pd.isna(val):
        return 'background-color: yellow'
    else:
        return ''


styled_df = df.style.applymap(highlight_nan)


styled_df
