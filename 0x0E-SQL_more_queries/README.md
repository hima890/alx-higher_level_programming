# SQL More Queries 📜💻

Welcome to the **SQL More Queries** project! This project contains various SQL scripts designed to perform complex queries, manage databases, and handle user privileges. Below you'll find detailed descriptions of each task along with their corresponding script files.

## Tasks Overview

### Task 0: My privileges! 🔐
**File:** `0-privileges.sql`

This script lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (localhost).

### Task 1: Root user 🌟
**File:** `1-create_user.sql`

This script creates the MySQL server user `user_0d_1` with all privileges and sets their password to `user_0d_1_pwd`.

### Task 2: Read user 📖
**File:** `2-create_read_user.sql`

This script creates the database `hbtn_0d_2` and the user `user_0d_2`, who only has SELECT privileges on this database. The user's password is set to `user_0d_2_pwd`.

### Task 3: Always a name 📛
**File:** `3-force_name.sql`

This script creates the table `force_name` in a given database. The table has an `id` column of type INT and a `name` column of type VARCHAR(256) that cannot be NULL.

### Task 4: ID can't be null 🚫
**File:** `4-never_empty.sql`

This script creates the table `id_not_null` in a given database. The `id` column has a default value of 1, and the `name` column is a VARCHAR(256).

### Task 5: Unique ID 🆔
**File:** `5-unique_id.sql`

This script creates the table `unique_id` in a given database. The `id` column is an INT with a default value of 1 and must be unique, while the `name` column is a VARCHAR(256).

### Task 6: States table 🗺️
**File:** `6-states.sql`

This script creates the database `hbtn_0d_usa` and the table `states` with a unique, auto-generated `id` and a non-null `name` column.

### Task 7: Cities table 🏙️
**File:** `7-cities.sql`

This script creates the `cities` table in the `hbtn_0d_usa` database. The table has an auto-generated primary key `id`, a `state_id` that is a foreign key referencing the `states` table, and a non-null `name` column.

### Task 8: Cities of California 🌇
**File:** `8-cities_of_california_subquery.sql`

This script lists all the cities in California from the `hbtn_0d_usa` database, sorted by `cities.id` in ascending order.

### Task 9: Cities by States 🌆
**File:** `9-cities_by_state_join.sql`

This script lists all cities in the `hbtn_0d_usa` database along with their state names, sorted by `cities.id` in ascending order.

### Task 10: Genre ID by show 📺
**File:** `10-genre_id_by_show.sql`

This script lists all TV shows in the `hbtn_0d_tvshows` database that have at least one genre linked, sorted by `tv_shows.title` and `tv_show_genres.genre_id`.

### Task 11: Genre ID for all shows 🎥
**File:** `11-genre_id_all_shows.sql`

This script lists all TV shows in the `hbtn_0d_tvshows` database and their genres. If a show doesn’t have a genre, it displays NULL.

### Task 12: No genre 🚫
**File:** `12-no_genre.sql`

This script lists all TV shows in the `hbtn_0d_tvshows` database that do not have any genre linked, sorted by `tv_shows.title`.

### Task 13: Number of shows by genre 📊
**File:** `13-count_shows_by_genre.sql`

This script lists all genres and the number of shows linked to each genre in the `hbtn_0d_tvshows` database, sorted in descending order by the number of shows.

### Task 14: My genres 🎭
**File:** `14-my_genres.sql`

This script lists all genres of the show Dexter in the `hbtn_0d_tvshows` database, sorted by genre name.

### Task 15: Only Comedy 😂
**File:** `15-comedy_only.sql`

This script lists all comedy shows in the `hbtn_0d_tvshows` database, sorted by show title.

### Task 16: List shows and genres 🎬
**File:** `16-shows_by_genre.sql`

This script lists all shows and their genres from the `hbtn_0d_tvshows` database. If a show doesn’t have a genre, it displays NULL in the genre column.

### Task 17: Not my genre 🚷
**File:** `100-not_my_genres.sql`

This script lists all genres not linked to the show Dexter in the `hbtn_0d_tvshows` database, sorted by genre name.

## Repository 📂
**GitHub repository:** [alx-higher_level_programming](https://github.com/user/alx-higher_level_programming)

**Directory:** `0x0E-SQL_more_queries`

Each script can be executed with the following command:
```bash
cat <script_name>.sql | mysql -hlocalhost -uroot -p <database_name>
```
Replace `<script_name>` with the appropriate file name and `<database_name>` with the database name if required.

Happy querying! 🚀✨