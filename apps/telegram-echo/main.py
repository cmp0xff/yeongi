import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    logger.info("Hello from telegram-echo!")


if __name__ == "__main__":
    main()
