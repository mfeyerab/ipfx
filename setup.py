from setuptools import setup, find_packages

setup(
    name = 'aibs_ipfx',
    version = '0.1.0',
    description = """intrinsic physiology feature extractor""",
    author = "David Feng",
    author_email = "davidf@alleninstitute.org",
    url = 'https://github.com/AllenInstitute/aibs.ipfx',
    packages = find_packages(),
    include_package_data=True,
    entry_points={
          'console_scripts': [
              'aibs.ipfx = aibs.ipfx.__main__:main'
        ]
    },
    setup_requires=['pytest-runner'],
)
