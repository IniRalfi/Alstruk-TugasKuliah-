import questionary 
from fitur.auth import login, register
from admin import menu_admin
from user import menu_user
from database.akun import load_akun, simpan_akun

def main():
  while True:
        # Menu utama
        main_choice = questionary.select(
            "Selamat datang di Pertafli!",
            choices=[
                {"name": "📲 Login", "value": "login"},
                {"name": "📝 Register", "value": "register"},
                {"name": "❌ Keluar", "value": "exit"}
            ]
        ).ask()

        if main_choice == "login":
            user_data = login()
            if user_data:
                if user_data["role"] == "admin":
                    menu_admin(user_data["username"])
                else:
                    menu_user(user_data["username"])
            
        elif main_choice == "register":
            register()
            
        elif main_choice == "exit":
            print("Terima kasih telah menggunakan Pertafli!")
            break

if __name__ == "__main__":
    main()