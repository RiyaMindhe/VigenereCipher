from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class VigenereCipher(App):

    def build(self):
        characters = "abcdefghijklmnopqrstuvwxyz"
        characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        characters += "1234567890"
        characters += " !@#$%^&*()-_+=`~;:'[]{}|<>,./?"
        characters += "\"\\"


        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_y":0.5, "center_x":0.5}
        self.window.add_widget(Image(source="logo.jfif"))
        self.greeting = Label(
            text="Supported Characters:\n" + characters + "\n ",
            font_size=18,
            color="#00FFCE"
        )
        self.window.add_widget(self.greeting)

        self.plaintext = Label(text="Message: ")
        self.plaintext1 = TextInput(
            multiline=False,
            padding_y=(20, 20),
            size_hint=(1, 0.5)
        )
        self.window.add_widget(self.plaintext1)

        self.keytext = Label(text="Password: ")
        self.keytext1 = TextInput(
            multiline=False,
            padding_y=(20, 20),
            size_hint=(1, 0.5)
        )
        self.window.add_widget(self.keytext1)


        self.button = Button(
            text="ENCRYPT MESSAGE",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFCE'
        )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)
        return self.window

    def callback(self, instance):
        characters = "abcdefghijklmnopqrstuvwxyz"
        characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        characters += "1234567890"
        characters += " !@#$%^&*()-_+=`~;:'[]{}|<>,./?"
        characters += "\"\\"
        character_count = len(characters)

        def encrypt_character(plain, key):

            key_code = characters.index(key)
            plain_code = characters.index(plain)
            cipher_code = (key_code + plain_code) % character_count
            cipher = characters[cipher_code]
            return cipher

        def encrypt(plain, key):

            cipher = ""
            for (plain_index, plain_character) in enumerate(plain):

                key_index = plain_index % len(key)
                key_character = key[key_index]
                cipher_character = encrypt_character(key_character, plain_character)
                cipher += cipher_character
                return cipher

        def invert_character(character):

            character_code = characters.index(character)
            inverted_code = (character_count - character_code) % character_count
            inverted_character = characters[inverted_code]
            return inverted_character

        def invert(text):

            inverted_text = ""
            for character in text:
                inverted_text += invert_character(character)
            return inverted_text

        for i in range(0,102):

            plaintext = self.plaintext1.text
            keytext = self.keytext1.text
            
            encrypted = plaintext.startswith("!")
            if encrypted:
                plaintext = plaintext[1:]
                keytext = invert(keytext)
            ciphertext = encrypt(plaintext, keytext)
            if not encrypted:
                ciphertext = "!" + ciphertext

            self.greeting.text = "Encrypted Message: " + ciphertext



if __name__ == "__main__":
    VigenereCipher().run()