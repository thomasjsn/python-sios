class Watcher:
    def __init__(self, topic, client):
        self.value = None
        self.topic = topic
        self.client = client

    def set_value(self, new_value):
        if self.value != new_value:
            self.value = new_value
            self.change()

    def change(self):
        print('change: {} to {}'.format(self.topic, self.value))
        self.client.publish(self.topic, self.value)
