from github import Github
from flask import send_file
from config import get_github_access_token

REPO_NAME = 'heroku-files'


github = Github("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")


def get_repos():
    for repo in github.get_user().get_repos():
        print(repo.name)


def get_file(filename):
    repository = github.get_user().get_repo(REPO_NAME)
    file = repository.get_contents(filename)

    print("HEHEHEHEHEH")
    print(file.download_url)

    return send_file("https://raw.githubusercontent.com/delbfinych/heroku-files/master/1.png")


def check_file_exist(filename):
    print(filename)
    try:
        file = get_file(filename)
    except:
        return False

    return True


def put_file(filename, content):

    repository = github.get_user().get_repo(REPO_NAME)

    if check_file_exist(filename):
        print(f'update_file {filename}')
        f = get_file(filename)
        f = repository.update_file(filename, "update_file via PyGithub", content, f.sha)
    else:
        print(f'create_file {filename}')
        f = repository.create_file(filename, "create_file via PyGithub", content)