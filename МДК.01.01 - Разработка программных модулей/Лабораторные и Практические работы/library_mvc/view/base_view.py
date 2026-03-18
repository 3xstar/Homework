import os

class BaseView:
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_header(self, title: str):
        print("\n" + "=" * 50)
        print(f"  {title} ")
        print("=" * 50)

    def show_message(self, message: str, success: bool = True):
        icon = "✅" if success else "❌"
        print(f"\n{icon} {message}")

    def confirm(self, message: str) -> bool:
        response = input(f"{message} (y/n): ").strip().lower()
        return response in ('y', 'yes', 'д', 'да')
    
    def wait_for_enter(self):
        input("\nНажмите Enter для продолжения...")