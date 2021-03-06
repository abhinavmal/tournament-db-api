-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- drop table if exists players cascade;
-- drop table if exists matches cascade;
drop database if exists tournament;

create database tournament;

ALTER DATABASE tournament OWNER TO vagrant;

\c tournament;

-- create database tournament;

-- ALTER DATABASE tournament OWNER TO abhinav;

create table players (
    id serial unique,
    name text
);

create table matches (
    round_id serial,
    winner_id serial references players(id),
    loser_id serial references players(id),
    tie boolean DEFAULT FALSE
);

-- Create Views

create view players_wins as (select players.id, players.name, count(matches.winner_id) as win_count
            from players left join matches on players.id = matches.winner_id group by players.id, players.name
            order by win_count desc);

create view matches_agg as (select players.id, players.name,
            case when matches.winner_id IS NULL then 0 ELSE count(players.id) END as total
            from players left join matches on players.id = matches.winner_id or players.id = matches.loser_id
            group by players.id, players.name, matches.winner_id);


-- Drop Tables if they exist
-- drop table IF EXISTS Players;
-- drop table IF EXISTS Matches
