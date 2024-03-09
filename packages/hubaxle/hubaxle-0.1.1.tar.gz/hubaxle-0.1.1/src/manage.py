#!/usr/bin/env -S poetry run python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # Make sure we're in the right directory.
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hubaxle.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
