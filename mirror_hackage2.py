# requires python-requests.org
import sys
import requests
import os
import hashlib
import traceback
import subprocess
import re

if len(sys.argv) < 2:
    sys.stderr.write("error: require path to mirror base as first argument")
    raise SystemExit(1)
base = sys.argv[1]

os.chdir(base)
#os.remove("00-index.tar.gz")
os.makedirs("package",0o777, True)

subprocess.run(["wget", "http://hackage.haskell.org/packages/archive/00-index.tar.gz"])

ps = subprocess.Popen(["tar", "tf", "00-index.tar.gz"], stdout=subprocess.PIPE)
fullNamesStr = subprocess.check_output(('cut', '-d/', '-f', '2,3'),stdin=ps.stdout, universal_newlines=True)

namesVersions = fullNamesStr.split("\n")
filtered = filter(lambda x : x != 'preferred-versions',namesVersions)
verDict = {}
#print(list(filtered)[1:20])
for nmVerStr in filtered:
    #print(nmVerStr)
    m = re.match(r"([\.\d]+)\/(.+)\.cabal",nmVerStr)
    if m:
        version = m.group(1)
        name = m.group(2)
        if ((name in verDict) and verDict[name] < version) or not (name in verDict):
            verDict[name] = version
    else:
        print(nmVerStr)
os.chdir("package")
baseUrl = "http://hackage.haskell.org/package/"        
for name, version in verDict.items():
    full = name + "-" + version
    print(full)
    fullUrl = baseUrl + full + "/" + full + ".tar.gz"
    subprocess.run(["wget", fullUrl])

