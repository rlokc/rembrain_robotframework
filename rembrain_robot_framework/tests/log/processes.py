import time

from rembrain_robot_framework import RobotProcess


class FailingProcess(RobotProcess):
    """
    Process that fails after :fail_threshold loops
    waits for :sleep_interval inbetween
    """

    def __init__(self, *args, **kwargs):
        super(FailingProcess, self).__init__(*args, **kwargs)

        self.log.debug(f"{self.__class__} constructor")
        self.fail_threshold = int(kwargs.get("fail_threshold", 3))
        self.sleep_interval = float(kwargs.get("sleep_interval", 0.5))
        self.count = 0

    def run(self) -> None:
        self.count = 0

        while True:
            self.log.info(f"Count: {self.count}")
            self.count += 1

            if self.fail_threshold and self.count >= self.fail_threshold:
                raise RuntimeError("Reached failure threshold")

            time.sleep(self.sleep_interval)
