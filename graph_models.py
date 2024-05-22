from django.core.management import execute_from_command_line
import sys


if __name__ == "__main__":
    sys.argv = [
        'manage.py', 'graph_models', '-a', '--output', 'my_project_models.png'
    ]
    execute_from_command_line(sys.argv)
