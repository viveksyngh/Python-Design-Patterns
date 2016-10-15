
class EventManager(object):

    def __init__(self):
        print "Event Manager: ", "Let me talk to the folks!.\n"

    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.book_hotel()

        self.florist = Florist()
        self.florist.set_flower_requirements()

        self.caterer = Caterer()
        self.caterer.set_cuisine()

        self.musician = Musician()
        self.musician.set_music_type()


class Hotelier(object):

    def __init__(self):
        print "Arranging the hotel for marriage? --"

    def __is_available(self):
        print "Is the hotel free for event on given day?"
        return True

    def book_hotel(self):
        if self.__is_available():
            print "Registered the booking\n\n"


class Florist(object):

    def __init__(self):
        print "Flower decorations for the event? --"

    def set_flower_requirements(self):
        print "Roses and Lillies would be used for decorations \n\n"


class Caterer(object):

    def __init__(self):
        print "Food arrangement for the events --"

    def set_cuisine(self):
        print "Chinese and continental cuisine to be served.\n\n"


class Musician(object):

    def __init__(self):
        print "Musical arrangement for the marriage -- "

    def set_music_type(self):
        print "Jazz and classical will be played\n\n"


class You(object):

    def __init__(self):
        print "Marrige arrangement ? !!!"

    def ask_event_manager(self):
        em = EventManager()
        em.arrange()

    def __del__(self):
        print "Thanks to the event manager. All preprations done."


you = You()
you.ask_event_manager()


# Marrige arrangement ? !!!
# Event Manager:  Let me talk to the folks!.

# Arranging the hotel for marriage? --
# Is the hotel free for event on given day?
# Registered the booking


# Flower decorations for the event? --
# Roses and Lillies would be used for decorations 


# Food arrangement for the events --
# Chinese and continental cuisine to be served.


# Musical arrangement for the marriage -- 
# Jazz and classical will be played


# Thanks to the event manager. All preprations done.