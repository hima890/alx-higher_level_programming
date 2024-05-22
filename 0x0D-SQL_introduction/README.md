# SQL Introduction - Task Readme

This repository contains a set of SQL scripts for various database management tasks using MySQL. Each script is designed to perform a specific operation, such as listing databases, creating tables, and manipulating data. Below is a detailed description of each task and the corresponding script file.

## Task Descriptions

### 0. List databases
**Script File:** `0-list_databases.sql`

This script lists all databases on your MySQL server.

```sql
SHOW DATABASES;
```

### 1. Create a database
**Script File:** `1-create_database_if_missing.sql`

This script creates a database named `hbtn_0c_0` if it does not already exist.

```sql
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
```

### 2. Delete a database
**Script File:** `2-remove_database.sql`

This script deletes the database `hbtn_0c_0` if it exists.

```sql
DROP DATABASE IF EXISTS hbtn_0c_0;
```

### 3. List tables
**Script File:** `3-list_tables.sql`

This script lists all the tables of a specified database. The database name is passed as an argument.

```sql
SHOW TABLES;
```

### 4. Create a table
**Script File:** `4-first_table.sql`

This script creates a table named `first_table` with the following columns:
- `id` INT
- `name` VARCHAR(256)

```sql
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
```

### 5. Full description
**Script File:** `5-full_table.sql`

This script prints the full description of the table `first_table` without using the `DESCRIBE` or `EXPLAIN` statements.

```sql
SHOW CREATE TABLE first_table;
```

### 6. List all rows in a table
**Script File:** `6-list_values.sql`

This script lists all rows in the table `first_table`.

```sql
SELECT * FROM first_table;
```

### 7. Insert a new row
**Script File:** `7-insert_value.sql`

This script inserts a new row into the table `first_table` with `id = 89` and `name = 'Best School'`.

```sql
INSERT INTO first_table (id, name) VALUES (89, 'Best School');
```

### 8. Count rows with a specific id
**Script File:** `8-count_89.sql`

This script counts the number of records with `id = 89` in the table `first_table`.

```sql
SELECT COUNT(*) FROM first_table WHERE id = 89;
```

### 9. Full table creation
**Script File:** `9-full_creation.sql`

This script creates a table `second_table` with the following columns:
- `id` INT
- `name` VARCHAR(256)
- `score` INT

It also inserts multiple rows into the table.

```sql
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

INSERT INTO second_table (id, name, score) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
```

### 10. List by best score
**Script File:** `10-top_score.sql`

This script lists all records of the table `second_table`, displaying both the score and the name, ordered by score in descending order.

```sql
SELECT score, name FROM second_table ORDER BY score DESC;
```

### 11. Select the best scores
**Script File:** `11-best_score.sql`

This script lists all records with a score greater than or equal to 10 in the table `second_table`, ordered by score in descending order.

```sql
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
```

### 12. Update a score
**Script File:** `12-no_cheating.sql`

This script updates the score of 'Bob' to 10 in the table `second_table`.

```sql
UPDATE second_table SET score = 10 WHERE name = 'Bob';
```

### 13. Remove low scores
**Script File:** `13-change_class.sql`

This script removes all records with a score less than or equal to 5 in the table `second_table`.

```sql
DELETE FROM second_table WHERE score <= 5;
```

### 14. Calculate average score
**Script File:** `14-average.sql`

This script computes the average score of all records in the table `second_table`.

```sql
SELECT AVG(score) AS average FROM second_table;
```

### 15. Count records by score
**Script File:** `15-groups.sql`

This script lists the number of records with the same score in the table `second_table`.

```sql
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
```

### 16. List records with names
**Script File:** `16-no_link.sql`

This script lists all records of the table `second_table` with non-empty names, ordered by score in descending order.

```sql
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
```

### 17. Convert to UTF8
**Script File:** `100-move_to_utf8.sql`

This script converts the `hbtn_0c_0` database, the `first_table` table, and the `name` field in `first_table` to UTF8 (utf8mb4, collate utf8mb4_unicode_ci).

```sql
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE hbtn_0c_0.first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 18. Average temperature
**Script File:** `101-avg_temperatures.sql`

This script displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

```sql
SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
```

### 19. Top city temperatures
**Script File:** `102-top_city.sql`

This script displays the top 3 city temperatures during July and August, ordered by temperature (descending).

```sql
SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
WHERE month IN ('July', 'August')
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
```

### 20. Max temperature by state
**Script File:** `103-max_state.sql`

This script displays the max temperature of each state, ordered by state name.

```sql
SELECT state, MAX(temperature) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
```

## Repository Structure

- **GitHub repository:** `alx-higher_level_programming`
- **Directory:** `0x0D-SQL_introduction`
- **Files:**
  - `0-list_databases.sql`
  - `1-create_database_if_missing.sql`
  - `2-remove_database.sql`
  - `3-list_tables.sql`
  - `4-first_table.sql`
  - `5-full_table.sql`
  - `6-list_values.sql`
  - `7-insert_value.sql`
  - `8-count_89.sql`
  - `9-full_creation.sql`
  - `10-top_score.sql`
  - `11-best_score.sql`
  - `12-no_cheating.sql`
  - `13-change_class.sql`
  - `14-average.sql`
  - `15-groups.sql`
  - `16-no_link.sql`
  - `100-move_to_utf8.sql`
  - `101-avg_temperatures.sql`
  - `102-top_city.sql`
  - `103-max_state.sql`

## Usage

To run any of these scripts, use the following command format, replacing `script_file.sql` with the appropriate file name:

```sh
mysql -hlocalhost -uroot -p < script_file.sql
```

You will be prompted to enter the MySQL root user's password.

For scripts that require a specific database name, you can pass it as an argument:

```sh
mysql -hlocalhost -uroot -p database_name < script_file.sql
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

