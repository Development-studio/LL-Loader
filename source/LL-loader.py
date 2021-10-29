import urllib.request
import os
import zipfile
import subprocess

pth=os.getcwd()

print('write down which versions you want to use(use full name of version, example 1.2.4 and 1.17.34.02)')
LL = input('what version of LL you need? ')
BDS = input('what version of BDS you need? ')
LXL = input('do you need install LXL? (yes/no) ')
if (LXL == 'yes'):
    LXL_ver = input('what version of LXL you need? ')

print('Beginning downloading files...') 
bds = 'https://minecraft.azureedge.net/bin-win/bedrock-server-'+ BDS +'.zip'
ll = 'https://github.com/LiteLDev/LiteLoaderBDS/releases/download/'+ LL +'/LiteLoader.zip'
if (LXL == 'yes'):
    lxl = 'https://github.com/LiteLDev/LiteXLoader/releases/download/v'+ LXL_ver + '/LiteXLoader.zip'
    urllib.request.urlretrieve(lxl, 'LiteXLoader.zip')
urllib.request.urlretrieve(bds, 'bedrock_server.zip') 
urllib.request.urlretrieve(ll, 'LiteLoader.zip')
print('Success!')

print('Starting extract files')
fantasy_zip = zipfile.ZipFile(pth + '\\bedrock_server.zip')
fantasy_zip.extractall(pth)
fantasy_zip = zipfile.ZipFile(pth + '\\LiteLoader.zip')
fantasy_zip.extractall(pth)
if (LXL == 'yes'):
    fantasy_zip = zipfile.ZipFile(pth + '\\LiteXLoader.zip')
    fantasy_zip.extractall(pth + '\\plugins')
fantasy_zip.close()

print('All file extracted! Starting generate server')

os.remove(pth + '\\LiteLoader.zip')
os.remove(pth + '\\bedrock_server.zip')
if (LXL == 'yes'):
    os.remove(pth + '\\LiteXLoader.zip')

os.system(pth + '\\SymDB2.exe')

for i in range( 0, 0 ):
    subprocess.call(('SymDB2.exe', str(i)))

os.system(pth + '\\bedrock_server.exe')

