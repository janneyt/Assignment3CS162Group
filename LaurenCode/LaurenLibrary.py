# author: Lauren Pigue
# date: 01/16/2021
# description: Assignment 3 - Write library simulating code


class LibraryItem:
    """Parent class which defines a Library Item Object; Child class: Book, Album and Movie classes inherits from this class"""

    def __init__(self, item_ID, item_title):
        """Init method for LibraryItem class"""
        self._item_ID = item_ID
        self._item_title = item_title
        self._checked_out_by = None
        self._requested_by = None
        self._location = "ON_SHELF"
        self._date_checked_out = None

    def get_item_ID(self):
        """Getter method for library item ID"""
        return self._item_ID

    def get_item_title(self):
        """Getter method for Library item title"""
        return self._item_title

    def get_checked_out_by(self):
        """Getter method for LibraryItem location"""
        return self._checked_out_by

    def get_requested_by(self):
        """Getter method for returning who requested the item"""
        return self._requested_by

    def get_location(self):
        """Getter method for location status of library item"""
        return self._location

    def get_date_checked_out(self):
        """Getter method for location status of library item"""
        return self._date_checked_out

    def set_checked_out_by(self, checked_out_member_info):
        """Setter method to set who has checked out an item, linked to member information"""
        self._checked_out_by = checked_out_member_info

    def set_date_checked_out(self, checkout_date):
        """Setter method to set the check out date to the current_date in library class"""
        self._date_checked_out = checkout_date


    def set_item_ID(self, item_ID):
        """Setter method to set the item ID"""
        self._item_ID = item_ID

    def set_item_title(self, item_title):
        """Setter method to set the item title"""
        self._item_ID = item_title

    def set_location(self, location):
        """Setter method to set who has checked out a certain item"""
        self._location = location

    def set_requested_by(self, requested_member_info):
        """Setter method to set who has requested a library item"""
        self._requested_by = requested_member_info
        return True


class Book(LibraryItem):
    """Child 'Book' class inherits from LibraryItem class"""

    def __init__(self, item_ID, item_title, author):
        """Init method for Book child class"""
        super().__init__(item_ID, item_title)
        self._author = author
        self._book_check_out_length = 21

    def get_author(self):
        """Getter method for author attribute in Book class"""
        return self._author

    def set_author(self, new_author):
        """Setter method for Author of a book in the library"""
        self._author = new_author

    def get_check_out_length(self):
        """Getter method for checkout length of book"""
        return self._book_check_out_length


class Album(LibraryItem):
    """Child 'Album' class inherits from LibraryItem class"""

    def __init__(self, item_ID, item_title, artist):
        """Init method for Album child class"""
        super().__init__(item_ID, item_title)
        self._artist = artist
        self._album_check_out_length = 14

    def get_artist(self):
        """Getter method for artist attribute in Album class"""
        return self._artist

    def set_artist(self, new_artist):
        """Setter method to set an album artist"""
        self._artist = new_artist

    def get_check_out_length(self):
        """Getter method for checkout length for Albums"""
        return self._album_check_out_length


class Movie(LibraryItem):
    """Child 'Movie' class inherits from LibaryItem class"""

    def __init__(self, item_ID, item_title, director):
        """Init method for Movie child class"""
        super().__init__(item_ID, item_title)
        self._director = director
        self._movie_check_out_length = 7

    def get_director(self):
        """Getter method for director attribute in Album class"""
        return self._director

    def set_director(self, new_director):
        """Setter method to set the director of a Movie"""
        self._director = new_director

    def get_check_out_length(self):
        """Getter method for checkout length for Movies"""
        return self._movie_check_out_length


class Patron:
    """Class defined to create a Patron object"""

    def __init__(self, patron_ID, patron_name):
        """Init method for Patron class"""
        self._patron_ID = patron_ID
        self._patron_name = patron_name
        self._checked_out_items = []
        self._fine_amount = 0.0

    def get_fine_amount(self):
        """Getter method for fine amount on patron's account"""
        return self._fine_amount

    def get_patron_ID(self):
        """Getter method for patron's ID"""
        return self._patron_ID

    def get_patron_name(self):
        """Getter method for patron's ID"""
        return self._patron_name

    def get_checked_out_items(self):
        """Getter method for collection of a patron's checked out items"""
        return self._checked_out_items

    def set_fine_amount(self, new_fine_amount):
        """Setter method for the fine amount on a patron's account"""
        self._fine_amount = new_fine_amount

    def set_patron_ID(self, new_patron_ID):
        """Setter method for patron's ID"""
        self._patron_ID = new_patron_ID

    def set_patron_name(self, new_patron_ID):
        """Setter method for patron's ID"""
        self._patron_name = new_patron_ID

    def set_checked_out_items(self, new_checked_out_items_list):
        """Setter method for collection of a patron's checked out items"""
        self._checked_out_items = new_checked_out_items_list

    def add_library_item(self, add_library_item):
        """Method adds a specified LibraryItem to checked_out_items"""
        self._checked_out_items.append(add_library_item)

    def remove_library_item(self, remove_library_item):
        """Method removes specified LibraryItem from checked_out_items"""
        self._checked_out_items.remove(remove_library_item)

    def amend_fine(self, amended_fine):
        """Method to amend the fine on a Patron's account"""
        self._fine_amount += amended_fine


