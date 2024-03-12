import logging
import logging.handlers

class RincewindLogger:
    def __init__(self):
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.DEBUG)  # Set to DEBUG to capture all messages; handlers will filter
        self._configured = False

        # Exposed attributes
        self.log_file_path = None
        self.max_days = None
        self.max_size_mb = None
        self.log_level = logging.INFO
        self.verbose = False
        self.stdout_log_level = None

    def setup(self, log_file_path: str, max_days: int, max_size_mb: int,
              log_level: int = logging.INFO, verbose: bool = False,
              stdout_log_level: int = None) -> None:
        """
        Sets up logging with file rotation, retention policies, and optional stdout logging.
        """
        # Store configuration
        self.log_file_path = log_file_path
        self.max_days = max_days
        self.max_size_mb = max_size_mb
        self.log_level = log_level
        self.verbose = verbose
        self.stdout_log_level = stdout_log_level if stdout_log_level is not None else log_level

        # Convert max size in MB to bytes for the RotatingFileHandler
        max_size_bytes = self.max_size_mb * 1024 * 1024

        # Define log format
        log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        # Setup file handler with rotation and retention based on size
        file_handler = logging.handlers.RotatingFileHandler(
            self.log_file_path, maxBytes=max_size_bytes, backupCount=self.max_days, encoding='utf-8'
        )
        file_handler.setFormatter(log_format)
        file_handler.setLevel(self.log_level)
        self._logger.addHandler(file_handler)

        # If verbose, add stdout handler with optional separate level
        if self.verbose:
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(log_format)
            stream_handler.setLevel(self.stdout_log_level)
            self._logger.addHandler(stream_handler)

        self._configured = True

    def log_info(self, message: str) -> None:
        """
        Logs an informational message.
        """
        self._ensure_configured()
        self._logger.info(message)

    def log_error(self, message: str) -> None:
        """
        Logs an error message.
        """
        self._ensure_configured()
        self._logger.error(message)

    def _ensure_configured(self) -> None:
        """
        Ensure the logger is configured; otherwise, use a default setup.
        """
        if not self._configured:
            self.setup('default.log', 7, 5)  # Use a default configuration

    @property
    def is_configured(self) -> bool:
        """
        Indicates whether the logger has been configured.
        """
        return self._configured
