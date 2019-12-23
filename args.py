import argparse
from datetime import datetime


def get_args():
    # TODO: Add --start-date, --end-date and --output arguments
    #       Convert the two dates to datetime objects
    parser = argparse.ArgumentParser()
    parser.add_argument('--start-date', required=True, help='Crawl Start Date')
    parser.add_argument('--end-date', required=True)
    parser.add_argument('--output', default='output.csv', help='Output CSV file')
