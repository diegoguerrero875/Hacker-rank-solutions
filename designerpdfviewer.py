#from hacker rank designer pdf viwer problem
def designerPdfViewer(h, word):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    heights = {alphabet[i]:h[i] for i in range(26)}
    max_height = 0
    for letter in word:
        if heights[letter] > max_height:
            max_height = heights[letter]
    return len(word) * max_height
