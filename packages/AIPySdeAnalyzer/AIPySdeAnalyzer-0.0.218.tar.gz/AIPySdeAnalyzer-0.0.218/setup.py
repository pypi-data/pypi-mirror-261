from setuptools import setup, find_packages,find_namespace_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="AIPySdeAnalyzer",
    version="0.0.218",
    install_requires=required,
    packages=find_namespace_packages(where='aipysanalyzer'),
    package_dir={'': 'aipysanalyzer'},
    entry_points={
        'console_scripts': [
        'updateParameters=aipysanalyzer.CLI.setParameters:update_user_parameters',
        'load-parameters=aipysanalyzer.CLI.loadParametres:main', 
            ],
    },
    author="Gil Kanfer",
    author_email="gil.kanfer.il@gmail.com",
    description="AI Powered Photoswitchable Screen analysis",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="",  # Consider adding a URL if you have a project page or source repository
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',  # Specify the minimum version of Python required
)