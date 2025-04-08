from stats import get_word_count, get_char_count
import sys

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  filepath = sys.argv[1]
  with open(filepath) as f:
    file_contents = f.read()

  #print(file_contents)
  print(f"--- Begin report of {filepath} ---")
  word_count = get_word_count(file_contents)
  print(f"Found {word_count} total words")
  char_count = get_char_count(file_contents)
  print_char_report(char_count)

def sort_on(dict):
  return dict["num"]

def print_char_report(dict):
  char_list = []
  for key in dict:
    if key.isalpha():
      new_item = {
        "char": key,
        "num": dict[key],
      }
      char_list.append(new_item)

  char_list.sort(reverse=True, key=sort_on)
  for item in char_list:
    print(f"{item["char"]}: {item["num"]}")


main()