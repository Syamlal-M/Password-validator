min_alpha = 3
min_digit = 2
min_special = 3
min_length = 8


alpha_counter = 0
digit_counter = 0
special_counter = 0

password = input('Enter your password : ')

if ' ' not in password and len(password) >= min_length:

    for item in password: 
        
        if item.isdigit():
            
            digit_counter = digit_counter + 1
            
        elif item.isalpha():
            
            alpha_counter = alpha_counter + 1
 
        else:
            
            special_counter = special_counter + 1
            
    if alpha_counter >= min_alpha and digit_counter >= min_digit and special_counter >= min_special:
        print('password is strong')
    else:
        print('Invalid password')
else:
        
    print('length error')
