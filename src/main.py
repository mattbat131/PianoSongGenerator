import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, create_engine
import mingus
import fluidsynth

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
    def __init__(self):
        self.beat = list()
        for i in range(64):
            #generate beat
            play_sound = 0
            amplitude = 0
            accent = 0
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
    for n in sound.sound:
        b = n[3]
        if b[0]:
            play = Note('[0]-[1]'.format(n.note, n.key))
            play.channel = n.octave
            play.velocity = b.amplitude
            fluidsynth.play_Note(play)

def get_rank():
    rank = 0
    print("GETTING RANK")
    return rank

def main():
    beat = Beat()
    sound = Sound(beat)
    play_sound(sound)
    rank = get_rank()
    song = Songs(rank, sound)
    session = Session()
    session.add(song)
    session.commit()

if __name__ == "__main__":
    main()

