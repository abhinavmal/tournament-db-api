# tournament-db-api
A DB-API using PostgreSQL to implement a Swiss tournament system.

## Dependencies
- Python 2.7
- [Bleach](https://bleach.readthedocs.io/en/latest/) for input sanitization
- [psycopg2](http://initd.org/psycopg/)
- [PostgreSQL](https://www.postgresql.org/)

## Testing the Tournament DB-API system
- The implementation assumes that a database with the name `tournament` has been already created, and the user
is connected to it. So run the following commands in the `psql` prompt (type `psql` on command line and it should take you to the `>psql prompt`) if that is not the case, to create and connect to the database:
    ```
    CREATE DATABASE tournament;
    \c tournament
    ```

- Run `git clone git@github.com:abhinavmal/tournament-db-api.git` on the command line and
`cd tournament-db-api` which contains `tournament_test.py`.
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
