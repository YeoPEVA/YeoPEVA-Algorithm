
while True: 
    encode_s = input()
    if encode_s == "END":
        break
    decode_s = ''

    for i in encode_s:
        decode_s = i + decode_s
    print(decode_s)