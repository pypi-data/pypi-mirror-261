from setuptools import setup, find_packages

setup(
    name='MailClassification',
    author='Ankit Mor',
    version='0.6',
    packages=find_packages(),
    description='Classify Mail to Cargo or Tonnage',
    long_description="""provide text in base64 form""",
    long_description_content_type="text/markdown",
    install_requires=[
        'requests',
        'beautifulSoup4',
        'spacy>=3.7.2',
        'torch == 2.1.2',
        'tensorflow == 2.15.0',
        'keras == 2.15.0',
        'sentence_transformers == 2.3.1',
        'joblib == 1.3.2'
    ],
)