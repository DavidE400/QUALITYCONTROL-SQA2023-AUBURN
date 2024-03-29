import random
import string
import scanner

def generate_fuzz_string(length):
    return ''.join(random.choice(string.printable) for _ in range(length))


def main():
    fuzz_str_arr = [generate_fuzz_string(24), generate_fuzz_string(48), generate_fuzz_string(0)]
    print('start fuzz testing...')

    for fuzz_str in fuzz_str_arr:
        ValidUserName = scanner.isValidUserName(fuzz_str)
        print(f"username test '{fuzz_str}' is valid: {ValidUserName}")
        ValidKey = scanner.isValidKey(fuzz_str)
        print(f"key test '{fuzz_str}' is valid: {ValidKey}")
        ValidPasswordName = scanner.isValidPasswordName(fuzz_str)
        print(f"password test '{fuzz_str}' is valid: {ValidPasswordName}")
        ValidSecret = scanner.checkIfValidSecret(fuzz_str)
        print(f"secret test '{fuzz_str}' is valid: {ValidSecret}")
        ValidKeyValue = scanner.checkIfValidKeyValue(fuzz_str)
        print(f"keyValue test '{fuzz_str}' is valid: {ValidKeyValue}")



if __name__ == '__main__':
    main()