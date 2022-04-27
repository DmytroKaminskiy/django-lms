from rest_framework.throttling import AnonRateThrottle


class AnonStudentThrottle(AnonRateThrottle):
    scope = 'students'

    # def allow_request(self, request, view):
    #     return False
