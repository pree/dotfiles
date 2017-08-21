#!/usr/bin/env python
"""Install script."""

from __future__ import print_function

from argparse import ArgumentParser
from glob import glob
from os import path
from subprocess import call

# User Configurations
NON_TOPICS = ['bin']
TOPIC_PRIORITY = ['install']

# Dotbot Configurations
DOTBOT = 'install/dotbot/bin/dotbot'
PLUGINS = []

# Path Processing
BASE_DIR = path.dirname(path.realpath(__file__))
DOTBOT = path.join(BASE_DIR, DOTBOT)


def main():
    """Main logic."""
    parser = ArgumentParser()
    parser.add_argument('profile', type=str, default='config.macos')
    args = parser.parse_args()

    configs = collect(args.profile)
    final_config = path.join(BASE_DIR, 'final.' + args.profile + '.yaml')
    combine(configs, final_config)
    install(final_config)


def collect(profile):
    """Collect all configuration files belong to a profile."""
    configs = []
    for topic in get_topics():
        configs += get_configs(topic, profile)
    return configs


def get_topics():
    """Collect all topics."""
    # Start with all subdirectories
    topics = [path.basename(p)
              for p in glob(path.join(BASE_DIR, '*')) if path.isdir(p)]
    # Remove non-topics and topic priority
    topics = [t for t in topics if t not in (NON_TOPICS + TOPIC_PRIORITY)]
    # Sort in order
    topics = TOPIC_PRIORITY + sorted(topics)
    return topics


def get_configs(topic, profile):
    """Collect all configuration files belong to a topic of a profile."""
    print('Process', topic)
    configs = []
    while profile:
        to_consider = path.join(BASE_DIR, topic, profile + '.yaml')
        if path.exists(to_consider):
            print('Add', path.basename(to_consider))
            configs.insert(0, to_consider)
        profile = profile[:profile.rfind('.')]
    print()
    return configs


def combine(configs, final_config):
    """Combine individual configuration files into a single final one."""
    with open(final_config, 'w+') as fc:
        for config in configs:
            with open(config, 'r') as c:
                # Comment the origin of following configurations
                fc.write('# ' + path.relpath(config, BASE_DIR) + '\n')
                # Copy the configurations
                fc.writelines(c.readlines())
                fc.write('\n')
    print('Combine into', path.basename(final_config))


def install(config):
    """Use Dotbot to install according to configuration."""
    print('Install')
    call([DOTBOT, '-d', BASE_DIR] + PLUGINS + ['-c', config])


if __name__ == '__main__':
    main()
