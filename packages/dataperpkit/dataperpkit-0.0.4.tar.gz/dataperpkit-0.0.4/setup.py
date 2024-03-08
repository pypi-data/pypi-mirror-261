from setuptools import setup, find_packages

setup(
    name="dataperpkit",
    version="0.0.4",
    author='Ahmed Eldesoky',
    author_email='ahmedeldesoky284@email.com',
    url="https://github.com/ahmed-eldesoky284/dataperpkit",
    description="An application that informs you of the time in different locations and timezones",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["numpy", "pandas"],
    entry_points={"console_scripts": ["DataPrepKit = src.main:main"]},
)