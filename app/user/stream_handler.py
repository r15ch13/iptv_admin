from abc import ABC, abstractmethod


# handler for iptv
class IStreamHandler(ABC):
    @abstractmethod
    def on_stream_statistic_received(self, params: dict):
        pass

    @abstractmethod
    def on_stream_sources_changed(self, params: dict):
        pass