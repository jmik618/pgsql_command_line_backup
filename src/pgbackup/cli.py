from argparse import ArgumentParser

class DriverAction(Action):
    def __call__(sself, parser, namespace, values, option_string=None):
        driver, destination = values
        namespace.driver = driver.lower()
        namespace.destination = destination

def create_parser():
    parser = ArgumentParser(description="""
    Back up PostgreSQL database locally or to AWS S3.
    """)
    parser.add_argument("url", help="URL of database to backup")
    parser.add_argument("--driver",
    help="How & where to store backup",
    nargs=2,
    action=DriverAction,
    required=True)
    return parser