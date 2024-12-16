class ResourceNotFoundException(Exception):
    status_code = 404
    code = 404
    message = "Resource not found"
    error_code = "resource_not_found"

    def __init__(self, message=None) -> None:
        if message:
            self.message = message
