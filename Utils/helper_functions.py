# functions to find files, get median,


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# function to open a file and return the data in a pandas dataframe
def open_file(file_path):
    df = pd.read_csv(file_path, sep=",")
    return df


# function to find the median row of a column in a dataframe and return the value and index of the row
def find_median(df, column):
    median = df[column].median()
    median_index = df[column].sub(median).abs().idxmin()
    print(median_index)
    return median, median_index


# function to plot a histogram of a column in a dataframe and save the plot as a png file given a row name and column name
def plot_histogram(
    df: pd.DataFrame,
    feature_name,
    image_name_column="image_name",
    row_name=None,
    histogram_=False,
    bins=50,
):
    """function to plot a histogram of a column in a dataframe and save the plot as a png file given a row name and column name

    Parameters
    ----------
    df : pandas dataframe
        dataframe of image quantification data and image names
    column_name : str
        name of the column in the dataframe to plot a histogram of
    row_name : str, optional
        name of row in dataframe (image name)
    histogram_ : bool, optional
        whether or not to plot a histogram, by default True
    bins : int, optional
        the number of bins to use in the histogram, by default 50
    """
    plt.subplots(figsize=(20, 2.5))
    sns.distplot(
        df[feature_name], bins=bins, kde=True, hist=False, kde_kws={"shade": True}
    )
    plt.axvline(
        df[df[image_name_column] == row_name][feature_name].values[0],
        color="r",
        linestyle="--",
    )
    plt.title(feature_name)
    # save the plot to a file
    plt.savefig(f"Figures/{feature_name}.png")
    # plt.show()
    plt.close()
