import click
from .app import app, db
from .models import Album, Author


@app.cli.command()
def syncdb():
    '''
     Création de toutes les tables de la BD
    '''
    db.create_all()


@app.cli.command()
@click.argument('filename')
def loaddb(filename):
    '''
     Create all tables and populate them with data in filename
    '''
    db.create_all()

    import yaml
    albums = yaml.load(open(filename), Loader=yaml.FullLoader)

    # Première passe qui lit tous les auteurs
    # et les stocke en BD en leur attribuant un id
    authors = dict()
    for alb in albums:
        aut = alb["by"]
        if aut not in authors:
            obj = Author(name=aut)
            # On ajoute l'objet o à la Base :
            db.session.add(obj)
            authors[aut] = obj
    # On dit à la DB d'intégrer toutes les nouvelles données
    # ce qui permet aux auteurs d'avoir un id
    db.session.commit()

    # Création des Albums
    for alb in albums:
        # on récupère l'objet Auteur correspondant
        aut = authors[alb["by"]]
        album = Album(entryID=alb["entryId"],
                    title=alb["title"],
                    #genre=alb["genre"],
                    img=alb["img"],
                    parent=alb["parent"],
                    releaseYear=alb["releaseYear"],
                    spotify=alb["spotify"],
                    author_id=aut.id)
        # On ajoute l'objet album à la Base :
        db.session.add(album)
    # on commite
    db.session.commit()
