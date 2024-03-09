from io import open

from setuptools import find_packages, setup

setup(
    name="bert_score_flex_plot_example",
    version="0.3.15",
    author="Fork author: Alon Mannor. Origianl authors: Tianyi Zhang*, Varsha Kishore*, Felix Wu*, Kilian Q. Weinberger, and Yoav Artzi",
    author_email="alon.mannor@gmail.com (fork author),  tzhang@asapp.com (original author)",
    description="An unofficial fork of PyTorch implementation of BERT score",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords="BERT NLP deep learning google metric",
    license="MIT",
    url="https://github.com/Amannor/bert_score/tree/flex_plot_example",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=[
        "torch>=1.0.0",
        "pandas>=1.0.1",
        "transformers>=3.0.0",
        "numpy",
        "requests",
        "tqdm>=4.31.1",
        "matplotlib",
        "packaging>=20.9",
    ],
    entry_points={
        "console_scripts": [
            "bert-score=bert_score_cli.score:main",
            "bert-score-show=bert_score_cli.visualize:main",
        ]
    },
    include_package_data=True,
    python_requires=">=3.6",
    tests_require=["pytest"],
    classifiers=[
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
