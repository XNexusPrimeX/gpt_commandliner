#!/usr/bin/env python3

import sys
from context import Context
import utils.logger as logger
from utils.cache_manager import CacheManager

argv = sys.argv
argv.pop(0)

match argv:
    case ["--clear" | "-c", *topic]:
        topic = ' '.join(topic)
        Context.create(topic)

    case ["--config", config, *args]:
        if config == "token":
            token = ''.join(args)

            if len(token) < 1:
                logger.error('token cannot be empty')
                exit()

            CacheManager.set("token", token)

    case [*message]:
        message = ' '.join(message)

        if(len(message) < 1):
            logger.error('what you doing broo?')
            exit()

        response = Context.use(message)

        print(response.content)