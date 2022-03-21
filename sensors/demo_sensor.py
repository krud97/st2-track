from st2reactor.sensor.base import PollingSensor
from ping3 import ping

class PingSensor(PollingSensor):
    def __init__(self, sensor_service, config=None, poll_interval=5) -> None:
        super(PingSensor, self).__init__(sensor_service=sensor_service,
                                    config=config,
                                    poll_interval=poll_interval
                                    )
        self._logger = self.sensor_service.get_logger(name=self.__class__.__name__)
        self._trigger_ref = 'str2track.demo_event'

    def setup(self):
        pass

    def poll(self):
        server = 'google.com'
        is_reachable = ping(server, size=1)
        self._logger.debug("Injecting Trigger instance...")
        self.sensor_service.dispatch(self._trigger_ref, is_reachable)

    def cleanup(self):
        pass

    def add_trigger(self):
        pass

    def update_trigger(self):
        pass

    def remove_trigger(self):
        pass
