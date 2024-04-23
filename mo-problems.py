import os

import requests


def read_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data

def main():
    filename = input("Enter filename: ")
    file_contents = read_file(filename)
    print("File contents:", file_contents)

def send_request():
    username = "admin"
    password = "P@ssw0rd"
    url = "https://example.com/login"

    response = requests.post(url, data={'username': username, 'password': password})
    return response.text

if __name__ == "__main__":
    main()
    send_request()