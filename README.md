# Git Issue Prioritizer
This script sorts and prioritizes issues of a git repositiory.

# GithubIssueParser
Usage:
```
from issue_parser import GithubIssueParser

token = <your github access token>
repo = "RIOT-OS/RIOT"
ignored_users = []
parser = GithubIssueParser(token, ignored_users, repo)
issues = parser.get_issues()
```

`get_issues()` takes a very long time, don't worry.

# Issue format
{
    "ticket": {
        "ticket-id": int,
        "area": str,
        "issue-type": str,
        "engagement": int,
        "date": str<"MM-DD-YYYY">
    }
}
