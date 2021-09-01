from github import Github, UnknownObjectException
from github.GithubException import GithubException
from .helpers import read_file
from os import listdir

def auth():
    token = input("Paste your GitHub api key: ")
    g = Github(token)
    user = g.get_user()
    return user


def upload_files(user, folder, file_name, content):
    try:
        repo = user.get_repo("URI-Source-Codes")
    except UnknownObjectException:
        repo = user.create_repo("URI-Source-Codes")

    try:
        repo.create_file(folder + '/' + file_name, "new source code", str(content))
    except GithubException:
        pass


def github():
    user = auth()

    base_folder = 'URI-Source-Codes/'
    language_folders = listdir(base_folder)
    for lang_folder in language_folders:
        source_files = listdir(base_folder + lang_folder)
        for source_file in source_files:
            content = read_file(base_folder+lang_folder+'/'+source_file)
            upload_files(user, lang_folder, source_file, content)
