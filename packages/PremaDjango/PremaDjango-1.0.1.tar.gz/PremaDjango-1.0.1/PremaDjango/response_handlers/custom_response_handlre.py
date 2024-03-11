"""Custom Response Handler."""

import math

from rest_framework import status
from rest_framework.response import Response


class CustomResponseHandler:
    """Custom Response Handler Class for Django REST Framework."""

    def __init__(self, serializer_class=None):
        """
        Initialize the class with an optional serializer class.

        Args:
            serializer_class: The serializer class to be used.

        Returns:
            None
        """
        self.serializer_class = serializer_class

    def _generate_response(self, status_code, message, data=None, **kwargs):
        """
        Generate a response with the given status code, message, and optional data.

        :param status_code: The status code for the response
        :param message: The message to be included in the response
        :param data: Optional data to be included in the response
        :param kwargs: Additional keyword arguments
        :return: Response object with the generated data and status code
        """
        response_data = {
            "status": status_code,
            "message": message,
            "data": data,
            **kwargs,
        }
        return Response(response_data, status=status_code)

    # Informational
    def continue_100(self, message=None, data=None, **kwargs):
        """
        Generate a response with status code 100 (Continue) along with the provided message and data.

        :param message: The message to be included in the response. Defaults to "Continue" if not provided.
        :param data: Additional data to be included in the response.
        :param kwargs: Additional keyword arguments to be passed to _generate_response.

        :return: The generated response with status code 100 (Continue).
        """
        if message is None:
            message = "Continue"
        return self._generate_response(status.HTTP_100_CONTINUE, message, data, **kwargs)

    def switching_protocols_101(self, message=None, data=None, **kwargs):
        """
        This function handles the switching protocols with an optional message and data.
        It returns the response generated with the status code 101 switching protocols,
        the provided message, data, and any additional keyword arguments.
        """

        if message is None:
            message = "Switching Protocols"
        return self._generate_response(status.HTTP_101_SWITCHING_PROTOCOLS, message, data, **kwargs)

    def processing_102(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Processing"
        return self._generate_response(status.HTTP_102_PROCESSING, message, data, **kwargs)

    def early_hints_103(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Early Hints"
        return self._generate_response(status.HTTP_103_EARLY_HINTS, message, data, **kwargs)

    # Successful
    def success_200(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Success"
        return self._generate_response(status.HTTP_200_OK, message, data, **kwargs)

    def created_201(self, message=None, data=None, **kwargs):
        if message is None:
            message = "New Record Created"
        return self._generate_response(status.HTTP_201_CREATED, message, data, **kwargs)

    def accepted_202(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Accepted"
        return self._generate_response(status.HTTP_202_ACCEPTED, message, data, **kwargs)

    def non_authoritative_information_203(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Non-Authoritative Information"
        return self._generate_response(status.HTTP_203_NON_AUTHORITATIVE_INFORMATION, message, data, **kwargs)

    def no_content_204(self, message=None, data=None, **kwargs):
        if message is None:
            message = "No Content"
        return self._generate_response(status.HTTP_204_NO_CONTENT, message, data, **kwargs)

    def reset_content_205(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Reset Content"
        return self._generate_response(status.HTTP_205_RESET_CONTENT, message, data, **kwargs)

    def partial_content_206(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Partial Content"
        return self._generate_response(status.HTTP_206_PARTIAL_CONTENT, message, data, **kwargs)

    def multi_status_207(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Multi-Status"
        return self._generate_response(status.HTTP_207_MULTI_STATUS, message, data, **kwargs)

    def already_reported_208(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Already Reported"
        return self._generate_response(status.HTTP_208_ALREADY_REPORTED, message, data, **kwargs)

    def im_used_226(self, message=None, data=None, **kwargs):
        if message is None:
            message = "IM Used"
        return self._generate_response(status.HTTP_226_IM_USED, message, data, **kwargs)

    def success_pagination_200(self, request, queryset, message=None):
        try:
            page = int(request.GET.get("page", 1))
            offset = int(request.GET.get("offset", request.GET.get("limit", 20)))
            limit = int(request.GET.get("offset", offset))
            if page < 1 or offset < 1 or limit < 1:
                raise ValueError("Invalid page, offset, or limit value")
        except ValueError:
            return Response({"error": "Invalid page, offset, or limit value"}, status=status.HTTP_400_BAD_REQUEST)

        if message is None:
            message = "Success"

        total = queryset.count()
        start_index = (page - 1) * offset
        end_index = start_index + limit

        paginated_queryset = queryset[start_index:end_index]
        serializer = self.serializer_class(paginated_queryset, many=True, context={'request': request})

        last_page = math.ceil(total / offset)
        next_page = min(page + 1, last_page) if total > 0 else 1

        response_data = {
            "status": status.HTTP_200_OK,
            "message": message,
            "total": total,
            "page": page,
            "next": next_page,
            "last_page": last_page,
            "data": serializer.data,
        }

        return Response(response_data, status=status.HTTP_200_OK)

    # Redirection
    def multiple_choices_300(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Multiple Choices"
        return self._generate_response(status.HTTP_300_MULTIPLE_CHOICES, message, data, **kwargs)

    def moved_permanently_301(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Moved Permanently"
        return self._generate_response(status.HTTP_301_MOVED_PERMANENTLY, message, data, **kwargs)

    def found_302(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Found"
        return self._generate_response(status.HTTP_302_FOUND, message, data, **kwargs)

    def see_other_303(self, message=None, data=None, **kwargs):
        if message is None:
            message = "See Other"
        return self._generate_response(status.HTTP_303_SEE_OTHER, message, data, **kwargs)

    def not_modified_304(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Not Modified"
        return self._generate_response(status.HTTP_304_NOT_MODIFIED, message, data, **kwargs)

    def use_proxy_305(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Use Proxy"
        return self._generate_response(status.HTTP_305_USE_PROXY, message, data, **kwargs)

    def temporary_redirect_307(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Temporary Redirect"
        return self._generate_response(status.HTTP_307_TEMPORARY_REDIRECT, message, data, **kwargs)

    def permanent_redirect_308(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Permanent Redirect"
        return self._generate_response(status.HTTP_308_PERMANENT_REDIRECT, message, data, **kwargs)

    # Client errors

    def bad_request_400(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Bad Request"
        return self._generate_response(status.HTTP_400_BAD_REQUEST, message, data, **kwargs)

    def unauthorized_401(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Unauthorized"
        return self._generate_response(status.HTTP_401_UNAUTHORIZED, message, data, **kwargs)

    def payment_required_402(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Payment Required"
        return self._generate_response(status.HTTP_402_PAYMENT_REQUIRED, message, data, **kwargs)

    def forbidden_403(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Forbidden"
        return self._generate_response(status.HTTP_403_FORBIDDEN, message, data, **kwargs)

    def not_found_404(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Not Found"
        return self._generate_response(status.HTTP_404_NOT_FOUND, message, data, **kwargs)

    def method_not_allowed_405(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Method Not Allowed"
        return self._generate_response(status.HTTP_405_METHOD_NOT_ALLOWED, message, data, **kwargs)

    def not_acceptable_406(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Not Acceptable"
        return self._generate_response(status.HTTP_406_NOT_ACCEPTABLE, message, data, **kwargs)

    def proxy_authentication_required_407(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Proxy Authentication Required"
        return self._generate_response(status.HTTP_407_PROXY_AUTHENTICATION_REQUIRED, message, data, **kwargs)

    def request_timeout_408(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Request Timeout"
        return self._generate_response(status.HTTP_408_REQUEST_TIMEOUT, message, data, **kwargs)

    def conflict_409(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Conflict"
        return self._generate_response(status.HTTP_409_CONFLICT, message, data, **kwargs)

    def gone_410(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Gone"
        return self._generate_response(status.HTTP_410_GONE, message, data, **kwargs)

    def length_required_411(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Length Required"
        return self._generate_response(status.HTTP_411_LENGTH_REQUIRED, message, data, **kwargs)

    def precondition_failed_412(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Precondition Failed"
        return self._generate_response(status.HTTP_412_PRECONDITION_FAILED, message, data, **kwargs)

    def request_entity_too_large_413(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Request Entity Too Large"
        return self._generate_response(status.HTTP_413_REQUEST_ENTITY_TOO_LARGE, message, data, **kwargs)

    def request_uri_too_long_414(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Request-URI Too Long"
        return self._generate_response(status.HTTP_414_REQUEST_URI_TOO_LONG, message, data, **kwargs)

    def unsupported_media_type_415(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Unsupported Media Type"
        return self._generate_response(status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, message, data, **kwargs)

    def requested_range_not_satisfiable_416(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Requested Range Not Satisfiable"
        return self._generate_response(status.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE, message, data, **kwargs)

    def expectation_failed_417(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Expectation Failed"
        return self._generate_response(status.HTTP_417_EXPECTATION_FAILED, message, data, **kwargs)

    def misdirected_request_421(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Misdirected Request"
        return self._generate_response(status.HTTP_421_MISDIRECTED_REQUEST, message, data, **kwargs)

    def unprocessable_entity_422(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Unprocessable Entity"
        return self._generate_response(status.HTTP_422_UNPROCESSABLE_ENTITY, message, data, **kwargs)

    def locked_423(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Locked"
        return self._generate_response(status.HTTP_423_LOCKED, message, data, **kwargs)

    def failed_dependency_424(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Failed Dependency"
        return self._generate_response(status.HTTP_424_FAILED_DEPENDENCY, message, data, **kwargs)

    def too_early_425(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Too Early"
        return self._generate_response(status.HTTP_425_TOO_EARLY, message, data, **kwargs)

    def upgrade_required_426(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Upgrade Required"
        return self._generate_response(status.HTTP_426_UPGRADE_REQUIRED, message, data, **kwargs)

    def precondition_required_428(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Precondition Required"
        return self._generate_response(status.HTTP_428_PRECONDITION_REQUIRED, message, data, **kwargs)

    def too_many_requests_429(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Too Many Requests"
        return self._generate_response(status.HTTP_429_TOO_MANY_REQUESTS, message, data, **kwargs)

    def request_header_fields_too_large_431(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Request Header Fields Too Large"
        return self._generate_response(status.HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE, message, data, **kwargs)

    def unavailable_for_legal_reasons_451(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Unavailable For Legal Reasons"
        return self._generate_response(status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, message, data, **kwargs)

        # Server errors

    def internal_server_error_500(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Internal Server Error"
        return self._generate_response(status.HTTP_500_INTERNAL_SERVER_ERROR, message, data, **kwargs)

    def not_implemented_501(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Not Implemented"
        return self._generate_response(status.HTTP_501_NOT_IMPLEMENTED, message, data, **kwargs)

    def bad_gateway_502(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Bad Gateway"
        return self._generate_response(status.HTTP_502_BAD_GATEWAY, message, data, **kwargs)

    def service_unavailable_503(self, message=None, data=None, **kwargs):
        """
        Handle Service Unavailable error by generating a response with status 503.
        :param message: (optional) A custom error message, defaults to "Service Unavailable"
        :param data: (optional) Additional data to include in the response
        :param kwargs: Additional keyword arguments for future use
        :return: Response with status 503 and custom message
        """
        if message is None:
            message = "Service Unavailable"
        return self._generate_response(status.HTTP_503_SERVICE_UNAVAILABLE, message, data, **kwargs)

    def gateway_timeout_504(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Gateway Timeout"
        return self._generate_response(status.HTTP_504_GATEWAY_TIMEOUT, message, data, **kwargs)

    def http_version_not_supported_505(self, message=None, data=None, **kwargs):
        if message is None:
            message = "HTTP Version Not Supported"
        return self._generate_response(status.HTTP_505_HTTP_VERSION_NOT_SUPPORTED, message, data, **kwargs)

    def variant_also_negotiates_506(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Variant Also Negotiates"
        return self._generate_response(status.HTTP_506_VARIANT_ALSO_NEGOTIATES, message, data, **kwargs)

    def insufficient_storage_507(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Insufficient Storage"
        return self._generate_response(status.HTTP_507_INSUFFICIENT_STORAGE, message, data, **kwargs)

    def loop_detected_508(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Loop Detected"
        return self._generate_response(status.HTTP_508_LOOP_DETECTED, message, data, **kwargs)

    def bandwidth_limit_exceeded_509(self, message=None, data=None, **kwargs):
        if message is None:
            message = "Bandwidth Limit Exceeded"
        return self._generate_response(status.HTTP_509_BANDWIDTH_LIMIT_EXCEEDED, message, data, **kwargs)

    def not_extended_510(self, message=None, data=None, **kwargs):
        """
        Generate a response with status HTTP 510 Not Extended, message, and data.
        """
        if message is None:
            message = "Not Extended"
        return self._generate_response(status.HTTP_510_NOT_EXTENDED, message, data, **kwargs)

    def network_authentication_required_511(self, message=None, data=None, **kwargs):
        """
        Perform network authentication and generate a response with the specified message and data.

        :param message: The message to be included in the response. Defaults to "Network Authentication Required" if not provided.
        :param data: Additional data to be included in the response.
        :param kwargs: Additional keyword arguments to be included in the response.
        :return: The response generated with the specified status code, message, and additional data.
        """

        if message is None:
            message = "Network Authentication Required"
        return self._generate_response(status.HTTP_511_NETWORK_AUTHENTICATION_REQUIRED, message, data, **kwargs)
