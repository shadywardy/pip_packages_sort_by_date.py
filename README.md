# pip_packages_sort_by_date.py

Welcome to **pip_packages_sort_by_date.py**! 🌟 This Python script helps you list all installed Python packages in your virtual environment, sorted by their installation date. It provides an easy way to keep track of when packages were installed, along with uninstall commands for your convenience.

## Features
- **Sorts packages** by their installation date in descending order.
- **Exports** the results to an Excel file, including uninstall commands.
- User-friendly and easy to customize!

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
    #site_packages_dir = r'D:\XXXXX\XXXXX\venv\Lib\site-packages'
    
    site_packages_dir = r'YOUR_PACKAGE_PATH'


2. **Run the Script**: Execute the script in your Python environment. This will generate an Excel file with all the installed packages sorted by installation date.

3. **Check the Output**: The Excel file will be saved at same of script path:
    ```plaintext
    D:\Django Training\MailFlow\installed_packages_with_uninstall_values.xlsx
    ```

### Example
```bash
python pip_packages_sort_by_date.py
```

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request if you have ideas for enhancements or bug fixes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

