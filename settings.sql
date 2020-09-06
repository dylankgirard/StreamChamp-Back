-- settings.sql
CREATE DATABASE streamchamp_back;
CREATE USER streamchamp_user
WITH PASSWORD 'streamchamp_2020';
GRANT ALL PRIVILEGES ON DATABASE streamchamp_back TO streamchamp_user;