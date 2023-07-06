import argparse

from helper_functions import find_median, open_file, plot_histogram


# define the main function for the program to run from here
def main(
    file_path: str,
    feature_name: str,
    image_name="image_name",
    median=True,
    histogram=True,
    bins=50,
):

    # open the file and return the data in a pandas dataframe
    df = open_file(file_path)

    # find the median of the feature in the dataframe and return the value and index of the row
    if median:
        median, median_index = find_median(df, feature_name)
        image_name = df[29:30].values[-1:].tolist()[0].pop()
        plot_histogram(
            df=df,
            feature_name=feature_name,
            image_name_column="image_name",
            row_name=image_name,
            histogram_=histogram,
            bins=bins,
        )
    else:
        plot_histogram(
            df,
            feature_name,
            image_name_column="image_name",
            row_name=image_name,
            histogram_=histogram,
            bins=bins,
        )


# run the main function if the program is run from the command line
if __name__ == "__main__":
    # initialize the parser
    parser = argparse.ArgumentParser(description="Process some integers.")
    # argument for the file path
    parser.add_argument("--file_path", type=str, help="path to the file")
    # argument for the feature name
    parser.add_argument("--feature_name", type=str, help="name of the feature to plot")
    # argument for the image name
    parser.add_argument("--image_name", type=str, help="name of the image to plot")
    # argument for whether or not to find the median
    parser.add_argument("--median", type=bool, help="whether or not to find the median")
    # argument for whether or not to plot the histogram
    parser.add_argument(
        "--histogram", type=bool, help="whether or not to plot the histogram"
    )
    # argument for the number of bins
    parser.add_argument(
        "--bins", type=int, help="number of bins to use in the histogram"
    )
    args = parser.parse_args()

    # call the main function
    main(
        args.file_path,
        args.feature_name,
        args.image_name,
        args.median,
        args.histogram,
        args.bins,
    )
