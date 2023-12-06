#!/usr/bin/env python3

import hashlib
import getpass

def encrypt_string(input_string, algorithm='sha256'):
    if algorithm not in hashlib.algorithms_available:
        print("Errore: Algoritmo non supportato.")
        return None

    hashed_string = hashlib.new(algorithm, input_string.encode('utf-8')).hexdigest()
    return hashed_string

def main():
    print("Questo è uno script per criptare una stringa.")
    
    input_string = getpass.getpass("Inserisci la stringa da criptare: ")
    
    if input_string:
        algorithm = input("Scegli l'algoritmo (sha256 di default): ") or 'sha256'
        encrypted_string = encrypt_string(input_string, algorithm)
        
        if encrypted_string:
            print(f"\nStringa criptata usando {algorithm}: {encrypted_string}\n")
    else:
        print("\nErrore: Devi fornire una stringa da criptare.\n")

if __name__ == "__main__":
    main()
