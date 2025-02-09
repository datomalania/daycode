#user & pass
import getpass

stored_un = "admin"
stored_pass = "123"

usern = input("შეიყვანე მომხმარებლის სახელი: ")
#გაითვალისწინეთ, ლინუქსიში პაროლის აკრეფისას სომბოლოები არ გამოისახება.
uspass = getpass.getpass("შეიყვანე პაროლი: ")

if usern == stored_un and uspass == stored_pass:
    print("სალამი, თქვენ გელოდებოდით!")
else:
    print("ბოდიში. სახელი ან პაროლი ხომ არ გეშლებათ?")
    
