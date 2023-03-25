# Git Issue Prioritizer
This script sorts and prioritizes issues of a git repositiory.

# Sorterator
## Token
You will need a Github access token, which you can create [here](https://github.com/settings/tokens?type=beta).
Choose `all repositories` and then set permissions for Issues to `read only`. This will create a taken
that can only read issues of all repositories.
Add a file called `token` to the repository and paste your token in there. The script will parse that file and
use that token to download the issues.

## Usage
1. Install requirements: `pip install requirements.txt`
2. Add token
3. Run `python sorterator.py`

# GithubIssueParser
## Usage:
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
