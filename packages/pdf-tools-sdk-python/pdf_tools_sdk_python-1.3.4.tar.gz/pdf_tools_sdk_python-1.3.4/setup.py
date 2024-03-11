from setuptools import setup, find_packages
import platform
import os

# Function to determine the correct subfolder based on platform and architecture
def get_lib_subfolder():
    sys = platform.system().lower()  # Use 'sys' to avoid confusion with 'system()' function
    arch = platform.machine().lower()

    # Map common architecture names to expected folder names
    arch_map = {
        'amd64': 'x64',
        'x86_64': 'x64',
        'arm64': 'arm64',
        'aarch64': 'arm64',
        'x86': 'x86',
        'i386': 'x86',
        'i686': 'x86'
    }
    arch_folder = arch_map.get(arch, '')

    if sys == 'windows':
        return f'win-{arch_folder}'
    elif sys == 'linux':
        return f'linux-{arch_folder}'
    elif sys == 'darwin':
        return f'osx-{arch_folder}'
    else:
        raise ValueError(f'Unsupported system/architecture: {sys}/{arch}')

# Get the correct subfolder for the current system/architecture
lib_subfolder = get_lib_subfolder()

# Define the path to include the correct libraries based on the current platform
if platform.system().lower() == 'windows':
    lib_path = f'lib/{lib_subfolder}/*.dll'
elif platform.system().lower() == 'darwin':
    lib_path = f'lib/{lib_subfolder}/*.dylib'
else:  # Assume Linux or other Unix-like OS by default
    lib_path = f'lib/{lib_subfolder}/*.so'

setup(
    name='pdf_tools_sdk_python',
    version='1.3.4',
    packages=find_packages(),
    description='Python package for Pdftools SDK',
    package_data={
        'pdf_tools_sdk_python': ['include/*.h', lib_path],
    },
    include_package_data=True,
    zip_safe=False,
)
