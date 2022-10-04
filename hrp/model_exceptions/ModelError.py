class ModelError(Exception):
    def __init__(self, message):
        super().__init__(message)
        # ToDo save error to log
