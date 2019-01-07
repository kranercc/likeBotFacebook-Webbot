from webbot import Browser 
from time import sleep
from selenium import webdriver

#kranetestaccountone pass kranetestaccount1
def firstLog(): #used for testing
    #prima data
    web.type('account' , into='email')
    web.type('pass' , into='password',id='pass')
    web.click("Log In")

user = ['user','pass','user','pass...etc the amount of accounts you have']

def secoundLog(): # used for debugging
    #dupaia te baga intr-un fel de check si tre sa bagi din nou
    web.type('kranetestaccountone',into='email',id='email')
    web.type('kranetestaccount1',into='pass',id='pass')
    web.click("Log In")
    sleep(1)

def pageToLike():
    #goto page to like
    web.go_to("https://www.facebook.com/kranezeul")
    sleep(3) #delay for notification
    web.click() # click to disable the notification thing
    web.scrolly(200)
    web.click("Like")
    #this sleep is for the human eye to see it being happend
    sleep(2)

def logOut():
    web.click(id='userNavigationLabel')
    web.click("Log Out") # end of the loop
    web.go_to('facebook.com/login')
    
def commentSection():
    pass
#the comment feature and page like are for sale
#the automated creation of accounts feature is for sale
# @ kranehecaru@gmail.com


#first authentification error
def authentification():
    pass
#first log 
#firstLog()
#then iterete thruw the lists
userx = 0
password = 1
while True:
    web = Browser()
    web.go_to('facebook.com/login') 
    web.type(user[userx] , into='email')
    web.type(user[password] , into='password',id='pass')
    web.click("Log In")
    pageToLike()
    #logOut()
    #logout or new instance
    web.close_current_tag()
    password +=2
    userx +=2
    if userx == len(user):
        break

# @ kranehecaru@gmail.com