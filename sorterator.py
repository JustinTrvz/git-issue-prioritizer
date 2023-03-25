from issue_parser import GithubIssueParser
from ticket import Ticket

def sort(tickets: [Ticket]):
    security_bug = []
    for x in tickets:
        if x.area == "security" and x.issue_type=="bug":
            security_bug.append(x)
    for x in security_bug:
        tickets.remove(x)
    security_bug = bubbleedsort(security_bug)

    security_enhancement = []
    for x in tickets:
        if x.area == "security" and x.issue_type=="enhancement":
            security_enhancement.append(x)
    for x in security_enhancement:
        tickets.remove(x)
    security_enhancement = bubbleedsort(security_enhancement)

    security_new_feature = []
    for x in tickets:
        if x.area == "security" and x.issue_type=="new feature":
            security_new_feature.append(x)
    for x in security_new_feature:
        tickets.remove(x)
    security_new_feature = bubbleedsort(security_new_feature)

    security_no_label = []
    for x in tickets:
        if x.area == "security":
            security_no_label.append(x)
    for x in security_no_label:
        tickets.remove(x)
    security_no_label = bubbleedsort(security_no_label)

    bug = []
    for x in tickets:
        if x.issue_type == "bug":
            bug.append(x)
    for x in bug:
        tickets.remove(x)
    bug = bubbleedsort(bug)

    improvements = []
    for x in tickets:
        if x.issue_type == "enhancement":
            improvements.append(x)
    for x in improvements:
        tickets.remove(x)
    improvements = bubbleedsort(improvements)

    new_feature = []
    for x in tickets:
        if x.issue_type == "new feature":
            new_feature.append(x)
    for x in new_feature:
        tickets.remove(x)
    new_feature = bubbleedsort(new_feature)

    uncategorized = []
    for x in tickets:
        uncategorized.append(x)
    uncategorized = bubbleedsort(uncategorized)

    tickets = security_bug + security_enhancement + security_new_feature + security_no_label + bug+improvements + new_feature + uncategorized

    return tickets


def bubbleedsort(tickets: [Ticket]):
    for x in range(0, len(tickets)):
        for y in range(0, len(tickets) - 1):

            if (tickets[y].engagement < tickets[y + 1].engagement) or (
                    tickets[y].engagement == tickets[y + 1].engagement and tickets[y].date > tickets[y + 1].date):
                tmp = tickets[y]
                tickets[y] = tickets[y + 1]
                tickets[y + 1] = tmp

    return tickets

def main():
    token = ""
    with open("token", "r") as file:
        token = file.read().splitlines()[0]
    repo = "RIOT-OS/RIOT"
    parser = GithubIssueParser(token, repo)
    tickets = parser.get_issues()

    sorted_tickets = sort(tickets)

    for x in sorted_tickets:
        print(x.ticket_id)

if __name__ == "__main__":
    main()
