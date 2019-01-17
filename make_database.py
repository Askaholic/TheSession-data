import csv
import sqlite3


def main():
    conn = sqlite3.connect('tunes.db')
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

    with open('csv/tunes.csv') as f:
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
    main()
