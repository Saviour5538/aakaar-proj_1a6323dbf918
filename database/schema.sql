-- Create users table
                CREATE TABLE users (
                    id INT PRIMARY KEY,
                    username VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NOT NULL,
                    password VARCHAR(255) NOT NULL
                );

                -- Create sessions table
                CREATE TABLE sessions (
                    id INT PRIMARY KEY,
                    user_id INT NOT NULL,
                    session_id VARCHAR(255) NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                );

                -- Create indexes on frequently queried columns
                CREATE INDEX idx_users_username ON users (username);
                CREATE INDEX idx_sessions_session_id ON sessions (session_id);