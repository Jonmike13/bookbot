def count_words(text):
        return len(text.split())

def count_characters(text):
	text = text.lower()
	char_dict = {}
	for char in text:
		if char in char_dict:
			char_dict[char] += 1
		else:
			char_dict[char] = 1
	return char_dict

def sort_character_counts(char_counts):
	sorted_list = [{"char": char, "num": count}
		for char, count in char_counts.items() if char.isalpha()]

	sorted_list.sort(key=lambda x: x["num"], reverse=True)
	return sorted_list

