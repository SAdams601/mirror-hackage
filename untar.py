import tarfile
import os
import shutil

if len(sys.argv) < 2:
    sys.stderr.write("Error: require path to mirror base as first argument")
    raise SystemExit(1)
base = sys.argv[1]

os.chdir(base)
for filename in os.listdir('.'):
    if (filename.endswith("tar.gz")):
        dirname = filename.split('.tar.gz')[0]
        if (not os.path.exists(dirname)):
            print("Untarring: " + filename)
            tar = tarfile.open(filename, "r:gz")
            tar.extractall()
            tar.close()
            shutil.move(filename, dirname)
        else:
            print("Skipping: " + filename)
    else:
        continue    

