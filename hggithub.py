
# Mimic the hggit extension.
try:
    from hggit import *
    hggit_reposetup = repo_setup
except ImportError:
    # Allow this module to be imported without
    # hg-git installed, eg for setup.py
    pass


__version__ = "0.1.0"


def reposetup(ui, repo, **kwargs):
    """
    Automatically adds Bitbucket->GitHub mirror paths to the repo.
    Also creates a `master` bookmark for the `default` branch.
    """
    hggit_reposetup(ui, repo, **kwargs)
    bb = "ssh://hg@bitbucket.org/"
    gh = "git+ssh://git@github.com/"
    for name, path in ui.configitems("paths"):
        if path.startswith(bb):
            git_path = path.replace(bb, gh).rstrip("/") + ".git"
            if name == "default":
                ui.setconfig("paths", "github", git_path)
                if "master" not in repo._bookmarks:
                    from mercurial.commands import bookmark
                    bookmark(ui, repo, mark="master", rev="default")
            else:
                ui.setconfig("paths", "github-" + name, git_path)
