def reverse_str(text: str) -> str:
    row = text.split(' ')
    reversed_list = []
    for word in row:
        list_ = [el for el in word if el.isalpha()]
        result = [list_.pop() if el.isalpha() else el for el in word]
        reversed_list.append(''.join(result))
    return ' '.join(reversed_list)


if __name__ == '__main__':
    cases = [('abcd efgh', 'dcba hgfe'), ('a1bcd efg!h', 'd1cba hgf!e'), ('', '')]
    for text, reversed_text in cases:
        assert reverse_str(text) == reversed_text
