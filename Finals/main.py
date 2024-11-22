from PositionalList import PositionalList as PositionalList
from LinkedStack import LinkedStack as Stack, into_postfix

S = Stack()
infix_expression = input("Enter an infix expression: ")

postfix_expression = into_postfix(infix_expression)

print(f"The postfix expression is: '{postfix_expression}'")


P = PositionalList()


numbers = [1, 72, 81, 25, 65, 91, 11]
for num in numbers:
    P.add_last(num)

print("Original list:")
for x in P:
    print(x, end=" ")
print()


def insertion_sort(L):
    """Sort the PositionalList in ascending order using insertion sort."""
    if len(L) > 1:
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)
            value = pivot.element()
            if value >= marker.element():
                marker = pivot
            else:
                walk = marker
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)


insertion_sort(P)
print("Sorted in ascending order:")
for x in P:
    print(x, end=" ")
print()


def insertion_sort_descending(L):
    """Sort the PositionalList in descending order using insertion sort."""
    if len(L) > 1:
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)
            value = pivot.element()
            if value <= marker.element():
                marker = pivot
            else:
                walk = marker
                while walk != L.first() and L.before(walk).element() < value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)


insertion_sort_descending(P)
print("Sorted in descending order:")
for x in P:
    print(x, end=" ")
print()
