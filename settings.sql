-- settings.sql
CREATE DATABASE photokeepr;
CREATE USER photouser WITH PASSWORD 'photo';
GRANT ALL PRIVILEGES ON DATABASE photokeepr TO photouser;