import argparse
import os
from dependify.parser import find_all_imports
from dependify.installer import get_missing_packages, install_package
from dependify.updater import update_requirements
from dependify.utils import print_header

def main():
    # Command-line interface
    parser = argparse.ArgumentParser(description="Dependify: Auto-manage Python dependencies.")
    parser.add_argument("--path", type=str, default=".", help="Path to the project directory")
    parser.add_argument("--update", action="store_true", help="Update requirements.txt with missing packages")
    args = parser.parse_args()

    # Parse imports from the project
    print_header("Analyzing Project for Missing Dependencies")
    imports = find_all_imports(args.path)
    print(f"📦 Found Imports: {', '.join(imports)}")

    # Identify missing packages
    print_header("Checking for Missing Dependencies")
    missing_packages = get_missing_packages(imports)
    if missing_packages:
        print(f"❌ Missing Packages: {', '.join(missing_packages)}")
        
        # Install missing packages
        for package in missing_packages:
            install_package(package)
        
        # Update requirements.txt if specified
        if args.update:
            update_requirements(missing_packages)
    else:
        print("🎉 No missing packages found. You're all set!")

if __name__ == "__main__":
    main()
