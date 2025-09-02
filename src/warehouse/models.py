from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from datetime import datetime

type String16 = str
type String8 = str

class Base(DeclarativeBase):
    type_annotation_map = {
        String16 : String(16),
        String8 : String(8)
    }

class Flags(Base):
    __tablename__ = 'flags'
    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    is_first_run : Mapped[bool | None]

class DimDateTime(Base):
    __tablename__ = 'dim_date_time'

    date_time : Mapped[datetime] = mapped_column(primary_key=True, index=True)
    is_holiday : Mapped[bool]
    is_weekend : Mapped[bool]
    weekday : Mapped[int]
    usa_session : Mapped[bool]
    london_session : Mapped[bool]
    tokyo_session : Mapped[bool]
    sydney_session : Mapped[bool]
    day_of_month : Mapped[int]
    month_id : Mapped[int]
    year_id : Mapped[int]
    session_id : Mapped[int]

class DimTimeFrame(Base):
    __tablename__ = 'dim_time_frame'
    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    name : Mapped[String16]
    included_1m : Mapped[int | None] = mapped_column(unique= True)

class DimSymbol(Base):
    __tablename__ = 'symbol'
    id: Mapped[int] = mapped_column(primary_key=True)
    pair_name : Mapped[String16] = mapped_column(unique=True)
    base_currency : Mapped[String8]
    quote_currency : Mapped[String8]

class DimCandle(Base):
    __tablename__ = 'dim_candle'
    id : Mapped[int] = mapped_column(primary_key=True)
    open : Mapped[float]
    high : Mapped[float]
    low : Mapped[float]
    close : Mapped[float]
    date_time : Mapped[datetime] = mapped_column(ForeignKey('dim_date_time.date_time'))
    symbol_id : Mapped[int] = mapped_column(ForeignKey('symbol.id'))
    time_frame_id : Mapped[int] = mapped_column(ForeignKey('dim_time_frame.id'))

    dim_date_time : Mapped[DimDateTime] = relationship("DimDateTime")
    dim_symbol : Mapped[DimSymbol] = relationship("DimSymbol")
    dim_time_frame : Mapped[DimTimeFrame] = relationship("DimTimeFrame")



