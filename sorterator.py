import json
from datetime import datetime
from types import SimpleNamespace

tickets = '{ \
    "ticket3": { "ticket-id": 789, "area": "security", "issue-type": "bug", "engagement": 3, "date": "23-01-2023" }, \
    "ticket1": { "ticket-id": 123, "area": "security", "issue-type": "bug", "engagement": 3, "date": "21-01-2023" }, \
    "ticket2": { "ticket-id": 456, "area": "security", "issue-type": "bug", "engagement": 3, "date": "22-01-2023" } \
}'


class Ticket:
    ticket_id = None
    area = None
    issue_type = None
    engagement = None
    date:datetime  = None


def main():
    # json_tickets = json.loads(tickets, object_hook=lambda d: SimpleNamespace(**d))
    # print(json_tickets)

    tickets = []
    #tickets.append(tf(1, "test", "bug", 1, "21-03-2023"))
    #tickets.append(tf(2, "security", "new feature", 17, "22-03-2023"))
    #tickets.append(tf(3, "improvement", "bug", 34, "23-03-2023"))
    #tickets.append(tf(4, "test", "new feature", 42, "24-03-2023"))
    #tickets.append(tf(5, "improvement", "bug", 128, "25-03-2023"))
    #tickets.append(tf(6, "security", "test", 5, "26-03-2023"))
    ##tickets.append(tf(7, "test", "bug", 3, "27-03-2023"))
    #tickets.append(tf(8, "test", "test", 7, "28-03-2023"))
    #tickets.append(tf(9, "improvement", "bug", 8, "29-03-2023"))
    #tickets.append(tf(10, "security", "new feature", 9, "30-03-2023"))
    #tickets.append(tf(11, "improvement", "bug", 13, "21-03-2023"))
    #tickets.append(tf(12, "test", "new feature", 2, "22-03-2023"))
    #tickets.append(tf(13, "improvement", "bug", 1000, "23-03-2023"))
    #tickets.append(tf(14, "security", "test", 0, "24-03-2023"))
    #tickets.append(tf(15, "test", "bug", 15, "25-03-2023"))
    #tickets.append(tf(16, "test", "test", 100, "26-03-2023"))
    #tickets.append(tf(17, "security", "bug", 99, "27-03-2023"))
    #tickets.append(tf(18, "improvement", "new feature", 77, "28-03-2023"))
    #tickets.append(tf(19, "test", "bug", 88, "29-03-2023"))
    #tickets.append(tf(20, "improvement", "new feature", -1, "30-03-2023"))

    tickets.append(tf(1, "test", "bug", 1, "21-03-2023"))
    tickets.append(tf(2, "security", "new feature", 1, "22-03-2023"))
    tickets.append(tf(3, "improvement", "bug", 1, "23-03-2023"))
    tickets.append(tf(4, "test", "new feature", 1, "24-03-2023"))
    tickets.append(tf(5, "improvement", "bug", 1, "25-03-2023"))
    tickets.append(tf(6, "security", "test", 1, "26-03-2023"))
    tickets.append(tf(7, "test", "bug", 1, "27-03-2023"))
    tickets.append(tf(8, "test", "test", 1, "28-03-2023"))
    tickets.append(tf(9, "improvement", "bug", 1, "29-03-2023"))
    tickets.append(tf(10, "security", "new feature", 1, "30-03-2023"))
    tickets.append(tf(11, "improvement", "bug", 1, "21-03-2023"))
    tickets.append(tf(12, "test", "new feature", 1, "22-03-2023"))
    tickets.append(tf(13, "improvement", "bug", 1, "23-03-2023"))
    tickets.append(tf(14, "security", "test", 1, "24-03-2023"))
    tickets.append(tf(15, "test", "bug", 1, "25-03-2023"))
    tickets.append(tf(16, "test", "test", 1, "26-03-2023"))
    tickets.append(tf(17, "security", "bug", 1, "27-03-2023"))
    tickets.append(tf(18, "improvement", "new feature", 1, "28-03-2023"))
    tickets.append(tf(19, "test", "bug", 1, "29-03-2023"))
    tickets.append(tf(20, "improvement", "new feature", 1, "30-03-2023"))

    sorted_tickets = sort(tickets)

    for x in sorted_tickets:
        print(x.ticket_id)


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


def tf(ticket_id, area, issue_type, engagement, date):
    ret = Ticket()
    ret.ticket_id = ticket_id
    ret.area = area
    ret.issue_type = issue_type
    ret.engagement = engagement
    ret.date = date
    return ret


if __name__ == "__main__":
    main()
