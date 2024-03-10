import requests

def status_200():
    r = requests.get('https://httpstat.us/200')
    return r.status_code

def status_201():
    r = requests.get('https://httpstat.us/201')
    return r.status_code

def status_300():
    r = requests.get('https://httpstat.us/300')
    return r.status_code

def status_301():
    r = requests.get('https://httpstat.us/301')
    return r.status_code

def status_302():
    r = requests.get('https://httpstat.us/302')
    return r.status_code

def status_401():
    r = requests.get('https://httpstat.us/401')
    return r.status_code

def status_402():
    r = requests.get('https://httpstat.us/402')
    return r.status_code

def status_403():
    r = requests.get('https://httpstat.us/403')
    return r.status_code

def status_404():
    r = requests.get('https://httpstat.us/404')
    return r.status_code

def status_501():
    r = requests.get('https://httpstat.us/501')
    return r.status_code

if __name__ == "__main__":
    print(status_200())