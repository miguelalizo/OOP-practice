from __future__ import annotations
from abc import ABC, abstractmethod

# Step 1: abstract middleware base


class iMiddleware(ABC):
    """Abstract imiddleware class serving as the base of the chain"""

    @abstractmethod
    def handle_request(self, request):
        """
        Handles request; must be implemented by concrete classes
        """
        pass


# concrete middleware implementations


class AuthenticationMiddleware(iMiddleware):
    """
    Middeleware responsible for user auth
    """

    def handle_request(self, request):
        """
        Handle authentication or pass to the next middleware in the chain
        """
        if self.authenticate(request):
            print("AuthenticationMiddleware: auth handled successfully")
            # pass request to next handler in the chain
            return request
        else:
            print("AuthenticationMiddleware: auth failed")
            # stop the chain
            return None

    def authenticate(self, request):
        """Implement auth logic here"""
        # Return True if auth is successful, else False
        if request["key"] == "super_secret":
            return True
        return False


class LoggingMiddleware(iMiddleware):
    """Middleware responsible for logging"""

    def handle_request(self, request):
        """Handle request logging and pass to the next middleware in the chain"""
        print("Logging middleware: Logging request")
        # Pass the request to the next middleware or handler in the chain.
        return request


class DataValidationMiddleware(iMiddleware):
    """Middlware responsible for data validation"""

    def handle_request(self, request):
        if self.validate_data(request):
            print("Data Validation middleware: Data is valid")
            # Pass the request to the next middleware or handler in the chain.
            return request
        else:
            print("Data Validation middleware: Invalid data")
            # Stop the chain if data validation fails.
            return None

    def validate_data(self, request):
        """Implement data validation logic here"""
        # return True if data is valid else False
        if request["data"] == "valid_data":
            return True
        return False


# 3. Request handling class


class MiddlewareChain:
    """
    Chain class to handle the final request and manage middleware
    """

    def __init__(self):
        self.middlewares = []

    def add_middleware(self, middleware):
        self.middlewares.append(middleware)

    def handle_request(self, request):
        for middleware in self.middlewares:
            request = middleware.handle_request(request)
            if request is None:
                print("Request process stopped")
                return
        print("Request process finalized")


# client code
if __name__ == "__main__":
    # create middleware instances
    auth_middleware = AuthenticationMiddleware()
    logging_middleware = LoggingMiddleware()
    data_valid_middleware = DataValidationMiddleware()

    # create chain and add middleware
    chain = MiddlewareChain()
    chain.add_middleware(auth_middleware)
    chain.add_middleware(logging_middleware)
    chain.add_middleware(data_valid_middleware)

    # simulate valid HTTP request
    http_request = {"user": "username", "data": "valid_data", "key": "super_secret"}
    chain.handle_request(http_request)

    # simulate invalid HTTP request
    http_request = {"user": "username", "data": "not_valid", "key": "super_secret"}
    chain.handle_request(http_request)
