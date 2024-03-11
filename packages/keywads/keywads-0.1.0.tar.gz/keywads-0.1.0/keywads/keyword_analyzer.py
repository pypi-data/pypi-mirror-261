# keyword_analyzer.py
import pandas as pd
import os

class KeywordAnalyzer:
    def __init__(self, file_path=None):
        if file_path is None:
            file_path = os.path.join('data', 'Keyword_Stat.xlsx')
        self.file_path = file_path
        self.df = None

    def load_data(self):
        try:
            self.df = pd.read_excel(self.file_path)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print(f"File not found at {self.file_path}. Please check the file path.")

    def preprocess_data(self):
        self.df['Average Bid'] = (self.df['Top of page bid (low range)'] + self.df['Top of page bid (high range)']) / 2
        self.df['Competition (indexed value)'] = self.df['Competition (indexed value)'].fillna(0)

    def calculate_ranks(self):
        self.df['Rank'] = self.df['Avg. monthly searches'] / (1 + self.df['Competition (indexed value)'])
        self.df['Adjusted Rank'] = self.df['Avg. monthly searches'] / ((1 + self.df['Competition (indexed value)']) * self.df['Average Bid'])
        self.df['Adjusted Rank'] = self.df.apply(
            lambda x: x['Avg. monthly searches'] / (1 + x['Competition (indexed value)']) if x['Average Bid'] == 0 else x['Adjusted Rank'], axis=1)

    def sort_and_extract_top_keywords(self, top_n=200):
        return self.df.sort_values(by='Adjusted Rank', ascending=False).head(top_n)

    def save_to_excel(self, data, output_file_name='top_200_keywords_adjusted.xlsx'):
        output_path = os.path.join('output', output_file_name)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        data.to_excel(output_path, index=False)
        print(f"The adjusted list of top keywords has been saved to {output_path}")

    def run_analysis(self, output_file_name='top_200_keywords_adjusted.xlsx', top_n=200):
        output_path = os.path.join('output', output_file_name)
        self.load_data()
        if self.df is not None:
            self.preprocess_data()
            self.calculate_ranks()
            top_keywords = self.sort_and_extract_top_keywords(top_n=top_n)
            self.save_to_excel(output_path, top_keywords)
