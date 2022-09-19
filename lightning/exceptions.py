from lightning_adapter.rest import ApiException


ELEMENTS_ERROR = "Elements error"
WEB_ELEMENT_ERROR = "WebElement error"


class WebDriverException(Exception):
    def __init__(self, message='', errors=''):
        # Call Exception.__init__(message)
        # to use the same Message header as the parent class
        super().__init__(message)
        self.errors = errors


# layer for passing error_type to our decorator
def parametrized(dec):
    def layer(*args, **kwargs):
        def repl(f):
            return dec(f, *args, **kwargs)
        return repl
    return layer


@parametrized
def webdriver_exception(func, error_type: str):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ApiException as e:
            raise WebDriverException(message=str(e), errors=error_type) from e
        except Exception as e:
            raise WebDriverException() from e
    return wrapper
