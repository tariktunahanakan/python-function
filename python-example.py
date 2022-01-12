import os
from typing import Text
fileNumber = int(input("Olusturmak Istedıgınız Dosya Sayisi: "))
    


filePath= str(input("Dosya Yolunu Yazınız: "))
def remove_file():
    for i in range(fileNumber):
        os.remove("Deneme-"+ str(i+1))
        print("Deneme "+ str(i+1),"Silindi")
def create_file():

    print("Dosya Şu Konuma Olusturulucak",filePath)
    os.chdir(filePath)

    for i in range(fileNumber):
        open("Deneme-"+ str(i+1),"w")
        print("Deneme "+ str(i+1),"Olusturuldu")
        
 

create_file()


def write_funciton():
    for i in range(fileNumber):
        os.chdir(filePath)
        with open("Deneme-"+ str(i+1),"w") as f:
            f.write("Deneme-"+ str(i+1)+" yazıldı")                        
            print("Deneme-"+ str(i+1)+"basarıyla yazıldı")
        f.close()
        
def read_function():
    for i in range(fileNumber):
        os.chdir(filePath)
        # os.open()
        # for i in os.listdir("Deneme-"+ str(i+1),"w"):
            # print(i)

        with open("Deneme-"+ str(i+1),"r") as f:
            # f.read("Deneme-"+ str(i+1))
            f.read("Deneme-"+ str(i+1))
            print("Deneme-"+ str(i+1)+"basarıyla okundu")
        f.close
    # pass


write_funciton()    
read_function()