def main():
  filepath = "books/frankenstein.txt"
  with open(filepath) as f:
    file_contents = f.read()
  #print(file_contents)
  print(f"--- Begin report of {filepath} ---")
  word_count = get_word_count(file_contents)
  print(f"{word_count} words found in the document")
  char_count = get_char_count(file_contents)
  print_char_report(char_count)

def get_word_count(text):
  words = text.split()
  word_count = len(words)
  return word_count

def get_char_count(text):
  char_dict = {}
  for char in text:
    lowered = char.lower()
    if lowered in char_dict:
      char_dict[lowered] += 1
    else:
      char_dict[lowered] = 1
  return char_dict

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
    print(f"The '{item["char"]}' charactr was found {item["num"]} times")


main()