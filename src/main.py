import sqlalchemy

class Songs(Base):
    __tablename__ = 'music'

    id = Column(Integer, primary_key=True)
    rank = Column(Integer)
    note[64] = Column()

    def __repr__(self):
        return "<Song note='%s', rank='%s')>" % ([note for note in self.note], self.rank)

def main():
    print("running")

if __name__ == "__main__":
    main()

