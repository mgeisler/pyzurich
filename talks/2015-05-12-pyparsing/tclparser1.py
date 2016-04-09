"""Sanitizer output parsing"""

from pyparsing import ParserElement, Suppress, Optional, ZeroOrMore, OneOrMore
from pyparsing import Literal, Word, Forward, Group, White, QuotedString
from pyparsing import StringEnd, restOfLine, alphanums


def _make_grammar():
    """Make a grammar for parsing a sanitized F5 config

    The syntax is Tcl, except for a 'Sanitized out =' string at the
    top. We only parse enough to find commands and their arguments.

    Return a ParseResult where 'prog' is a list of commands. Each
    command has a name and some arguments. These arguments can be
    further nested lists in case of '{ ... }' and '[ ... ]' blocks.
    """
    ParserElement.setDefaultWhitespaceChars(' ')

    white = Suppress(Optional(White()))
    comment = white + '#' - restOfLine
    lbrace, rbrace = Suppress('{'), Suppress('}')
    lbracket, rbracket = Suppress('['), Suppress(']')
    cmds = Forward()
    braces = Group(lbrace - white - Optional(cmds) - white - rbrace)
    brackets = Group(lbracket - white - Optional(cmds) - white - rbracket)

    string = QuotedString(quoteChar='"', escChar='\\', multiline=True)
    word = string | braces | brackets | Word(alphanums + '-:()_./<>%*$|!=&?')
    cmd = Group(word('name') + ZeroOrMore(word)('args'))
    cmd_sep = OneOrMore(Literal('\n') | ';')
    cmds << (cmd + ZeroOrMore(Suppress(cmd_sep) + cmd))

    prog_end = Suppress(Optional(cmd_sep)) + StringEnd()
    prog = cmds + prog_end

    sanitized_begin = Suppress(Optional(White()))
    sanitized = sanitized_begin + Optional('Sanitized out =') + prog('prog')
    sanitized.ignore(comment)

    return sanitized


def extract_pools(config):
    """Extract pools from a sanitized F5 config.

    All pools are returned in a mapping of pool name to the list of
    pool members.
    """
    grammar = _make_grammar()

    # Normalize line endings.
    config = config.replace('\r\n', '\n')

    # Work around the sanitizer removing too much from the line when
    # removing an IP address
    config = config.replace('servers <REMOVED>\n', 'servers {\n')

    pools = {}
    result = grammar.parseString(config)

    for cmd in result.prog:
        if cmd.name == 'pool':
            pool_name = cmd.args[0]
            parts = cmd.args[1]
            for p in parts:
                if p.name == 'members':
                    if len(p) == 2:
                        # A pool with a list of members
                        pools[pool_name] = [m.name for m in p.args[0]]
                    else:
                        # A single unpacked member
                        pools[pool_name] = [p.args[0]]
    return pools

if __name__ == '__main__':
    import fileinput
    import pprint
    from pyparsing import ParseException, ParseSyntaxException

    data = ''.join(fileinput.input())
    try:
        pprint.pprint(extract_pools(data))
    except (ParseException, ParseSyntaxException), e:
        print e.line
        print " "*(e.column-1) + "^"
        print e
