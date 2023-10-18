CREATE DATABASE reporting;
CREATE USER reportusr WITH PASSWORD 'StrongDBPassword';
GRANT ALL PRIVILEGES ON DATABASE reporting TO postgres;
ALTER ROLE reportusr SET client_encoding TO 'utf8';
ALTER ROLE reportusr SET default_transaction_isolation TO 'read committed';
ALTER ROLE reportusr SET timezone TO 'CET';
\c reporting postgres
grant all on schema public to reportusr;
