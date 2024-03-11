# source_file_transformer.py
import pandas as pd
import os

class SourceFileTransformer:
    def __init__(self, source_file_path=''):
        self.source_file_path = source_file_path
        self.transformed_df = None

    def load_and_transform_source(self):
        try:
            source_df = pd.read_excel(self.source_file_path, skiprows=2)
            columns_to_keep = [
                'Keyword', 'Avg. monthly searches', 'Competition',
                'Competition (indexed value)', 'Top of page bid (low range)',
                'Top of page bid (high range)', 'Ad impression share'
            ]
            self.transformed_df = source_df[columns_to_keep]
            data_types = {
                'Keyword': 'object',
                'Avg. monthly searches': 'int64',
                'Competition': 'object',
                'Competition (indexed value)': 'float64',
                'Top of page bid (low range)': 'float64',
                'Top of page bid (high range)': 'float64',
                'Ad impression share': 'object'
            }
            self.transformed_df = self.transformed_df.astype(data_types)
            print("Transformation successful.")
        except Exception as e:
            print(f"An error occurred during file loading or transformation: {e}")

    def save_transformed_file(self, output_path=None):
        if output_path is None:
            output_path = os.path.join('data', 'Keyword_Stat.xlsx')
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        self.transformed_df.to_excel(output_path, index=False)
        print(f"The transformed file has been saved to {output_path}")

