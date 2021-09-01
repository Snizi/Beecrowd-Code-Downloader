from github import Github, UnknownObjectException
from github.GithubException import GithubException
from .helpers import read_file
from os import listdir
from .constants import BASE_FOLDER


def auth():
    token = input("Enter your GitHub api key: ")
    g = Github(token)
    user = g.get_user()
    return user


def upload_files(user, folder, file_name, content):
    try:
        repo = user.get_repo("URI-Source-Codes")
    except UnknownObjectException:
        repo = user.create_repo("URI-Source-Codes")

    try:
        repo.create_file(
            folder + '/' + file_name,
            "new source code",
            str(content))
    except GithubException:
        pass


def github():
    user = auth()

    src_folder = BASE_FOLDER
    language_folders = listdir(src_folder)
    for lang_folder in language_folders:
        source_files = listdir(src_folder + lang_folder)
        for source_file in source_files:
            content = read_file(src_folder + lang_folder + '/' + source_file)
            upload_files(user, lang_folder, source_file, content)
