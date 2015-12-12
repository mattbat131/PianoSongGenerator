import sqlalchemy

class Songs(Base):
    __tablename__ = 'music'

    id = Column(Integer, primary_key=True)
    rank = Column(Integer)
    note[64] = Column()

    def __repr__(self):
        return "<Song note='%s', rank='%s')>" % ([note for note in self.note], self.rank)

class Beat:
    def __init__(self):
        self.beat = list()
        for i in range(64):
            #generate beat
            play_sound = 0
            amplitude = 0
            accent = 0
            self.beat.append(zip(play_sound, amplitude, accent))

    def get_beat():
        return self.beat

class Sound(Beat):
    def __init__(self, note, type, octave):
        self.sound = list()
        for beat in self.beat:
            #generate notes
            key = 0
            octave = 0
            note = 0
            self.sound.append(zip(note, key, octave, beat))

    def get_sound():
        return self.sound

def main():
    print("running")

if __name__ == "__main__":
    main()

