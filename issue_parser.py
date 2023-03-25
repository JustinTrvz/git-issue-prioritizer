from github import Github
import array
import json
from tqdm import tqdm


class GithubIssueParser:
    """
    GithubIssueParser downloads issues of a specified repository
    from Github and extracts the information that is relevant to the
    sorting script.
    """
    def __init__(self, access_token: str, ignored_users: array, repo: str = "RIOT-OS/RIOT"):
        """
        Initializes an instance of a Github Issue Parser

        Parameters
        ----------
        access_token : str
            Github access token, must be created manually
        repo : str
            Github repository that should be accessed, syntax: "<owner>/<repo>"
        ignored_users : array
            Array contains users to be ignored (e.g. bots)
        """
        self._ignored_users = ignored_users
        print(f'Initializing Github Issue Parser for repository {repo}')
        self._g = Github(access_token)
        self._repo = self._g.get_repo(repo)

    def _get_issues_and_remove_prs(self):
        """
        Gets issues from repository and filters out all pull
        requests, so we only have actual issues left.
        """
        issues = self._repo.get_issues(state='open')
        print('Looking for open issues...')
        issues = [issue for issue in tqdm(issues) if issue.pull_request is None]
        print(f'Found {len(issues)} open issues')
        return issues

    def _count_issue_engagement(self, issue):
        """
        Count number of individual people who have
        engaged in the comment section of an issue.

        Parameters
        ----------
        issue : github.Issue.Issue
        """
        issue_engagement = 0
        if issue.comments > 0:
            comments = issue.get_comments()
            for comment in comments:
                if comment.user.login not in self._ignored_users:
                    issue_engagement += 1
        return issue_engagement

    def _issues_get_labels(self, issue):
        """
        Get relevant labels from an issue

        Parameters
        ----------
        issue : github.Issue.Issue
        """
        important_labels = [
            "Area: security",
            "Type: bug",
            "Type: new feature",
            "Type: enhancement"]

        area = ""
        issue_type = ""
        for label in issue.labels:
            if label.name in important_labels:
                if label.name == "Area: security":
                    area = "security"
                else:
                    types = label.name.split(" ")[1:]
                    types = ' '.join(types)
                    issue_type = types
        return area, issue_type

    def _issues_to_json(self, issue_list):
        """
        Creates json object of issue list

        :param
            issue_list: listed issues
        :return
            issue_json: isses as json format
        """
        issue_dict = {"tickets": []}
        for issue in issue_list:
            issue_dict["tickets"].append(issue)
        issue_json = json.dumps(issue_dict, indent=4)
        return issue_json

    def get_issues(self):
        """
        Returns a list of Github issues.
        Issue structure:
            {
                "ticket": {
                    "ticket_id": int,
                    "area": str,
                    "issue_type": str,
                    "engagement": int,
                    "date": str
                    }
            }
        """
        issue_list = []
        issues = self._get_issues_and_remove_prs()

        print("Converting issues into custom format...")
        for issue in tqdm(issues):
            tmp = {
                "ticket": {
                    "ticket_id": 0,
                    "area": "",
                    "issue_type": "",
                    "engagement": 0,
                    "date": ""
                }
            }
            tmp["ticket"]["ticket_id"] = issue.id
            tmp["ticket"]["engagement"] = self._count_issue_engagement(issue)

            area, issue_type = self._issues_get_labels(issue)
            tmp["ticket"]["area"] = area
            tmp["ticket"]["issue_type"] = issue_type

            tmp["ticket"]["date"] = issue.created_at.strftime('%Y-%m-%d-%H-%M-%S')
            issue_list.append(tmp)
        issue_json = self._issues_to_json(issue_list)
        return issue_json
