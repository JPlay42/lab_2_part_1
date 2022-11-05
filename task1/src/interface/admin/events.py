from task1.src.interface.interface import Interface


class EventsAdminInterface(Interface):
    def run(self):
        print('Select an action: ')
        print('1) Create new event with auto-generated ID')
        print('2) Create new event with custom ID')
        print('3) Read event by ID')
        print('4) Read all events')
        print('5) Update existing event')
        print('6) Delete event')

    def create(self):
        pass

    def create_with_id(self):
        pass

    def read(self):
        pass

    def read_all(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
