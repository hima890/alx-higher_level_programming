### README for SQLAlchemy and ORM Concepts

#### Introduction
This repository demonstrates the usage of SQLAlchemy, an SQL toolkit and Object-Relational Mapping (ORM) library for Python. SQLAlchemy provides a full suite of well-known enterprise-level persistence patterns, designed for efficient and high-performing database access.

#### Project Structure
- **model_state.py**: Defines the `State` class and its relationship with the `City` class.
- **model_city.py**: Defines the `City` class and its relationship with the `State` class.
- **100-relationship_states_cities.py**: A script that creates a new `State` “California” with a `City` “San Francisco” in the database `hbtn_0e_100_usa`.

#### Prerequisites
- Python 3.x
- SQLAlchemy
- MySQLdb
- MySQL server

#### Installation
1. **Clone the repository**:
    ```sh
    git clone https://github.com/hima890/sqlalchemy_orm_example.git
    cd sqlalchemy_orm_example
    ```

2. **Set up a virtual environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```sh
    pip install SQLAlchemy MySQL-python
    ```

4. **Set up MySQL server**:
    Ensure your MySQL server is running and accessible. Create a database named `hbtn_0e_100_usa`.

#### Models
1. **State Model** (`model_state.py`):
    - Represents the `states` table.
    - Attributes:
        - `id`: Integer, primary key.
        - `name`: String(128), cannot be null.
    - Relationships:
        - `cities`: One-to-many relationship with the `City` class. If the `State` is deleted, all linked `City` objects are automatically deleted.

2. **City Model** (`model_city.py`):
    - Represents the `cities` table.
    - Attributes:
        - `id`: Integer, primary key.
        - `name`: String(128), cannot be null.
        - `state_id`: Integer, foreign key to `states.id`, cannot be null.
    - Relationships:
        - `state`: Many-to-one relationship with the `State` class.

#### Script
**100-relationship_states_cities.py**:
- Description: A script that adds a `State` “California” with a `City` “San Francisco” to the database `hbtn_0e_100_usa`.
- Usage:
    ```sh
    python3 100-relationship_states_cities.py <mysql_username> <mysql_password> <database_name>
    ```
- Arguments:
    - `mysql_username`: Your MySQL username.
    - `mysql_password`: Your MySQL password.
    - `database_name`: The database to connect to.

#### Example Output
After running the script, the database should have a new entry in the `states` table with the name "California" and an associated entry in the `cities` table with the name "San Francisco".

#### Troubleshooting
- Ensure your MySQL server is running and the credentials provided are correct.
- If there are connection issues, check your MySQL server’s bind address and port.

#### Additional Resources
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/14/)
- [MySQL Documentation](https://dev.mysql.com/doc/)

#### License
This project is licensed under the MIT License.

#### Author
[Ibrahim Hanafi](https://github.com/hima890) - Initial work.

Feel free to contribute to this repository by creating issues or submitting pull requests.
