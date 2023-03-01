import csv

from github import Github
import time
from .consts import TARGET, ORG, TOKEN


class GithubHandler:
    def __init__(self):
        self.g = Github(TOKEN)
        self.user = self.g.get_organization(ORG)

    def get_repos_users(self):
        repos = self.user.get_repos()

        f = open("{}-{}.csv".format(TARGET, time.strftime("%Y%m%d-%H%M%S")), 'w', newline='')
        writer = csv.writer(f)
        writer.writerow([TARGET])
        for repo in repos:
            if TARGET in repo.name:
                writer.writerow([repo.name.split("{}-".format(TARGET))[1]])
                writer.writerow(self.get_repo_files(repo))

        f.close()

    def get_repo_files(self, repo):
        contents = repo.get_contents("/")
        names = []
        while len(contents) > 1:
            file_content = contents.pop(0)
            if file_content.type == "dir":
                contents.extend(repo.get_contents(file_content.path))
            elif file_content.type == "file" and file_content.name.endswith("ipynb"):
                names.append(file_content.name)

        return names
