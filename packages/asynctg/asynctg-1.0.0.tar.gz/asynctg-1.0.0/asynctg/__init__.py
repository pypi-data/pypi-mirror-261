#!/bin/env python3

__version__ = '1.3.5'
VERSION = __version__

__all__ = (
    'Client',
    'NextFunction',
    'TelegramError',
)
from .client import (
    logger,
    Client,
    NextFunction,
    TelegramError,
)
