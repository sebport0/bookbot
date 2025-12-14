def get_num_words(text):
    return len(text.split())


def get_num_chars(text):
    chars_count = {}
    text_lower = text.lower()
    for c in text_lower:
        if chars_count.get(c):
            chars_count[c] += 1
        else:
            chars_count[c] = 1
    return chars_count


def _sort_on(d):
    return d["num"]


def sort_results(d):
    output = []
    for c, num in d.items():
        if c.isalpha():
            output.append({"char": c, "num": num})
    output.sort(reverse=True, key=_sort_on)
    return output
