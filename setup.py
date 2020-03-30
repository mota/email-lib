from setuptools import setup, find_packages

def get_requirements():
    try:
        with open('./requirements.txt') as handle:
            return handle.readlines()
    except:
        pass

def readme_content():
    with open('README.md') as handle:
        return handle.read()

setup(
    name="email-lib",
    version="0.1.0",
    author="Pierre Wacrenier",
    author_email="pierre@wacrenier.me",
    description="Simplify email organization",
    long_description=readme_content(),
    url="https://github.com/mota/email-lib",
    install_requires=get_requirements(),
    packages=find_packages(),

    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)