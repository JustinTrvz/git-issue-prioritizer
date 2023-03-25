class Ticket:
    """
    Github ticket class
    """
    def __init__(self, ticket_id, area, issue_type, engagement, date):
        """
        Initializes and instance of a Github ticket.

        Parameters
        ----------
        ticket_id : int
            Github issue ID
        area : str
            Area of the ticket
        issue_type : str
            Type of ticket
        engagement : int
            Number of commentators below issue
        date : str
            Date and time the issue was posted
        """
        self.ticket_id : int = ticket_id
        self.area : str = area
        self.issue_type : str = issue_type
        self.engagement : int = engagement
        self.date : str = date
