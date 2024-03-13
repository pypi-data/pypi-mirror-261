# ------------------------------------------------------------------------------
#  es7s/core
#  (c) 2024 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------
from ..._decorators import catch_and_log_and_exit, cli_command, cli_argument, cli_flag


@cli_command(__file__, "GNU date formats")
@cli_argument("locale", type=str, required=False, nargs=-1)
@cli_flag("-l", "--list", help="Print list of available locales and exit.")
@cli_flag(
    "-e",
    "--empty",
    help="Display all format letters (by default rows without any results are hidden).",
)
@cli_flag("-W", "--whitespace", help="Visualize non-printable characters (usually whitespace).")
@catch_and_log_and_exit
class invoker:
    """
    Print a table with all supported GNU datetime formats for specified
    LOCALE(s).\n\n

    Command for system-wide locale installation:\n\n

        sudo apt-get install language-pack-<LANG_CODE>\n\n

    There is also an 'es7s' shortcut command 'install-locale'.
    """

    def __init__(self, **kwargs):
        from es7s.cmd.print_date_formats import action

        action(**kwargs)
