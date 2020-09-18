class PluginLoader:

    def __init__(self):
        self.base = "src.plugin"

    def load(self, name):
        config = {}
        manifest = open('src/plugin/' + name + '/MANIFEST')

        for line in manifest:
            l = line.replace('\n','').split("=")
            config[l[0]] = l[1]

        a = config['entrypoint'].split('.')

        module = __import__(self.base + '.' + name + '.' + a[0],fromlist='.')
        c = getattr(module, a[1])
        return c()
