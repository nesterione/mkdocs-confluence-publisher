from setuptools import setup, find_packages

setup(
    name='mkdocs-confluence-publisher',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'mkdocs>=1.0',
        'atlassian-python-api>=3.14.0',
    ],
    entry_points={
        'mkdocs.plugins': [
            'confluence-publisher = mkdocs_confluence_publisher:ConfluencePublisherPlugin',
        ]
    },
    # Add more metadata as needed
    author='Your Name',
    author_email='your.email@example.com',
    description='A MkDocs plugin to publish documentation to Confluence',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/mkdocs-confluence-publisher',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
