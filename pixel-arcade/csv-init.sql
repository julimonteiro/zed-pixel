CREATE TEMP VIEW csv AS SELECT * FROM read_csv_auto(getenv('ZED_FILE'), header = true);
SELECT * FROM csv LIMIT 20;
