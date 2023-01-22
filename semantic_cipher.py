""" Created by Carlos Garcia @Ardiot"""


import hashlib
import json


class SemanticCypher:
    def __init__(self, dictionary_path, password="", consistency=True) -> None:

        self.encryptDict = {}
        self.decryptDict = {}
        self.HashedWords = []
        self.password = password
        self.consistency = consistency

        try:
            with open(dictionary_path) as f:
                self.list_of_words = f.read().splitlines()
        except:
            raise ("Problems with dictionary file")
        else:
            self.generateCryptogram()

    def generateCryptogram(self):
        """This function creates both encrypt and decrypt dictionaries"""

        hash_word_dictionary = {}
        for word in self.list_of_words:
            word_hash = hashlib.sha256(word.encode() + self.password.encode()).digest()
            self.HashedWords.append(word_hash)
            hash_word_dictionary[word_hash] = word.lower()

        # Sort list of hashes
        self.HashedWords.sort()

        # Fill encrypt and decrypt dictionaries
        for index, _ in enumerate(self.HashedWords):
            self.encryptDict[self.list_of_words[index]] = hash_word_dictionary[
                self.HashedWords[index]
            ]
            self.decryptDict[
                hash_word_dictionary[self.HashedWords[index]]
            ] = self.list_of_words[index]

    def encrypt(self, plain_text_msg: str) -> str:
        """Encrypt message.

        If consitency
            Then it wont encrypt input text unless all words are inside the word list. Return empty string
        else:
            If a word is not inside word list it wont encrypt it and it'll jump to the next.

        Args:
            plain_text_msg (str): Plain text input

        Returns:
            str: Cypher text
        """

        cypher_text = ""
        if self.consistency:
            if self.checkInputCorrelance(plain_text_msg):
                for word in plain_text_msg.split():
                    cypher_text += self.encryptDict[word.lower()] + " "
        else:
            for word in plain_text_msg.split():
                if word in self.encryptDict:
                    cypher_text += self.encryptDict[word.lower()] + " "

        return cypher_text

    def decrypt(self, cypher_text: str) -> str:
        """Decrypt cypher text

        Args:
            cypher_text (str): Encrypted text

        Returns:
            str: Decrypted message
        """
        decrypted_msg = ""
        if self.consistency:
            for word in cypher_text.split():
                if word.lower() in self.decryptDict:
                    decrypted_msg += self.decryptDict[word.lower()] + " "
                else:
                    return ""
        else:
            for word in cypher_text.split():
                if word.lower() in self.decryptDict:
                    decrypted_msg += self.decryptDict[word.lower()] + " "

        return decrypted_msg

    def checkInputCorrelance(self, msg: str) -> bool:
        """Return true if all word in input msg are inside word list

        Args:
            msg (str): Message you want to check
        """
        words_not_in_list = 0
        for word in msg.split():
            if word.lower() not in self.list_of_words:
                words_not_in_list += 1

        if words_not_in_list == 0:
            return True
        else:
            return False

    def debug(self):
        """Debug dictionaries"""
        with open("encrypt_dict_dump.json", "w") as outfile:
            json.dump(self.encryptDict, outfile, indent=2)

        with open("decrypt_dict_dump.json", "w") as outfile:
            json.dump(self.decryptDict, outfile, indent=2)
