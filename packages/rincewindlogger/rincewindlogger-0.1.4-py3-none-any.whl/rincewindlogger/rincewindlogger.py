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
        self.rotation_type = 'size'  # Default to size-based rotation
        self.rotation_interval = '1D'  # Default to daily rotation for time-based
    def setup(self, log_file_path: str, max_days: int, max_size_mb: int,
              log_level: int = logging.INFO, verbose: bool = False,
              stdout_log_level: int = None, rotation_type: str = 'size',
              rotation_interval: str = '1D') -> None:
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
        self.rotation_type = rotation_type
        self.rotation_interval = rotation_interval


        # Convert max size in MB to bytes for the RotatingFileHandler
        max_size_bytes = self.max_size_mb * 1024 * 1024

        # Define log format
        log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        if self.rotation_type == 'size':
            # Convert max size in MB to bytes for the RotatingFileHandler
            max_size_bytes = self.max_size_mb * 1024 * 1024
            file_handler = logging.handlers.RotatingFileHandler(
                self.log_file_path, maxBytes=max_size_bytes, backupCount=self.max_days, encoding='utf-8'
            )
        elif self.rotation_type == 'time':
            # Setup time-based rotation
            try:
                # Assuming self.rotation_interval is a string like 'S', 'M', 'H', etc.
                file_handler = logging.handlers.TimedRotatingFileHandler(
                    self.log_file_path, when=self.rotation_interval, backupCount=self.max_days, encoding='utf-8', utc=True
                )
            except ValueError as e:
                raise ValueError(f"Invalid rotation_interval: {self.rotation_interval}. Error: {e}")
        else:
            raise ValueError("Invalid rotation_type. Use 'size' or 'time'.")

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

    def log_debug(self, message: str) -> None:
        """
        Logs a debug message.
        """
        self._ensure_configured()
        self._logger.debug(message)

    def log_warning(self, message: str) -> None:
        """
        Logs a warning message.
        """
        self._ensure_configured()
        self._logger.warning(message)

    def log_critical(self, message: str) -> None:
        """
        Logs a critical message.
        """
        self._ensure_configured()
        self._logger.critical(message)
    def log_exception(self, message: str, e: Exception) -> None:
        """
        Logs an exception message.
        """
        self._ensure_configured()
        self._logger.exception(message, e)

    def log_traceback(self, message: str):
        """
        Logs a message with traceback.
        """
        self._ensure_configured()
        self._logger.exception(message)
    def log_exception(self, message: str) -> None:
        """
        Logs an exception message along with the traceback.
        """
        self._ensure_configured()
        self._logger.exception(message)  # Automatically logs the stack trace

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
