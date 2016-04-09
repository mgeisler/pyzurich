"""Sanitizer output parsing"""


def parse_f5_config(config):
    """Very simple sanitizer output parser.

    This only parses "{ ... }" groups and ";" command separators.
    Everything else is treated as commands and command arguments.

    Each command is a list itself, and "{ ... }" groups are nested
    lists. Returns a list of commands.
    """

    # Normalize line endings.
    config = config.replace('\r\n', '\n')

    # Work around the sanitizer removing too much from the line when
    # removing an IP address.
    config = config.replace('servers <REMOVED>\n', 'servers {\n')

    # Standardize command separators.
    config = config.replace('\n', ';')

    # Ensure we can cleanly split on the symbols we care about.
    for symbol in ';{}':
        config = config.replace(symbol, ' %s ' % symbol)

    tokens = config.split()

    def parse_commands(pos):
        commands = []
        command = []
        while pos < len(tokens):
            token = tokens[pos]
            if token == ';':
                if command:
                    # Avoid creating empty commands when seeing
                    # repeated command separators.
                    commands.append(command)
                    command = []
            elif token == '{':
                nested, pos = parse_commands(pos + 1)
                command.append(nested)
            elif token == '}':
                if command:
                    commands.append(command)
                return commands, pos
            else:
                command.append(token)
            pos += 1
        if command:
            commands.append(command)
        return commands, pos

    commands, pos = parse_commands(0)

    if pos != len(tokens):
        msg = 'Could only parse %d of %d tokens' % (pos, len(tokens))
        raise RuntimeError(msg)
    return commands


def clean(name):
    """Remove port numbers and route domain from name.

    >>> clean('foo')
    'foo'
    >>> clean('foo:http')
    'foo'
    >>> clean('foo%123')
    'foo'
    >>> clean('foo%123:ssh')
    'foo'
    """
    name = name.partition(':')[0]
    name = name.partition('%')[0]
    return name


def extract_pools(config):
    """Extract pools from a sanitized F5 config.

    All pools are returned in a mapping of pool name to the list of
    pool members.
    """
    commands = parse_f5_config(config)

    pools = {}

    for cmd in commands:
        if cmd[0] == 'pool':
            pool_name = cmd[1]
            parts = cmd[2]
            for p in parts:
                if p[0] == 'members':
                    if len(p) == 2:
                        # A pool with a list of members
                        pools[pool_name] = [clean(m[0]) for m in p[1]]
                    else:
                        # A single unpacked member
                        pools[pool_name] = [clean(p[1])]
    return pools

if __name__ == '__main__':
    import fileinput
    import pprint

    data = ''.join(fileinput.input())
    try:
        pprint.pprint(extract_pools(data))
    except RuntimeError as exc:
        print exc
