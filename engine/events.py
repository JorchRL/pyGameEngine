class Event:
    """
    Base class for all events.
    Represents a message that can be emitted by scenes or game components and processed by the FSM.
    """
    pass


class EventDispatcher:
    """
    Mediator class for managing event-based communication.
    - Allows scenes and engine components to publish events.
    - FSM subscribes to these events and takes action when required.
    """

    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event_type, callback):
        """
        Subscribes a listener (callback function) to a specific event type.
        """
        pass

    def unsubscribe(self, event_type, callback):
        """
        Unsubscribes a listener from a specific event type.
        """
        pass

    def publish(self, event):
        """
        Emits an event to all listeners subscribed to its type.
        """
        pass
