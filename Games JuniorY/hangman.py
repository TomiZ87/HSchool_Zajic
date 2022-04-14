import random
text_file = open("Games JuniorY/wordlist.txt", "r")
file_words = text_file.read()
word_list = file_words.split(", ")
#word_list = ["lags", "southend", "radiotherapy", "courtroom", "emule", "torches", "cuisines", "devine", "pkgconfig", "karst", "suspend", "effector", "deborah", "onward", "texturing", "citibank", "destinations", "wolff", "sonet", "design", "neve", "robin", "optimus", "styli", "divine", "abrahams", "coal", "antrim", "personalise", "bacchus", "burdened", "lac", "preteens", "epidemiology", "justifies", "impasse", "taipei", "mcqueen", "minivan", "exogenous", "rockville", "cougars", "poppy", "toothbrush", "waterways", "soo", "losers", "divided", "university", "polled", "osp", "smelly", "ft", "tara", "macroscopic", "dpi", "upfront", "bessemer", "gsa", "tableau", "brooms", "shelling", "introduction", "pittsburgh", "tellers", "staffordshire", "struc", "takeaway", "adamant", "glands", "dartford", "economies", "harcore", "continuing", "defamatory", "security", "stumbling", "manchester", "jagged", "wie", "juillet", "married", "computations", "capabilities", "blemish", "asthma", "avert", "chi", "domains", "nikki", "varnish", "estefan", "shrink", "concordia", "freight", "spine", "gizmodo", "orthopaedic", "stats", "tying", "wenn", "weakness", "sec", "swarthmore", "ricochet", "woodville", "makita", "unable", "wunder", "attenuation", "toulouse", "clearly", "disneyland", "crescendo", "specificity", "dildo", "nutr", "concerto", "repre", "laundering", "rectangles", "flo", "spam", "instantiate", "atty", "britten", "gao", "eoc", "martinique", "wto", "heisenberg", "manolo", "blah", "doorway", "prb", "kabbalah", "website", "floods", "infra", "disturbance", "det", "beats", "so", "gabba", "conqueror", "fiore", "plas", "hydrangea", "diarrhoea", "materialism", "nouvelle", "raine", "calculated", "blt", "galleria", "usability", "composing", "ira", "dimer", "viaggi", "qualifying", "dermatitis", "fumbles", "itmj", "chops", "certificated", "sergio", "flavorful", "dailies", "bangor", "qualifiers", "binders", "lipoic", "townships", "mx", "steeped", "bagpipes", "venerable", "ducky", "nco", "rakes", "schuster", "diligently", "unmounted", "sensory", "cjd", "caucasus", "quartet", "topography", "refraction", "endocrinol", "mates", "hug", "karon", "ds", "accordance", "rct", "cyc", "durability", "circadian", "yoshida", "stallman", "ahrq", "disgusting", "estonia", "cashiers", "mykonos", "never", "theaters", "hideaway", "forwarding", "ge", "ore", "heaton", "steyn", "liz", "bloomingdale", "enforceable", "ascend", "testicles", "warsaw", "fibre", "linksys", "backside", "punks", "ray", "fibromyalgia", "glut", "brutally", "tradition", "submarines", "winzip", "obstacle", "stockpiles", "onion", "dogfart", "enterta", "strat", "gsi", "memset", "encapsulation", "occupant", "microns", "insolvent", "trilogy", "closings", "huey", "blasen", "hungary", "prequalification", "hurt", "plt", "looting", "foothold", "passaic", "een", "baden", "sim", "longhorn", "storing", "defaulting", "sunsets", "tics", "hendricks", "knobs", "thoroughbred", "abacus", "bizjournalshire", "jealous", "fdisk", "ewan", "hopewell", "tumble", "vermillion", "luminance", "renewables", "clique", "descends", "towing", "reprocessing", "mgr", "abramson", "rum", "mrna", "prophecy", "soiled", "equitable", "unilaterally", "conception", "reserva", "reorganisation", "emit", "cracker", "fee", "accountable", "doll", "ephedra", "oktoberfest", "harmonica", "judaism", "vidsvidsvids", "divisor", "asserts", "gonzalez", "promoter", "jungle", "discogs", "miyazaki", "innovation", "azerbaijani", "mangled", "active", "invisionfree", "basque", "jpn", "commodity", "trademarks", "antiqua", "afforded", "coeds", "securely", "argv", "masterpiece", "nonprescription", "capo", "collars", "sigs", "decipher", "jeffrey", "trolleys", "hasbro", "fellowship", "inconceivable", "irp", "floss", "osceola", "silica", "gaines", "emits", "paulson", "zodb", "jeopardize", "disinfection", "adios", "estrogen", "sluggish", "eeoc", "tuscany", "illuminati", "infirmary", "lars", "tannins", "prob", "bebop", "furtherance", "revere", "git", "postulate", "vided", "laurie", "forth", "calcite", "sham", "supernatural", "reservations", "terracotta", "worthwhile", "radicals", "meridia", "unwind", "theoretical", "shaping", "inmarsat", "eyeliner", "tent", "variant", "edward", "toffee", "aimed", "alicante", "profanity", "primate", "fitted", "coveted", "recentchanges", "rwandan", "canadians", "placebo", "sulfuric", "jobsearch", "snorting", "customizable", "etymology", "intercollegiate", "synagogues", "xfs", "fisica", "saddle", "surcharge", "mad", "messenger", "canvas", "wild", "speakerphone", "cbc", "histocompatibility", "investigated", "naturalized", "flocked", "inactivity", "equatorial", "sanction", "firewalls", "lis", "localisation", "crease", "devices", "cimarron", "doug", "knowledgebase", "infousa", "callmanager", "grosso", "cher", "distributed", "recycling", "smr", "imitating", "mansell", "zwischen", "zahn", "kingman", "santana", "excelled", "pads", "streams", "ica", "eiffel", "databases", "running", "asi", "uniformed", "chechnya", "regt", "roses", "eighty", "livejournal", "edgewall", "paganism", "soda", "soic", "embolism", "cretaceous", "graveyard", "willi", "desnudos", "rhesus", "received", "fca", "ari", "uae", "liberalization", "instance", "custom", "ruin", "compositions", "pondicherry", "bulging", "wrecked", "treatise", "licking", "fronted", "midlife", "restaurants", "edm", "guadalupe", "comoros", "pontoon", "rfi", "unzipped", "trillian", "arcade", "skimmer", "associated", "oralsex", "tna", "blowfish", "evacuees", "nairobi", "timer", "aldershot", "jigsaws", "invited", "abbas", "indefinitely", "terrain", "bellevue", "abstractions", "jardine", "ocala", "weeping", "blanks", "nile", "ladder", "elizabeth", "kryptonite", "gunpowder", "lancelot", "aguilera", "impressed", "relied", "mkportal", "founded", "cypriot", "extremists", "pella", "zeiss", "transform", "clemson", "firmly", "gleaming", "slide", "stationery", "henrietta", "roc", "imate", "mediocre", "purcell", "rout", "hangs", "yusuf", "mlb", "act", "hovering", "murata", "dwr", "insurances", "bypassing", "rap", "indra", "methadone", "upto", "smarts", "byblos", "hermione", "convex", "rah", "intimacy", "mse", "correo", "finer", "quarters", "claimed", "preferences", "emperor", "crosley", "crucial", "minors", "almond", "carcinomas", "asshole", "lading", "denison", "merrell", "smokes", "nepal", "alfonso", "baer", "extremes", "possibly", "calorimeter", "garages", "extending", "bil", "axles", "stott", "tabs", "jacob", "gauntlet", "bullshit", "frozen", "cigars", "belling", "interspersed", "inhibitor", "contention", "isomerase", "hubris", "phys", "incline", "assistive", "bios", "ethno", "ects", "stewart", "drain", "environment", "prong", "fide", "spock", "exiting", "novosibirsk", "peep", "noise", "super", "xiang", "sideline", "vogt", "torrey", "ahl", "intermodal", "humiliation", "vivendi", "freepics", "departmental", "cheese", "examine", "sampling", "competes", "monsoon", "casio", "solemnly", "vnd", "epub", "bar", "snug", "bering", "pornographic", "credible", "fishman", "chakras", "officejet", "saucer", "zip", "markers", "srx", "gradually", "existential", "bugle", "arrowhead", "iru", "turbine", "wye", "verifier", "grand", "bandit", "aan", "illinois", "quotient", "westwood", "toast", "beliefs", "joann", "rawlins", "unfunded", "cerritos", "profession", "lavish", "ocarina", "sprinkle", "terre", "exim", "kiel", "powweb", "mpumalanga", "exch", "bunk", "restricting", "gratuitous", "opr", "odom", "gere", "unconfirmed", "milwaukee", "namm", "adamson", "mgp", "stanford", "criticized", "skyscrapers", "followup", "jeg", "receiverdvb", "merge", "seduces", "bde", "powerseller", "woodwind", "editing", "critic", "autumn", "redo", "deceleration", "zea", "ra", "jan", "waive", "hcv", "commun", "whitaker", "runway", "stiff", "swanson", "heinemann", "abusing", "beckwith", "metaphysics", "aire", "brazos", "tea", "jubilee", "cosh", "flue", "basements", "kroner", "agosto", "spurs", "vegetarians", "margarine", "mcs", "croatia", "reformatted", "mirth", "exo", "heaters", "temperate", "recovered", "symptom", "lovejoy", "hydrological", "xy", "cutter", "heirloom", "bombed", "deportation", "carmarthenshire", "nikos", "sperry", "ure", "palma", "craftsmen", "showtimes", "zorn", "reaction", "borrowed", "peruse", "cabins", "slideshow", "yes", "nanotech", "innova", "matsushita", "bonny", "guarding", "soros", "trannies", "timely", "confront", "concave", "squeak", "levers", "romance", "betsy", "puma", "sau", "amon", "criteria", "romanian", "aussie", "margin", "subsequently", "puffs", "iar", "goggle", "correctional", "kenji", "stranded", "vec", "lining", "accelerating", "neumann", "fddi", "delineation", "extraterrestrial", "unpatched", "annealing", "bel", "employed", "hg", "passwort", "enough", "scarica", "gazette", "demand", "glitch", "yonge", "patrol", "nonetheless", "unisys", "messy", "naturists", "lanvin", "economic", "lang", "figurines", "metaphors", "deane", "niven", "isakmp", "evelyn", "flex", "bras", "activism", "caffe", "yahoo", "alfredo", "ogden", "wip", "visibly", "warriors", "taxpayers", "mansions", "fasta", "dub", "tripp", "westmoreland", "basingstoke", "permissive", "larsson", "unenforceable", "ailments", "oecd", "yashica", "ibb", "tat", "civilizations", "bluffs", "jumpstart", "nanotube", "cruelly", "ital", "nonparametric", "thorax", "waistband", "mbs", "murcia", "pasco", "cortez", "mont", "genocide", "mmap", "actin", "ahead", "followers", "ory", "chimpanzee", "acclaim", "elusive", "shrinking", "amorphous", "gouvernement", "fervor", "preliminaries", "midpoint", "bytecode", "reis", "narrow", "rife", "sharpen", "arrogant", "glyphs", "att", "snows", "realistically", "baffle", "comparative", "raster", "vax", "gatineau", "ano", "coded", "shiseido", "soars", "ellicott", "suspicious", "phoneid", "documents", "coolest", "crowded", "disciplined", "sadly", "laid", "ridley", "retractions", "plates", "terry", "loading", "naia", "mobygames", "calcareous", "ovens", "reflection", "collette", "dam", "levels", "rabbits", "swings", "beneficially", "analysing", "bobs", "pooping", "downer", "bet", "clamav", "distrib", "quote", "sud", "canons", "shipman", "spd", "lng", "tolerance", "mojo", "vaguely", "blackrock", "cathay", "fichier", "mathcad", "hayden", "classed", "involuntarily", "summarise", "tragedies", "granularity", "farris", "compton", "atk", "investments", "treating", "carpool", "usefulness", "castor", "fld", "pai", "passer", "toward", "asses", "jin", "psd", "bap", "sustain", "polyphonic", "milt", "lagerfeld", "prank", "pd", "hamden", "egullet", "transcriber", "redox", "mailscanner", "virtuous", "www", "obligatory", "hesitated", "sizeable", "perch", "pt", "gaiman", "wnw", "gutted", "regarder", "erasmus", "northward", "delong", "old", "apo", "spain", "closeness", "karachi", "mencken", "cyberspace", "pta", "catholicism", "ghost", "penetration", "boinc", "traitor", "nba", "burma", "scion", "syp", "northside", "product", "brookstone", "nortel", "lethal", "inserts", "caucasian", "flickr"]
word = random.choice(word_list)
win = False
player = ""
number_of_mistakes = len(word) + 4
mistakes = 0
guessed_whole = False

