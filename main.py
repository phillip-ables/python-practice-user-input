  # http://www.practicepython.org/exercise/2014/01/29/01-character-input.html
name = input("What is your name? ")
age = input("What is your age? ")
number =input("Time is precious " + name + ", Enter a number: ")
tillOneHundred = 100 - int(age)
print((name+", you have "+ str(tillOneHundred)+" yars til you are ONE HUNDRED\n")*int(number))
  # for x in range(0, int(number)):
      # print(name + ", you have "+ str(tillOneHundred) + " years until you are ONE HUNDRED")

  # The only tricky thing here was having to cast everythings type
  # input as a string but needs an int type
  # output as an int but need a str type