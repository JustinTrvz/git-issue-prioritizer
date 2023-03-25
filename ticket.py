import json

class Ticket:
    def __init__(self,
                 ticket_id: str,
                 area: str,
                 issue_type: str,
                 engagement: int,
                 date: str):
        self.ticket_id = ticket_id
        self.area = area
        self.issue_type = issue_type
        self.engagement = engagement
        self.date = date

    def to_string(self):
        return json.dumps(vars(self))

    def get_ticket_id(self):
        return self.ticket_id

    def set_ticket_id(self, ticket_id: str):
        self.ticket_id = ticket_id

    def get_area(self):
        return self.area

    def set_area(self, area: str):
        self.area = area

    def get_issue_type(self):
        return self.issue_type

    def set_issue_type(self, issue_type: str):
        self.issue_type = issue_type

    def get_engagement(self):
        return self.engagement

    def set_engagement(self, engagement: int):
        self.engagement = engagement

    def get_date(self):
        return self.date

    def set_date(self, date: str):
        self.date = date

    def get_sort_rank(self):
        return self.sort_rank

    def set_sort_rank(self, sort_rank):
        self.sort_rank = sort_rank