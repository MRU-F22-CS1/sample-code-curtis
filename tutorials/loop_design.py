# sum = 0
# count = 5
# while count <= 50:
#    sum = sum + count
#    count = count + 5

# print("The sum is", sum)
# print("The answer is", 
#       5 + 10 + 15 + 20 + 25 + 30 + 35 + 40 + 45 + 50)
def is_vowel(c: str) -> bool:
   """Returns True if c is a vowel, otherwise False."""
   c = c.lower()
   return (c == "a" or c == "e" or c == "i" 
           or c == "o" or c == "u" or c == "y")

def count_vowels() -> int:
   """"""
   char = input("Enter a character: ")
   vowel_count = 0
   while char != "!":
      if is_vowel(char):
         vowel_count = vowel_count + 1
      char = input("Enter a character: ")

   return vowel_count

def main() -> None:
   print(f"There are {count_vowels()} vowels")

main()