##first of all create a gmail account for your raspberry PI
import yagmail ## install this library using pip install yagmail
password = "" ## declare empty pass string
with open("/home/raspberry/password/pass","r") as f: ## store the pi gmail's pass in the folder written
    password=f.read() ## Read the password 
yag=yagmail.SMTP('raspaazhmeer@gmail.com',password) ## initialize the module by typing email and password of gmail
yag.send(to= 'aazhmeerchhapra@gmail.com', ## fill out the contents of the email
         subject='sending email using python',
         contents="ki haal chaaal ne tik ho naaaaa????",
         attachments="/home/raspberry/Downloads/evai.jpg"
         )
print("Email-sent")
    