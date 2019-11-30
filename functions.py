

def emojitotext(emoji):
    import emojis
    
    text=emojis.decode('{}'.format(emoji))
    text=text.replace(":"," ")
    return text


def texttoemoji(text):
    import emojis 
    texts=[]
    text=text.split()
    print(text)
    for i in text:
    	i=":{}:".format(i)
    	texts.append(i)
    	text=''.join(texts)
    	emoj=emojis.encode(text)
        
    return emoj


