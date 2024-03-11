def encrypt(text):
    encrypted_text = ''.join(format(ord(char), '08b') for char in text)
    return encrypted_text  



def decrypt(text):
    binary_chunks = [text[i:i+8] for i in range(0, len(text), 8)]      
    decrypted_text = ''.join(chr(int(chunk, 2)) for chunk in binary_chunks)
    return decrypted_text
