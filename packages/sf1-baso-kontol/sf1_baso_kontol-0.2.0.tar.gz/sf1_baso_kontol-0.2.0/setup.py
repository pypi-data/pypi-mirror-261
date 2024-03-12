import pathlib
import setuptools


setuptools.setup(
        name="sf1_baso_kontol",
        version="0.2.0",
        description="pypi test",
        long_description=pathlib.Path("README.md").read_text(),
        long_description_content_type="text/markdown",
        url="https://github.com/IrfanDect/baso_kontol_cli",
        author="IrfanDect",
        author_email="jancok@gmail.com",
        license="MIT",
        install_requires=["rich","requests","prompt-toolkit","baso_kontol"],
        extras_require={
            "excel": ["openpyxl"],
            },
        packages=setuptools.find_packages(),
        include_package_data=True,
        classifiers=[
        'Intended Audience :: Developers', 'Topic :: Utilities',
        'License :: Public Domain', 'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
        ],
        keywords="super_baso_kontol",
        entry_points={"console_script": ["sf1_baso_kontol = sf1_baso_kontol.cli:main"]}
        )
