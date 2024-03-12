import asyncio
from typing import Dict, Any, Callable, Awaitable, Optional
import aio_pika
from atb_lib import ColoredLogger, RabbitMqService

_DEFAULT_TTL_MS = 5000
_DEFAULT_RECONNECT_SEC = 5


class RabbitMQCommunicator:
    def __init__(self,
                 config: Dict[str, Any],
                 logger: ColoredLogger,
                 callback: Optional[Callable[..., Awaitable[None]]] = None) -> None:
        self._logger = logger
        self._rabbitmq_producer = None
        self._rabbitmq_consumer = None
        producer_config = config.get('rabbitmq_producer', {})
        consumer_config = config.get('rabbitmq_consumer', {})
        self._producer_reconnect_interval_sec = producer_config.get('reconnect_interval_sec', _DEFAULT_RECONNECT_SEC)
        self._consumer_reconnect_interval_sec = consumer_config.get('reconnect_interval_sec', _DEFAULT_RECONNECT_SEC)
        if producer_config:
            self._rabbitmq_producer = RabbitMqService(
                producer_config.get('url', ""),
                producer_config.get('queue_name', ""),
                int(producer_config.get('message_ttl_ms', _DEFAULT_TTL_MS)),
                self._logger
            )
        if consumer_config and callback:
            self._rabbitmq_consumer = RabbitMqService(
                consumer_config.get('url', ""),
                consumer_config.get('queue_name', ""),
                int(consumer_config.get('message_ttl_ms', _DEFAULT_TTL_MS)),
                self._logger,
                callback
            )
        elif consumer_config and not callback:
            raise ValueError("No callback specified")

    async def attempt_with_retry(self, func: Callable[[], Awaitable[None]],
                                 action_desc: str, interval_sec: int,
                                 reconnect_func: Callable[[], Awaitable[None]] = None) -> None:
        while True:
            try:
                await func()
                break
            except aio_pika.exceptions.AMQPError as e:
                # If it's a recoverable networking error, attempt to reconnect before retrying
                self._logger.error(f"Recoverable networking error during {action_desc}: {e}")
                if reconnect_func is not None:
                    await reconnect_func()
                self._logger.info(f"Attempting to retry {action_desc} in few seconds...")
                await asyncio.sleep(interval_sec)
            except Exception as e:
                # For other errors, just retry
                self._logger.error(f"Error during {action_desc}: {e}")
                self._logger.info(f"Attempting to retry {action_desc} in few seconds...")
                await asyncio.sleep(interval_sec)

    async def send_message(self, message):
        await self.attempt_with_retry(lambda: self._rabbitmq_producer.send_message(message), "send message to RabbitMQ",
                                      self._producer_reconnect_interval_sec, lambda: self._rabbitmq_producer.connect())

    async def receive_messages(self):
        await self.attempt_with_retry(lambda: self._rabbitmq_consumer.receive_messages(),
                                      "start receiving messages from RabbitMQ", self._consumer_reconnect_interval_sec,
                                      lambda: self._rabbitmq_consumer.connect())

    async def connect_rabbitmq_producer(self):
        await self.attempt_with_retry(self._rabbitmq_producer.connect,
                                      "connect to RabbitMQ producer",
                                      self._producer_reconnect_interval_sec)

    async def connect_rabbitmq_consumer(self):
        await self.attempt_with_retry(self._rabbitmq_consumer.connect,
                                      "connect to RabbitMQ consumer",
                                      self._consumer_reconnect_interval_sec)

    async def close(self):
        self._logger.info("Closing RabbitMQ producer...")
        try:
            await self._rabbitmq_producer.close()
        except Exception as e:
            self._logger.error(f"Error closing resource: {e}")
