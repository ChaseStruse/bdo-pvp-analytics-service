from sqlalchemy import Column, String, Date, Boolean, Integer, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, declarative_base
import uuid

Base = declarative_base()

class Match(Base):
	__tablename__ = "matches"
	id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
	match_type = Column(String, nullable=False)
	adventurer_name = Column(String, nullable=False)
	match_date = Column(Date, nullable=False)
	allied_team_win = Column(Boolean, nullable=False)

	player_stats = relationship("PlayerStats", back_populates="match", cascade="all, delete-orphan")


class PlayerStats(Base):
	__tablename__ = "player_stats"
	id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
	match_id = Column(UUID(as_uuid=True), ForeignKey("matches.id"), nullable=False)
	team = Column(Enum("allied", "enemy", name="team_enum"), nullable=False)

	adventurer_name = Column(String, nullable=False)
	class_name = Column(String, nullable=True)
	class_type = Column(String, nullable=True)
	kills = Column(Integer, nullable=False)
	deaths = Column(Integer, nullable=False)
	cc = Column(Integer, nullable=False)
	dealt = Column(Integer, nullable=False)
	taken = Column(Integer, nullable=False)
	healed = Column(Integer, nullable=False)
	mvp_ace = Column(String, nullable=True)

	match = relationship("Match", back_populates="player_stats")