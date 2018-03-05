import wget, os
s='https://www.securitystronghold.com/gates/images/orbit-downloader.png'
filename = wget.download(s)
os.rename(filename, u''+os.getcwd()+'/'+filename)
