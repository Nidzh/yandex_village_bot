from fastapi import status


class APPException(Exception):
    status_code: int = 500
    type: str = "base.error"
    detail: str = "Произошла непредвиденная ошибка"
    loc: list = []

    def __init__(self, status_code: int = None, detail: str = None, **kwargs):
        self.status_code = status_code or self.status_code
        self.detail = detail or self.detail
        if kwargs:
            for k, v in kwargs.items():
                self.loc.append({k: v})


class NotAuthenticated(APPException):
    status_code = status.HTTP_401_UNAUTHORIZED
    type = "auth.not_authenticated"
    detail = "Authentication credentials were not provided."


class PermissionDenied(APPException):
    status_code = status.HTTP_403_FORBIDDEN
    type = "auth.permission_denied"
    detail = "You do not have permission to perform this action."


class NotFound(APPException):
    status_code = status.HTTP_404_NOT_FOUND
    type = "resource.not_found"
    detail = "The requested resource was not found."


class Conflict(APPException):
    status_code = status.HTTP_409_CONFLICT
    type = "resource.conflict"
    detail = "Conflict with the current state of the resource."


class BadRequest(APPException):
    status_code = status.HTTP_400_BAD_REQUEST
    type = "request.bad_request"
    detail = "Invalid request."
