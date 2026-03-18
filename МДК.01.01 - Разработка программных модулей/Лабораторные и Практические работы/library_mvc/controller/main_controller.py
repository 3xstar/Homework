from controller.book_controller import BookController
from view.books_view import BooksView

class MainController:
    def __init__(self, book_controller: BookController, main_view: BooksView):
        self.book_controller = book_controller
        self.view = main_view

    def run(self):
        while True:
            choice = self.view.show_main_menu()
            
            if choice == '1':
                self.book_controller.show_all()
            elif choice == '2':
                self.book_controller.search()
            elif choice == '3':
                self.book_controller.add()
            elif choice == '4':
                self.book_controller.edit()
            elif choice == '5':
                self.book_controller.delete()
            elif choice == '6':
                self.book_controller.toggle_status()
            elif choice == '7':
                self.book_controller.show_stats()
            elif choice == '8':
                self.view.show_header("Выход")
                print("\n👋 До свидания!")
                break
            else:
                self.view.show_message("Неверный выбор", False)
            
            if choice != '8':
                self.view.wait_for_enter()