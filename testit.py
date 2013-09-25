from git import *
import uuid

repo = Repo('.')
shiz = str(uuid.uuid4()).upper() + '.json'

outfile = open(shiz,'w')
outfile.write(shiz)
outfile.close()

repo.git.add('.')
repo.git.commit('-a', '-m Autocommit')
repo.git.push()
