def remove_fourth_character(word: str) -> str:
    inicio = word[:3]
    final = word[4:]
    return inicio + final


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
