from setuptools import setup, find_packages

setup(
    name='ip-check',
    version='1.0',
    description='Powerful cdn network speed test utils.',
    author="nobitaqaq",
    author_email="xiaoleigs@gmail.com",
    keywords=["cdn", "speed test", "network speed"],
    packages=find_packages(include=['ipcheck', 'ipcheck.app', 'ipcheck.app.*']),
    entry_points={
        'console_scripts': [
            'ip-check = ipcheck.main:main'
        ]
    },
    python_requires=">=3.8",
    install_requires=[
        'ipaddress',
        'tcppinglib',
        'urllib3',
        'zipp',
    ],
)
