__author__ = 'mstipanov'


class ApiRequestErrorDetails(object):
    messageId = ""
    text = ""
    variables = ""
    additionalDescription = ""

    def __init__(self, text=""):
        self.text = text

    def __str__(self):
        return "ApiRequestErrorDetails: {" \
               "messageId = \"" + str(self.messageId) + "\", " \
                                                        "text = \"" + str(self.text) + "\", " \
                                                                                       "variables = \"" + str(
            self.variables) + "\", " \
                              "additionalDescription = \"" + str(self.additionalDescription) + "\"" \
                                                                                               "}"


class ApiRequestError(object):
    client_correlator = ""
    serviceException = ApiRequestErrorDetails()

    def __init__(self, client_correlator="", serviceException=ApiRequestErrorDetails()):
        self.client_correlator = client_correlator
        self.serviceException = serviceException

    def __str__(self):
        return "ApiRequestError: {" \
               "clientCorrelator = \"" + str(self.client_correlator) + "\", " \
                                                                       "serviceException = " + str(
            self.serviceException) + "" \
                                     "}"


class ApiException(Exception):
    request_error = ApiRequestError()

    def __init__(self, request_error=ApiRequestError()):
        self.request_error = request_error

    def __str__(self):
        return "ApiException: {" \
               "requestError = " + str(self.request_error) + "" \
                                                            "}"
