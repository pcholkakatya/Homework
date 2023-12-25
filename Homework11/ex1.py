class Publication:
    def __init__(self, title, author, year, publishing_house):
        self.title = title
        self.author = author
        self.year = year
        self.publishing_house = publishing_house
    def main(self):
        print(f'Издательство: {self.publishing_house}')
    def display(self):
        print(f'Название: {self.title}\nАвтор: {self.author}\nГод выпуска: {self.year}')
              
class Book(Publication):
    def __init__(self, title, author, year, publishing_house, isbn):
        super().__init__(title, author, year, publishing_house)
        self.isbn = isbn
    def main(self):
        super().main()
    def display(self):
        super().display()
        print(f'ISBN: {self.isbn}')   

class Magazine(Publication):
    def __init__(self, title, author, year, publishing_house, issue_number):
        super().__init__(title, author, year, publishing_house)
        self.issue_number = issue_number
    def main(self):
        super().main()
    def display(self):
        super().display()
        print(f'Номер выпуска: {self.issue_number}')   
    
warcraft = Book('Rise of the Horde', 'Christie Golden', 2006, 'ACT', 9780989700139)
warcraft.main()
warcraft.display()
warcraft = Magazine('Scooby-Doo', 'Mark Evanier', 1969, 'Gold Key Comics', 10)
warcraft.main()
warcraft.display()
