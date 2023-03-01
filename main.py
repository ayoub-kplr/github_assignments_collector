import csv

from utils.github_handler import GithubHandler
from utils.text_processor import Processor
from utils.consts import TARGET


def get_org_assignments():
    filename = "Workshop_List.csv"
    with open(filename, mode='r') as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            splited_lines = lines
            processor = Processor()
            if processor.compare(TARGET, splited_lines[0]) > 0:
                return splited_lines[len(splited_lines) - 1] if len(splited_lines) == 3 else []
    return None


def unsolved_assignments(org_assignments, done_assignments):
    solved = []
    unsolved = []
    processor = Processor()
    for org_assignment in org_assignments:
        for done_assignment in done_assignments:
            if processor.compare(done_assignment, org_assignment, split_repo="_", split_spaced="_") > 0:
                solved.append(org_assignment)
            else:
                unsolved.append(org_assignment)

    return solved, unsolved


if __name__ == '__main__':
    g = GithubHandler()
    g.get_repos_users()
    assignments = get_org_assignments()
    print(assignments)

# get_repos_users()
