import argparse

# Insert your decode_Caesar_cipher function here
def decode_Caesar_cipher(s, n):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) + n) % len(alpha)]
    print(text)


# Write your parser here
parser = argparse.ArgumentParser("Decipher the secret message")
parser.add_argument("--word", type=str)
parser.add_argument("--offset", type=int)
args = parser.parse_args()

decode_Caesar_cipher(args.word, args.offset * -1)