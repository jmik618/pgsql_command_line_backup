pgbackup
========

CLI for backing up remote PostgresSQL databases locally or to AWS S3.

Preparing for Development
-------------------------

1. Ensure ``pip`` and ``pipevn`` are installed
2. Clone repository: ``git clone git@github.com:/example/pgbackup``
3. ``cd`` intyo repository
4. Fetch development dependencies ``make install``
5. Activate virtualenv: ``pipenv shell``

Usage
-----

Pass in a fiull database URL, the storage driver, and destination.

S3 Example w/ bucket name:

::

	$ pgbackup postgres://bob@example.com:5432/db_one --driver s3 backups

Local Example w/ local path:

	$ pgbackup postgres://bob@example.com:5432/db_one --driver local /var/local/db/backups

Running Tests
-------------

::

	$ make

If virtualenv isn't active then use:

::

	$ pipenv run make