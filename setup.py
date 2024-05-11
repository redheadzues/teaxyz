from setuptools import setup

setup(
    author='User',
    author_email='example@mail.com',
    name='sNupY',
    version='0.0.1',
    url='https://github.com/redheadzues/teaxyz',
    project_urls={
        'Homepage': 'https://github.com/redheadzues/teaxyz',
        'Source': 'https://github.com/redheadzues/teaxyz',
    },
    py_modules=['hi_tea'],
    entry_points={
        'console_scripts': [
            'hi-tea=hi_tea:hello_tea_xyz'
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
)
