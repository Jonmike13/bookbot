import sys

from stats import count_words
from stats import count_characters
from stats import sort_character_counts

def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	#book_text = get_book_text(filepath)
	#num_words = count_words(book_text)
	#char_counts = count_characters(book_text)
	#sorted_chars = sort_character_counts(char_counts)

	filepath = sys.argv[1]
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {filepath} ")
	book_text = get_book_text(filepath)

	num_words = count_words(book_text)
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")

	char_counts = count_characters(book_text)
	sorted_chars = sort_character_counts(char_counts)
	print("--------- Character Count -------")

	for item in sorted_chars:
		print(f"{item['char']}: {item['num']}")
	print("============= END ===============")

if __name__ == "__main__":
	main()


