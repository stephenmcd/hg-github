
# Mimic the hggit extension.
try:
    from hggit import *
    hggit_reposetup = reposetup
except ImportError:
    # Allow this module to be imported without
    # hg-git installed, eg for setup.py
    pass


__version__ = "0.1.2"


def reposetup(ui, repo, **kwargs):
    """
    Automatically adds Bitbucket->GitHub mirror paths to the repo.
    Also creates a `master` bookmark for the `default` branch.
    """
    hggit_reposetup(ui, repo, **kwargs)
    bb = "ssh://hg@bitbucket.org/"
    for pathname, path in ui.configitems("paths"):
        if path.startswith(bb):
            user, project = path.replace(bb, "").split("/", 1)
            # Strip slash and everything after it,
            # such as mq patch queue path.
            project = project.split("/")[0]
            for k, v in ui.configitems("github"):
                if k == "username":
                    user = v
            gh_path = "git+ssh://git@github.com/%s/%s.git" % (user, project)
            if pathname == "default":
                if "master" not in repo._bookmarks:
                    from mercurial.commands import bookmark
                    bookmark(ui, repo, mark="master", rev="default")
                gh_pathname = "github"
            else:
                gh_pathname = "github-" + pathname
            ui.setconfig("paths", gh_pathname, gh_path)


