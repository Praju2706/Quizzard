# usser class to represent a user
class User:
    def __init__(self, username, password,score=0):
        self.username = username
        self.password = password
        self.score = score
        
    def __str__(self):
        return f"User({self.username}, Score: {self.score})"