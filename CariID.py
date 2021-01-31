#coding=utf-8
#coding by Fb.Com SUMANDO
#python2
import requests,os,re
baner = """
                ▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●
                  AUTHOR : SUMANDO .S
                   ASAL KOTA : MEDAN
                   WA . 085361524681
                ▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●"""
def id():
	try:
		u = raw_input('\nMasukkan username > ')
		url = 'https://www.facebook.com/'+u
		r = requests.get(url).text
		name = re.search('Title">(.*?)</', r).group(1).strip('| Facebook')
		id = re.search('profile/(.*?)" ', r).group(1)
		print '\nNama > '+name
		print 'Id   > '+id+'\n'
		exit()

	except requests.exceptions.ConnectionError:
		print '× Koneksi bermasalah'
		exit()
	except AttributeError:
		print '[×] USERNAME NOT FOUND'
		exit()

def user():
	try:
		u = raw_input('\nMasukkan id > ')
		url = 'https://www.facebook.com/'+u
		r = requests.get(url).text
		name = re.search('Title">(.*?)</', r).group(1).strip('| Facebook')
		user = re.search('https://www.facebook.com/(.*?)" />', r).group(1)

		print '\nNama     > '+name
		print 'Username > '+user+'\n'
		exit()

	except requests.exceptions.ConnectionError:
		print '[×] KONEKSI TERPUTUS'
		exit()
	except AttributeError:
		print '[×] YOUR ID NOT FOUND'
		exit()

os.system('clear')
print baner
print '1. CARI ID MENGGUNAKAN USURNAME'
print '2. CARI USURNAME MENGGUNAKAN ID\n'

while True:
	p = raw_input('>> ')
	if p=="":
		print '[×] BENAR DIKIT LAH TOL'
	elif p=="1":
		id()
	elif p=="2":
		user()
	else:
		print '[×] BENER DIKIT LAH TOL'
