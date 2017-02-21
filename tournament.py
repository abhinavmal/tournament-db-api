#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    cur = conn.cursor()
    cur.execute(""" delete from matches """)
    conn.commit()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    cur = conn.cursor()
    cur.execute(""" delete from players """)
    conn.commit()
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    cur = conn.cursor()
    cur.execute(""" select count(*) as num from players """)
    players = cur.fetchone()
    conn.close()
    return int(players[0])


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect()
    cur = conn.cursor()
    clean_name = bleach.clean(name)
    sql = """ insert into players values (default, %s) """
    params = (clean_name,)
    cur.execute(sql, params)
    conn.commit()
    conn.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place,
    or a player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn = connect()
    cur = conn.cursor()
    sql = """select players_wins.id, players_wins.name, \
             players_wins.win_count, matches_agg.total \
             from players_wins left join matches_agg on \
             players_wins.id = matches_agg.id group by players_wins.id, \
             players_wins.name, players_wins.win_count, matches_agg.total \
             order by players_wins.win_count desc;"""
    cur.execute(sql)
    player_standings = cur.fetchall()
    return player_standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn = connect()
    cur = conn.cursor()
    clean_winner = bleach.clean(winner)
    clean_loser = bleach.clean(loser)
    sql = """ insert into matches values (default, %s, %s) """
    params = (clean_winner, clean_loser)
    cur.execute(sql, params)
    conn.commit()
    conn.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()
    pairs = []
    i = 0
    while i < len(standings):
        pair = (standings[i][0], standings[i][1],
                standings[i+1][0], standings[i+1][1])
        pairs.append(pair)
        i += 2
    return pairs
