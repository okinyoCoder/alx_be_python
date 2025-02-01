class Book:
    def __init__(self, title, author):
        """ class Constructor"""
        self.title = title
        self.author = author
        self._is_checked_out = bool

    def isNotAvailables(self):
        self._is_checked_out = True
    
    def isAvailable(self):
        self._is_checked_out = False