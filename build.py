# -*- coding: utf-8 -*-
import os
from jinja2 import Environment, PackageLoader

LOADER = PackageLoader('site', 'templates')
PROVIDER = LOADER.provider
PROVIDER.module_path = os.path.dirname(os.path.abspath(__file__))

ENV = Environment(loader=LOADER)


def write(template_path, output_path, **context):
    with open(output_path, 'w') as output:
        template = ENV.get_template(template_path)
        output_string = template.render(**context)
        output.write(output_string.encode('utf-8'))


def get_events(events_root):

    for season in sorted(os.listdir(events_root)):
        if not os.path.isdir(os.path.join(events_root, season)):
            continue
        for filename in sorted(os.listdir(os.path.join(events_root, season))):
            if not os.path.isfile(os.path.join(events_root, season, filename)):
                continue
            episode, ext = os.path.splitext(filename)
            if ext == '.html':
                yield dict(
                    template_path='html/events/{}/{}'.format(season, filename),
                    output_path='events/s{}e{}'.format(season, filename),
                    season=season,
                    episode=episode,
                    file=filename
                )


def main():

    write('html/home.html', 'index.html')
    write('html/coc.html', 'code-of-conduct.html')
    write('html/forum.html', 'mail.html')
    write('html/twitter_embed.html', 'tweets.html')

    events = []

    for event in get_events('templates/html/events'):
        events.append(event)
        write(**event)

    write('html/events.html', 'events/index.html', events=events[::-1])

if __name__ == "__main__":
    main()
