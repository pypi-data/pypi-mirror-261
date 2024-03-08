from setuptools import setup, find_packages

setup(
    name="gmail-api-auth",
    version="0.1.0",
    author="SokinjoNS",
    author_email="sokinjo.155@gmail.com",
    description="A module for authenticating Gmail API access.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  # Specify the format of the long_description
    url="https://github.com/SokinjoNS/gmail-api-auth",
    packages=find_packages(),
    install_requires=[
        'google-auth',
        'google-auth-oauthlib',
        'google-auth-httplib2',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)
