#!/usr/bin/env python3

import hashlib
import sys

if len(sys.argv) >= 2:
    print("")
    print(hashlib.md5(sys.argv[1].encode('utf-8')).hexdigest())
    print("")
else:
    print("")
    print("Errore: Inserisci scringa da cryptare")
    print("")