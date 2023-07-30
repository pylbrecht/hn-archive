#!/usr/bin/env python3

import argparse
import pathlib
import urllib.request
import json

URL = 'https://news.ycombinator.com/item?id={}'


def parse_bookmarks(bookmarks):
    for line in bookmarks.read_text().strip('\n').split('-'):
        story_id, _ = line.split('q')
        yield story_id


def main(args):
    story_ids = parse_bookmarks(args.bookmarks)

    for id in story_ids:
        with urllib.request.urlopen(f'https://hacker-news.firebaseio.com/v0/item/{id}.json') as f:
            response = json.loads(f.read().decode('utf-8'))
            print(f'{URL.format(id)} {response["title"]}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('bookmarks', type=pathlib.Path)

    args = parser.parse_args()
    main(args)
