#!/usr/bin/env python3
# coding=utf-8
"""
do not include the projects from the github directory for push
"""

import os
import sys

from consoleprinter import console
from consoleprinter import require_python3




g_checkout = """

# coding=utf-8
\"\"\"
recreate workspace
\"\"\"
import os

from consoleprinter import console
from git import Repo
def checkout_project(project):
    \"\"\"
    @type project: tuple
    @return: None
    \"\"\"
    projdir, giturl = project
    if not os.path.exists(os.path.join(projdir, ".git")):
        console('pulling', giturl, color='orange', fileref=False)
        os.makedirs(projdir)
        print(Repo.clone_from(giturl, projdir).active_branch, "cloned")
    else:
        print(os.path.dirname(projdir)+"/"+os.path.basename(projdir), "ok")
"""

g_drive_main = """
    for project in project_list:
        try:
            checkout_project(project)
        except:
            console("error",*project, color='red')

if __name__ == "__main__":
    main()
"""


def print_stdout(chara, cnt=0, moddiv=1):
    """
    @type chara: str
    @type cnt: int
    @type moddiv: int
    @return: None
    """
    cnt += 1

    if cnt % moddiv == 0:
        sys.stdout.write(chara)
        sys.stdout.flush()

    return cnt


def handle_new_projects(new_projects):
    if len(new_projects) > 0:
        proj_list_imports = g_checkout + "\n\n"
        proj_list_imports += "def main():\n    \"\"\"\n    main\n    \"\"\"\n"
        proj_list_header = "    project_list = ["
        numspaces = len(proj_list_header)
        proj_list = ""
        first = True
        spaces = ""

        for new_project in new_projects:
            if first:
                spaces = " " * numspaces

            project = spaces + str(new_project) + ",\n"
            project = project.replace("\", \"", "\",\n" + spaces + " \"")
            proj_list += project
            first = False

        proj_list = proj_list.strip().strip(",")
        proj_list += "]"
        proj_list_imports = proj_list_imports.replace("import Repo", "import Repo\n\n")
        proj_list_imports = proj_list_imports.replace("from git", "\nfrom git")
        g_driver = g_drive_main.replace("if __name__", "\n\nif __name__")
        output = proj_list_imports + proj_list_header + proj_list + "\n" + g_driver
        open(os.path.expanduser("~/workspace/devenv_private/current_workspace.py"), "wt").write(output.strip() + "\n")


def main():
    """
    main
    """
    require_python3()
    forks = set()
    write_file = True
    projects_set = set()
    excludes = []
    workspacefolder = os.path.join(os.path.expanduser("~"), "workspace")

    if os.path.exists(os.path.join(workspacefolder, ".gitutilsexclude")):
        excludes.extend([os.path.join(workspacefolder, x.strip()) for x in open(os.path.join(workspacefolder, ".gitutilsexclude")).read().split("\n") if x.strip()])


    wsfolders = [os.path.join(workspacefolder, folder) for folder in os.listdir(workspacefolder) if os.path.join(workspacefolder, folder) not in excludes]

    print(len(wsfolders))

    new_projects = []

    for wsfolder in wsfolders:
        for root, dirlist, files in os.walk(wsfolder):

                if root.endswith(".git"):
                    print_stdout(".")

                    if os.path.exists(root + "/config"):
                        config = open(root + "/config").read()
                        if len(config.split("url ="))==1:
                            print("\nno url found", root)
                        else:
                            config = config.split("url =")[1].split("\n")[0].strip()
                            if root.strip("/.git") not in excludes:
                                new_projects.append('("' + os.path.dirname(root) + '", "' + config + '")')

                    project_dir = root.strip("/.git/")
                    project_base_folder = os.path.basename(os.path.dirname(project_dir))
                    if project_base_folder == "forks":
                        project_name = os.path.basename(project_dir)

                        for project_name_iter in projects_set:
                            if project_name in project_name_iter:
                                forks.add(project_name_iter)

    for fork in forks:
        projects_set.remove(fork)

    if write_file:
        afile = open(os.path.expanduser("~") + "/workspace/git_utils/exclude_dirs", "wt")

        for projectname in projects_set:

            afile.write(str(projectname) + "\n")

        afile.close()
    new_projects = [project_name for project_name in new_projects if "workspace/github" not in project_name]
    new_projects2 = []
    for d in new_projects:
        if eval(d)[0] not in excludes:
            new_projects2.append(d)
    print
    new_projects=new_projects2
    print()
    console(len(new_projects), "projects", color='blue', fileref=False)

    handle_new_projects(new_projects)



if __name__ == "__main__":
    main()
