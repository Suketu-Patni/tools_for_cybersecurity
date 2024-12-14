import subprocess

possible_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"

# string = "0" + 29*"_"

# "Enter your password (30 characters long, all characters are alphanumeric or '_') : 0 / 30 characters match"

password = ""


# print(output)

num_char_matches = 0
output_23 = 0

while num_char_matches != 30:
    for char in possible_chars:
        string = password + char + (29-num_char_matches)*"_"
        command = f"echo \"{string}\" | ./notwordle"
        output = subprocess.check_output(command, shell=True, executable="/bin/bash").decode().strip()

        if (output[-24]+output[-23]).strip() != str(output_23):
            num_char_matches += 1
            password += char
            output_23 += 1
            break

print(password)
