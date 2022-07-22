import math
def oddoreven(num):
  num = num[-1]
  test0 = num == 0
  test1 = num == 1
  test2 = num == 2
  test3 = num == 3
  test4 = num == 4
  test5 = num == 5
  test6 = num == 6
  test7 = num == 7
  test8 = num == 8
  test9 = num == 9
  if test1 == true or test3 ==true or test5 ==true or test7 == true or test9 == true:
    print(Number is Odd)
  if test2 == true or test4 == true or test6 == true or test8 == true or test0 == true:
      print(Number is Even)
