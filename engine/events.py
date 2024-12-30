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
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(callback)

    def unsubscribe(self, event_type, callback):
        """
        Unsubscribes a listener from a specific event type.
        """
        if event_type in self.subscribers:
            self.subscribers[event_type].remove(callback)
            if not self.subscribers[event_type]:
                del self.subscribers[event_type]

    def publish(self, event):
        """
        Emits an event to all listeners subscribed to its type.
        """
        event_type = type(event)
        if event_type in self.subscribers:
            for callback in self.subscribers[event_type]:
                callback(event)