class Library:
    """Class represents Library object through which necessary operations occur"""

    def __init__(self):
        """Init method for Library class object"""
        self._current_date = 0
        self._holdings = []
        self._members = []

    def get_current_date(self):
        """Getter method for current date"""
        return self._current_date

    def get_holdings(self):
        """Getter method for collection of holdings"""
        return self._holdings

    def get_members(self):
        """Getter method for collection of members"""
        return self._current_date

    def set_current_date(self, new_date):
        """Setter method for current date"""
        self._current_date = new_date

    def set_holdings(self, new_holdings_list):
        """Setter method for collection of holdings"""
        self._holdings = new_holdings_list

    def set_members(self, new_members_list):
        """Setter method for collection of members"""
        self._current_date = new_members_list

    def add_library_item(self, new_library_item):
        """Adds new library item to collection of library holdings"""
        self._holdings.append(new_library_item)

    def add_patron(self, new_patron):
        """Adds a new patron to the collection of Library members"""
        self._members.append(new_patron)

    def get_library_item_from_id(self, item_ID):
        """Getter method returns LibraryItem object corresponding to the ID parameter"""
        for item in self._holdings:
            if item.get_item_ID() is item_ID:
                return item
        return None

    def get_patron_from_id(self, patron_ID):
        """Getter method returns Patron object corresponding to the ID parameter"""
        for patron in self._members:
            if patron.get_patron_ID() is patron_ID:
                return patron
        return None

    def check_out_library_item(self, patron_ID, item_ID):
        """Method for Patron to check out library item"""
        patron = self.get_patron_from_id(patron_ID)
        if patron is None:
            return "patron not found"
        item = self.get_library_item_from_id(item_ID)
        if item is None:
            return "item not found"
        if item.get_checked_out_by() != None:
            return "item already checked out"
        if item.get_requested_by() != None and patron != item.get_requested_by():
            return "item on hold by other patron"
        else:
            item.set_checked_out_by(patron)
            item.set_date_checked_out(self._current_date)
            item.set_location("CHECKED_OUT")
        if item.get_requested_by() is patron:
            item.set_requested_by(None)
        patron.add_library_item(item)
        return "checkout successful"

    def return_library_item(self, item_ID):
        """Method for Patron to return a library item"""
        item = self.get_library_item_from_id(item_ID)
        if item is None:
            return "item not found"
        if item.get_checked_out_by() is None:
            return "item already in library"
        item.get_checked_out_by().remove_library_item(item)
        if item.get_requested_by() is not None:
            item.set_location("ON_HOLD_SHELF")
        else:
            item.set_location("ON_SHELF")
        item.set_checked_out_by(None)
        return "return successful"

    def request_library_item(self, patron_ID, item_ID):
        """Method for Patron to request a library item"""
        patron = self.get_patron_from_id(patron_ID)
        item = self.get_library_item_from_id(item_ID)
        if patron is None:
            return "patron not found"
        if item is None:
            return "item not found"
        if item.get_requested_by() is not None:
            return "item already on hold"
        if item.get_location() == "ON_SHELF":
            item.set_location("ON_HOLD_SHELF")
        return "request successful"

    def pay_fine(self, patron_ID, fine_payment):
        """Method for Patron to pay library fine"""
        patron = self.get_patron_from_id(patron_ID)
        if patron is None:
            return "patron not found"
        patron.amend_fine(-fine_payment)
        return "payment successful"

    def increment_current_date(self):
        """Method increments length of time an item has been checked out and manages Patron's fine total"""
        self._current_date += 1
        for patron in self._members:
            for item in patron.get_checked_out_items():
                date_tracker = self._current_date - item.get_date_checked_out()
                if item.get_check_out_length() < date_tracker:
                    patron.amend_fine(.10)

def main():




    b1 = Book("345", "Phantom Tollbooth", "Juster")
    a1 = Album("456", "...And His Orchestra", "The Fastbacks")
    m1 = Movie("567", "Laputa", "Miyazaki")
    print(b1.get_author())
    print(a1.get_artist())
    print(m1.get_director())
    print(b1.get_location())

    p1 = Patron("abc", "Felicity")
    p2 = Patron("bcd", "Waldo")

    lib = Library()
    lib.add_library_item(b1)
    lib.add_library_item(a1)
    lib.add_patron(p1)
    lib.add_patron(p2)
    lib.request_library_item(p2.get_patron_ID(),b1.get_item_ID())

    lib.check_out_library_item("bcd", "456")
    loc = a1.get_location()
    lib.request_library_item("abc", "456")
    for i in range(57):
        lib.increment_current_date()  # 57 days pass
    p2_fine = p2.get_fine_amount()
    lib.pay_fine("bcd", p2_fine)
    lib.return_library_item("456")


if __name__ == "__main__":
    main()

