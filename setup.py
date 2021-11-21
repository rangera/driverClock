from setuptools import find_packages, setup

setup(
    name='compliance_clock',
    version='1.0.0',
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
    package_dir={"": "compliance_clock"},
    packages=find_packages(where="compliance_clock"),
    python_requires=">=3.8",
)