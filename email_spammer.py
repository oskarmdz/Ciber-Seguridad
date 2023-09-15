import yagmail

email = "correo@gmail.com"
password = "contraseña_del_correo"

yag = yagmail.SMTP(user=email,password=password)


with open('list.txt','r+') as f:
    for l in f:
        destinatary = l
        print(destinatary)
        title = "Título del correo"
        html = "<p>Mensaje</p>"
        try:
            yag.send(destinatary,title,html)
        except:
            pass
