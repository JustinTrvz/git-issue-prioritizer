from github import Github
import array
from tqdm import tqdm
from ticket import Ticket

from sorterator import *


class GithubIssueParser:
    """
    GithubIssueParser downloads issues of a specified repository
    from Github and extracts the information that is relevant to the
    sorting script.
    """

    def __init__(self, access_token: str, ignored_users: array = ['riot-ci'], repo: str = "RIOT-OS/RIOT"):
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
        if not access_token:
            raise AttributeError("Attribute 'access_token' is empty.")

        self._ignored_users = ignored_users
        print(f'Initializing Github Issue Parser for repository {repo}')
        self._g = Github(access_token)
        self._repo = self._g.get_repo(repo)
        self.ticket_list = []

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

    def _convert_and_sort_issues(self):
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
        issues = self._get_issues_and_remove_prs()

        print("Converting issues into custom format...")
        for issue in tqdm(issues):
            area, issue_type = self._issues_get_labels(issue)
            ticket_obj = Ticket(ticket_id=issue.number, area=area, issue_type=issue_type,
                                engagement=self._count_issue_engagement(issue),
                                date=issue.created_at.strftime('%Y-%m-%d %H:%M:%S'))
            self.ticket_list.append(ticket_obj)
        print(f"Created ticket list with {len(self.ticket_list)} entries")
        self.ticket_list = sort(self.ticket_list)

    def get_ticket_list(self):
        """
        Returns converted and sorted ticket list.

        :return:
            converted and sorted ticket list
        """
        self._convert_and_sort_issues()
        return self.ticket_list

    def print_result(self, ):
        """
        Prints ticket list in a human readable format to the console
        """
        counter = 0
        for issue in self.ticket_list:
            print(f"#{counter}: " + issue.to_string())
            counter += 1

    def ticket_list_to_json(self, output_location):
        """
        Saved sorted ticket list as json file to the desired location.

        :param
            output_location: save location (e.g. '/home/user/Documents')
        """
        sort_rank = 0
        ticket_dict = {}
        for ticket in self.ticket_list:
            ticket_dict[sort_rank] = json.loads(ticket.to_string())
            sort_rank += 1
        with open(f'{output_location}/data.json', 'w') as output_file:
            json.dump(ticket_dict, output_file)


if __name__ == "__main__":
    with open("token", "r") as token_file:
        token = token_file.read().splitlines()[0]
    gh_parser = GithubIssueParser(
        access_token=token,
        ignored_users=["riot-ci"],
        repo="RIOT-OS/RIOT"
    )
    ticket_list = gh_parser.get_ticket_list()
    gh_parser.print_result()
    gh_parser.ticket_list_to_json("/home/jtrvz/Git/git-issue-prioritizer")
