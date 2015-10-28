import socket
hostname = socket.gethostname().split('.')[0]


config = {
    # Consumer stuff
    "bugyou.consumer.enabled":True,
    # Turn on logging for bugfiler
    "logging": dict(
        loggers=dict(
            bugyou={
                "level": "DEBUG",
                "propagate": False,
                "handlers": ["console"],
            },
        ),
    ),
}
