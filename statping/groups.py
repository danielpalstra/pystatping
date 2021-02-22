from . import exceptions


class Groups(object):
    def __init__(self, connection):
        self.connection = connection

    def get_all_groups(self):

        return self.connection.get("groups")

    def create_group(self, group):

        response = self.connection.post("groups", group)
