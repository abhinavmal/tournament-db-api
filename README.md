# tournament-db-api
A DB-API using PostgreSQL to implement a Swiss tournament system.

## Dependencies
- Python 2.7
- [Bleach](https://bleach.readthedocs.io/en/latest/) for input sanitization
- [psycopg2](http://initd.org/psycopg/)
- [PostgreSQL](https://www.postgresql.org/)

## Testing the Tournament DB-API system
- Run `git clone git@github.com:abhinavmal/tournament-db-api.git` on the command line and
`cd tournament-db-api` which contains `tournament.sql` and `tournament_test.py`.

- Go the `psql` command prompt and run `\i tournament.sql` to create the database tournament and associated tables for players and matches. This will also connect the default user to the database.
<!-- - The implementation assumes that a database with the name `tournament` has been already created, and the user
is connected to it. So run the following commands in the `psql` prompt (type `psql` on command line and it should take you to the `>psql prompt`) if that is not the case, to create and connect to the database:
    ```
    CREATE DATABASE tournament;
    \c tournament
    ``` -->

- By default, the owner of the database is 'vagrant' and this is also specified explicitly in the `tournament.sql` file at line 15: `ALTER DATABASE tournament OWNER TO vagrant;`, and in `tournament.py` at line 12: `psycopg2.connect("dbname=tournament user=vagrant")` while connecting to the database. You can run this as the `vagrant` user by running a Vagrant VM on your system using the provided `Vagrantfile` and setup-config file `pg_config.sh` (requires installation of Vagrant and VirtualBox) and running `vagrant up` and then, `vagrant ssh` from the directory that contains the `Vagrantfile`, OR

- You can configure your own installation of PostgreSQL by referring to the `pg_config.sh` file at the lines 13 to 16. See example changes below:
```
 13 su postgres -c 'createuser -dRS <your-user-name>'
 14 su <your-user-name> -c 'createdb'
 15 su <your-user-name> -c 'createdb tournament'
 16 su <your-user-name> -c 'psql forum -f /vagrant/forum/tournament.sql'
 ```


- Run `python tournament_test.py` and you should see the following result if everything goes well:
```
1. Old matches can be deleted.
2. Player records can be deleted.
3. After deleting, countPlayers() returns zero.
4. After registering a player, countPlayers() returns 1.
5. Players can be registered and deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After one match, players with one win are paired.
Success!  All tests pass!
```

## Limitations
- The database schema has provision for a tie in a match but the API does not currently implement it.
- This system will currently only work for a single tournament and needs to be updated to handle multiple
tournaments.
