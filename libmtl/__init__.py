# coding=utf-8
from Levenshtein import ratio

arr_abrev = {'AC': 'Ahuntsic-Cartierville',
             'AJ': 'Anjou',
             'BF': 'Beaconsfield',
             'BU': "Baie-d'Urfé",
             'BV': 'Sainte-Anne-de-Bellevue',
             'CL': 'Côte-Saint-Luc',
             'CN': 'Côte-des-Neiges-Notre-Dame-de-Grâce',
             'DO': 'Dollard-des-Ormeaux',
             'DV': 'Dorval',
             'HS': 'Hampstead',
             'ID': "L'Île-Dorval",
             'IS': "L'Île-Bizard-Sainte-Geneviève",
             'KL': 'Kirkland',
             'LC': 'Lachine',
             'LN': 'Saint-Léonard',
             'LR': 'Saint-Laurent',
             'LS': 'LaSalle',
             'ME': 'Montréal-Est',
             'MH': 'Mercier-Hochelaga-Maisonneuve',
             'MN': 'Montréal-Nord',
             'MO': 'Montréal-Ouest',
             'MR': 'Mont-Royal',
             'OM': 'Outremont',
             'PC': 'Pointe-Claire',
             'PM': 'Le Plateau-Mont-Royal',
             'PR': 'Pierrefonds-Roxboro',
             'RO': 'Rosemont-La Petite-Patrie',
             'RP': 'Rivière-des-Prairies-Pointe-aux-Trembles',
             'SO': 'Le Sud-Ouest',
             'SV': 'Senneville',
             'VD': 'Verdun',
             'VM': 'Ville-Marie',
             'VS': 'Villeray-Saint-Michel-Parc-Extension',
             'WM': 'Westmount'}

def get_abrev(name):
    """
    Get the abreviation for a given 'arrondissement' name.
    Uses Levensthein distance to match the name
    """
    ret = None
    dist = 0
    for abr, real_name in arr_abrev.items():
        new_dist = ratio(name, real_name)
        if new_dist > dist:
            dist = new_dist
            ret = abr

    return ret

def get_name(abr):
    """
    Given an abbreviation, return the name or "Unknown"
    """
    try:
        return arr_abrev[abr]
    except KeyError:
        return "Unknown"
