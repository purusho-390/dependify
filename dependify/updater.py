def update_requirements(missing_packages, requirements_file="requirements.txt"):
    """
    Add missing packages to the requirements.txt file.
    """
    with open(requirements_file, "a") as f:
        for package in missing_packages:
            f.write(f"{package}\n")
    print("✅ Updated requirements.txt with missing packages.")
