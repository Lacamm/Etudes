# modele_4_final.py
# Version 4 du modèle

repertoire='/pub/1A/DocNum/PhotosDeMartine/images/'

images = ["adler-2611528__340.jpg","adler-2872995__340.jpg","adler-3366239__340.jpg","adler-339128__340.jpg","adler-3551609__340.jpg","alcedo-atthis-881594__340.jpg","animal-1854225__340.jpg","bald-eagle-1728739__340.jpg","bald-eagle-2715461__340.jpg","bald-eagles-341898__340.jpg","barn-owl-1107397__340.jpg","barn-owl-2550068__340.jpg","barn-owl-2988291__340.jpg","beautiful-16736__340.jpg","bee-eaters-3749679__340.jpg","bird-1045954__340.jpg","bird-197052__340.jpg","bird-2823767__340.jpg","bird-3113835__340.jpg","bird-3158784__340.jpg","bird-3183441__340.jpg","bird-3732867__340.jpg","bird-386725__340.jpg","blank.gif","blue-bird-ultramarine-flycatcher-superciliaris-260nw-5082443.jpg","book-863418__340.jpg","broad-billed-hummingbird-using-different-260nw-526559815.jpg","burrowing-3649048__340.jpg","chaffinch-1420407__340.jpg","crow-3604685__340.jpg","dove-2680487__340.jpg","eagle-1753002__340.jpg","eagle-217591__340.jpg","easter-349026__340.jpg","european-eagle-owl-2010346__340.jpg","flock-birds-on-white-background-260nw-198745910.jpg","flock-flying-birds-starlings-vector-260nw-302351489.jpg","flock-flying-birds-vector-260nw-439952854.jpg","gulls-370012__340.jpg","hummingbird-1823829__340.jpg","hummingbird-691483__340.jpg","jay-548381__340.jpg","kingfisher-1068684__340.jpg","kingfisher-1905255__340.jpg","kingfisher-2046453__340.jpg","kingfisher-881975__340.jpg","mallard-3747770__340.jpg","owl-1576572__340.jpg","owl-1705112__340.jpg","owl-1727370__340.jpg","owl-1834152__340.jpg","owl-3184032__340.jpg","owl-50267__340.jpg","parrot-2756488__340.jpg","peacock-1868__340.jpg","peacock-2201428__340.jpg","peacock-2363750__340.jpg","peacock-feather-186339__340.jpg","pelican-336583__340.jpg","portrait-1072696__340.jpg","red-robin-3743702__340.png","robin-3750940__340.jpg","seagull-1511862__340.jpg","seagull-1900657__340.jpg","seagull-79658__340.jpg","set-birds-flowers-line-drawings-260nw-412369294.jpg","sparrow-9950__340.jpg","spring-bird-2295431__340.jpg","spring-bird-2295434__340.jpg","spring-bird-2295436__340.jpg","sunset-100367__340.jpg","swan-2107052__340.jpg","swan-293157__340.jpg","swan-3466552__340.jpg","swans-1436266__340.jpg","vector-silhouette-flying-birds-on-260nw-537952999.jpg","white-tailed-eagle-416795__340.jpg"]

def tableau_to_dico(tableau):
    """
        Transforme la liste de tuple en dictionnaire
    """
    dico = dict()
    for n in range(len(tableau)):
        dico['page-'+str(n)+'.html'] = tableau[n]
    return dico


def tableau_liste_to_tableau_infos(tableau):
    """
        Rajoute les liens des pages
    """
    tableau_infos_pages = []
    tableau_infos=()

    for n in range(len(tableau)):
        if n == 0:
            tableau_infos=(tableau[n],'page-'+str(n+1)+'.html',None)
        elif n == len(tableau)-1:
            tableau_infos=(tableau[n],None,'page-'+str(n-1)+'.html')
        else:
            tableau_infos=(tableau[n],'page-'+str(n+1)+'.html','page-'+str(n-1)+'.html')
        tableau_infos_pages.append(tableau_infos)

    return tableau_infos_pages


def liste_images_to_tableau_liste_images(liste):
    """
    trie le nombre d'image par page
    """
    cpt = 0
    liste_liens = []
    petite_liste = []
    for img in liste:
        if cpt ==3:
            liste_liens.append(petite_liste)
            petite_liste = []
            petite_liste.append(img)
            cpt = 1
        else:
            petite_liste.append(img)
            cpt += 1
    liste_liens.append(petite_liste)
    return liste_liens

tableau_liste_images = liste_images_to_tableau_liste_images(images)

tableau_infos_pages=tableau_liste_to_tableau_infos(tableau_liste_images)

dico_infos_pages=tableau_to_dico(tableau_infos_pages)