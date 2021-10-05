from rembrain_robot_framework import RobotProcess


# todo it must not be in this library!
# todo replace and remove
class AmqpWorker(RobotProcess):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.shared.update_config.value = False

    def run(self):
        self.log.info(f"{self.__class__.__name__} started, name: {self.name}.")

        while True:
            # it receive decoded data!
            command = self.consume()

            if command["message"] == "update_config":
                self.shared.update_config.value = True
            else:
                self.log.warning(f"Unprocessed command received: {command}")
