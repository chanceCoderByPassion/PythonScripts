import random
def p_gen(characters)->str:
    special_chars = ['!','@','#','$','%']
    alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    special=False
    digit=False
    alphabet=False
    capital=False
    small=False
    final_password = ''
    for _ in range(characters):
        if not special:
            final_password+=special_chars[random.randint(0,len(special_chars)-1)]
            special = True
        elif not digit:
            final_password+=digits[random.randint(0,len(digits)-1)]
            digit = True
        elif not capital:
            final_password+=(alphabets[random.randint(0,len(alphabets)-1)]).upper()
            capital = True
        elif not small:
            final_password+=(alphabets[random.randint(0,len(alphabets)-1)]).lower()
            small = True
        else:
            final_password+=(alphabets[random.randint(0,len(alphabets)-1)])

    # Jumble the generated password
    list_of_password_chars = list(final_password)
    random.shuffle(list_of_password_chars)
    return ''.join(list_of_password_chars)

count_of_chars = None

while 1:
    try:
        count_of_chars = int(input('Enter number of password characters:'))
    except Exception as e:
        print(e.__class__)
    else:
        if count_of_chars <= 7:
            print("Enter Longer password length")
            continue
        else:
            break

print(p_gen(count_of_chars))
