# coding=utf-8
"""
recreate workspace
"""
import os
from consoleprinter import console

from git import Repo


def checkout_project(project):
    """
    @type project: tuple
    @return: None
    """
    projdir, giturl = project
    if not os.path.exists(os.path.join(projdir, ".git")):
        console('pulling', giturl, color='orange', fileref=False)
        os.makedirs(projdir)
        print(Repo.clone_from(giturl, projdir).active_branch, "cloned")
    else:
        print(os.path.dirname(projdir)+"/"+os.path.basename(projdir), "ok")


def main():
    """
    main
    """
    project_list = [("/Users/rabshakeh/workspace/active8-management",
                     "ssh://faith.active8.nl/git/Active8/active8-management.git"),
                    ("/Users/rabshakeh/workspace/brainyquote",
                     "git@github.com:erikdejonge/brainyquote.git"),
                    ("/Users/rabshakeh/workspace/coreos/coreos-kubernetes-vagrant-ansible-demo",
                     "git@github.com:erikdejonge/coreos-kubernetes-vagrant-ansible-demo.git"),
                    ("/Users/rabshakeh/workspace/coreos/etcd",
                     "git@github.com:coreos/etcd.git"),
                    ("/Users/rabshakeh/workspace/coreos/flannel",
                     "git@github.com:coreos/flannel.git"),
                    ("/Users/rabshakeh/workspace/cp-pep8",
                     "git@github.com:erikdejonge/cp-pep8.git"),
                    ("/Users/rabshakeh/workspace/cryptobox/crypto_api",
                     "git@github.com:erikdejonge/crypto_api.git"),
                    ("/Users/rabshakeh/workspace/cryptobox/crypto_data",
                     "ssh://faith.active8.nl/git/cryptobox/crypto_data.git"),
                    ("/Users/rabshakeh/workspace/cryptobox/crypto_tree",
                     "faith.active8.nl:/git/cryptobox/crypto_tree.git"),
                    ("/Users/rabshakeh/workspace/cryptobox/cryptobox_app",
                     "git@github.com:erikdejonge/cryptobox_app.git"),
                    ("/Users/rabshakeh/workspace/cryptobox/cryptobox_containers",
                     "git@github.com:erikdejonge/cryptobox_containers.git"),
                    ("/Users/rabshakeh/workspace/cryptobox/cryptobox_deploy",
                     "ssh://faith.active8.nl/git/cryptobox/cryptobox_deploy.git"),
                    ("/Users/rabshakeh/workspace/cryptobox/cryptobox_design",
                     "git@github.com:Active8-BV/cryptobox_design.git"),
                    ("/Users/rabshakeh/workspace/cryptobox/cryptobox_provisioning",
                     "git@github.com:Active8-BV/cryptobox_provisioning.git"),
                    ("/Users/rabshakeh/workspace/cryptobox/cryptobox_test",
                     "git@github.com:erikdejonge/cryptobox_test.git"),
                    ("/Users/rabshakeh/workspace/cryptobox/cryptobox_webapp",
                     "ssh://faith.active8.nl/git/cryptobox/cryptobox_webapp.git"),
                    ("/Users/rabshakeh/workspace/cryptobox/cryptobox_website",
                     "git@github.com:Active8-BV/cryptobox_website.git"),
                    ("/Users/rabshakeh/workspace/cryptobox/cryptoboxcli",
                     "git@github.com:Active8-BV/cryptoboxcli.git"),
                    ("/Users/rabshakeh/workspace/cryptobox/docs",
                     "ssh://faith.active8.nl/git/cryptobox/docs.git"),
                    ("/Users/rabshakeh/workspace/cryptobox/mailer",
                     "git@github.com:erikdejonge/mailer.git"),
                    ("/Users/rabshakeh/workspace/cryptobox/sms",
                     "ssh://faith.active8.nl/git/sms.git"),
                    ("/Users/rabshakeh/workspace/cryptobox/www_cryptobox_nl",
                     "faith.active8.nl:/git/cryptobox/www_cryptobox_nl.git"),
                    ("/Users/rabshakeh/workspace/de_jonge_vakkleding",
                     "ssh://faith.active8.nl/git/de_jonge_vakkleding.git"),
                    ("/Users/rabshakeh/workspace/devenv",
                     "git@github.com:erikdejonge/devenv.git"),
                    ("/Users/rabshakeh/workspace/documentation",
                     "git@github.com:Active8-BV/documentation.git"),
                    ("/Users/rabshakeh/workspace/forks/business-rules",
                     "git@github.com:erikdejonge/business-rules.git"),
                    ("/Users/rabshakeh/workspace/forks/business-rules-ui",
                     "git@github.com:erikdejonge/business-rules-ui.git"),
                    ("/Users/rabshakeh/workspace/forks/CoreGI",
                     "git@github.com:erikdejonge/CoreGI.git"),
                    ("/Users/rabshakeh/workspace/forks/django-htmlmin",
                     "git@github.com:erikdejonge/django-htmlmin.git"),
                    ("/Users/rabshakeh/workspace/forks/docker-library",
                     "git@github.com:erikdejonge/docker-library.git"),
                    ("/Users/rabshakeh/workspace/forks/kube-register",
                     "git@github.com:erikdejonge/kube-register.git"),
                    ("/Users/rabshakeh/workspace/forks/macdown",
                     "git@github.com:erikdejonge/macdown.git"),
                    ("/Users/rabshakeh/workspace/forks/puffin",
                     "git@github.com:erikdejonge/puffin.git"),
                    ("/Users/rabshakeh/workspace/forks/python-kubernetes",
                     "git@github.com:erikdejonge/python-kubernetes.git"),
                    ("/Users/rabshakeh/workspace/forks/schema",
                     "git@github.com:erikdejonge/schema.git"),
                    ("/Users/rabshakeh/workspace/forks/signature_pad",
                     "git@github.com:erikdejonge/signature_pad.git"),
                    ("/Users/rabshakeh/workspace/forks/youtube-dl",
                     "git@github.com:erikdejonge/youtube-dl.git"),
                    ("/Users/rabshakeh/workspace/ghresearch",
                     "git@github.com:erikdejonge/ghresearch.git"),
                    ("/Users/rabshakeh/workspace/git_utils",
                     "git@github.com:erikdejonge/git_utils.git"),
                    ("/Users/rabshakeh/workspace/github-stars-syncer",
                     "git@github.com:erikdejonge/github-stars-syncer.git"),
                    ("/Users/rabshakeh/workspace/microservicebase",
                     "git@github.com:erikdejonge/microservicebase.git"),
                    ("/Users/rabshakeh/workspace/newsrivr",
                     "git@github.com:erikdejonge/newsrivr.git"),
                    ("/Users/rabshakeh/workspace/odooserver",
                     "ssh://faith.active8.nl:/git/DJV/odooserver.git"),
                    ("/Users/rabshakeh/workspace/pip/appinstance",
                     "git@github.com:erikdejonge/appinstance.git"),
                    ("/Users/rabshakeh/workspace/pip/arguments",
                     "git@github.com:erikdejonge/arguments.git"),
                    ("/Users/rabshakeh/workspace/pip/cmdssh",
                     "git@github.com:erikdejonge/cmdssh.git"),
                    ("/Users/rabshakeh/workspace/pip/consoleprinter",
                     "git@github.com:erikdejonge/consoleprinter.git"),
                    ("/Users/rabshakeh/workspace/pip/historybash",
                     "git@github.com:erikdejonge/historybash.git"),
                    ("/Users/rabshakeh/workspace/pip/httpdebug",
                     "git@github.com:erikdejonge/httpdebug.git"),
                    ("/Users/rabshakeh/workspace/pip/openmacapp",
                     "git@github.com:erikdejonge/openmacapp.git"),
                    ("/Users/rabshakeh/workspace/pip/pycodequality",
                     "git@github.com:erikdejonge/pycodequality.git"),
                    ("/Users/rabshakeh/workspace/pip/pyprofiler",
                     "git@github.com:erikdejonge/pyprofiler.git"),
                    ("/Users/rabshakeh/workspace/pip/reposmon",
                     "git@github.com:erikdejonge/reposmon.git"),
                    ("/Users/rabshakeh/workspace/pip/sortpythonmethods",
                     "git@github.com:erikdejonge/sortpythonmethods.git"),
                    ("/Users/rabshakeh/workspace/pip/unittester",
                     "git@github.com:erikdejonge/unittester.git"),
                    ("/Users/rabshakeh/workspace/pip/vckube",
                     "git@github.com:erikdejonge/vckube.git"),
                    ("/Users/rabshakeh/workspace/printer_osx_pdf",
                     "git@github.com:erikdejonge/printer_osx_pdf.git"),
                    ("/Users/rabshakeh/workspace/research",
                     "git@github.com:erikdejonge/research.git"),
                    ("/Users/rabshakeh/workspace/scanners/arachni",
                     "git@github.com:Arachni/arachni.git"),
                    ("/Users/rabshakeh/workspace/scanners/w3af",
                     "https://github.com/andresriancho/w3af.git"),
                    ("/Users/rabshakeh/workspace/servefolder",
                     "git@github.com:erikdejonge/servefolder.git"),
                    ("/Users/rabshakeh/workspace/sort_photo",
                     "git@github.com:erikdejonge/sort_photo.git"),
                    ("/Users/rabshakeh/workspace/tarsnap/kivaloo",
                     "git@github.com:erikdejonge/kivaloo.git"),
                    ("/Users/rabshakeh/workspace/tarsnap/scrypt",
                     "git@github.com:erikdejonge/scrypt.git"),
                    ("/Users/rabshakeh/workspace/tarsnap/spiped",
                     "git@github.com:erikdejonge/spiped.git"),
                    ("/Users/rabshakeh/workspace/tarsnap/tarsnap",
                     "git@github.com:erikdejonge/tarsnap.git"),
                    ("/Users/rabshakeh/workspace/uren_active8_nl",
                     "rabshakeh@faith.active8.nl:/git/Active8/uren_active8_nl"),
                    ("/Users/rabshakeh/workspace/vckube-createproject",
                     "git@github.com:erikdejonge/vckube-createproject"),
                    ("/Users/rabshakeh/workspace/www_amsterdamenco_nl",
                     "ssh://faith.active8.nl/git/RabobankAmsterdam/www_amsterdamenco_nl.git"),
                    ("/Users/rabshakeh/workspace/www_dinnerdinsdag_nl",
                     "rabshakeh@faith.active8.nl:/git/RabobankRotterdam/www_dinnerdinsdag_nl.git")]

    for project in project_list:
        checkout_project(project)


if __name__ == "__main__":
    main()
