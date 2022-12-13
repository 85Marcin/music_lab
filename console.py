# Use this file to test your repository functions 
import pdb
from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist_1 = Artist('Linkin park')
album_1 = Album('hybrid theory', 'rock', artist_1)

artist_repository.save(artist_1)
album_repository.save(album_1)


artist_repository.select(artist_1.id)