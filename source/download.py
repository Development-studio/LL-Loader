import urllib.request
a = input("Select type of download ")
if (a == "1"):
    print('Beginning downloading files...') 
    zip = 'https://minecraft.azureedge.net/bin-win/bedrock-server-1.17.34.02.zip'
    urllib.request.urlretrieve(zip, 'bedrock_server.zip')
else:
    print('Beginning downloading files...')
    zip1 = 'http://mica1529.ru/LL_loader/LiteLoader.zip' 
    urllib.request.urlretrieve(zip1, 'LiteLoader.zip')
print("Success!")
