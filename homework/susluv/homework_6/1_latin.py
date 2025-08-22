text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, '
        'facilisis vitae semper at, dignissim vitae libero')
words = text.split()
words_with_ing = []
for word in words:
    if word.endswith('.'):
        word = word.replace('.', 'ing.')
    elif word.endswith(','):
        word = word[:-1] + 'ing,'
    else:
        word = word + 'ing'
    words_with_ing.append(word)
print(' '.join(words_with_ing))
