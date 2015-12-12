import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.dialects import sqlite
import pygame
import pygame.midi
from time import sleep
import pickle

Base = declarative_base()
note_list = [27.5, 29.1352, 30.8677, ]


class Songs(Base):
    __tablename__ = 'music'

    id = Column(Integer, primary_key=True)
    rank = Column(Integer)
    song = Column(String)

    def __init__(self, rank, song):
        self.rank = rank
        self.song = song

    def __repr__(self):
        return "<(song='%s', rank='%s')>" % (self.song, self.rank)

engine = create_engine('sqlite:///songs.db')
Session = sessionmaker()
Session.configure(bind=engine)
Base.metadata.create_all(engine)

class Beat:
    def __init__(self):
        self.beat = list()
        for i in range(64):
            #generate beat
            play_sound = 1
            amplitude = 100
            accent = 2
            self.beat.append((play_sound, amplitude, accent))

    def get_beat():
        return self.beat

class Sound():
    def __init__(self, b):
        self.sound = list()
        for beat in b.beat:
            #generate notes
            key = '#'
            octave = 0
            note = 'A'
            self.sound.append((note, key, octave, beat))

    def get_sound():
        return self.sound

def play_sound(sound):
    pygame.init()
    pygame.midi.init()

    port = pygame.midi.get_default_output_id()
    midi_out = pygame.midi.Output(port, 0)
    midi_out.set_instrument(0)

    for n in sound.sound:
        b = n[3]
        if b[0]:
            #play = Note('[0]-[1]'.format(n.note, n.key))
            midinum = n[2]
            velocity = b[3]
            midi_out.note_on(72, 127)
            sleep(.5)
            midi_out.note_off(72, 127)

def get_rank():
    rank = 0
    return rank

def main():
    beat = Beat()
    sound = Sound(beat)
    play_sound(sound)
    rank = get_rank()
    song = Songs(rank, pickle.dumps(sound))
    session = Session()
    session.add(song)
    session.commit()
    for u in session.query(Songs):
        print(u)

if __name__ == "__main__":
    main()

