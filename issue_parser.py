from github import Github

class GithubIssueParser:
    def __init__(self, access_token : str, repo : str = "RIOT-OS/RIOT"):
        """
        Initializes an instance of a Github Issue Parser

        Parameters
        ----------
        access_token : str
            Github access token, must be created manually
        repo : str
            Github repository that should be accessed, syntax: "<owner>/<repo>"
        """
        print(f'Initializing Github Issue Parser for repository {repo}')
        self._g = Github(access_token)
        self._repo = self._g.get_repo(repo)

    def _get_issues_and_remove_prs(self):
        issues = self._repo.get_issues(state='open')
        issues = [i for i in issues if i.pull_request == None]
        return issues

    def _count_issue_engagement(self, issues):
        ignored_users = ["riot-ci"]
        issue_engagement = 0
        if issues.comments > 0:
            comments = issues.get_comments()
            for comment in comments:
                if comment.user.login not in ignored_users:
                    issue_engagement += 1
        return issue_engagement

    def _issues_get_labels(self, issues):
        important_labels = [
            "Area: security",
            "Type: bug",
            "Type: new feature",
            "Type: enhancement"]

        area = ""
        issue_type = ""
        for label in issues.labels:
            if label.name in important_labels:
                if label.name == "Area: security":
                    area = "security"
                else:
                    types = label.name.split(" ")[1:]
                    types = ' '.join(types)
                    issue_type = types
        return area, issue_type

    def get_issues(self):
        """
        Returns a list of Github issues.
        Issue structure:
            {
                "ticket": {
                    "ticket-id": int,
                    "area": str,
                    "issue-type": str,
                    "engagement": int,
                    "date": str
                    }
            }
        """
        issue_list = []
        issues = self._get_issues_and_remove_prs()

        for issue in issues:
            tmp = {
                "ticket": {
                    "ticket-id": 0,
                    "area": "",
                    "issue-type": "",
                    "engagement": 0,
                    "date": ""
                }
            }
            tmp["ticket"]["ticket-id"] = issue.id
            tmp["ticket"]["engagement"] = self._count_issue_engagement(issue)

            area, issue_type = self._issues_get_labels(issue)
            tmp["ticket"]["area"] = area
            tmp["ticket"]["issue_type"] = issue_type

            tmp["ticket"]["date"] = issue.created_at.strftime("%x").replace("/", "-")
            issue_list.append(tmp)
        return issue_list
