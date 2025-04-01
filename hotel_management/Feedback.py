class Feedback:
    """Class representing feedback from guests."""

    def __init__(self, feedback_id: str, guest, rating: int, comments: str):
        self.feedback_id = feedback_id
        self.guest = guest
        self.rating = rating
        self.comments = comments

    def __str__(self):
        return f"Feedback {self.feedback_id} from {self.guest.name}: {self.comments} (Rating: {self.rating})"