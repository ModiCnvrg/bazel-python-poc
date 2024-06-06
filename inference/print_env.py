import os
import sys
import pkg_resources

def print_environment_details():
    print("Current working directory:", os.getcwd())
    print("Executable path:", sys.executable)
    print("Python version:", sys.version)
    print("Runfiles directory:", os.environ.get('RUNFILES_DIR', 'Not set'))
    print("PATH:", os.environ.get('PATH', 'Not set'))
    print("LD_LIBRARY_PATH:", os.environ.get('LD_LIBRARY_PATH', 'Not set'))
    print("PYTHONPATH:", os.environ.get('PYTHONPATH', 'Not set'))






def print_installed_packages():
    print("\nInstalled Python packages:")
    installed_packages = pkg_resources.working_set
    for package in installed_packages:
        print(f"{package.project_name} ({package.version})")

def find_files_with_prefix(prefix):
    result = []
    for root, dirs, files in os.walk("/"):
        for file in files:
            if file.startswith(prefix):
                result.append(os.path.join(root, file))
    return result

def print_cuda_locations():
    cuda_prefix = 'numpy.core._multiarray_umath'
    cuda_locations = find_files_with_prefix(cuda_prefix)
    if cuda_locations:
        print(f"CUDA runtime libraries ({cuda_prefix}*):")
        for location in cuda_locations:
            print(f" - {location}")
    else:
        print(f"No CUDA runtime libraries starting with {cuda_prefix} found")

if __name__ == "__main__":
    print_environment_details()
    print_installed_packages()
    print_cuda_locations()
