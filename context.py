import os
import json
import openai
from utils.cache_manager import CacheManager

CACHE_FILENAME = ".cache"

class Context:
    @staticmethod
    def create(topic: str):
        if not os.path.exists(CACHE_FILENAME):
            with open(CACHE_FILENAME, 'w') as f:
                f.write('{ "token": "", "topic": "", "msgs": [] }')

        with open(CACHE_FILENAME, 'r') as f:
            data = json.load(f)
             
        data["topic"] = topic
        data["msgs"] = []

        with open(CACHE_FILENAME, 'w') as f:
            json.dump(data, f)

    @staticmethod
    def use(msg):
        openai.api_key = CacheManager.get('token', errMsg="invalid token")

        msgs = CacheManager.get('msgs') or []
        msgs.append({ "role": "user", "content": msg })

        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=msgs
        )

        resMsg = res.choices[0].message
        msgs.append(resMsg)

        CacheManager.set('msgs', msgs)

        return resMsg
                