import json
from datetime import datetime
from types import SimpleNamespace
from ticket import Ticket


def sort(tickets: [Ticket]):
    security_bug = []
    for ticket in tickets:
        if ticket.area == "security" and ticket.issue_type == "bug":
            security_bug.append(ticket)
    for ticket in security_bug:
        tickets.remove(ticket)
    security_bug = bubbleedsort(security_bug)

    security_enhancement = []
    for ticket in tickets:
        if ticket.area == "security" and ticket.issue_type == "enhancement":
            security_enhancement.append(ticket)
    for ticket in security_enhancement:
        tickets.remove(ticket)
    security_enhancement = bubbleedsort(security_enhancement)

    security_new_feature = []
    for ticket in tickets:
        if ticket.area == "security" and ticket.issue_type == "new feature":
            security_new_feature.append(ticket)
    for ticket in security_new_feature:
        tickets.remove(ticket)
    security_new_feature = bubbleedsort(security_new_feature)

    security_no_label = []
    for ticket in tickets:
        if ticket.area == "security":
            security_no_label.append(ticket)
    for ticket in security_no_label:
        tickets.remove(ticket)
    security_no_label = bubbleedsort(security_no_label)

    bug = []
    for ticket in tickets:
        if ticket.issue_type == "bug":
            bug.append(ticket)
    for ticket in bug:
        tickets.remove(ticket)
    bug = bubbleedsort(bug)

    improvements = []
    for ticket in tickets:
        if ticket.issue_type == "enhancement":
            improvements.append(ticket)
    for ticket in improvements:
        tickets.remove(ticket)
    improvements = bubbleedsort(improvements)

    new_feature = []
    for ticket in tickets:
        if ticket.issue_type == "new feature":
            new_feature.append(ticket)
    for ticket in new_feature:
        tickets.remove(ticket)
    new_feature = bubbleedsort(new_feature)

    uncategorized = []
    for ticket in tickets:
        uncategorized.append(ticket)
    uncategorized = bubbleedsort(uncategorized)

    tickets = security_bug + security_enhancement + security_new_feature + security_no_label + bug + improvements + new_feature + uncategorized
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
