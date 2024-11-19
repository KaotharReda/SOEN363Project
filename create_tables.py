import psycopg2

# Function to create a database connection
def create_connection():
    try:
        connection = psycopg2.connect(
            dbname="spotifyapplemusicdb", 
            user="postgres",  
            password="postgrespass",  
            host="localhost" 
        )
        return connection
    except Exception as e:
        print("Error connecting to the database:", e)
        return None

# Function to create tables
def create_tables(connection):
    with connection.cursor() as cursor:
        # Create Song table with auto-increment id
        cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS Song (
                song_id SERIAL PRIMARY KEY,
                       title VARCHAR(255),
                       artist VARCHAR(255),
                       album VARCHAR(255),
                       release_date DATE,
                       genre VARCHAR(100)
            );
        ''')
        print('Song table created successfully')
        connection.commit()

        # Create Spotify-specific song table with auto-increment id
        cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS SpotifySong (
                spotify_song_id SERIAL PRIMARY KEY,
                song_id INT REFERENCES Song(song_id),
                spotify_popularity_score INT CHECK (spotify_popularity_score >= 0 AND spotify_popularity_score <=100),
                spotify_stream_count INT CHECK (spotify_stream_count >= 0),
                spotify_url VARCHAR(255)
            ); 
        ''') 
        print('SpotifySong table created successfully')
        connection.commit()

        # Create Apple Music-specific song table with auto-increment id
        cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS AppleMusicSong (
                apple_music_song_id SERIAL PRIMARY KEY,
                song_id INT REFERENCES Song(song_id),
                apple_music_chart_position INT CHECK (apple_music_chart_position >= 0),
                apple_music_stream_count INT CHECK (apple_music_stream_count >= 0),
                apple_music_url VARCHAR(255)
            );
        ''')
        print('AppleMusicSong table created successfully')
        connection.commit()


# Main function to run the script
def main():
    connection = create_connection()
    if connection:
        create_tables(connection)
        print("Tables created successfully!")
        connection.close()  # Close the connection

if __name__ == "__main__":
    main()
