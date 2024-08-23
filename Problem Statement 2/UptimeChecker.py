import argparse
import logging
import sys
import httpx


class UptimeChecker:
    """
    A class to check the uptime of an application by sending an HTTP request.

    Attributes:
        url (str): The URL of the application to check.
        expected_status_code (int): The expected HTTP status code.
    """

    def __init__(self, url: str, expected_status_code: int = 200) -> None:
        """
        Initializes the UptimeChecker object.

        Args:
            url (str): The URL of the application to check.
            expected_status_code (int, optional): The expected HTTP status code. Defaults to 200.
        Returns:
            None
        """
        self.url = url
        self.expected_status_code = expected_status_code

    def check_uptime(self) -> None:
        """
        Checks the uptime of the application by sending an HTTP request to the specified URL.

        The application is considered 'down' if the response status code is not equal to the
        expected status code. In this case, the script will exit with a status code of 1.

        Returns:
            None
        """
        try:
            response = httpx.get(self.url)
            if response.status_code != self.expected_status_code:
                logging.error(
                    f"Expected status code {self.expected_status_code}, got {response.status_code}"
                )
                return False
        except httpx.RequestError as e:
            logging.exception(e)
            return False
        return True


def main() -> None:
    """
    Parses command line arguments and checks the uptime of the specified application.

    This function will exit with a status code of 1 if the application is down or if an error
    occurs while checking the uptime.

    Returns:
        None
    """
    parser = argparse.ArgumentParser(description="Check the uptime of an application")
    parser.add_argument("url", help="The URL of the application to check")
    parser.add_argument(
        "--status-code", type=int, default=200, help="The expected HTTP status code"
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)

    uptime_checker = UptimeChecker(args.url, args.status_code)
    is_system_up = uptime_checker.check_uptime()
    if is_system_up:
        logging.info("Application is up")
    else:
        logging.info("Application is down")
        sys.exit(1)


if __name__ == "__main__":
    main()
