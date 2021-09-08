def solution(string):
  backwards_string = ""
  for x in string:
    backwards_string = x + backwards_string
  return backwards_string