import aio_pika
from hydromill.message.message import Message

TRACEPARENT = "traceparent"


class Marshaler:
    def __init__(
        self,
        not_persistent_delivery_mode: bool = False,
    ):
        self.not_persistent_delivery_mode = not_persistent_delivery_mode

    def marshal(self, msg: Message) -> aio_pika.Message:
        """ """
        publishing = aio_pika.Message(
            body=msg.payload,
            headers=msg.metadata,
        )

        if not self.not_persistent_delivery_mode:
            publishing.delivery_mode = aio_pika.DeliveryMode.PERSISTENT

        self.postprocess_publishing(publishing)

        return publishing

    def unmarshal(self, msg: aio_pika.IncomingMessage) -> Message:
        """ """
        message = Message(
            metadata=msg.body,
            payload=msg.headers,
        )

        return message

    def postprocess_publishing(
        self,
        publishing: aio_pika.Message,
    ) -> aio_pika.Message:
        """ """
        try:
            import elasticapm
        except ModuleNotFoundError:
            return publishing

        if TRACEPARENT not in publishing.headers:
            traceparent = elasticapm.get_trace_parent_header()
            if traceparent is not None:
                publishing.headers[TRACEPARENT] = traceparent

        return publishing
