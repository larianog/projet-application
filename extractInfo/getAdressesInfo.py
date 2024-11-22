def getAdressesInfo(result):
    addresses = []
    for item in result:
        if len(item) > 0:
            addresses.append(item)

    # Code postal	
    # Ville	
    # État	
    # Pays
    # N'habite pas à l'addresse indiquée (NPAI)	
    zips = []	
    villes = []
    etats = []
    pays = []
    for address in addresses:
        
        nomRue = address["adress"]
        ville = address["city"]
        nomPays = address["country_name"]
        codePostal = address["zip"]
        type_adresse = address["type"]
        npai = address["npai"]

        telephone = address["mobile"]
        prefix_telephone = address["mobile_prefix"]

        coordonnees = { nomRue = nomRue, ville = ville, codePostal = codePostal, nomPays = nomPays, npai = npai,
                        telephone = telephone, prefix_telephone = prefix_telephone
                        }
        
        infoAddresse.update = (type_adresse = type_adresse, addresse = coordonnees)

    return infoAddresse