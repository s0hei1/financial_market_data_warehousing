from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from datetime import datetime

type String16 = str
type String8 = str

class Base(DeclarativeBase):
    type_annotation_map = {
        String16 : String(16),
        String8 : String(8)
    }

class DimDateTime:
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

class DimTimeFrame:
    __tablename__ = 'dim_time_frame'
    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    name : Mapped[String16]
    included_1m : Mapped[int | None] = mapped_column(unique= True)

class DimCurrencyPair:
    id: Mapped[int] = mapped_column(primary_key=True)
    pair_name : Mapped[String16] = mapped_column(unique=True)
    base_currency : Mapped[String8]
    quote_currency : Mapped[String8]

class DimCandle:
    __tablename__ = 'dim_candle'
    id : Mapped[int] = mapped_column(primary_key=True)
    open : Mapped[float]
    high : Mapped[float]
    low : Mapped[float]
    close : Mapped[float]
    date_time : Mapped[datetime] = mapped_column()

