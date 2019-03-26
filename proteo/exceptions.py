class ProteinNotFoundError(Exception):
    def __init__(self, message=None):
        if message:
            self.message = message
        else:
            self.message = "Protein not found"

    def __str__(self):
        return self.message
