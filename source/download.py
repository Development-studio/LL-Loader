import urllib.request
import os
import zipfile
import subprocess

pth=os.getcwd()

print('Beginning downloading files...') 
zip = 'https://minecraft.azureedge.net/bin-win/bedrock-server-1.17.34.02.zip'
zip1 = 'https://github.com/LiteLDev/LiteLoaderBDS/releases/download/1.2.4/LiteLoader.zip'
urllib.request.urlretrieve(zip, 'bedrock_server.zip') 
urllib.request.urlretrieve(zip1, 'LiteLoader.zip')
print("Success!")


print('Starting extract files')
fantasy_zip = zipfile.ZipFile(pth + '\\bedrock_server.zip')
fantasy_zip.extractall(pth)
fantasy_zip = zipfile.ZipFile(pth + '\\LiteLoader.zip')
fantasy_zip.extractall(pth)
fantasy_zip.close()

print('All file extracted! Starting generate server')
os.system(pth + '\\SymDB2.exe')


for i in range( 0, 0 ):
    subprocess.call(('SymDB2.exe', str(i)))

os.system(pth + '\\bedrock_server.exe')

my_file = open('LL-loader.txt', 'w+')
my_file.write('Hello!' + '\n')
my_file.write('Thx for using LL-loader' + '\n')
my_file.write('Github: https://github.com/Development-studio/LL-Loader')
my_file.close()

