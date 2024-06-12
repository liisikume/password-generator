import random
from password_generator_source_words import source_words


class PasswordGenerator:
    def __init__(self):
        self.num_of_words = 3
        self.original_words_phrase = []
        self.random_words_phrase = []
        self.word_separator = random.choice("-_.+")
        self.a_string = ""
        self.password_accepted = True

    @property
    def random_words_result(self):
        return self.word_separator.join(self.random_words_phrase)

    def get_valid_input(self):
        while True:
            try:
                self.num_of_words = int(input("Enter the number of words in your password from 2 to 5: "))
                if 2 <= self.num_of_words <= 5:
                    break
                else:
                    print("Error: Select a number between 2 to 5.")
            except ValueError:
                print("Error: Please enter a valid number.")

    def choose_random_words(self):
        words = random.sample(source_words, self.num_of_words - 1)
        words.append(random.choice(source_words))
        self.random_words_phrase = words
        self.original_words_phrase = list(words)

    def substitute_characters(self):
        words = self.random_words_phrase
        shortest_word = min(words, key=len)

        random_index = random.randint(0, len(shortest_word) - 1)

        while not shortest_word[random_index].isalpha():
            random_index = random.randint(0, len(shortest_word) - 1)

        substituted_word = (
                shortest_word[:random_index]
                + str(random.randint(1, 99))
                + shortest_word[random_index + 1:]
        )

        words[words.index(shortest_word)] = substituted_word

    def replace_with_special_characters(self):
        replacements = {
            'i': '!', 'l': '!',
            'a': '@',
            's': '$',
            'e': '€',
        }

        replace_characters = list(replacements.keys())
        random.shuffle(replace_characters)

        for mandatory_letter in replace_characters:
            mandatory_indices = [i for i, char in enumerate(self.random_words_result) if
                                 char.lower() == mandatory_letter.lower()]
            if not mandatory_indices:
                continue
            random_index = random.choice(mandatory_indices)
            break
        else:
            mandatory_letter = replace_characters[0]
            random_index = random.randint(0, len(self.random_words_result) - 1)

        modified_word = self.random_words_result[:random_index] + replacements[
            mandatory_letter] + self.random_words_result[random_index + 1:]

        random_letter_index = random.randint(0, len(modified_word) - 1)
        selected_letter = modified_word[random_letter_index]
        while not selected_letter.isalpha() or not selected_letter.islower():
            random_letter_index = random.randint(0, len(modified_word) - 1)
            selected_letter = modified_word[random_letter_index]

        modified_word = (
                modified_word[:random_letter_index] +
                selected_letter.upper() +
                modified_word[random_letter_index + 1:]
        )

        if modified_word == self.random_words_result:
            random_special_char = random.choice(list(replacements.values()))
            random_index = random.randint(0, len(self.random_words_result))
            modified_word = (
                    self.random_words_result[:random_index] +
                    random_special_char +
                    self.random_words_result[random_index:]
            )

        return modified_word

    def print_results(self):
        initial_password = self.word_separator.join(self.original_words_phrase)
        print("Your initial password:", initial_password)
        print("---------------------------------------------")
        final_password = self.replace_with_special_characters()
        print("Your final password:", final_password)
        print("---------------------------------------------")

        self.password_accepted = input("Create new password? (y/n): ") == 'y'
        if not self.password_accepted:
            print("Your password is:", final_password)


def main():
    password_generator = PasswordGenerator()

    while password_generator.password_accepted:
        print("*** Password Generator ***")
        print("---------------------------\n")

        print("Option 1. Autogenerate password")
        print("Option 2. Choose a number of words in your password")
        print("---------------------------\n")

        choice = input("Select option 1 or option 2: ")
        print("---------------------------------\n")

        if choice == '1':
            password_generator.choose_random_words()
            password_generator.substitute_characters()
            password_generator.print_results()

        elif choice == '2':
            password_generator.get_valid_input()
            password_generator.choose_random_words()
            password_generator.substitute_characters()
            password_generator.print_results()


if __name__ == "__main__":
    main()
