import pprint
import requests
from tensorfuse_python.testing.constants import webhook, passthrough, python


class Processor:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def preprocess(self, data):
        raise NotImplementedError


class WebhookProcessor(Processor):
    def __init__(self, url, name):
        self.url = url
        super().__init__(name=name, type=webhook)

    def process(self, data):
        output = requests.post(self.url, json=data)
        # pprint.pprint(output)
        return output.json()


class PassthroughProcessor(Processor):
    def __init__(self, name):
        super().__init__(name=name, type=passthrough)

    def process(self, data):
        return data
    

class PythonProcessor(Processor):
    def __init__(self, function, name):
        self.function = function
        super().__init__(name=name, type=python)


    def process(self, data):
        output = self.function(data)
        # pprint.pprint("PythonProcessor Output: {}".format(output))
        return output


def get_processor(processor_type, config):
    name = config.get('name', None)
    if processor_type == webhook:
        if 'url' in config:
            url = config['url']
        else:
            raise ValueError('url is required for webhook preprocessor')
        return WebhookProcessor(url=url, name=name)
    elif processor_type == passthrough:
        return PassthroughProcessor(name=name)
    elif processor_type == python:
        return PythonProcessor(function=config['value'], name=name)
    else:
        raise NotImplementedError
