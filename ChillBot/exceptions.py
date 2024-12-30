class UserNotFound(Exception):
    """Throws an exception whenever ID is not found."""
    def __init__(self):
        super().__init__("User ID does not exist in the database")
    
    def __str__(self) -> str:
        return self.args[0]