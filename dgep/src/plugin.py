import imp
import os

for plugin in [dI for dI in os.listdir('plugin') if os.path.isdir(os.path.join('plugin',dI))]:
    config = {}
    manifest = open('plugin/' + plugin + '/MANIFEST')

    for line in manifest:
        l = line.replace('\n','').split("=")
        config[l[0]] = l[1]

    #print(config)

    a = config['entrypoint'].split('.')

    module = __import__('plugin.' + plugin + '.' + a[0],fromlist='.')
    c = getattr(module, a[1])
    i = c()
    i.run()
