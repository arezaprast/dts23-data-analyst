import requests
url = "https://storage.googleapis.com/dqlab-dataset/hello.txt"
response = requests.get(url)
# Cetak kode status dari response
print(response)
# Cetak isi file hello.txt menggunakan method response.iter_lines()
print("\n>> Cetak isi file hello.txt menggunakan method response.iter_lines():")
for baris in response.iter_lines():
	print(baris)
	
# Membaca file hello.txt dengan fungsi read()
''' print(" Membaca file hello.txt dengan fungsi read()")
    file = open("Hello.txt", "r")
    content = file.read()
    file.close()
    print(content)
'''
# Membaca file hello.txt dengan fungsi read line()
''' print(" Membaca file hello.txt dengan fungsi readlines()")
    file = open("Hello.txt", "r")
    first_line = file.readline()
    second_line = file.readline()
    file.close()
    print(first_line)
    print(second_line)
'''
