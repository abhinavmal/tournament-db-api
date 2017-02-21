# tournament-db-api
A DB-API using PostgreSQL to implement a Swiss tournament system.

## Dependencies
- Python 2.7
- [Bleach](https://bleach.readthedocs.io/en/latest/) for input sanitization
- [psycopg2](http://initd.org/psycopg/)
- [PostgreSQL](https://www.postgresql.org/)

## Testing the Tournament DB-API system
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
