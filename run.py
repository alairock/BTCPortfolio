from app import core
import yaml
import os

f = yaml.load(open('env.yml'))
for x in f:
    os.environ[x] = f[x]

if __name__ == '__main__':
    core.run()
