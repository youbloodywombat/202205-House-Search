epping = df[df["suburb"]=="Epping"]["price"]
northrocks = df[df["suburb"]=="North Rocks"]["price"]
eastwood = df[df["suburb"]=="Eastwood"]["price"]
baulkham = df[df["suburb"]=="Baulkham Hills"]["price"]
winston = df[df["suburb"]=="Winston Hills"]["price"]
kellyville = df[df["suburb"]=="Kellyville"]["price"]
blacktown = df[df["suburb"]=="Blacktown"]["price"]
castle = df[df["suburb"]=="Castle Hill"]["price"]
ryde = df[df["suburb"]=="Ryde"]["price"]
rouse = df[df["suburb"]=="Rouse Hill"]["price"]
beecroft = df[df["suburb"]=="Beecroft"]["price"]
ermington = df[df["suburb"]=="Ermington"]["price"]
northmead = df[df["suburb"]=="Northmead"]["price"]
newington = df[df["suburb"]=="Newington"]["price"]
concord = df[df["suburb"]=="Concord"]["price"]
marsfield = df[df["suburb"]=="Marsfield"]["price"]
hornsby = df[df["suburb"]=="Hornsby"]["price"]



epping  = api.search(locations=["Epping"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
northrocks  = api.search(locations=["North Rocks"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
eastwood  = api.search(locations=["Eastwood"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
baulkham  = api.search(locations=["Baulkham Hills"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
winston  = api.search(locations=["Winston Hills"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
kellyville  = api.search(locations=["Kellyville"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
blacktown  = api.search(locations=["Blacktown"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
castle  = api.search(locations=["Castle Hill"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
ryde  = api.search(locations=["Ryde"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
rouse  = api.search(locations=["Rouse Hill"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
beecroft  = api.search(locations=["Beecroft"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
ermington  = api.search(locations=["Ermington"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
northmead  = api.search(locations=["Northmead"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
newington  = api.search(locations=["Newington"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
concord  = api.search(locations=["Concord"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
marsfield  = api.search(locations=["Marsfield"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
hornsby  = api.search(locations=["Hornsby"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Lidcombe  = api.search(locations=["Lidcombe"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Homebush  = api.search(locations=["Homebush"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Straithfield  = api.search(locations=["Straithfield"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Ashfield  = api.search(locations=["Ashfield"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Leichhardt  = api.search(locations=["Leichhardt"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Annandale  = api.search(locations=["Annandale"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
AllambieHeights  = api.search(locations=["Allambie Heights"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Forestville  = api.search(locations=["Forestville"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Lindfield  = api.search(locations=["Lindfield"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Gordon  = api.search(locations=["Gordon"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Pymble  = api.search(locations=["Pymble"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
LaneCove  = api.search(locations=["Lane Cove"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Meadowbank  = api.search(locations=["Meadowbank"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
SummerHill  = api.search(locations=["Summer Hill"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Rydalmere  = api.search(locations=["Rydalmere"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Rosehill  = api.search(locations=["Rosehill"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Westmead  = api.search(locations=["Westmead"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Girraween  = api.search(locations=["Girraween"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
BeaumontHills  = api.search(locations=["Beaumont Hills"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
KellyvilleRidge  = api.search(locations=["Kellyville Ridge"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
ThePonds  = api.search(locations=["The Ponds"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Schofields  = api.search(locations=["Schofields"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
MarsdenPark  = api.search(locations=["Marsden Park"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
KingsLangley  = api.search(locations=["Kings Langley"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
BellaVista  = api.search(locations=["Bella Vista"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
BoxHill  = api.search(locations=["Box Hill"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
PennantHills  = api.search(locations=["Pennant Hills"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Earlwood  = api.search(locations=["Earlwood"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Marrickville  = api.search(locations=["Marrickville"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Dulwich  = api.search(locations=["Dulwich"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Petersham  = api.search(locations=["Petersham"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Campsie  = api.search(locations=["Campsie"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Canterbury  = api.search(locations=["Canterbury"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Berala  = api.search(locations=["Berala"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Leppington  = api.search(locations=["Leppington"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
EdmondsonPark  = api.search(locations=["Edmondson Park"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
MacquariePark  = api.search(locations=["Macquarie Park"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Chatswood  = api.search(locations=["Chatswood"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Carlingford  = api.search(locations=["Carlingford"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Kogarah  = api.search(locations=["Kogarah"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Rockdale  = api.search(locations=["Rockdale"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Cherrybrook  = api.search(locations=["Cherrybrook"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Eastwood  = api.search(locations=["Eastwood"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Homebush  = api.search(locations=["Homebush"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Minto  = api.search(locations=["Minto"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
QuakersHill  = api.search(locations=["Quakers Hill"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Revesby  = api.search(locations=["Revesby"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
SevenHills  = api.search(locations=["Seven Hills"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
StanhopeGardens  = api.search(locations=["Stanhope Gardens"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Waterloo  = api.search(locations=["Waterloo"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
DulwichHill  = api.search(locations=["Dulwich Hill"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
NorthRyde  = api.search(locations=["North Ryde"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Straithfield  = api.search(locations=["Straithfield"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
NorthStraithfield  = api.search(locations=["North Straithfield"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Manly  = api.search(locations=["Manly"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Randwick  = api.search(locations=["Randwick"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])
Kensington  = api.search(locations=["Kensington"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])

test = api.search(locations=["NSW"], property_types=["townhouse","house"], channel="sold", exclude_keywords=["pool"])


priority_suburbs = [epping,northrocks,eastwood,baulkham,winston,kellyville,blacktown,castle,ryde,rouse,beecroft,ermington,northmead,newington,concord,marsfield,hornsby,Lidcombe,Homebush,Straithfield,Ashfield,Leichhardt,Annandale,AllambieHeights,Forestville,Lindfield,Gordon,Pymble,LaneCove,Meadowbank,SummerHill,Rydalmere,Rosehill,Westmead,Girraween,BeaumontHills,KellyvilleRidge,ThePonds,Schofields,MarsdenPark,KingsLangley,BellaVista,BoxHill,PennantHills,Earlwood,Marrickville,Dulwich,Petersham,Campsie,Canterbury,Berala,Leppington,EdmondsonPark,MacquariePark,Chatswood,Carlingford,Kogarah,Rockdale,Cherrybrook,Eastwood,Homebush,Minto,QuakersHill,Revesby,SevenHills,StanhopeGardens,Waterloo,DulwichHill,NorthRyde,Straithfield,NorthStraithfield,Manly,Randwick,Kensington]


suburb_list = [epping_listings, northrocks_listings, eastwood_listings, baulkham_listings, winston_listings, kellyville_listings, blacktown_listings, castle_listings, ryde_listings, rouse_listings, beecroft_listings, ermington_listings, northmead_listings, newington_listings, concord_listings, marsfield_listings, ]
suburb_list = [epping_listings, northrocks_listings, eastwood_listings, baulkham_listings, winston_listings, kellyville_listings, blacktown_listings, castle_listings, ryde_listings, rouse_listings, beecroft_listings, ermington_listings, northmead_listings, newington_listings, concord_listings, marsfield_listings, hornsby_listings, Lidcombe_listings, Homebush_listings, Straithfield_listings, Ashfield_listings, Leichhardt_listings, Annandale_listings, AllambieHeights_listings, Forestville_listings, Lindfield_listings, Gordon_listings, Pymble_listings, LaneCove_listings, Meadowbank_listings, SummerHill_listings, Rydalmere_listings, Rosehill_listings, Westmead_listings, Girraween_listings, BeaumontHills_listings, KellyvilleRidge_listings, ThePonds_listings, Schofields_listings, MarsdenPark_listings, KingsLangley_listings, BellaVista_listings, BoxHill_listings, PennantHills_listings, Earlwood_listings, Marrickville_listings, Dulwich_listings, Petersham_listings, Campsie_listings, Canterbury_listings, Berala_listings, Leppington_listings, EdmondsonPark_listings, MacquariePark_listings, Chatswood_listings, Carlingford_listings, Kogarah_listings, Rockdale_listings, Cherrybrook_listings, Eastwood_listings, Homebush_listings, Minto_listings, QuakersHill_listings, Revesby_listings, SevenHills_listings, StanhopeGardens_listings, Waterloo_listings]

epping_listings = final2[final2["suburb"]== "Epping"]
northrocks_listings = final2[final2["suburb"]== "North Rocks"]
eastwood_listings = final2[final2["suburb"]==   "Eastwood"]
baulkham_listings = final2[final2["suburb"]==   "Baulkham Hills"]
winston_listings = final2[final2["suburb"]==    "Winston Hills"]
kellyville_listings = final2[final2["suburb"]== "Kellyville"]
blacktown_listings = final2[final2["suburb"]==  "Blacktown"]
castle_listings = final2[final2["suburb"]== "Castle Hill"]
ryde_listings = final2[final2["suburb"]==   "Ryde"]
rouse_listings = final2[final2["suburb"]==  "Rouse Hill"]
beecroft_listings = final2[final2["suburb"]==   "Beecroft"]
ermington_listings = final2[final2["suburb"]==  "Ermington"]
northmead_listings = final2[final2["suburb"]==  "Northmead"]
newington_listings = final2[final2["suburb"]==  "Newington"]
concord_listings = final2[final2["suburb"]==    "Concord"]
marsfield_listings = final2[final2["suburb"]==  "Marsfield"]
hornsby_listings = final2[final2["suburb"]==    "Hornsby"]
Lidcombe_listings = final2[final2["suburb"]==   "Lidcombe"]
Homebush_listings = final2[final2["suburb"]==   "Homebush"]
Straithfield_listings = final2[final2["suburb"]==   "Straithfield"]
Ashfield_listings = final2[final2["suburb"]==   "Ashfield"]
Leichhardt_listings = final2[final2["suburb"]== "Leichhardt"]
Annandale_listings = final2[final2["suburb"]==  "Annandale"]
AllambieHeights_listings = final2[final2["suburb"]==    "Allambie Heights"]
Forestville_listings = final2[final2["suburb"]==    "Forestville"]
Lindfield_listings = final2[final2["suburb"]==  "Lindfield"]
Gordon_listings = final2[final2["suburb"]== "Gordon"]
Pymble_listings = final2[final2["suburb"]== "Pymble"]
LaneCove_listings = final2[final2["suburb"]==   "Lane Cove"]
Meadowbank_listings = final2[final2["suburb"]== "Meadowbank"]
SummerHill_listings = final2[final2["suburb"]== "Summer Hill"]
Rydalmere_listings = final2[final2["suburb"]==  "Rydalmere"]
Rosehill_listings = final2[final2["suburb"]==   "Rosehill"]
Westmead_listings = final2[final2["suburb"]==   "Westmead"]
Girraween_listings = final2[final2["suburb"]==  "Girraween"]
BeaumontHills_listings = final2[final2["suburb"]==  "Beaumont Hills"]
KellyvilleRidge_listings = final2[final2["suburb"]==    "Kellyville Ridge"]
ThePonds_listings = final2[final2["suburb"]==   "The Ponds"]
Schofields_listings = final2[final2["suburb"]== "Schofields"]
MarsdenPark_listings = final2[final2["suburb"]==    "Marsden Park"]
KingsLangley_listings = final2[final2["suburb"]==   "Kings Langley"]
BellaVista_listings = final2[final2["suburb"]== "Bella Vista"]
BoxHill_listings = final2[final2["suburb"]==    "Box Hill"]
PennantHills_listings = final2[final2["suburb"]==   "Pennant Hills"]
Earlwood_listings = final2[final2["suburb"]==   "Earlwood"]
Marrickville_listings = final2[final2["suburb"]==   "Marrickville"]
Dulwich_listings = final2[final2["suburb"]==    "Dulwich"]
Petersham_listings = final2[final2["suburb"]==  "Petersham"]
Campsie_listings = final2[final2["suburb"]==    "Campsie"]
Canterbury_listings = final2[final2["suburb"]== "Canterbury"]
Berala_listings = final2[final2["suburb"]== "Berala"]
Leppington_listings = final2[final2["suburb"]== "Leppington"]
EdmondsonPark_listings = final2[final2["suburb"]==  "Edmondson Park"]
MacquariePark_listings = final2[final2["suburb"]==  "Macquarie Park"]
Chatswood_listings = final2[final2["suburb"]==  "Chatswood"]
Carlingford_listings = final2[final2["suburb"]==    "Carlingford"]
Kogarah_listings = final2[final2["suburb"]==    "Kogarah"]
Rockdale_listings = final2[final2["suburb"]==   "Rockdale"]
Cherrybrook_listings = final2[final2["suburb"]==    "Cherrybrook"]
Eastwood_listings = final2[final2["suburb"]==   "Eastwood"]
Homebush_listings = final2[final2["suburb"]==   "Homebush"]
Minto_listings = final2[final2["suburb"]==  "Minto"]
QuakersHill_listings = final2[final2["suburb"]==    "Quakers Hill"]
Revesby_listings = final2[final2["suburb"]==    "Revesby"]
SevenHills_listings = final2[final2["suburb"]== "Seven Hills"]
StanhopeGardens_listings = final2[final2["suburb"]==    "Stanhope Gardens"]
Waterloo_listings = final2[final2["suburb"]==   "Waterloo"]
DulwichHill = final2[final2["suburb"]=="Dulwich Hill"]
NorthRyde = final2[final2["suburb"]=="North Ryde"]
Straithfield = final2[final2["suburb"]=="Straithfield"]
NorthStraithfield = final2[final2["suburb"]=="North Straithfield"]
Manly = final2[final2["suburb"]=="Manly"]
Randwick = final2[final2["suburb"]=="Randwick"]
Kensington = final2[final2["suburb"]=="Kensington"]
  
  
  
  
  
  
  

"Epping","North Rocks","Eastwood","Baulkham Hills","Winston Hills","Kellyville","Blacktown","Castle Hill","Ryde","Rouse Hill","Beecroft","Ermington","Northmead","Newington","Concord","Marsfield","Hornsby","Lidcombe","Homebush","Straithfield","Ashfield","Leichhardt","Annandale","Allambie Heights","Forestville","Lindfield","Gordon","Pymble","Lane Cove","Meadowbank","Summer Hill","Rydalmere","Rosehill","Westmead","Girraween","Beaumont Hills","Kellyville Ridge","The Ponds","Schofields","Marsden Park","Kings Langley","Bella Vista","Box Hill","Pennant Hills","Earlwood","Marrickville","Dulwich","Petersham","Campsie","Canterbury","Berala","Leppington","Edmondson Park","Macquarie Park","Chatswood","Carlingford","Kogarah","Rockdale","Cherrybrook","Eastwood","Homebush","Minto","Quakers Hill","Revesby","Seven Hills","Stanhope Gardens","Waterloo","Dulwich Hill","North Ryde","Straithfield","North Straithfield","Manly","Randwick","Kensington"

Abbotsbury
Abbotsford
Acacia Gardens
Agnes Banks
Airds
Alexandria
Alfords Point
Allambie Heights
Allawah
Ambarvale
Annandale
Annangrove
Arcadia
Arncliffe
Arndell Park
Artarmon
Ashbury
Ashcroft
Ashfield
Asquith
Auburn
Austral
Avalon Beach
Badgerys Creek
Balgowlah
Balgowlah Heights
Balmain
Balmain East
Bangor
Banksia
Banksmeadow
Bankstown
Bankstown Aerodrome
Barangaroo
Barden Ridge
Bardia
Bardwell Park
Bardwell Valley
Bass Hill
Baulkham Hills
Bayview
Beacon Hill
Beaconsfield
Beaumont Hills
Beecroft
Belfield
Bella Vista
Bellevue Hill
Belmore
Belrose
Berala
Berkshire Park
Berowra
Berowra Creek
Berowra Heights
Berowra Waters
Berrilee
Beverley Park
Beverly Hills
Bexley
Bexley North
Bidwill
Bilgola Beach
Bilgola Plateau
Birchgrove
Birrong
Blackett
Blacktown
Blair Athol
Blairmount
Blakehurst
Bligh Park
Bondi
Bondi Beach
Bondi Junction
Bonnet Bay
Bonnyrigg
Bonnyrigg Heights
Bossley Park
Botany
Bow Bowing
Box Hill
Bradbury
Breakfast Point
Brighton-Le-Sands
Bringelly
Bronte
Brooklyn
Brookvale
Bundeena
Bungarribee
Burraneer
Burwood
Burwood Heights
Busby
Cabarita
Cabramatta
Cabramatta West
Caddens
Cambridge Gardens
Cambridge Park
Camellia
Cammeray
Campbelltown
Camperdown
Campsie
Canada Bay
Canley Heights
Canley Vale
Canoelands
Canterbury
Caringbah
Caringbah South
Carlingford
Carlton
Carnes Hill
Carramar
Carss Park
Cartwright
Castle Cove
Castle Hill
Castlecrag
Castlereagh
Casula
Catherine Field
Cattai
Cecil Hills
Cecil Park
Centennial Park
Chatswood
Chatswood West
Cheltenham
Cherrybrook
Chester Hill
Chifley
Chippendale
Chipping Norton
Chiswick
Chullora
Church Point
Claremont Meadows
Clarendon
Clareville
Claymore
Clemton Park
Clontarf
Clovelly
Clyde
Coasters Retreat
Cobbitty
Colebee
Collaroy
Collaroy Plateau
Colyton
Como
Concord
Concord West
Condell Park
Connells Point
Constitution Hill
Coogee
Cottage Point
Cowan
Cranebrook
Cremorne
Cremorne Point
Cromer
Cronulla
Crows Nest
Croydon
Croydon Park
Curl Curl
Currawong Beach
Currans Hill
Daceyville
Dangar Island
Darling Point
Darlinghurst
Darlington
Davidson
Dawes Point
Dean Park
Dee Why
Denham Court
Denistone
Denistone East
Denistone West
Dharruk
Dolans Bay
Dolls Point
Doonside
Double Bay
Dover Heights
Drummoyne
Duffys Forest
Dulwich Hill
Dundas
Dundas Valley
Dural
Eagle Vale
Earlwood
East Hills
East Killara
East Lindfield
East Ryde
Eastern Creek
Eastgardens
Eastlakes
Eastwood
Edensor Park
Edgecliff
Edmondson Park
Elanora Heights
Elderslie
Elizabeth Bay
Elizabeth Hills
Elvina Bay
Emerton
Enfield
Engadine
Englorie Park
Enmore
Epping
Ermington
Erskine Park
Erskineville
Eschol Park
Eveleigh
Fairfield
Fairfield East
Fairfield Heights
Fairfield West
Fairlight
Fiddletown
Five Dock
Forest Glen
Forest Lodge
Forestville
Frenchs Forest
Freshwater
Galston
Georges Hall
Gilead
Girraween
Gladesville
Glebe
Gledswood Hills
Glen Alpine
Glendenning
Glenfield
Glenhaven
Glenmore Park
Glenorie
Glenwood
Gordon
Granville
Grays Point
Great Mackerel Beach
Green Valley
Greenacre
Greendale
Greenfield Park
Greenhills Beach
Greenwich
Gregory Hills
Greystanes
Guildford
Guildford West
Gymea
Gymea Bay
Haberfield
Hammondville
Harrington Park
Harris Park
Hassall Grove
Haymarket
Heathcote
Hebersham
Heckenberg
Henley
Hillsdale
Hinchinbrook
Hobartville
Holroyd
Holsworthy
Homebush
Homebush West
Horningsea Park
Hornsby
Hornsby Heights
Horsley Park
Hoxton Park
Hunters Hill
Huntingwood
Huntleys Cove
Huntleys Point
Hurlstone Park
Hurstville
Hurstville Grove
Illawong
Ingleburn
Ingleside
Jamisontown
Jannali
Jordan Springs
Kangaroo Point
Kareela
Kearns
Kellyville
Kellyville Ridge
Kemps Creek
Kensington
Kenthurst
Kentlyn
Killara
Killarney Heights
Kings Langley
Kings Park
Kingsford
Kingsgrove
Kingswood
Kirkham
Kirrawee
Kirribilli
Kogarah
Kogarah Bay
Ku-ring-gai Chase
Kurnell
Kurraba Point
Kyeemagh
Kyle Bay
La Perouse
Lakemba
Lalor Park
Lane Cove
Lane Cove North
Lane Cove West
Lansdowne
Lansvale
Laughtondale
Lavender Bay
Leets Vale
Leichhardt
Len Waters Estate
Leppington
Lethbridge Park
Leumeah
Lewisham
Liberty Grove
Lidcombe
Lilli Pilli
Lilyfield
Lindfield
Linley Point
Little Bay
Liverpool
Llandilo
Loftus
Londonderry
Long Point
Longueville
Lovett Bay
Lower Portland
Lucas Heights
Luddenham
Lugarno
Lurnea
Macquarie Fields
Macquarie Links
Macquarie Park
Maianbar
Malabar
Manly
Manly Vale
Maraylya
Marayong
Maroota
Maroubra
Marrickville
Marsden Park
Marsfield
Mascot
Matraville
Mays Hill
McCarrs Creek
McGraths Hill
McMahons Point
Meadowbank
Melrose Park
Menai
Menangle Park
Merrylands
Merrylands West
Middle Cove
Middle Dural
Middleton Grange
Miller
Millers Point
Milperra
Milsons Passage
Milsons Point
Minchinbury
Minto
Minto Heights
Miranda
Mona Vale
Monterey
Moore Park
Moorebank
Morning Bay
Mortdale
Mortlake
Mosman
Mount Annan
Mount Colah
Mount Druitt
Mount Kuring-Gai
Mount Lewis
Mount Pritchard
Mount Vernon
Mulgoa
Mulgrave
Narellan
Narellan Vale
Naremburn
Narrabeen
Narraweena
Narwee
Nelson
Neutral Bay
Newington
Newport
Newtown
Normanhurst
North Balgowlah
North Bondi
North Curl Curl
North Epping
North Kellyville
North Manly
North Narrabeen
North Parramatta
North Rocks
North Ryde
North St Marys
North Strathfield
North Sydney
North Turramurra
North Wahroonga
North Willoughby
Northbridge
Northmead
Northwood
Norwest
Oakhurst
Oakville
Oatlands
Oatley
Old Guildford
Old Toongabbie
Oran Park
Orchard Hills
Oxford Falls
Oxley Park
Oyster Bay
Paddington
Padstow
Padstow Heights
Pagewood
Palm Beach
Panania
Parklea
Parramatta
Peakhurst
Peakhurst Heights
Pemulwuy
Pendle Hill
Pennant Hills
Penrith
Penshurst
Petersham
Phillip Bay
Picnic Point
Pitt Town
Pleasure Point
Plumpton
Point Piper
Port Botany
Port Hacking
Potts Hill
Potts Point
Prairiewood
Prestons
Prospect
Punchbowl
Putney
Pymble
Pyrmont
Quakers Hill
Queens Park
Queenscliff
Raby
Ramsgate
Ramsgate Beach
Randwick
Redfern
Regents Park
Regentville
Revesby
Revesby Heights
Rhodes
Richmond
Riverstone
Riverview
Riverwood
Rockdale
Rodd Point
Rookwood
Rooty Hill
Ropes Crossing
Rose Bay
Rosebery
Rosehill
Roselands
Rosemeadow
Roseville
Roseville Chase
Rossmore
Rouse Hill
Royal National Park
Rozelle
Ruse
Rushcutters Bay
Russell Lea
Rydalmere
Ryde
Sackville North
Sadleir
Sandringham
Sandy Point
Sans Souci
Schofields
Scotland Island
Seaforth
Sefton
Seven Hills
Shalvey
Shanes Park
Silverwater
Singletons Mill
Smeaton Grange
Smithfield
South Coogee
South Granville
South Hurstville
South Maroota
South Penrith
South Turramurra
South Wentworthville
South Windsor
Spring Farm
St Andrews
St Clair
St Helens Park
St Ives
St Ives Chase
St Johns Park
St Leonards
St Marys
St Peters
Stanhope Gardens
Stanmore
Strathfield
Strathfield South
Summer Hill
Surry Hills
Sutherland
Sydenham
Sydney
Sydney Olympic Park
Sylvania
Sylvania Waters
Tamarama
Taren Point
Telopea
Tempe
Tennyson Point
Terrey Hills
The Ponds
The Rocks
Thornleigh
Toongabbie
Tregear
Turramurra
Turrella
Ultimo
Varroville
Vaucluse
Villawood
Vineyard
Voyager Point
Wahroonga
Waitara
Wakeley
Wallacia
Wareemba
Warrawee
Warriewood
Warwick Farm
Waterfall
Waterloo
Watsons Bay
Wattle Grove
Waverley
Waverton
Wedderburn
Wentworth Point
Wentworthville
Werrington
Werrington County
Werrington Downs
West Hoxton
West Pennant Hills
West Pymble
West Ryde
Westleigh
Westmead
Wetherill Park
Whalan
Whale Beach
Wheeler Heights
Wiley Park
Willmot
Willoughby
Willoughby East
Windsor
Windsor Downs
Winston Hills
Wisemans Ferry
Wolli Creek
Wollstonecraft
Woodbine
Woodcroft
Woodpark
Woollahra
Woolloomooloo
Woolooware
Woolwich
Woronora
Woronora Heights
Yagoona
Yarrawarrah
Yennora
Yowie Bay
Zetland