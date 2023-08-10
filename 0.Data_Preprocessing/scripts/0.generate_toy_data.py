# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: base
#     language: python
#     name: python3
# ---

# %%
import pathlib

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# %%
# Define paths
test_data_output_path = pathlib.Path("../data/test_data_output.csv")

# %%
# set seed
np.random.seed(40)
# generate fake image data with 6 columns and 100 rows with image names as one of the columns and data from random gaussian data, geometric, poisson, binomial, exponential, uniform distributions
df = pd.DataFrame(np.random.randn(100, 6), columns=list("ABCDEF"))
# df['image_name'] = ['image_' + str(i) for i in range(100)]
# df['geometric'] = np.random.geometric(p=0.5, size=100)
# df['poisson'] = np.random.poisson(lam=1.0, size=100)
# df['binomial'] = np.random.binomial(n=10, p=0.5, size=100)
# df['exponential'] = np.random.exponential(scale=1.0, size=100)

# add image name column to the dataframe
df["image_name"] = ["image_" + str(i) for i in range(100)]

df.to_csv(test_data_output_path, index=False)

# %%
# determine how many bins are needed for the histogram based on the number of unique image names in the dataframe
bins = len(df["image_name"].unique())
bins = 25

# create a density plot for each column in the dataframe except the image name column
# the number of bins is set to the number of unique image names in the dataframe
# set the lower and upper bounds of the x-axis to the min and max values of the column being plotted
for col in df.columns:
    if col != "image_name":
        sns.distplot(df[col], bins=bins, kde=True, hist=False, kde_kws={"shade": True})

# %%

# %%
# if given an image name show where in the distribution the image falls for each column in the dataframe
image_name = "image_1"
for col in df.columns:
    if col != "image_name":
        sns.distplot(df[col], bins=bins, kde=True, hist=False, kde_kws={"shade": True})
        plt.axvline(
            df[df["image_name"] == image_name][col].values[0], color="r", linestyle="--"
        )
        plt.title(col)
        plt.show()

# %%
