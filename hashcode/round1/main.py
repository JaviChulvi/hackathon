import sys

class Library:
    books = []
    signup_days = 0
    rate = 0
    books_used = []

    def __init__(self, books, signup_days, rate):
        self.books = books
        self.signup_days = signup_days
        self.rate = rate

    def read(self, used, ordered_books):
        print(ordered_books)
        print(used)
        books_left = self.calculate_books_left(used)
        score = -1
        reading = 0
        for book in ordered_books:
            if book.id in books_left and book.id not in used:
                used.append(book.id)
                books_left = self.calculate_books_left(used)
                print("LIBRO USADO: ", book.id)
                score += book.score
                reading += 1
                self.books_used.append(book)
            if reading == self.rate or len(self.calculate_books_left(used)) == 0:
                break
            print(score)
        return score, used

    def calculate_books_left(self, used):
        books_left = []
        for id in self.books:
            if id not in used:
                books_left.append(id)
        return books_left

    def score(self, used, scores, days_left):
        score = 0
        days_left -= self.signup_days

        if days_left > 0:
            books_left = self.calculate_books_left(used)

            books_available = days_left * self.rate
            

            if len(books_left) < books_available:
                books_available = len(books_left)

            cont = 0
            for i in books_left:
                if cont <= books_available:
                    score += scores[i]
                    cont+=1
                else:
                    break
          
        return score

class Book:
    id = 0
    score = 0
    def __init__(self, id, score):
        self.id = id
        self.score = score

def read_input(input_file):
    with open(input_file) as f:
        first_line = f.readline().split(' ')

        n_books = int(first_line[0])
        n_libraries = int(first_line[1])
        days = int(first_line[2])

        second_line = f.readline().split(' ')
        scores_books = [int(i) for i in second_line]
        
        # Crear objetos libro
        books = []
        cont = 0
        for score in scores_books:
            book = Book(cont, score)
            books.append(book)
        #print(books)
        dic_libraries = {}
        #print(n_books, n_libraries, days, scores_books.sort())
        for i in range(n_libraries):
            library_info = f.readline().split(' ')
            library_books = int(library_info[0])

            signup_process = int(library_info[1])
            shipbooks_day = int(library_info[2])

            library_books = f.readline().split(' ')
            books_library = [int(i) for i in library_books]
            library = Library(books_library, signup_process, shipbooks_day)
            dic_libraries[i] = library

    return n_books, n_libraries, days, books, dic_libraries
    
def get_best_library(days, used, scores, remaining_libraries):
    max = 0
    id = -1
    for i in remaining_libraries:
        value = dic_libraries[i].score(used, scores, days)
        if value > max:
            max = value
            id = i
    return id

def getBookScore(book):
    return book.score

def write_output(input_file):
    f = open(input_file[:-3]+'out',"w")
    f.write("almenos lo hemos intentado, que eso es lo que cuenta. apache y pa casa. look a pair of boobs --> (·Y·)")
    f.close()
    

if __name__ == '__main__':
    input_file = sys.argv[1]
    write_output(input_file)
    n_books, n_libraries, days, books, dic_libraries = read_input(input_file)
    scores = [i.score for i in books]
    print(books)
    ordered_books = books
    ordered_books.sort(key = getBookScore, reverse = True)
    print(ordered_books)
    scores_libraries = []
    #for i in range(n_libraries):
    #    value = dic_libraries[i].score(used, scores, days)
    #    scores_libraries.append(value)

    d = 0
    signin_library = None

    remaining_libraries = [i for i in range(n_libraries)]
    working_libraries = []
    finished_libraries = []
    used = [] # lista ids de libro


    total_score = 0
    for day in range(days):

        days_left = days-day
        print("DAY: ", day)
        #print("books used :", used)
        if d == 0:
            if signin_library is not None:
                working_libraries.append(signin_library)
            best_library = get_best_library(days_left, used, scores, remaining_libraries)
            if best_library >= 0:
                signin_library = dic_libraries[best_library]
                d = signin_library.signup_days
        else:
            d -= 1
        # a leer libro capullo

        for working in working_libraries:
            score, used = working.read(used, ordered_books)
            print(score)         
            if score > 0:
                total_score += score
            else:
                finished_libraries.append(working)
                working_libraries.remove(working)
        

        print("TOTAL SCORE: ", total_score)
        for finished in finished_libraries:
            print(finished.books_used)
        