import os

from flake8.api.legacy import StyleGuide
from flake8.main.application import Application


def test_flake8():
    argv = [
        '--ignore=%s' % ','.join([
            'D100', 'D101', 'D102', 'D103', 'D104', 'D105',
            'E501']),
        '--exclude', 'vcstool/compat/shutil.py',
        '--import-order-style=google']
    style_guide = get_style_guide(argv)
    base_path = os.path.join(os.path.dirname(__file__), '..')
    paths = [
        os.path.join(base_path, 'scripts'),
        os.path.join(base_path, 'test'),
        os.path.join(base_path, 'vcstool'),
    ]
    report = style_guide.check_files(paths)
    assert report.total_errors == 0, \
        'Found %d code style warnings' % report.total_errors


def get_style_guide(argv=None):
    # this is a fork of flake8.api.legacy.get_style_guide
    # to allow passing command line argument
    application = Application()
    application.find_plugins()
    application.register_plugin_options()
    application.parse_configuration_and_cli(argv)
    application.make_formatter()
    application.make_notifier()
    application.make_guide()
    application.make_file_checker_manager()
    return StyleGuide(application)


if __name__ == '__main__':
    test_flake8()
