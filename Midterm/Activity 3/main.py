from ArrayS import ArrayStack, ParenthesesMatcher, FileReverser

matcher = ParenthesesMatcher()

check1 = '(10 + x) / y (x - 5)'
check2 = '((10 + 1))) - 10 + 4 ( 1+ (('

if matcher.is_matched(check1):
    print("A correct")
else:
    print("A wrong")

if matcher.is_matched(check2):
    print("B correct")
else:
    print("B wrong")


FileReverser.reverse_file('File.txt')