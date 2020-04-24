import os

def setup():
  if generate_settings_txt():
    return 1
  generate_zoom_codes_txt()
  return 0

def generate_settings_txt():
  try:
    settings = open("./settings.txt", "x")
    settings.write("Organization url:\n")
    url = input("Enter your organization url. This is could be any url that was given to you to join a meeting: ")
    temp = url.split("/j/")
    if len(temp) == 1:
      print("error: invalid zoom url")
      return 1
    settings.write(temp[0]+"/j/\n")
    settings.write("Browser Load Time:\n3\nZoom Load Time:\n3")
    settings.close()
    return 0
  except:
    return 0


def generate_zoom_codes_txt():
  meetings = 0
  try: 
    open("./zoom_codes.txt" , "x")
  except:
    codes_txt = open("./zoom_codes.txt" , "r")
    codes_txt.seek(0,0)
    meetings = int(codes_txt.readline())
    codes_txt.close()
  codes_txt = open("./zoom_codes.txt" , "r")
  buffer = open("./buffer.txt", "w")
  codes_txt.readline()
  for line in codes_txt:
    buffer.write(line)
  print("Welcome to zoom codes setup!")
  codes_txt.close()
  while True:
    name = input("Enter the meeting name. Enter q to quit: ")
    if name == "q":
      break
    else:
      buffer.write(name + "\n")
    code = input("Enter the meeting code or a link to join the meeting: ")
    if "http" in code:
      temp = code.split("/")
      next_ = False
      for i in temp:
        if next_ == True:
          buffer.write(i + "\n")
          break
        if i == "j":
          next_ = True
      if not next_:
        print("error: invalid zoom url")
        return 1
    else:
      buffer.write(code + "\n")
    password = input("Enter the meeting password. Enter a 0 if there isn't one: ")
    buffer.write(password + "\n")
    meetings += 1
  buffer.close()
  buffer = open("./buffer.txt", "r")
  codes_txt = open("./zoom_codes.txt" , "w")
  codes_txt.write(str(meetings) + "\n")
  for line in buffer:
    codes_txt.write(line)
  codes_txt.close()
  buffer.close()
  os.system("del /f .\\buffer.txt")

setup()