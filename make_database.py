import csv
import os
import sqlite3
import sys


def main(infile_name, outfile_name):
    conn = sqlite3.connect(outfile_name)
    c = conn.cursor()
    c.execute(
        '''CREATE TABLE tunes (
            tune int,
            setting int,
            name text,
            type text,
            meter text,
            mode text,
            abc text,
            date datetime,
            username text
        )'''
    )

    with open(infile_name) as f:
        reader = csv.reader(f, delimiter=",", skipinitialspace=True, escapechar="\\")
        next(reader)
        for row in reader:
            if not row:
                continue
            c.execute(
                '''INSERT INTO tunes VALUES
                    (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''',
                row
            )
    conn.commit()
    conn.close()


if __name__ == '__main__':
    if len(sys.argv) > 2:
        infile = sys.argv[1]
        outfile = sys.argv[2]
    else:
        infile = os.path.join('csv', 'tunes.csv')
        outfile = 'tunes.db'

    main(infile, outfile)
