import importlib
import subprocess
import sys

def ensure_package(package_name):
    try:
        importlib.import_module(package_name)
    except ImportError:
        print(f"Installing {package_name}...", end=' ', flush=True)
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name, "--quiet"])
        print("Done")
    else:
        print("Package already installed")

# Example usage:
# ensure_package("requests")
