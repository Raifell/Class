import requests
import webbrowser
import json

artix = 5

if artix == 1:
    # GET
    URL = 'https://google.com'

    page = requests.get(URL)
    page.raise_for_status()

    if str(page) == '<Response [200]>':

        with open('example.html', 'w') as file:
            file.write(page.text)

        url = 'example.html'
        webbrowser.open_new_tab(url)
    else:
        print('Connect Error!')

elif artix == 2:
    # PUT
    page = requests.put('https://httpbin.org/put', data={'key': 'value'})
    page.raise_for_status()

    txt = 'myfile.json'
    with open(txt, 'wb') as file:
        file.write(page.content)

elif artix == 3:
    # DELITE
    page = requests.delete('https://httpbin.org/put', data={'key': 'value'})
    page.raise_for_status()

    txt = 'myfile.json'
    with open(txt, 'wb') as file:
        file.write(page.content)

elif artix == 4:
    # HEAD
    page = requests.head('https://httpbin.org/get')
    page.raise_for_status()
    print(page)

elif artix == 5:
    # OPTIONS
    page = requests.options('https://httpbin.org/get')
    page.raise_for_status()
    a = page.headers
    for x, z in a.items():
        if x == 'Allow':
            print(z)

