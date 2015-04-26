# coding=utf-8
from Levenshtein import ratio
import requests
import re

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

def extract_zipcode(string):
    """
    Given a string, extract a zipcode if it's present in the string
    """
    zipsearch =re.compile(r'[A-Z]\d[A-Z] *\d[A-Z]\d')
    if zipsearch.search(string):
        return zipsearch.search(string).group()
    else:
        return False

def getZipcode(longitude, latitude):
    """
    Given coordonates, return the zipcode
    """
    r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s' % (latitude, longitude))
    addresses = r.json()
    zipcode = [ extract_zipcode(a['formatted_address'])  for a in addresses['results'] if extract_zipcode(a['formatted_address'])  ].pop()
    return zipcode

def getArrondissementCode(longitude, latitude):
    """
    Given coordonates, return the arrondissement name
    """
    r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s' % (latitude, longitude))
    addresses = r.json()
    try:
        arr = [ a['formatted_address'].split(',')[0] for a in addresses['results'] if 'sublocality' in a['types'] ].pop()
    except:
        arr = "Rivière-des-Prairies-Pointe-aux-Trembles" 
        
    return get_abrev(arr)



