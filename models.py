from sqlalchemy.orm import DeclarativeBase, Mapped,mapped_column,relationship
from sqlalchemy import ForeignKey, Text
from typing import List

class Base(DeclarativeBase):
    pass



class User(Base):
    __tablename__ ='users'
    id:Mapped[int] = mapped_column(primary_key=True)
    username:Mapped[str] = mapped_column(nullable=False)
    email_address:Mapped[str]
    comments:Mapped[List["Comments"]] = relationship(back_populates='users')
    
    def __repr__(self) -> str:
        return f"<User username={self.username}>"
   


class Comments(Base):
    __tablename__ ='comments'
    id:Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column (ForeignKey('users.id'), nullable=False)
    text:Mapped[str] = mapped_column(Text, nullable=False)
    use:Mapped["User"] =relationship(back_populates='comments')
    
    def __repr__(self) -> str:
        return f"<Comment text= {self.text} by {self.user.username}>"