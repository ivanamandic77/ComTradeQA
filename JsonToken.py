import requests

def testLogin(email, password):
    requestData={
        "email":email,
        "password":password
    }
    response=requests.post("https://comtradeqa.herokuapp.com/api/users/login",requestData)
    print(response.status_code)
    if(response.status_code==200):
        print("Uspesno ste se ulogovali!")
        responseData=response.json()
        print(responseData)
        print("Auth Token is",responseData["token"])
    else:
        print("Neuspesno logovanje!")

email=input("Unesite email:")
password=input("Unesite sifru:")
testLogin(email,password)
