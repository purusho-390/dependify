import subprocess
import pkg_resources

def install_package(package_name):
    """
    Install a package using pip.
    """
    try:
        subprocess.check_call(["pip", "install", package_name])
        print(f"✅ Installed: {package_name}")
    except subprocess.CalledProcessError:
        print(f"❌ Failed to install: {package_name}")

def get_missing_packages(imports):
    """
    Identify packages not currently installed in the environment.
    """
    installed_packages = {pkg.key for pkg in pkg_resources.working_set}
    return [pkg for pkg in imports if pkg.lower() not in installed_packages]
