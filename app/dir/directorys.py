import json
from glob import glob


class directorys():
    def __init__(self):
        dir = glob('**/dirs.json', recursive=True)
        with open(dir[0], 'r') as f:
            c = f.read()
            self.content = json.loads(c)

    def database(self):
        return self.content['database']

    def api(self):
        return self.content['api']

    def auth(self):
        return self.content['authentication']

    


