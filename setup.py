import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='math_quiz',
    version='1.0.0',
    author='Yatin Arora',
    author_email='yatin.arora@fau.de',
    description='A math quiz game for data science survival skills assignment 2',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/yatindma/dsss-2nd-assignment.git',
    packages=setuptools.find_packages(),
    python_requires='>=3.7',
    install_requires=[],
)