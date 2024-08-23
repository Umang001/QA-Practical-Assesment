import argparse
import logging
import psutil
import time


# Define a class to monitor system resources
class SystemMonitor:
    """
    A class used to monitor system resources such as CPU, memory, disk, and process count.

    Attributes:
        cpu_threshold (int): The threshold value for CPU usage
        memory_threshold (int): The threshold value for memory usage
        disk_threshold (int): The threshold value for disk usage
        process_threshold (int): The threshold value for process count
        interval (int): The interval in seconds to check system resources
    """

    # Initialize the class with threshold values for CPU, memory, disk, and process count
    def __init__(
        self,
        *,
        cpu_threshold: int,
        memory_threshold: int,
        disk_threshold: int,
        process_threshold: int,
        interval: int,
    ) -> None:
        """
        Initialize the class with the provided threshold values and interval.

        Args:
            cpu_threshold (int): The maximum allowed CPU usage percentage
            memory_threshold (int): The maximum allowed memory usage percentage
            disk_threshold (int): The maximum allowed disk usage percentage
            process_threshold (int): The maximum allowed process count
            interval (int): The interval in seconds to check system resources
        """
        # Store the threshold values as instance variables
        self.cpu_threshold = cpu_threshold  # CPU usage threshold
        self.memory_threshold = memory_threshold  # Memory usage threshold
        self.disk_threshold = disk_threshold  # Disk usage threshold
        self.process_threshold = process_threshold  # Process count threshold
        self.interval = interval  # Interval to check system resources

    # Method to check CPU usage
    def check_cpu_usage(self) -> None:
        """
        Check the current CPU usage and print a message if it's above the threshold.

        Returns:
            None
        """
        # Get the current CPU usage percentage
        cpu_usage = psutil.cpu_percent(interval=1)  # Get CPU usage percentage
        # Check if the CPU usage is above the threshold
        if cpu_usage > self.cpu_threshold:
            # Print a message indicating high CPU usage
            logging.warning(
                f"CPU usage is high: {cpu_usage}%"
            )  # Print high CPU usage message

    # Method to check memory usage
    def check_memory_usage(self) -> None:
        """
        Check the current memory usage and print a message if it's above the threshold.

        Returns:
            None
        """
        # Get the current memory usage percentage
        memory_usage = psutil.virtual_memory().percent  # Get memory usage percentage
        # Check if the memory usage is above the threshold
        if memory_usage > self.memory_threshold:
            # Print a message indicating high memory usage
            logging.warning(
                f"Memory usage is high: {memory_usage}%"
            )  # Print high memory usage message

    # Method to check disk usage
    def check_disk_usage(self) -> None:
        """
        Check the current disk usage and print a message if it's above the threshold.

        Returns:
            None
        """
        # Get the current disk usage percentage
        disk_usage = psutil.disk_usage("/").percent  # Get disk usage percentage
        # Check if the disk usage is above the threshold
        if disk_usage > self.disk_threshold:
            # Print a message indicating high disk usage
            logging.warning(
                f"Disk usage is high: {disk_usage}%"
            )  # Print high disk usage message

    # Method to check process count
    def check_process_count(self) -> None:
        """
        Check the current process count and print a message if it's above the threshold.

        Returns:
            None
        """
        # Get the current process count
        process_count = len(psutil.pids())  # Get process count
        # Check if the process count is above the threshold
        if process_count > self.process_threshold:
            # Print a message indicating high process count
            logging.warning(
                f"Process count is high: {process_count}"
            )  # Print high process count message

    # Method to continuously monitor system resources
    def monitor_system(self) -> None:
        """
        Continuously monitor system resources and check for threshold values.

        Returns:
            None
        """
        # Loop indefinitely
        while True:
            # Check CPU usage
            self.check_cpu_usage()  # Check CPU usage
            # Check memory usage
            self.check_memory_usage()  # Check memory usage
            # Check disk usage
            self.check_disk_usage()  # Check disk usage
            # Check process count
            self.check_process_count()  # Check process count
            # Wait for the specified interval before checking again
            time.sleep(self.interval)  # Wait for interval


if __name__ == "__main__":
    try:
        # Define the command-line arguments
        parser = argparse.ArgumentParser(description="System Monitor")
        parser.add_argument(
            "--cpu-threshold", type=int, default=80, help="CPU usage threshold"
        )
        parser.add_argument(
            "--memory-threshold", type=int, default=80, help="Memory usage threshold"
        )
        parser.add_argument(
            "--disk-threshold", type=int, default=80, help="Disk usage threshold"
        )
        parser.add_argument(
            "--process-threshold", type=int, default=80, help="Process count threshold"
        )
        parser.add_argument(
            "--interval", type=int, default=60, help="Monitoring interval in seconds"
        )

        # Parse the command-line arguments
        args = parser.parse_args()

        # Create an instance of the SystemMonitor class with threshold values and interval
        monitor = SystemMonitor(
            cpu_threshold=args.cpu_threshold,
            memory_threshold=args.memory_threshold,
            disk_threshold=args.disk_threshold,
            process_threshold=args.process_threshold,
            interval=args.interval,
        )

        # Start monitoring the system
        monitor.monitor_system()
    except KeyboardInterrupt:
        pass
