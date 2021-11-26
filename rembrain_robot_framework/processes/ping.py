import os
import subprocess
import time

from rembrain_robot_framework import RobotProcess


class PingProcess(RobotProcess):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # get container ID - it's assumed, that we're in a docker container
        try:
            docker_s = subprocess.check_output(["cat", "/proc/1/cpuset"]).decode("utf-8")
            self.container_id = docker_s[8: 8 + 12]
        except Exception as e:
            self.container_id = "ERROR"
            self.log.error(e, exc_info=True)

    def run(self):
        self.log.info(f"{self.__class__.__name__} started, name: {self.name}.")

        while True:
            processor_info = {
                "associated_robot": os.environ["ROBOT_NAME"],
                "template_type": os.environ["TEMPLATE_TYPE"],
                "active": self.shared.processor_active.value,
                "id": self.container_id
            }
            self.publish(processor_info)
            time.sleep(1)
