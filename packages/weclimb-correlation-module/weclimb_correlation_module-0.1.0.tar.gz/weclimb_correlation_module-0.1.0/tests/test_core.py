import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class ClimateDataAnalysis:
    """
    A class for loading, preprocessing, aggregating, and analyzing climate data.
    """
    
    def __init__(self, datasets_info):
        """
        Initializes the ClimateDataAnalysis class.

        Parameters:
        - datasets_info: A list of dictionaries, each containing the path, variables,
          and levels (if applicable) for each dataset to be analyzed.
        """
        self.datasets_info = datasets_info
        self.datasets = {}  # Stores loaded xarray datasets.
        self.aggregated_data = {}  # Stores aggregated data for analysis.
        self.dataframe = pd.DataFrame()  # DataFrame for storing aggregated data for correlation analysis.

    def load_and_process_datasets(self):
        """
        Loads datasets specified in datasets_info, performing initial preprocessing checks.
        """
        for dataset_info in self.datasets_info:
            path = dataset_info['path']
            try:
                dataset = xr.open_dataset(path)
                if self.pre_process(dataset):
                    # Only add datasets to processing queue if they pass preprocessing checks.
                    self.datasets[path] = dataset
                    print(f"Successfully processed {path}")
                else:
                    print(f"Dataset {path} did not pass pre-processing checks.")
            except Exception as e:
                print(f"Failed to process {path}: {e}")

    def pre_process(self, dataset):
        """
        Preprocesses a dataset to ensure it has a 'time' dimension and minimal missing data.

        Parameters:
        - dataset: The xarray Dataset to check.

        Returns:
        - bool: True if dataset passes the checks, False otherwise.
        """
        if 'time' not in dataset.dims:
            print("Dataset does not have a 'time' dimension.")
            return False
        
        missing_threshold = 0.1  # Threshold for allowed missing data percentage.
        for var in dataset.data_vars:
            missing_data_fraction = dataset[var].isnull().mean().item()
            if missing_data_fraction > missing_threshold:
                print(f"Variable {var} has {missing_data_fraction*100:.2f}% missing data, exceeding the threshold.")
                return False
        
        return True

    def aggregate_over_time(self, freq='A'):
        """
        Aggregates data over time for all variables in all loaded datasets.

        Parameters:
        - freq: Frequency for aggregation (e.g., 'M' for monthly, 'A' for annual).
        """
        for path, dataset in self.datasets.items():
            for dataset_info in self.datasets_info:
                if dataset_info['path'] == path:
                    variables = dataset_info['variables']
                    levels = dataset_info.get('levels', None)
                    for variable in variables:
                        if variable in dataset.variables:
                            self.aggregate_variable(dataset, variable, levels, freq, path)

    def aggregate_variable(self, dataset, variable, levels, freq, path):
        """
        Helper function to aggregate a specific variable over time.

        Parameters:
        - dataset: The xarray Dataset containing the variable.
        - variable: The name of the variable to aggregate.
        - levels: Specific levels (if any) to aggregate over.
        - freq: The frequency for aggregation.
        - path: The path of the dataset for logging purposes.
        """
        try:
            if levels:
                for level in levels:
                    # Aggregate for each specified level.
                    aggregated = dataset[variable].sel(level=level).resample(time=freq).mean()
                    key = f"{variable}_{level}"
                    self.aggregated_data[key] = aggregated
            else:
                # Aggregate single-level variables.
                aggregated = dataset[variable].resample(time=freq).mean()
                self.aggregated_data[variable] = aggregated
            print(f"Successfully aggregated {variable} in {path} over {freq}")
        except Exception as e:
            print(f"Failed to aggregate {variable} in {path}: {e}")

    def create_dataframe_from_aggregated_data(self):
        """
        Converts aggregated data into a pandas DataFrame for correlation analysis.
        """
        combined_data = {}
        for var, data_array in self.aggregated_data.items():
            combined_data[var] = data_array.to_series()
        self.dataframe = pd.DataFrame(combined_data)

    def plot_correlation_matrix(self):
        """
        Plots a correlation matrix using seaborn for the aggregated data.
        """
        if not self.dataframe.empty:
            plt.figure(figsize=(10, 8))
            sns.heatmap(self.dataframe.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5, vmin=-1, vmax=1)
            plt.title('Correlation Matrix of Climate Variables')
            plt.xticks(rotation=45)
            plt.yticks(rotation=45)
            plt.show()
        else:
            print("The DataFrame is empty. Please ensure data is loaded and processed before plotting.")

    def get_correlation_matrix(self):
        """
        Retrieves the correlation matrix of the DataFrame.

        Returns:
        - The correlation matrix if the DataFrame is not empty, None otherwise.
        """
        if not self.dataframe.empty:
            return self.dataframe.corr()
        else:
            print("The DataFrame is empty. Please ensure data is loaded and processed before calculating.")
            return None

    def get_extreme_correlations(self):
        """
        Identifies and returns the highest and lowest correlations from the correlation matrix.

        Returns:
        - A dictionary with the highest and lowest correlation pairs and their values.
        """
        corr_matrix = self.get_correlation_matrix()
        if corr_matrix is not None:
            corr_pairs = corr_matrix.unstack()
            sorted_pairs = corr_pairs.sort_values(kind="quicksort")
            strong_positive = sorted_pairs[(sorted_pairs < 1) & (sorted_pairs > 0)]
            strong_negative = sorted_pairs[sorted_pairs < 0]
            highest_corr = strong_positive[-1]
            lowest_corr = strong_negative[0]
            highest_pair = strong_positive.idxmax()
            lowest_pair = strong_negative.idxmin()
            print(f"Highest correlation ({highest_pair}): {highest_corr}")
            print(f"Lowest correlation ({lowest_pair}): {lowest_corr}")
            return {'highest': {'pair': highest_pair, 'corr': highest_corr}, 'lowest': {'pair': lowest_pair, 'corr': lowest_corr}}
        else:
            return None

    def unload_datasets(self):
        """
        Clears the loaded xarray datasets from memory to free up resources.
        """
        self.datasets.clear()
        print("Datasets have been unloaded from memory.")


# Example of using the class with custom variables
datasets_info = [
    {
        'path': '/media/posiden/posiden/ERA5_Data/pv_250_500_850hpa.nc',
        'variables': ['pv'],
        'levels': [250, 500, 850]
    },
    {
        'path': '/media/posiden/posiden/ERA5_Data/hcc_tcc_tp.nc',
        'variables': ['hcc', 'tcc', 'tp'],
        'levels': None
    },
    {
        'path': '/media/posiden/posiden/ERA5_Data/rh_250_500_850hpa.nc',
        'variables': ['r'],
        'levels': [250, 500, 850]
    },
    {
        'path': '/media/posiden/posiden/ERA5_Data/t_250_500_850hpa.nc',
        'variables': ['t'],
        'levels': [250, 500, 850]
    }
]

# Initialize the ClimateDataAnalysis class with the datasets information
analysis = ClimateDataAnalysis(datasets_info)

# Load and preprocess the datasets
analysis.load_and_process_datasets()

# Aggregate data annually for all variables in all datasets
analysis.aggregate_over_time(freq='A')

# Create a DataFrame from the aggregated data
analysis.create_dataframe_from_aggregated_data()

# Plot the correlation matrix for the aggregated data
analysis.plot_correlation_matrix()

# Retrieve and print the highest and lowest correlations
extreme_correlations = analysis.get_extreme_correlations()
print("Extreme Correlations:", extreme_correlations)

# Unload the datasets to free up memory
analysis.unload_datasets()
