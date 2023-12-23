class Publication:
    def __init__(self, title, author, year, publishing_house):
        self.title = title
        self.author = author
        self.year = year
        self.publishing_house = publishing_house
    def main(self):
        print(self.publishing_house)
    def display(self):
        print(self.title, self.author, self.year)

class Book(Publication):
    def __init__(self, title, author, year, publishing_house, isbn):
        super().__init__(title, author, year, publishing_house)
        self.isbn = isbn
    def main(self):
        super().main()
    def display(self):
        super().display()
        print(self.isbn)   

class Magazine(Publication):
    def __init__(self, title, author, year, publishing_house, issue_number):
        super().__init__(title, author, year, publishing_house)
        self.issue_number = issue_number
    def main(self):
        super().main()
    def display(self):
        super().display()
        print(self.issue_number)   
    
warcraft = Publication('Rise of the Horde', 'Christie Golden', 2006, 'АСТ')
warcraft.main()
warcraft.display()
warcraft = Book('Rise of the Horde', 'Christie Golden', 2006, 'АСТ', 'isbn')
warcraft.main()
warcraft.display()
warcraft = Magazine('Rise of the Horde', 'Christie Golden', 2006, 'АСТ', 30)
warcraft.main()
warcraft.display()
