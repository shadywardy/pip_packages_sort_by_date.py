import os
from datetime import datetime
from importlib.metadata import distributions
import glob
import pandas as pd
from openpyxl import Workbook

def get_installation_date(package_path):
    """Return the creation/modification date of the .dist-info folder."""
    if os.path.exists(package_path):
        return datetime.fromtimestamp(os.path.getctime(package_path))
    return None

def list_packages_sorted_by_installation_date():
    packages = []
    
    # Use the provided 'site-packages' directory
    #site_packages_dir = r'D:\XXXXX\XXXXX\venv\Lib\site-packages'
    
    site_packages_dir = r'YOUR_PACKAGE_PATH'

  
        
    for dist in distributions():
        package_name = dist.metadata['Name']
        package_version = dist.version
        
        # Search for the .dist-info folder using glob
        dist_info_pattern = os.path.join(site_packages_dir, f"{package_name.replace('-', '_')}*.dist-info")
        dist_info_dirs = glob.glob(dist_info_pattern)
        
        if not dist_info_dirs:
            print(f"Missing package path: {dist_info_pattern}")
            continue
        
        dist_info_dir = dist_info_dirs[0]  # Pick the first match
        
        install_date = get_installation_date(dist_info_dir)
        
        if install_date:
            packages.append({
                'Package Name': package_name,
                'Version': package_version,
                'Install Date': install_date,
                'Uninstall Command': f"pip uninstall -y {package_name}"
            })
    
    # Sort packages by installation date
    sorted_packages = sorted(packages, key=lambda x: x['Install Date'], reverse=True)
    
    # Create a pandas DataFrame
    df = pd.DataFrame(sorted_packages)
    
    # Write the DataFrame to an Excel file with uninstall commands directly
    
    script_dir = os.path.dirname(os.path.abspath(__file__))

    final_output_file = os.path.join(script_dir, "installed_packages_with_uninstall_values.xlsx")

        # Create a pandas DataFrame
    df = pd.DataFrame(sorted_packages)


    df.to_excel(final_output_file, index=False)
    
    print(f"\nFinal data with uninstall commands exported to: {final_output_file}")

list_packages_sorted_by_installation_date()
