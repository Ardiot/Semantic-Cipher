""" Created by Carlos Garcia @Ardiot"""

from semantic_cypher import SemanticCypher


def main():

    cypher = SemanticCypher(
        "list_of_English_GB_words.txt",
        password="1234",
        consistency=True,
    )

    plain_text_msg = "Hello friend"
    cypher_text = cypher.encrypt(plain_text_msg)

    print(f'Cypher from "{plain_text_msg}" to "{cypher_text}"')

    decryt_msg = cypher.decrypt(cypher_text)
    print(f'Decrypt cypher text from "{cypher_text}" to "{decryt_msg}" ')


if __name__ == "__main__":
    main()
