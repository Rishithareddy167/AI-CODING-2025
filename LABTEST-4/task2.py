import numpy as np
import pandas as pd

# try to import zscore from scipy, otherwise define a fallback
try:
    from scipy.stats import zscore
    def compute_zscores(df):
        return np.abs(zscore(df, nan_policy='omit'))
except Exception:
    def compute_zscores(df):
        # fallback: (x - mean)/std where std uses ddof=0 for population
        return np.abs((df - df.mean()) / df.std(ddof=0))

def main():
    np.random.seed(42)

    # generate data
    feature1 = np.random.normal(loc=50, scale=10, size=100)
    feature2 = np.random.normal(loc=30, scale=5, size=100)

    # inject outliers at the same indices as your example
    feature1[5] = 150
    feature1[15] = -30
    feature2[25] = 100
    feature2[75] = -20

    df = pd.DataFrame({'feature1': feature1, 'feature2': feature2})

    # compute z-scores (returns a numpy array with same shape)
    z_scores = compute_zscores(df)

    # select rows where all z-scores < threshold
    threshold = 3.0
    mask = (z_scores < threshold).all(axis=1)
    filtered_df = df[mask].copy()

    # determine removed indices
    removed_indices = df.index[~mask].tolist()

    # save cleaned data
    out_path = 'cleaned_data.csv'
    filtered_df.to_csv(out_path, index=False)

    # print confirmation and summary
    print("Outliers removed. Cleaned data saved to '{}'.".format(out_path))
    print("Original rows:", df.shape[0], "Cleaned rows:", filtered_df.shape[0])
    print("Removed indices (0-based):", removed_indices)
    print("\nFirst 5 rows of cleaned data:\n", filtered_df.head().to_string(index=False))
    print("\nSummary statistics:\n", filtered_df.describe().to_string())

if __name__ == '__main__':
    main()