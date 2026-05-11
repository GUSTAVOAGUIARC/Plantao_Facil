from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Troca(Base):
    __tablename__ = "trocaplantao"

    id = Column(Integer, primary_key=True, index=True)
    solicitante = Column(String(255), nullable=False)
    destinatario = Column(String(255), nullable=False)
    meudia = Column(String(10), nullable=False)
    horariosolicitante = Column(String(20), nullable=False)
    diacolega = Column(String(10), nullable=False)
    horariodestinatario = Column(String(20), nullable=False)
    motivo = Column(String(500), nullable=True)
    situacao = Column(String(50), default="Pendente")
    cpfSolicitante = Column(String(14),ForeignKey("users.cpf"), nullable=False)
    cpfDestinatario = Column(String(14),ForeignKey("users.cpf"), nullable=False)
    user = relationship("User", back_populates="trocas")