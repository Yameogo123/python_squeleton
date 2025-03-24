from setuptools import setup, find_packages

setup(
    name="{{ cookiecutter.package_name | lower | replace(' ', '_') | replace('-', '_') }}",
    version="0.1.0",
    description="{{ cookiecutter.description }}",
    author=[
        {"name": '{{ cookiecutter.author_name }}', "email": ""},
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=['click'],
    python_requires='>=3.9',
    entry_points={
        'console_scripts': [
            'cli_main_script = {{ cookiecutter.package_name | lower | replace(" ", "_") | replace("-", "_") }}.cli_main_script:main',
        ]
    }

)