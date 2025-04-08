

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