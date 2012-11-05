dictionary = {'direction': ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back'], 'verb': ['go', 'stop', 'kill', 'eat'], 'stop': ['the', 'in', 'of', 'from', 'at', 'it'], 'noun': ['door', 'bear', 'princess', 'cabinet']}

def scan(sentence):
    response = []
    words = sentence.split()
    for word in words:
        found_in_dictionary = False
        for key in dictionary.keys():
            if word in dictionary[key]:
                response.append((key, word))
                found_in_dictionary = True
                break
        if not found_in_dictionary:                
            try:
                response.append(('number', int(word)))
            except ValueError:
                response.append(('error', word))
                    
    return response
    

            
        
