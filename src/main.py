import sqlalchemy
from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, create_engine
try:
    import cPickle
except:
    import pickle as cPickle
import math
import struct
import pyaudio
from random import randint
import random
import codecs
from noise import pnoise1

Base = declarative_base()

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
    def __init__(self, beats):
        self.beat = list()
        for i in range(64):
            #generate beat
            play_sound = pnoise1(0, 1)
            amplitude = pnoise1(1, 100)
            duration = random.uniform(.01, 1)
            self.beat.append((play_sound, amplitude, duration))


    def get_beat():
        return self.beat

class Sound():
    def __init__(self, b, notes):
        self.sound = list()
        for beat in b.beat:
            #generate notes
            frequency = pnoise1(1000, 5000)
            self.sound.append((frequency, beat))


    def get_sound():
        return self.sound


fs = 48000
p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paFloat32,
    channels=1,
    rate=fs,
    output=True)


def get_beat_pattern(beats, ranks):
    return 0


def get_sound_pattern(notes, ranks):
    return 0


def play_tone(frequency, amplitude, duration, fs, stream):
    N = int(fs / frequency)
    T = int(frequency * duration)  # repeat for T cycles
    dt = 1.0 / fs
    # 1 cycle
    tone = (amplitude * math.sin(2 * math.pi * frequency * n * dt)
            for n in xrange(N))
    # todo: get the format from the stream; this assumes Float32
    data = ''.join(struct.pack('f', samp) for samp in tone)
    for n in xrange(T):
        stream.write(data)


def get_rank():
    rank = input("You like it???? rate me [0-10] plz: ")
    return rank


def main():
    session = Session()
    beat_pattern = [0]
    note_pattern = [0]
    
    if session.query(Songs).first() is not None:
        info = list()
        ranks = list()
        for x in session.query(Songs):
            info.append(x.song)
            ranks.append(x.rank)
            
        beat_pattern = get_beat_pattern([list(cPickle.loads(b))[1] for b in info], ranks)
        note_pattern = get_sound_pattern([list(cPickle.loads(n))[0] for n in info], ranks)
        
    beat = Beat(beat_pattern)
    sound = Sound(beat, note_pattern)
    #for note in sound.sound:
     #   if note[1][0] == 1:
      #      play_tone(note[0], note[1][1], note[1][2], fs, stream)
    rank = get_rank()
    song = Songs(rank, cPickle.dumps(zip(sound.sound)))
    session.add(song)
    session.commit()
    for u in session.query(Songs):
        print("Rank: ", u.rank, "Song: ", list(cPickle.loads(u.song)))
    

if __name__ == "__main__":
    main()

