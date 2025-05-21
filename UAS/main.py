import questionary
from fitur.auth import login, register

def auth_menu():
  choice = questionary.select(
    "pilih opsi: ",
    choices=[
      "Login",
      "Register",
      "Keluar"
    ]).ask()
  
  if choice == "Login":
    return login()
  elif choice == "Register":
    return register()
  else:
    return 'Anda Memilih keluar!'