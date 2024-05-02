import argparse
import hashlib
import string
import time

def get_args():
    parser = argparse.ArgumentParser(description='Simple Password Cracker')
    parser.add_argument('hashed_pw', help='The hashed password to crack')
    parser.add_argument('--min-length', type=int, default=4,
                        help='Minimum password length (default: 4)')
    parser.add_argument('--max-length', type=int, default=8,
                        help='Maximum password length (default: 8)')
    parser.add_argument('--charset', default=string.ascii_letters + string.digits,
                        help='Character set for the password (default: ascii letters and digits)')
    return parser.parse_args()

def crack_password(hashed_pw, min_length, max_length, charset):
    for password_length in range(min_length, max_length + 1):
        for char in charset:
            for comb in itertools.product(charset, repeat=password_length):
                candidate_password = ''.join(comb)
                if hashlib.sha256(candidate_password.encode()).hexdigest() == hashed_pw:
                    return candidate_password
    return None

def main():
    args = get_args()
    hashed_pw = args.hashed_pw
    min_length = args.min_length
    max_length = args.max_length
    charset = args.charset

    print(f'Cracking hashed password: {hashed_pw}')
    print(f'Character set: {charset}')
    print(f'Minimum length: {min_length}')
    print(f'Maximum length: {max_length}')
    print('This may take a while...')

    result = crack_password(hashed_pw, min_length, max_length, charset)
    if result:
        print(f'Cracked password: {result}')
    else:
        print('Password cracking failed.')

if __name__ == '__main__':
    main()