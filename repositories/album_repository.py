from db.run_sql import run_sql
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

from models.album import Album


def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        artist = artist_repository.select(result['artist_id'])
        album = Album(result['title'], result['genre'], artist, result['id'] )
    return album

def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        album = Album(row['title'], row['genre'], row['id'] )
        albums.append(album)
    return albums


def delete_all():
    sql = "DELETE  FROM albums"
    run_sql(sql)