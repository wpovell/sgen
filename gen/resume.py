import yaml

class Resume:
    def __init__(self, env, fn='resume.yaml'):
        self.env = env
        with open(fn) as f:
            self.data = yaml.load(f)

    def gen(self):
        with open('dist/resume/index.html', 'w') as f:
            html = self.env.get_template('resume.html').render(self.data)
            f.write(html)
