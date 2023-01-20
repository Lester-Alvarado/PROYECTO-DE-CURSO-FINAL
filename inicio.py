from sqlalchemy.orm import declarative_base,sessionmaker, relationship
from sqlalchemy import Column, Integer, String, create_engine, delete, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property

Base = declarative_base()
engine = create_engine("sqlite:///:memory:")

class Pelicula(Base):
  __tablename__ = "pelicula"


  id = Column(Integer, primary_key=True)
  titulo = Column(String, nullable=False)
  imagen_poster = Column(String, nullable=False)
  clasificacion = Column(String)
  funciones = Column(Integer, unique=True)
  id_funcion = Column(Integer, primary_key=True)
  fecha = Column(String, unique=True)
  hora = Column(String, unique=True)


if __name__ == "__main__":
  Base.metadata.create_all(engine)

  Session = sessionmaker(bind=engine)
  session = Session()

  pelicula = Pelicula(
    titulo="Avatar: El Camino del Agua",
    imagen_poster="https://cdn.shopify.com/s/files/1/0057/3728/3618/products/avatar-the-way-of-water_zqtfz53g_480x.progressive.jpg?v=1654873098",
    clasificacion="Aventura, Acción, Ciencia ficción",
    funciones="1",
    fecha="19 de Enero 2023",
    hora="18:00 horas"
  )

  cantidad_peliculas = session.query(Pelicula).count()
  print(f"La cantidad de Peliculas es: {cantidad_peliculas}")

  session.add(pelicula)
  # session.commit()
  print(pelicula.titulo)

  pelicula2 = Pelicula(
    titulo="Super Mario Bros.",
    imagen_poster="https://cdn.shopify.com/s/files/1/0057/3728/3618/products/312925347_491450766268101_8828582980273617041_n_480x.progressive.jpg?v=1672865756",
    clasificacion="Animación, Aventura, Comedia",
    funciones="1",
    fecha="20 de Enero 2023",
    hora="19:00 horas"
  )
  session.add(pelicula2)
  # session.commit()

  pelicula3 = Pelicula(
    titulo="Gira Mundial de Trolls",
    imagen_poster="https://cdn.shopify.com/s/files/1/0057/3728/3618/products/trolls-world-tour_u7rr2rju_1_480x.progressive.jpg?v=1614116583",
    clasificacion="Animación, Aventura, Comedia" "Mayores de 10",
    funciones="1",
    fecha="21 de Enero 2023",
    hora="20:00 horas"
  )
  session.add(pelicula3)
  # session.commit()

  pelicula4 = Pelicula(
    titulo="Escarabajo azul",
    imagen_poster="https://cdn.shopify.com/s/files/1/0057/3728/3618/products/blue-beetle_qtxekmcw_480x.progressive.jpg?v=1673382997",
    clasificacion="Aventura, Acción, Ciencia ficción",
    funciones="1",
    fecha="22 de Enero 2023",
    hora="18:00 horas"
  )
  session.add(pelicula4)
  # session.commit()

  pelicula5 = Pelicula(
    titulo="Mazmorras y dragones: Honor entre ladrones",
    imagen_poster="https://cdn.shopify.com/s/files/1/0057/3728/3618/products/scan002_cf9be9aa-fa1f-4ff4-a0e9-c894e72e655e_480x.progressive.jpg?v=1672415990",
    clasificacion="Animación, Aventura, Comedia",
    funciones="7 pm a 9 pm",
    fecha="23 de Enero 2023",
    hora="19:00  a 21:00 horas"
  )

  cantidad_peliculas = session.query(Pelicula).count()
  print(f"La cantidad de Peliculas es: {cantidad_peliculas}")

  session.add(pelicula5)
  # session.commit()
  
  print(pelicula2)

