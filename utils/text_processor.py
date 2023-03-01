

class Processor:
    def compare(self, repo_name, spaced_name, split_repo=",", split_spaced=" "):
        repo_name = repo_name.lower()
        spaced_name = spaced_name.lower()
        s0List = repo_name.split(split_repo)
        s1List = spaced_name.split(split_spaced)
        return len(list(set(s0List)&set(s1List)))