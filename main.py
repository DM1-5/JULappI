import pywhatkit as kit
import nltk
import random
import json
# Constants
MSG = "Hola Jul"
PHONE = ""
WORDS_WITH_I = "WORDS_WITH_I.json"

def create_json(words_with_i: str) -> None:
  """
  Creates a JSON file with 1000 Spanish words starting with 'i'.

  Parameters:
  wordsWithI (str): The name of the JSON file to create.

  Returns:
  None
  """
  nltk.download('cess_esp')
  spanish_words_starting_with_i = [word.lower() for word in nltk.corpus.cess_esp.words() if word.lower().startswith('i')][:1000]
  with open(WORDS_WITH_I, 'w') as file:
    json.dump(spanish_words_starting_with_i, file)

def random_word()-> str:
  """
  Returns a random word from a JSON file.

  If the JSON file does not exist, it creates a new one.
  If there is an error decoding the JSON file, it creates a new one.
  If there is a permission error when trying to open the file, it prints an error message.
  If any other unexpected error occurs, it prints the error message.

  Returns:
    str: A random word from the JSON file.
  """
  try:
    with open(WORDS_WITH_I) as f:
      data = json.load(f)
      palabra = random.choice(data)
      return palabra
  except FileNotFoundError:
    print("File not found, creating a new one...")
    create_json(WORDS_WITH_I)
    return random_word()
  except json.JSONDecodeError:
    print("Error decoding JSON, creating a new file...")
    create_json(WORDS_WITH_I)
    return random_word()
  except PermissionError:
    print("Permission denied when trying to open the file.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")

def send_message(message: str) -> None:
  """
    Prints the message and sends it as a WhatsApp message.

    Parameters:
    message (str): The message to be sent.

    Returns:
    None
  """
  print(message)
  kit.sendwhatmsg_instantly(PHONE ,message, 15, True, 5)

def main() -> None:
    """
    Generates a random word from the JSON file, prefixes it with 'Hola Jul', and sends it as a message.

    Returns:
    None
    """
    send_message(f"{MSG}{random_word()}")

if __name__ == "__main__":
  main()

