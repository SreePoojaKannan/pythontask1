import os
print("HELLO POOJA!\n")
print("HOW CAN I HELP YOU???")
print()
while True:
      p=input()
      if("Hey dude open my" in p) and (("browser" in p) or ("explorer" in p)):
          print("Opening your browser!")
          os.system(r'"C:\Users\LATHIKA KANNAN\AppData\Local\Google\Chrome\Application\chrome.exe"')
          print("Here it is...")
          print()
      elif("Hey dude open my" in p) and (("notepad" in p) or ("texteditor" in p)):
          print("Opening your text editor!")
          os.system("notepad")
          print("Here it is...")
          print()
      elif(("Hey dude open my" in p) and ("calculator" in p)):
          print("Opening your calculator!")
          os.system("calc")
          print("Here it is...")
          print()
      elif("Hey dude open my" in p) and ("mediaplayer" in p):
          print("Opening your windows media player!")
          os.system(r'"C:\Program Files (x86)\Windows Media Player\\wmplayer.exe"')
          print("Here it is...")
          print()
      elif("Hey dude open my" in p) and ("paint" in p):
          print("Opening your paint!")
          os.system("mspaint")
          print("Here it is...")
          print()
      elif("quit" in p):
          print("Quitting!")          
          print()
      elif("Hey dude open my" in p) and ("anacondanavigator" in p):
          print("Opening your Anaconda Navigator!")
          os.system(r'"C:\ana\pythonw.exe C:\ana\cwp.py C:\ana C:\ana\pythonw.exe C:\ana\Scripts\anaconda-navigator-script.py"')
          print("Here it is...")
          print()
      elif("Hey dude open my" in p) and ("myfavouritepicture" in p):
          print("Opening your most favourite picture!")
          os.system(r'"C:\Users\LATHIKA KANNAN\Desktop\mypicture.jpg"')
          print("Here it is...")
          print()
      elif("Hey dude open my" in p) and ("excelsheet" in p):
          print("Opening your Excel sheet!")
          os.system(r'"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"')
          print("Here it is...")
          print()
      else:
           print("Sorry i don't find such file here!")
           
           os.system(exit())
