# Keywads Library

## About

The Keywads Library is a Python package designed to simplify the process of analyzing keyword data from Excel files. It includes tools for transforming source files into a standardized format and analyzing keyword metrics to rank keywords based on competition and search volume.

## Installation

To use this library, clone or download it into your project directory or a location in your Python path.

```bash
git clone https://github.com/hashangit/keywads.git
```

## Prerequisites

Ensure you have Python and `pandas` installed in your environment:

```bash
pip install pandas
```

## How to Use

### Structure Your Application Folder

We recommend structuring your application folder as follows for ease of use with default settings:

```
your_project/
│
├── keywads/
│   ├── __init__.py
│   ├── source_file_transformer.py
│   └── keyword_analyzer.py
│
├── data/
│   └── your_source_file.xlsx
│
├── output/
│
└── your_script.py
```

### Example Usage

1. **Transforming a Source File**: First, ensure your source Excel file is in the `data` folder. Then use `SourceFileTransformer` to standardize the format.

2. **Analyzing Keywords**: After transforming the source file, use `KeywordAnalyzer` to analyze and rank keywords, saving the results in the `output` folder.

Here's an example snippet you can put in `your_script.py`:

```python
from keywads import SourceFileTransformer, KeywordAnalyzer

# Transform the source file
transformer = SourceFileTransformer(source_file_path='data/your_source_file.xlsx')
transformer.load_and_transform_source()
transformer.save_transformed_file()

# Analyze keywords
analyzer = KeywordAnalyzer()
analyzer.run_analysis()
```

This will process `your_source_file.xlsx` from the `data` folder, standardize it, and then analyze the keywords, saving the results as `top_200_keywords_adjusted.xlsx` in the `output` folder.

### Custom Paths

You can also specify custom paths for both the source and output files if your project structure differs from the recommended setup:

```python
# Specify custom paths
custom_source_path = 'path/to/your/custom_source_file.xlsx'
custom_output_path = 'path/to/your/custom_output_directory/'

# Initialize the transformer with a custom path
transformer = SourceFileTransformer(source_file_path=custom_source_path)
transformer.load_and_transform_source()
transformer.save_transformed_file(output_path=custom_output_path + 'Keyword_Stat.xlsx')

# Initialize the analyzer with custom input and output paths
analyzer = KeywordAnalyzer(file_path=custom_output_path + 'Keyword_Stat.xlsx')
analyzer.run_analysis(output_file_name='Custom_Top_200_Keywords.xlsx')
```

### Note

Remember to replace `your_source_file.xlsx`, `path/to/your/custom_source_file.xlsx`, and `path/to/your/custom_output_directory/` with the actual paths to your files and directories.

## Support

For support, please open an issue in the GitHub repository at https://github.com/hashangit/keywads.

## License

[MIT License](LICENSE) - see the LICENSE file for details.