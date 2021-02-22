from . import exceptions


class Messages(object):
    def __init__(self, connection):
        self.connection = connection

    def get_all_messages(self):
        path = "messages"
        response = self.connection.get(path)

        return response

    def create_message(self, message):

        path = "messages"
        response = self.connection.post(path, message)

        return response

    def update_message(self, message_id, message):

        path = "messages"
        response = self.connection.post(path, message)

        return response

    def delete_message(self, message_id):

        path = f"messages/{message_id}"
        response = self.connection.delete(path)

        return response
