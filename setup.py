
from setuptools import setup


setup(
    name = "hg-github",
    version = __import__("hggithub").__version__,
    author = "Stephen McDonald",
    author_email = "steve@jupo.org",
    description = "A Mercurial extension for working with GitHub repositories",
    long_description = open("README.rst").read(),
    url = "http://github.com/stephenmcd/hg-github",
    py_modules=["hggithub",],
    install_requires=["hg-git", "sphinx-me"],
    zip_safe = False,
    license="BSD",
    classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Topic :: Software Development :: Version Control",
    ]
)
