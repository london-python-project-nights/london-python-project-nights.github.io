import os
from jinja2 import Environment, PackageLoader

loader = PackageLoader('site', 'templates')
provider = loader.provider
provider.module_path = os.path.dirname(os.path.abspath(__file__))

env = Environment(loader=loader)

def write(template_path, output_path):
    with open(output_path, 'w') as output:
        template = env.get_template(template_path)
        output_string = template.render()
        output.write(output_string)


write('html/home.html', 'index.html')
write('html/coc.html', 'code-of-conduct.html')
write('html/forum.html', 'mail.html')
