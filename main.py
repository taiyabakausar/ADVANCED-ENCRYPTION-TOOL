import argparse
from encrypt_decrypt import generate_key, encrypt_file, decrypt_file

def main():
    parser = argparse.ArgumentParser(description="Advanced Encryption Tool")
    subparsers = parser.add_subparsers(dest="command")

    # Encrypt command
    encrypt_parser = subparsers.add_parser("encrypt", help="Encrypt a file")
    encrypt_parser.add_argument("--input", required=True, help="Input file to encrypt")
    encrypt_parser.add_argument("--output", required=True, help="Output file for encrypted data")
    encrypt_parser.add_argument("--key", required=True, help="Encryption key (32 bytes)")

    # Decrypt command
    decrypt_parser = subparsers.add_parser("decrypt", help="Decrypt a file")
    decrypt_parser.add_argument("--input", required=True, help="Input file to decrypt")
    decrypt_parser.add_argument("--output", required=True, help="Output file for decrypted data")
    decrypt_parser.add_argument("--key", required=True, help="Decryption key (32 bytes)")

    args = parser.parse_args()

    if args.command == "encrypt":
        encrypt_file(args.input, args.output, args.key.encode())
        print(f"File encrypted successfully: {args.output}")
    elif args.command == "decrypt":
        decrypt_file(args.input, args.output, args.key.encode())
        print(f"File decrypted successfully: {args.output}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()