#!/usr/bin/env python3
import zipfile


with zipfile.ZipFile('SimpleAPI.zip', 'r') as zip_ref:
    zip_ref.extractall('/alx-backend-user-data/0x01-Basic_authentication')
    zip_ref.close()
