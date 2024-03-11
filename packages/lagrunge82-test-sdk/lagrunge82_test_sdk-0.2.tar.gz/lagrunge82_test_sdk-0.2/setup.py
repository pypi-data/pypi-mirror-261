from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name='lagrunge82_test_sdk',
    version='0.2',
    description='Python SDK for accessing OpenWeatherMap API',
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Lagrunge82/lagrunge82_test_sdk",
    author="Lagrunge",
    author_email="lagrunge82@gmail.com",
    packages=find_packages(),
    install_requires=[
        'annotated-types==0.6.0',
        'certifi==2024.2.2',
        'charset-normalizer==3.3.2',
        'idna==3.6',
        'pydantic==2.6.3',
        'pydantic_core==2.16.3',
        'requests==2.31.0',
        'typing_extensions==4.10.0',
        'urllib3==2.2.1',
    ],
)