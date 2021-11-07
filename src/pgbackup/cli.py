from argparse import Action, ArgumentParser

from pgbackup.pgdump import dump

known_drivers = ['local', 's3']

class DriverAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        if driver.lower() not in known_drivers:
            parser.error("Uknown driver. Available drivers are 'local' & 's3'")
        namespace.driver = driver.lower()
        namespace.destination = destination

def create_parser():
    parser = ArgumentParser(description="""
    Back up PostgreSQL database locally or to AWS S3.
    """)
    parser.add_argument("url", help="URL of the Postgres database to backup")
    parser.add_argument("--driver", "-d",
        help="How & where to store backup",
        nargs=2,
        action=DriverAction,
        metavar=("DRIVER", "DESTINATION"),
        required=True)
    return parser

def main():
    import time
    import boto3
    from pgbackup import pgdump, storage

    args = create_parser().parse_args()
    dump = pgdump.dump(args.url)
    if args.driver == 's3':
        client = boto3.client('s3')
        timestamp = time.strftime("%Y-%m-%dT%H:%M", time.localtime())
        file_name = pgdump.dump_file_name(args.url, timestamp)
        print(f"Backing database up to {args.destination} in S3 as {file_name}")
        storage.s3(client, dump.stdout, args.destination, file_name)
    else:
        timestamp = time.strftime("%Y-%m-%dT%H:%M", time.localtime())
        file_name = pgdump.dump_file_name(args.url, timestamp)
        outfile = open(args.destination + "/" + file_name, 'wb')
        print(f"Backing datase up locally to {outfile.name}")
        storage.local(dump.stdout, outfile)
