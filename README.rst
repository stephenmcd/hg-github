hg-github
=========

hg-github is a `Mercurial`_ extension that wraps `hg-git`_, and
supports a work-flow where repositories are hosted on `Bitbucket`_
and mirrored on `GitHub`_. This work-flow normally requires adding
Git paths to each repository's config file, and creating Mercurial
bookmarks pointing to the GitHub repository's branch name. hg-github
takes care of these for you automatically. hg-github is
`BSD licensed`_.

Installation
============

The easiest way to install hg-github is directly from `PyPi`_ using
`pip`_ or `setuptools`_ by running the respective command below::

    $ pip install -U hg-github

or::

    $ easy_install -U hg-github

Otherwise you can download hg-github and install it directly
from source::

    $ python setup.py install

Once installed, add ``hggithub`` to the extensions section in your
global ``.hgrc`` file::

    [extensions]
    hggithub =

Note that there isn't a dash in ``hggithub`` in your ``.hgrc`` file.
You also don't need to add the hg-git extension, as it is
wrapped and used automatically by hg-github.

Once installed, assuming the default remote location of your
repository is on Bitbucket, the GitHub path is automatically added and
given the name ``github``, so you can push to it with the following
command::

    $ hg push github

Repository Paths
================

As mentioned above, the GitHub path is given the name ``github`` when
the default remote location is on Bitbucket. For other named Bitbucket
locations, the name ``github-NAME`` is given, where ``NAME`` is the
name of the path located on BitBucket. For example consider the
following ``.hg/hgrc`` repo config::

    [paths]
    default = ssh://hg@bitbucket.org/stephenmcd/hg-git
    somefork = ssh://hg@bitbucket.org/stephenmcd/hg-git-temp

hg-git will add entries to the config file as follows. Note that the
config file isn't actually written to::

    [paths]
    default = ssh://hg@bitbucket.org/stephenmcd/hg-github
    somefork = ssh://hg@bitbucket.org/stephenmcd/hg-github-temp

    github = git+ssh://git@github.com/stephenmcd/hg-github.git
    github-somefork = git+ssh://git@github.com/stephenmcd/hg-github-temp.git

GitHub Username
===============

hg-github assumes you have the same username on GitHub and Bitbucket.
If you have a different GitHub username, you can specify it by adding
the following section to your global ``.hgrc`` file. For example my
GitHub username is ``stephenmcd``::

    [github]
    username = stephenmcd

.. _`Mercurial`: http://mercurial.selenic.com/
.. _`hg-git`: http://hg-git.github.com/
.. _`GitHub`: https://github.com/
.. _`Bitbucket`: https://bitbucket.org/
.. _`BSD licensed`: http://www.linfo.org/bsdlicense.html
.. _`PyPI`: http://pypi.python.org/
.. _`pip`: http://www.pip-installer.org/
.. _`setuptools`: http://pypi.python.org/pypi/setuptools

