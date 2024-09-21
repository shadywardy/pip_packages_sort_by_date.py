# pip_packages_sort_by_date.py

Welcome to **pip_packages_sort_by_date.py**! 🌟 This Python script helps you effortlessly list all installed Python packages in your virtual environment, sorted by their installation date. It's a handy tool for tracking package management and quickly accessing uninstall commands.

## Features
- **Sorts packages** by installation date in descending order, so you can easily see the newest additions!
- **Exports** the results to an Excel file, including uninstall commands for a streamlined package management experience.
- User-friendly and easily customizable to fit your needs!

## Getting Started

### Prerequisites
To run this script, ensure you have the following dependencies installed:

- `pandas`
- `openpyxl`

You can install these dependencies via pip:

```bash
pip install pandas openpyxl
```

### Usage

1. **Set the Path**: In the script, update the `site_packages_dir` variable to point to your `site-packages` directory.

    ```python
    # Use the provided 'site-packages' directory
    # site_packages_dir = r'D:\XXXXX\XXXXX\venv\Lib\site-packages'
    
    site_packages_dir = r'YOUR_PACKAGE_PATH'
    ```

2. **Run the Script**: Execute the script in your Python environment. This will generate an Excel file with all the installed packages sorted by installation date.

3. **Check the Output**: The Excel file will be saved in the same directory as the script:
    ```plaintext
    D:\XXXXX\XXXXXX\installed_packages_with_uninstall_values.xlsx
    ```

### Example
```bash
python pip_packages_sort_by_date.py
```

### Sample Output
Here’s what your output Excel sheet will look like:

| Package Name | Version | Install Date        | Uninstall Command               |
|--------------|---------|---------------------|----------------------------------|
| numpy        | 1.21.2 | 2023-09-01 12:00:00 | pip uninstall -y numpy          |
| pandas       | 1.3.3  | 2023-08-15 09:30:00 | pip uninstall -y pandas         |
| requests     | 2.26.0 | 2023-07-10 14:45:00 | pip uninstall -y requests       |
| Flask        | 2.0.1  | 2023-06-20 10:15:00 | pip uninstall -y Flask          |

## Contributing
Contributions are welcome! If you have ideas for enhancements or bug fixes, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
