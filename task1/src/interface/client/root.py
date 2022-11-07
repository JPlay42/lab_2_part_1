from datetime import datetime

from task1.src.interface.interface import Interface
from task1.src.storage import TicketsRepository, EventsRepository
from task1.src.storage.entities.ticket import Ticket


class RootClientInterface(Interface):
    __tickets_repo = TicketsRepository()
    __events_repo = EventsRepository()

    def run(self):
        print('Which action should you do?')
        print('1) Create a ticket with custom ID')
        print('2) Show the price of ticket with specified ID')
        print('3) Print a ticket with specified ID')
        choice = super()._input_options(3)
        match choice:
            case 1:
                self.__create()
            case 2:
                self.__show_price()
            case 3:
                self.__print_ticket()

    def __create(self):
        name = input('Name: ')
        print('Available events: ')
        all_events = self.__events_repo.read_all()
        available_event_ids = list()
        for event in all_events.values():
            if event.is_in_the_future():
                available_event_ids.append(event.id)
                print(f'{event.id}: {event.name}, {event.price} USD')
        event_id = int(input('Event ID: '))
        if event_id not in available_event_ids:
            print('No such event')
            return
        event = all_events[event_id]
        ticket_id = self.__get_ticket_id()
        is_student = super()._get_boolean(input('Are you student? (yes/no): '))
        ticket = Ticket.of(
            ticket_id,
            event,
            name,
            datetime.now(),
            is_student
        )
        self.__tickets_repo.create(ticket)
        print(f'Ticket\'s price: {ticket.price()}')

    def __show_price(self):
        ticket = self.__tickets_repo.read(self.__get_ticket_id())
        if ticket is not None:
            print(f'Ticket\'s price: {ticket.price()}')
        else:
            print('No such ticket')

    def __print_ticket(self):
        print(self.__tickets_repo.read(self.__get_ticket_id()))

    @staticmethod
    def __get_ticket_id():
        return int(input('Ticket ID: '))
