from task1.src.interface.admin.events import EventsAdminInterface
from task1.src.interface.admin.tickets import TicketsAdminInterface
from task1.src.interface.interface import Interface


class RootAdminInterface(Interface):
    def run(self):
        print('Which entities should you work with?')
        print('1) Events')
        print('2) Tickets')
        match self._input_options(2):
            case 1:
                EventsAdminInterface().run()
            case 2:
                TicketsAdminInterface().run()