print("Game: Hangman")
print("Try to guess the characters of the words and ulimately to guess the whole word!")
print("You can enter characters (you have certain attempts) or \nyou can enter the whole word (but if it is incorrect, the game is over, you can use this only once)")
guess = []
guessed = []
for x in word:
    guess.append("_")

while ("_" in guess and mistakes < number_of_mistakes) and not guessed_whole:
    print("\n\nYou have make " +str(number_of_mistakes-mistakes) + " more mistakes! You made " +str(mistakes)+" mistakes!")
    print("You used these letters " + str(guessed))
    print("The word: ")
    print(' '.join([str(elem) for elem in guess]) + " ("+str(len(word))+" letters)")
    player = input("Guess the character: ").lower()
    if len(player) == 1:
        if player in word:
            if player in guess:
                print("You already guessed this word correctly")
                mistakes += 1
            else:
                print("Nice, you guessed another letter!")
                positions = []
                iteration = 0
                for x in word:
                    if x == player:
                        positions.append(iteration)
                    iteration += 1
                print(positions)
                for y in positions:
                    guess[y] = player
        else:
            print("What a shame, the letter you entered wasnt found in the word!")
            if player not in guessed:
                guessed.append(player)
            mistakes += 1
    else:
        agreement = input("Do you really want to guess the whole word? If it not right, the game will end. Y for yes, n for no: ").lower()
        if agreement == "y":
            if player == word:
                guessed_whole = True
            else:
                print("Unfortunatally, this isnt the guessing word")
                mistakes = number_of_mistakes
        else:
            print("Okey!")
if "_" in guess and mistakes >= number_of_mistakes:
    print("\n\nYou ran out of attempts, the word was " + word.upper())
else:
    print("\n\nYou won! Indeed, The word was " + word.upper() + "!")
    print("You used these letters " +str(guessed))
    print("You made " +str(mistakes)+" mistakes!")



    