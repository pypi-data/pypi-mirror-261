import asyncio
from typing import Dict, Any, Callable, Awaitable, Optional

from atb_lib import ColoredLogger, RabbitMqService


class RabbitMQCommunicator:

    def __init__(self,
                 config: Dict[str, Any],
                 logger: ColoredLogger,
                 callback: Optional[Callable[..., Awaitable[None]]] = None) -> None:

        self._logger = logger

        producer_config = config.get('rabbitmq_producer', {})
        consumer_config = config.get('rabbitmq_consumer', {})

        self._rabbitmq_producer_reconnect_interval_sec = producer_config.get('reconnect_interval_sec', None)
        self._rabbitmq_consumer_reconnect_interval_sec = consumer_config.get('reconnect_interval_sec', None)

        if producer_config:
            self._rabbitmq_producer = RabbitMqService(
                producer_config.get('url', ""),
                producer_config.get('queue_name', ""),
                int(producer_config.get('message_ttl_ms', 5000)),
                self._logger
            )

        if consumer_config and self._callback:
            self._rabbitmq_consumer = RabbitMqService(
                consumer_config.get('url', ""),
                consumer_config.get('queue_name', ""),
                int(consumer_config.get('message_ttl_ms', 5000)),
                self._logger,
                callback
            )
        elif consumer_config and not self._callback:
            raise ValueError("No callback specified")

    async def _callback(self):
        pass

    async def connect_rabbitmq_producer(self):
        while True:
            try:
                self._logger.info("Connecting to RabbitMQ producer...")
                await self._rabbitmq_producer.connect()
                break
            except Exception as e:
                self._logger.error(f"Error connecting to RabbitMQ producer: {e}")
                self._logger.info("Attempting to reconnect in a few seconds...")
                await asyncio.sleep(self._rabbitmq_producer_reconnect_interval_sec)

    async def connect_rabbitmq_consumer(self):
        while True:
            try:
                self._logger.info("Connecting to RabbitMQ consumer...")
                await self._rabbitmq_consumer.connect()
                break
            except Exception as e:
                self._logger.error(f"Error connecting to RabbitMQ consumer: {e}")
                self._logger.info("Attempting to reconnect in a few seconds...")
                await asyncio.sleep(self._rabbitmq_consumer_reconnect_interval_sec)

    async def send_message(self, message):
        while True:
            try:
                await self._rabbitmq_producer.send_message(message)
                break
            except Exception as e:
                self._logger.error(f"Error sending message to RabbitMQ: {e}")
                self._logger.info("Attempting to resend message in a few seconds...")
                await asyncio.sleep(self._rabbitmq_producer_reconnect_interval_sec)

    async def close(self):
        self._logger.info("Closing RabbitMQ producer...")
        try:
            await self._rabbitmq_producer.close()
        except Exception as e:
            self._logger.error(f"Error closing resource: {e}")
