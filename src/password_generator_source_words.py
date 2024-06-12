source_words = ["aabits", "aadress", "aas", "aasta", "aastaaeg", "aastane", "aastavahetus", "abi", "abielluma", "abielu", "abielupaar", "abikaasa", "abil", "abiline", "abistama", "abivalmis", "administraator", "advokaat", "aed", "aedvili", "aeg", "aeglane", "aeglaselt", "aeroobika", "aevastama", "aga", "ahaa", "ahi", "ahv", "aim", "aina", "aine", "ainsus", "ainuke", "ainukene", "ainult", "ainus", "aitama", "aitamine", "ajakiri", "ajakirjandus", "ajakirjanik", "ajaleht", "ajaline", "ajaliselt", "ajaloolane", "ajalooline", "ajalugu", "ajama", "ajastu", "ajavahemik", "aju", "ajutine", "ajutiselt", "aken", "aknalaud", "aktiivne", "aktiivselt", "aktiivsus", "aktsia", "aktsiaselts", "aku", "akulaadija", "akvaarium", "ala", "alaealine", "alaline", "alandama", "alarm", "alasti", "alates", "alati", "album", "algaja", "algama", "algatama", "algatus", "algklass", "algkool", "algselt", "algul", "algus", "alkohol", "alkoholivaba", "alkohoolik", "all", "alla", "allahindlus", "allapoole", "allergia", "alles", "allikas", "allkiri", "allpool", "alluma", "alluv", "alt", "alternatiiv", "altpoolt", "alumine", "alus", "aluspesu", "alustama", "alustamine", "alustass", "ambur", "ameeriklane", "amet", "ametikoht", "ametlik", "ametlikult", "ametnik", "ammu", "ananass", "andekas", "andestama", "andma", "andmed", "andmine", "ankeet", "annetus", "annus", "ansambel", "antenn", "anum", "aparaat", "apelsin", "appi", "aprill", "apteek", "arbuus", "arendama", "arendamine", "arenema", "areng", "arg", "arhiiv", "arhitekt", "arm", "armas", "armastama", "armastus", "armee", "armukade", "armuke", "armuma", "arst", "artikkel", "aru", "aruanne", "arukas", "arusaadav", "arusaam", "arusaamatu", "arusaamatus", "arutama", "arutamine", "arutelu", "arutlema", "arutlus", "arv", "arvama", "arvamus", "arvatavasti", "arve", "arvestama", "arvestus", "arvustus", "arvutama", "arvuti", "asemel", "asemele", "asend", "asendama", "asetama", "asfalt", "asi", "asjaajamine", "asjalik", "asjaolu", "asjaosaline", "asjatundja", "aste", "astuma", "astumine", "asukoht", "asuma", "asutama", "asutus", "auaste", "august", "auhind", "auk", "aur", "aus", "ausalt", "austama", "austatud", "austus", "auto", "autojuht", "automaat", "autor", "autoteenindus", "avaldama", "avaldamine", "avalduma", "avaldus", "avalik", "avalikkus", "avalikult", "avalikustama", "avama", "avamine", "avanema", "avar", "avarii", "avastama", "avastamine", "baar", "bakter", "ballett", "banaan", "bassein", "beebi", "bensiin", "bensiinijaam", "betoon", "bioloogia", "blankett", "blond", "broiler", "broneerima", "buss", "bussijaam", "bussijuht", "bussipeatus", "bussipilet", "daam", "delegatsioon", "demokraatia", "demokraatlik", "detail", "detsember", "dialoog", "dieet", "diivan", "diplom", "diplomaat", "diplomaatiline", "direktor", "dirigent", "disainer", "distants", "doktor", "dokument", "dollar", "draama", "dress", "dressid", "ebameeldiv", "ebamugav", "ebaoluline", "ebaseaduslik", "ebatavaline", "ebaviisakas", "ebaأµiglane", "ebaأµnnestuma", "edasi", "edasine", "edaspidi", "edastama", "edel", "edenema", "edetabel", "edu", "edukalt", "edukas", "eel", "eelarve", "eeldama", "eeldus", "eelis", "eelistama", "eelistus", "eelkأµige", "eelmine", "eelnema", "eemal", "eemaldama", "eemale", "eemalt", "ees", "eeskiri", "eeskuju", "eesnimi", "eesotsas", "eespool", "eest", "eesti", "eestikeelne", "eestlane", "eestpoolt", "efekt", "ega", "ehe", "ehitaja", "ehitama", "ehitamine", "ehitis", "ehitus", "ehitusmaterjal", "ehk", "ehkki", "ehmatama", "ehtne", "eile", "eilne", "eitama", "eitav", "ekraan", "eks", "eksam", "eksima", "eksimus", "eksisteerima", "eksitus", "ekskursioon", "ekspert", "elama", "elamine", "elamisluba", "elamu", "elamus", "elanik", "elanikkond", "elav", "elekter", "elektrik", "elektripliit", "elektrooniline", "element", "elevant", "elu", "eluaasta", "elukaaslane", "elukoht", "elukutse", "elulugu", "elund", "eluohtlik", "eluruum", "elus", "elutuba", "eluviis", "ema", "emakeel", "emane", "emme", "emotsionaalne", "emotsioon", "enam", "enamasti", "enamik", "enamus", "enda", "endine", "endiselt", "energia", "energiline", "energiliselt", "enese", "enesekindlus", "enesetapp", "enesetunne", "enne", "ennustama", "eraelu", "eraisik", "erakond", "erakorraline", "eraldama", "eraldi", "eramaja", "erand", "erapooletu", "eri", "eriala", "erialane", "eriline", "erinema", "erinev", "erinevalt", "erinevus", "eristama", "eriti", "ese", "esialgne", "esialgu", "esik", "esikoht", "esile", "esimees", "esimene", "esindaja", "esindama", "esindus", "esineja", "esinema", "esinemine", "esitama", "esitamine", "esiteks", "esitlema", "esitus", "esmaabi", "esmakordselt", "esmalt", "esmane", "esmaspev", "etapp", "etendus", "ette", "etteheide", "ettekandja", "ettekanne", "ettekujutus", "ettepanek", "ettepoole", "ettevaatlik", "ettevaatlikult", "ettevaatus", "ettevalmistus", "euro", "eurone", "eurooplane", "fail", "fakt", "festival", "film", "filmima", "filosoofia", "finaal", "firma", "fond", "foto", "fotoaparaat", "fotograaf", "funktsioon", "gaas", "gaasipliit", "galerii", "garanteerima", "garantii", "garderoob", "geograafia", "giid", "graafik", "gramm", "grammatika", "grillima", "gripp", "grupp", "haamer", "haarama", "haav", "haavama", "habe", "hai", "haige", "haigekassa", "haigla", "haigus", "haigusleht", "hais", "haisema", "hakkama", "hakkima", "hakkliha", "halb", "hale", "hall", "halloo", "halvasti", "halvenema", "hambaarst", "hambahari", "hambapasta", "hammas", "hammustama", "hani", "hankima", "hankimine", "hapnik", "hapu", "hapukapsas", "hapukoor", "hapukurk", "harakas", "hari", "haridus", "harilik", "harilikult", "harima", "harjuma", "harjumus", "harjutama", "harjutamine", "harjutus", "harrastama", "haru", "haruldane", "harva", "hauakivi", "haud", "haukuma", "hea", "heaks", "heategevus", "heeringas", "hein", "heitma", "hektar", "hele", "heli", "helikopter", "helilooja", "helisema", "helistama", "helkur", "herilane", "hernes", "hetk", "higi", "higistama", "hiir", "hiline", "hilinema", "hilinemine", "hilja", "hiljem", "hiljuti", "hiljutine", "hind", "hindama", "hindamine", "hing", "hingama", "hinnang", "hinne", "hirm", "hirmus", "hirmutama", "hobi", "hobune", "hoiak", "hoiatama", "hoiatus", "hoidma", "hoidmine", "hoiduma", "hoius", "homme", "hommik", "hommikumantel", "hommikune", "hommikuti", "homne", "honorar", "hooaeg", "hoog", "hool", "hooldaja", "hooldama", "hooldus", "hoolealune", "hoolikalt", "hoolima", "hoolimata", "hoolitsema", "hoolitsemine", "hoone", "hoopis", "hoov", "hotell", "hukkuma", "hukkunu", "hulgas", "hulgast", "hulk", "hulka", "hull", "hunnik", "hunt", "huul", "huulepulk", "huumor", "huumorimeel", "huvi", "huviline", "huvitama", "huvitav", "ida", "idee", "iga", "igapevane", "igasugune", "igatahes", "igati", "igatsema", "igav", "iialgi", "iiveldama", "ikka", "ikkagi", "ilm", "ilma", "ilmaennustus", "ilmakaar", "ilmateade", "ilme", "ilmne", "ilmnema", "ilmselt", "ilmuma", "ilmumine", "ilmutama", "ilu", "ilus", "ilutulestik", "ime", "imelik", "imema", "imestama", "imetlema", "imik", "inetu", "infarkt", "info", "informatsioon", "informeerima", "infotehnoloogia", "ingel", "inglane", "inglise", "ingliskeelne", "inimene", "inimlik", "instituut", "internet", "internetipank", "intervjuu", "intress", "investeerima", "isa", "isane", "ise", "iseenda", "iseenese", "iseenesest", "isegi", "iseloom", "iseloomulik", "iseloomustama", "iseseisev", "iseseisvalt", "iseseisvus", "isik", "isiklik", "isiklikult", "isiksus", "isikukood", "isikutunnistus", "issi", "iste", "istekoht", "istuma", "istung", "istutama", "isu", "jaa", "jaam", "jaanipev", "jaanuar", "jaatav", "jagama", "jagamine", "jagu", "jaguma", "jagunema", "jah", "jahe", "jahimees", "jaht", "jahu", "jakk", "jaksama", "jala", "jalakija", "jalalaba", "jalaluu", "jalanأµu", "jalats", "jalg", "jalgpall", "jalgratas", "jalgrattur", "jalgsi", "jalutama", "janu", "jaoks", "jaoskond", "jaotama", "jogurt", "joodik", "jooga", "joogivesi", "jook", "jooks", "jooksma", "jooksmine", "jooksul", "jooma", "joomine", "joon", "joonis", "joonistama", "joonlaud", "jope", "juba", "jube", "juhataja", "juhatama", "juhatus", "juhe", "juhend", "juhendaja", "juhendama", "juhiluba", "juht", "juhtima", "juhtimine", "juhtiv", "juhtkond", "juhtum", "juhtuma", "juhtunu", "juhus", "juhuslik", "juhuslikult", "julge", "julgelt", "julgema", "julgeolek", "julgus", "julm", "jumal", "jumalateenistus", "juriidiline", "jurist", "just", "justkui", "jutt", "jutukas", "jutumrgid", "jutustama", "juubel", "juuksed", "juuksur", "juuli", "juuni", "juur", "juurde", "juures", "juurest", "juurvili", "juust", "juut", "kaal", "kaalikas", "kaalud", "kaaluma", "kaamera", "kaart", "kaas", "kaasa", "kaasaegne", "kaasas", "kaaskiri", "kaaslane", "kaasmaalane", "kaasnema", "kaassأµna", "kaastunne", "kabe", "kabinet", "kade", "kaduma", "kadumine", "kadunu", "kaebama", "kaebus", "kael", "kaelakee", "kaer", "kaev", "kaevama", "kagu", "kahanema", "kahekesi", "kahekordne", "kaheksa", "kaheksas", "kaheksasada", "kaheksateist", "kahetoaline", "kahetsema", "kahju", "kahjuks", "kahjulik", "kahjum", "kahjustama", "kahtlane", "kahtlema", "kahtlemata", "kahtlus", "kahtlustama", "kahvel", "kaine", "kainelt", "kaitse", "kaitsevgi", "kaitsja", "kaitsma", "kaitsmine", "kajakas", "kajastama", "kajut", "kakao", "kaklema", "kaklus", "kaks", "kaksik", "kaksikud", "kakssada", "kaksteist", "kaktus", "kala", "kalad", "kalamees", "kalduma", "kalender", "kaljukits", "kalkun", "kallal", "kallale", "kallas", "kallim", "kallis", "kalliskivi", "kallistama", "kalmistu", "kama", "kamin", "kamm", "kammima", "kampaania", "kampsun", "kana", "kanal", "kanaliha", "kanalisatsioon", "kand", "kandidaat", "kandideerima", "kandiline", "kandma", "kandmine", "kanep", "kange", "kangelane", "kann", "kannatama", "kannatanu", "kannatlik", "kannatus", "kannel", "kant", "kantselei", "kaotaja", "kaotama", "kaotamine", "kaotus", "kapp", "kapsas", "kapten", "kapuuts", "kardin", "kari", "karikakar", "karikas", "karistama", "karistamine", "karistus", "karjuma", "karjr", "karm", "karp", "kartma", "kartul", "karu", "karusmari", "karv", "karvane", "kas", "kask", "kass", "kassa", "kassipoeg", "kast", "kastan", "kaste", "kastma", "kasu", "kasukas", "kasulik", "kasum", "kasutaja", "kasutajanimi", "kasutama", "kasutamine", "kasutus", "kasv", "kasvama", "kasvataja", "kasvatama", "kasvatamine", "kasvatus", "kasvuhoone", "katastroof", "kate", "katkema", "katkestama", "katki", "katkine", "katma", "katoliku", "katse", "katsetama", "katsetus", "katsuma", "katus", "kaua", "kauaks", "kaubamaja", "kaudu", "kauge", "kaugel", "kaugele", "kaugelt", "kaugeltki", "kaugus", "kaunis", "kaunistama", "kaup", "kauplema", "kauplus", "kauss", "kava", "kaval", "kavandama", "kavatsema", "keefir", "keegi", "keel", "keelama", "keeld", "keelduma", "keeleoskus", "keema", "keemia", "keerama", "keerlema", "keeruline", "keetma", "keha", "kehaline", "kehaosa", "kehtestama", "kehtima", "kehtiv", "kehv", "kelder", "kelk", "kell", "kellaaeg", "kelner", "kena", "kenasti", "kera", "kerge", "kergelt", "kergesti", "kerkima", "kes", "keset", "keskaegne", "keskealine", "keskel", "keskele", "keskelt", "keskenduma", "keskharidus", "keskkond", "keskkool", "kesklinn", "keskmine", "keskmiselt", "keskus", "kestma", "kett", "kevad", "kevadine", "kibe", "kihluma", "kiht", "kihutama", "kiik", "kiirabi", "kiire", "kiirelt", "kiirendama", "kiiresti", "kiirtee", "kiirus", "kiirustama", "kiitma", "kiitus", "kiiver", "kile", "kilekott", "kilo", "kilogramm", "kilomeeter", "kilone", "kilpkonn", "kindel", "kindlalt", "kindlasti", "kindlus", "kindlustama", "kindlustus", "kindral", "king", "kingitus", "kingsepp", "kink", "kinkima", "kinnas", "kinni", "kinnine", "kinnisvara", "kinnitama", "kinnitus", "kino", "kippuma", "kirg", "kiri", "kirik", "kirjalik", "kirjalikult", "kirjand", "kirjandus", "kirjanik", "kirjastus", "kirjavahetus", "kirjeldama", "kirjeldus", "kirju", "kirjutama", "kirjutamine", "kirjutis", "kirjutuslaud", "kirp", "kirre", "kirss", "kirst", "kirurg", "kirves", "kisa", "kitarr", "kits", "kitsas", "kiusama", "kivi", "klaas", "klahv", "klass", "klassijuhataja", "klassika", "klassikaline", "klassivend", "klaver", "klaviatuur", "kleepima", "kleit", "klient", "kliima", "klooster", "klubi", "kodakondsus", "kodanik", "kodu", "koduleht", "kodulind", "kodulinn", "koduloom", "kodumaa", "kodumaine", "kodumasin", "kodune", "kodutu", "koer", "kogelema", "kogema", "kogemata", "kogemus", "kogenud", "kogu", "kogudus", "kogum", "koguma", "kogumine", "kogunema", "koguni", "kogus", "kohal", "kohale", "kohalik", "kohalt", "kohanema", "kohapeal", "kohaselt", "kohati", "kohe", "kohev", "koht", "kohta", "kohtama", "kohtlema", "kohtuma", "kohtumine", "kohtunik", "kohtuotsus", "kohupiim", "kohus", "kohustama", "kohustus", "kohustuslik", "kohutav", "kohv", "kohver", "kohvik", "kohvimasin", "kohvipaus", "kokk", "kokku", "kokkulepe", "kokkutulek", "kokteil", "kole", "kolima", "kolimine", "kolju", "kollane", "kolleeg", "kolm", "kolmandik", "kolmapev", "kolmas", "kolmekordne", "kolmetoaline", "kolmnurk", "kolmnurkne", "kolmsada", "kolmteist", "kolmveerand", "koma", "komisjon", "komitee", "komm", "komme", "kommentaar", "kommenteerima", "kompanii", "komplekt", "kompromiss", "konflikt", "kongress", "konjak", "konkreetne", "konkurents", "konkurss", "konn", "konserv", "kontakt", "kontekst", "konto", "kontor", "kontoritarbed", "kontroll", "kontrollima", "kontrollimine", "konts", "kontsert", "konverents", "koobas", "kook", "kool", "koolilaps", "koolimaja", "koolitus", "koolivend", "koolon", "koondama", "koondis", "koonduma", "koopia", "koor", "koorem", "koorima", "koormus", "koos", "koosnema", "koosolek", "koosseis", "koostama", "koostamine", "koostis", "kopeerima", "kops", "koputama", "kord", "kordama", "korduma", "korduv", "korduvalt", "koridor", "koristaja", "koristama", "koristamine", "korjama", "korjamine", "kork", "korpus", "korraga", "korraks", "korral", "korraldama", "korraldamine", "korraldus", "korralik", "korralikult", "korrastama", "korrektne", "korruptsioon", "korrus", "korrutama", "korsten", "korter", "kortermaja", "korts", "kortsus", "korv", "korvpall", "kosk", "kosmeetik", "kosmeetika", "kosmos", "kostma", "kotkas", "kotlet", "kott", "kraad", "kraadiklaas", "kraadine", "kraan", "kraanikauss", "krae", "krediitkaart", "kreem", "krevett", "kriis", "kriitik", "kriitika", "kriitiline", "kristlik", "kritiseerima", "krokodill", "kroon", "krooniline", "krunt", "kruus", "kruvi", "kruvikeeraja", "kuduma", "kudumine", "kuhu", "kuhugi", "kui", "kuid", "kuidagi", "kuidas", "kuigi", "kuiv", "kuivama", "kuivatama", "kuju", "kujund", "kujundama", "kujundamine", "kujunema", "kujutama", "kujutis", "kukal", "kukeseen", "kukk", "kukkuma", "kukutama", "kuld", "kuldne", "kuldnokk", "kulg", "kulgema", "kull", "kulm", "kulp", "kultuur", "kultuurikeskus", "kulu", "kulul", "kuluma", "kulutama", "kulutus", "kumb", "kumbki", "kumm", "kummaline", "kummardama", "kummik", "kuna", "kunagi", "kunagine", "kuni", "kuninganna", "kuningas", "kunst", "kunstimuuseum", "kunstlik", "kunstnik", "kurat", "kurb", "kurbus", "kurg", "kuri", "kuritegevus", "kuritegu", "kurjategija", "kurk", "kurss", "kursus", "kurt", "kurtma", "kurv", "kurvalt", "kurvastama", "kus", "kusagil", "kusagile", "kusagilt", "kusjuures", "kuskil", "kuskile", "kuskilt", "kust", "kustuma", "kustutama", "kustutuskumm", "kutse", "kutsekool", "kutsikas", "kutsuma", "kuu", "kuues", "kuul", "kuulaja", "kuulama", "kuulamine", "kuulma", "kuulmine", "kuulsus", "kuuluma", "kuulumine", "kuulus", "kuulutama", "kuulutus", "kuum", "kuus", "kuusk", "kuussada", "kuusteist", "kvaliteet", "kvaliteetne", "kvartal", "kviitung", "kes", "kest", "laad", "laadima", "laager", "laat", "labidas", "ladu", "laduma", "laekuma", "laen", "laenama", "laenutama", "laenutus", "laev", "lagi", "lagunema", "lahe", "lahendama", "lahendamine", "lahendus", "lahing", "lahja", "lahke", "lahku", "lahkuma", "lahkumine", "laht", "lahti", "lahtine", "lahus", "lahutama", "lahutus", "lai", "laiali", "laialt", "laiendama", "laienema", "laine", "laip", "laisk", "laiune", "laius", "lamama", "lame", "lammas", "lammutama", "lamp", "langema", "langetama", "langus", "laps", "lapsehoidja", "lapselaps", "lapsepأµlv", "lapsevanem", "las", "laskemoon", "laskma", "laskuma", "lasteaed", "lastekodu", "lastevanemad", "lauamng", "laud", "laul", "laulatus", "laulja", "laulma", "laulupidu", "laup", "laupev", "lausa", "lause", "lausuma", "laut", "lava", "lavastaja", "lavastama", "lavastus", "leedu", "leedulane", "leek", "legend", "lehm", "leht", "lehvitama", "leib", "leidma", "leidmine", "leiduma", "lein", "leiutama", "lektor", "lemmik", "lemmikloom", "lend", "lendama", "lennujaam", "lennuk", "lennuvli", "lepatriinu", "leping", "leppima", "lesk", "lett", "levi", "levik", "levima", "levitama", "libe", "libisema", "liblikas", "lift", "ligi", "ligikaudu", "liha", "lihas", "lihtne", "lihtsalt", "liialdama", "liialt", "liiga", "liige", "liiges", "liigne", "liigutama", "liigutus", "liik", "liiklus", "liiklusmrk", "liikuma", "liikumine", "liim", "liin", "liit", "liiter", "liitma", "liitrine", "liitsأµna", "liituma", "liitumine", "liiv", "lill", "lilla", "lillepott", "lillkapsas", "limonaad", "lina", "lind", "linn", "linnaosa", "linnapea", "lint", "lipp", "lips", "lisa", "lisama", "lisanduma", "loe", "loend", "loeng", "loetelu", "lohutama", "lokkis", "loll", "lomp", "lonkama", "loobuma", "loobumine", "loodetavasti", "loodus", "looduslik", "loogiline", "loojuma", "loom", "looma", "loomaaed", "loomaliha", "loomine", "looming", "loominguline", "loomulik", "loomulikult", "loosung", "lootma", "lootus", "lootusetu", "loovutama", "loss", "loterii", "luba", "lubadus", "lubama", "lugeja", "lugema", "lugemine", "lugu", "lugupeetud", "lugupidamine", "luik", "lukk", "lumememm", "lumi", "lumine", "lusikas", "luteri", "luu", "luukere", "luuletaja", "luuletus", "maa", "maadlus", "maailm", "maailmameister", "maakond", "maal", "maalima", "maanduma", "maantee", "maapind", "maas", "maasikas", "maast", "maastik", "madal", "madalal", "madalale", "madalalt", "madrats", "madrus", "madu", "magama", "magamiskott", "magamistuba", "mage", "magu", "magus", "magustoit", "maha", "mahl", "mahlane", "maht", "mahtuma", "mai", "maikelluke", "maine", "mainima", "maitse", "maitseaine", "maitsev", "maitsma", "maja", "majandus", "majanduslik", "majanduslikult", "majonees", "makaron", "maks", "makse", "maksja", "maksma", "maksmine", "maksuamet", "male", "mandariin", "mander", "mantel", "mari", "mark", "marsruut", "masendus", "masin", "mask", "mass", "matemaatika", "materiaalne", "materjal", "matk", "matkama", "matma", "matus", "matused", "medal", "meditsiin", "meel", "meeldima", "meeldiv", "meeldivalt", "meelega", "meelelahutus", "meeleolu", "meelest", "meelitama", "meene", "meenuma", "meenutama", "mees", "meeskond", "meessugu", "meeter", "meetod", "meetrine", "mehaanik", "mehhanism", "meie", "meik", "meil", "meiliaadress", "meister", "meremees", "meri", "mesi", "mesilane", "metall", "mets", "metskits", "metsloom", "miinus", "miks", "miljard", "miljon", "millal", "millalgi", "millegiprast", "millimeeter", "milline", "mina", "minek", "minema", "mineraalvesi", "minevik", "mingi", "mingisugune", "ministeerium", "minister", "minut", "mis", "miski", "missugune", "mitmekesi", "mitmes", "mitmesugune", "mitmus", "mitte", "mitu", "mobiiltelefon", "modell", "moment", "mood", "moodi", "moodne", "moodustama", "moos", "mootor", "mootorratas", "moraalne", "mudel", "mugav", "mugavus", "muide", "muidu", "muidugi", "muinasjutt", "mujal", "mujale", "mujalt", "muld", "mulje", "mull", "mullu", "mullune", "muna", "murdma", "murduma", "mure", "murelik", "muretsema", "muretu", "muru", "muruniiduk", "musi", "must", "muster", "mustikas", "muu", "muudatus", "muudkui", "muuseas", "muuseum", "muusik", "muusika", "muusikal", "muusikaline", "muutlik", "muutma", "muutmine", "muutuma", "muutumine", "muutus", "naaber", "naasma", "nad", "nael", "naer", "naeratama", "naeratus", "naerma", "nagi", "nagu", "nahk", "naine", "naissugu", "nakkushaigus", "nali", "naljakas", "napilt", "napp", "nappima", "narkomaan", "narkootikum", "nartsiss", "natuke", "natukene", "nautima", "neelama", "neer", "negatiivne", "neitsi", "neiu", "neli", "nelisada", "neliteist", "neljandik", "neljas", "nelk", "nemad", "nii", "niigi", "niikuinii", "niimoodi", "niipalju", "niipea", "niisama", "niisiis", "niiske", "niisugune", "niit", "niitma", "niiviisi", "nimekiri", "nimeline", "nimelt", "nimetama", "nimetus", "nimi", "nina", "ninasarvik", "ning", "nisu", "noh", "nohu", "nojah", "nokk", "noogutama", "nool", "noor", "noormees", "nooruk", "norm", "normaalne", "notar", "november", "nuga", "nukk", "null", "number", "nupp", "nurk", "nurmenukk", "nutma", "nutt", "nuuskama", "nuusutama", "objekt", "odav", "oder", "ohkama", "ohoo", "oht", "ohtlik", "ohustama", "ohutu", "ohver", "ohvitser", "oja", "okas", "oks", "oksendama", "oktoober", "olek", "olema", "olemasolu", "olematu", "olemine", "olemus", "olend", "olenema", "oletama", "olevik", "olgu", "olud", "olukord", "oluline", "oluliselt", "oma", "omadus", "omaette", "omakorda", "omaksed", "omama", "omamoodi", "omand", "omandama", "omandamine", "omane", "omanik", "omavahel", "omavaheline", "ometi", "onu", "ookean", "ooper", "ootama", "ootamatu", "ootamatult", "ootus", "operatsioon", "optimistlik", "orav", "orel", "organ", "organisatsioon", "organiseerima", "organism", "orkester", "osa", "osakond", "osaleja", "osalema", "osalemine", "osaline", "osaliselt", "osav", "osavalt", "oskama", "oskus", "ost", "ostja", "ostma", "ostmine", "ostukeskus", "osutama", "osutuma", "ots", "otsa", "otsas", "otsast", "otse", "otsene", "otseselt", "otsima", "otsimine", "otstarbekas", "otstarve", "otsus", "otsustama", "otsustamine", "otsustav", "paar", "paat", "paavst", "paber", "padi", "pael", "pagar", "pagas", "paha", "pahandama", "pahandus", "pahane", "paigaldama", "paigaldamine", "paigutama", "paik", "paiknema", "paiku", "paindlik", "paistetus", "paistma", "pakane", "pakend", "pakiruum", "pakk", "pakkima", "pakkuma", "pakkumine", "paks", "pala", "palav", "palavik", "paljas", "palju", "palk", "palkama", "pall", "palsam", "paluma", "palun", "palve", "palvetama", "panema", "pangaarve", "pangaautomaat", "pangakaart", "pangakonto", "pank", "pankrot", "pankur", "pann", "pannkook", "panus", "papp", "paprika", "paraad", "paragrahv", "paraku", "parandama", "parandamine", "parandus", "paranema", "paras", "paratamatult", "parem", "paremal", "paremale", "paremalt", "park", "parkima", "parkimine", "parkla", "parlament", "parool", "part", "partei", "partii", "partner", "pass", "pasta", "pastakas", "pastor", "patarei", "patsient", "paus", "pea", "peaaegu", "peagi", "peal", "peale", "pealegi", "pealinn", "pealkiri", "pealt", "pealtnha", "pealtvaataja", "pealuu", "peamine", "peaminister", "peamiselt", "peaosa", "peatama", "peategelane", "peatoimetaja", "peatuma", "peatus", "peavalu", "pedagoog", "peegel", "peegeldama", "peen", "peenar", "peenike", "peenis", "peenraha", "peet", "pehme", "peigmees", "peitma", "peituma", "peksma", "pension", "pere", "perearst", "perekond", "perekonnaliige", "perekonnanimi", "perekonnaseis", "pereliige", "peremees", "perenaine", "periood", "pesa", "pesema", "pesemine", "pesu", "pesumasin", "pesupulber", "petersell", "petma", "pettuma", "pettus", "pidama", "pidamine", "pidev", "pidevalt", "pidi", "pidu", "pidulik", "pidur", "pidurdama", "pigem", "pigistama", "pihta", "piibel", "piim", "piinlik", "piir", "piirama", "piirduma", "piirivalve", "piirkond", "piisama", "piisav", "piisavalt", "pikaajaline", "pikali", "pikalt", "pikendama", "pikk", "pikkune", "pikkus", "piklik", "pildistama", "pilet", "pilk", "pill", "piloot", "pilt", "pilv", "pilves", "pilvine", "pilvitu", "pime", "pimedus", "pind", "pindala", "pinge", "pinginaaber", "pingutama", "pingutus", "pink", "pintsak", "pintsel", "pipar", "piparkook", "pirn", "pirukas", "pisar", "pisike", "pistma", "pisut", "plaan", "plaanima", "plaaster", "plaat", "plahvatama", "plahvatus", "plakat", "plaksutama", "planeerima", "planeet", "plast", "plats", "pleier", "plekk", "pliiats", "pliiatsiteritaja", "pliit", "ploom", "pluss", "pluus", "poeg", "poiss", "poks", "poliitik", "poliitika", "poliitiline", "polikliinik", "politsei", "politseinik", "pomm", "pood", "pool", "poolaasta", "pooldama", "poole", "pooleks", "pooleli", "poolest", "poolsaar", "poolt", "poolteist", "pooma", "populaarne", "populaarsus", "porgand", "pori", "portree", "positiivne", "positsioon", "post", "postiindeks", "postkaart", "postkast", "postkontor", "postmark", "pott", "praad", "praadima", "praam", "praegu", "praegune", "praht", "praktika", "praktiline", "prantslane", "prantsuse", "preemia", "preester", "preili", "president", "pressima", "prillid", "printer", "prints", "printsess", "probleem", "professionaalne", "professor", "programm", "projekt", "pronks", "proov", "proovikabiin", "proovima", "protest", "protseduur", "protsent", "protsess", "proua", "provints", "prussakas", "pruukima", "pruun", "pruut", "publik", "pudel", "puder", "puhas", "puhastama", "puhastamine", "puhkama", "puhkema", "puhkepev", "puhkus", "puhtalt", "puhtus", "puhul", "puhuma", "puiestee", "puit", "pulber", "pulk", "pulm", "pulmad", "pult", "punane", "punkt", "puravik", "purju", "purjus", "purk", "purskkaev", "puru", "purunema", "putukas", "puu", "puuduma", "puudumine", "puudus", "puudutama", "puue", "puuk", "puur", "puus", "puutuma", "puuvili", "puuvill", "puuvillane", "raadio", "raam", "raamat", "raamatukogu", "raamatupidaja", "raamatupidamine", "raamatupood", "raba", "rada", "radiaator", "raha", "rahakott", "rahaline", "rahaliselt", "rahastama", "rahasumma", "rahe", "rahu", "rahuldama", "rahuldamine", "rahulik", "rahulikult", "rahustama", "rahvas", "rahvus", "rahvuslik", "rahvusvaheline", "rahvusvaheliselt", "raiskama", "rajama", "rajamine", "rajoon", "rakendama", "rakett", "rakk", "rand", "range", "ranne", "rannik", "raport", "raputama", "rase", "raske", "raskelt", "raskus", "rass", "rasv", "rasvane", "ratas", "ratastool", "ratsutama", "raud", "raudne", "raudtee", "raudteejaam", "ravi", "ravikindlustus", "ravim", "ravima", "reaalne", "reaalselt", "reageerima", "rebane", "rebima", "redel", "redis", "reede", "reegel", "referaat", "reform", "registratuur", "registreerima", "registreerimine", "regulaarne", "regulaarselt", "reguleerima", "reha", "rehv", "reis", "reisija", "reisima", "reket", "reklaam", "reklaamima", "rekord", "rektor", "religioon", "relv", "remont", "remontima", "rent", "rentima", "reserveerima", "ressurss", "restoran", "retsept", "rida", "ridaelamu", "rihm", "riideese", "riidepuu", "riidlema", "riie", "riietus", "riigiametnik", "riigiasutus", "riigikogu", "riik", "riiklik", "riis", "riisuma", "riiul", "riiv", "riivima", "rikas", "rike", "rikki", "rikkis", "rikkuma", "rikkumine", "rikkus", "rind", "ring", "ringi", "rinnahoidja", "rippuma", "ripsmed", "riputama", "risk", "rist", "risti", "ristima", "ristmik", "rivaal", "roheline", "rohi", "rohkem", "rohkesti", "roll", "romaan", "romantiline", "rong", "ronima", "rool", "roomama", "roos", "roosa", "rooste", "rootsi", "rootslane", "rott", "rubla", "rukis", "rukkilill", "rulluisk", "rumal", "rumalalt", "rumalus", "rusikas", "ruttama", "ruttu", "ruuduline", "ruum", "ruut", "ruutmeeter", "saabas", "saabuma", "saabumine", "saade", "saadik", "saag", "saagima", "saaja", "saak", "saal", "saama", "saamine", "saar", "saatekiri", "saatel", "saatkond", "saatma", "saatmine", "saatus", "saavutama", "saavutamine", "saavutus", "saba", "sada", "sadakond", "sadam", "sadama", "sadu", "sage", "sagedus", "sageli", "sahtel", "sai", "sajand", "saksa", "sakslane", "saksofon", "saladus", "salaja", "salajane", "salaprane", "salat", "sale", "sall", "salvestama", "sama", "samamoodi", "samas", "samasugune", "samet", "samm", "sammal", "samuti", "sandaal", "sari", "sarnane", "sarnanema", "sarv", "sattuma", "saun", "savi", "seade", "seadma", "seadus", "seadusevastane", "seaduslik", "seal", "sealhulgas", "sealiha", "sealne", "sealsamas", "sealt", "seas", "seast", "see", "seega", "seejuures", "seekord", "seekordne", "seelik", "seeme", "seen", "seep", "seeria", "sees", "seesama", "seespool", "seest", "seestpoolt", "seevastu", "segadus", "segama", "segamini", "segane", "segi", "segu", "seiklus", "sein", "seis", "seisma", "seisnema", "seisukoht", "seisukord", "seisund", "seitse", "seitsesada", "seitseteist", "seitsmes", "sekka", "sekkuma", "seks", "seksuaalne", "sekund", "seletama", "seletus", "selg", "selge", "selgelt", "selgitama", "selgitus", "selgroog", "selguma", "selgus", "selili", "seljakott", "selline", "selts", "seltskond", "semikoolon", "seminar", "seni", "senine", "senini", "sent", "sentimeeter", "seos", "seoses", "sepik", "sepp", "september", "serv", "sest", "sibul", "side", "sidekriips", "sidrun", "siduma", "siga", "sigaret", "signaal", "siht", "sihtasutus", "sihtkoht", "sihtnumber", "siia", "siiani", "siid", "siider", "siil", "siin", "siinkohal", "siinne", "siinsamas", "siiras", "siis", "siiski", "siit", "sild", "sile", "silm", "silmapaistev", "silp", "silt", "sina", "sinep", "sinimustvalge", "sinine", "sink", "sinna", "sipelgas", "sirge", "sirgelt", "sisaldama", "sisemine", "sisenema", "sisestama", "sisse", "sisseastumine", "sissejuhatus", "sissekirjutus", "sissepoole", "sissetulek", "sisu", "sisukord", "sisustus", "situatsioon", "skandaal", "skeem", "skorpion", "sobima", "sobiv", "soe", "soeng", "sokk", "solvama", "solvuma", "soo", "soodne", "soodsalt", "soodustus", "soojendama", "soojus", "sool", "soolane", "soome", "soomlane", "sooritama", "soov", "soovija", "soovima", "soovitama", "soovitus", "sort", "sosistama", "sotsiaalne", "spetsiaalne", "spetsiaalselt", "spetsialist", "sponsor", "spordiala", "sport", "sportlane", "sportlik", "staadion", "stabiilne", "start", "startima", "statistika", "stiil", "stipendium", "stjuardess", "streik", "stress", "struktuur", "subtiiter", "sugu", "sugulane", "suhe", "suhkur", "suhteline", "suhteliselt", "suhtes", "suhtlema", "suhtlemine", "suhtlus", "suhtuma", "suhtumine", "suits", "suitsetama", "suitsetamine", "sukelduma", "sukk", "sulama", "sularaha", "sularahaautomaat", "sulatama", "sulg", "sulgema", "sulgemine", "sulud", "summa", "sundima", "supp", "surema", "surm", "surnu", "surnuaed", "surnud", "surnukeha", "suruma", "surve", "suss", "suu", "suudlema", "suudlus", "suuline", "suuliselt", "suunama", "suund", "suunduma", "suur", "suurendama", "suurendamine", "suurenema", "suurenemine", "suureprane", "suurepraselt", "suuresti", "suurune", "suurus", "suusataja", "suusatama", "suusk", "suutma", "suveniir", "suvi", "suvila", "suvine", "silima", "silitama", "taas", "taastama", "taastamine", "tabama", "tabel", "tablett", "taevas", "taga", "tagama", "tagant", "tagantpoolt", "tagaotsitav", "tagapool", "tagasi", "tagasihoidlik", "tagastama", "tagatis", "tagavara", "tagumik", "tagumine", "tagurpidi", "taha", "tahapoole", "tahe", "tahke", "tahtma", "tahtmine", "tahvel", "taim", "tainas", "tajuma", "takistama", "takistus", "takso", "taksojuht", "taktika", "tald", "taldrik", "talje", "talu", "taluma", "talunik", "talv", "talvine", "tamm", "tankima", "tants", "tantsija", "tantsima", "taoline", "taotlema", "taotlus", "tapeet", "tapma", "tapmine", "tarbija", "tarbima", "tarbimine", "targalt", "tark", "tarkus", "tarve", "tarvis", "tarvitama", "tasa", "tasakaal", "tasand", "tasane", "tase", "tasku", "taskurtik", "tass", "tasu", "tasuline", "tasuma", "tasumine", "tasuta", "tatar", "taust", "tava", "tavaline", "tavaliselt", "teade", "teadlane", "teadlik", "teadlikult", "teadma", "teadmine", "teadus", "teaduslik", "teadvus", "teadvustama", "teatama", "teatav", "teatavasti", "teater", "teatud", "teave", "teavitama", "tee", "teekond", "teel", "teema", "teene", "teenima", "teenindama", "teenindus", "teenistus", "teenus", "teenustasu", "teesklema", "tegelane", "tegelema", "tegelik", "tegelikkus", "tegelikult", "tegema", "tegemine", "tegevus", "tegija", "tegu", "tegur", "tegutsema", "tegutsemine", "tehas", "tehing", "tehnika", "tehniline", "tehnoloogia", "teie", "teine", "teineteise", "teisalt", "teiseks", "teisiti", "teismeline", "teistsugune", "teke", "tekikott", "tekitama", "tekitamine", "tekk", "tekkima", "tekkimine", "teksad", "teksased", "tekst", "telefon", "telefoninumber", "telekanal", "telekas", "teler", "televiisor", "televisioon", "telk", "tellija", "tellima", "tellimus", "tellis", "tema", "temperatuur", "tempo", "tennis", "teooria", "teos", "teostama", "tera", "terav", "teravili", "tere", "territoorium", "terve", "tervelt", "tervik", "tervis", "tervislik", "tervist", "tervitama", "tervitus", "testament", "tibu", "tige", "tigu", "tihane", "tihe", "tihedalt", "tihti", "tiib", "tiiger", "tiitel", "tikk", "tilk", "till", "tingima", "tingimus", "tipp", "toetaja", "toetama", "toetamine", "toetuma", "toetus", "tohtima", "tohutu", "toiduaine", "toidupood", "toime", "toimetaja", "toimetama", "toimetus", "toimik", "toimima", "toiming", "toimuma", "toimumine", "toimunu", "toit", "toitma", "toituma", "toll", "tollal", "tolm", "tolmuimeja", "tolmune", "tomat", "tonn", "toode", "tool", "tooma", "toon", "toorelt", "toores", "tootja", "tootma", "tootmine", "tore", "torkama", "torm", "tormine", "torn", "tort", "toru", "toss", "traagiline", "traat", "traditsioon", "traditsiooniline", "trahv", "traktor", "tramm", "transport", "trauma", "treener", "treenima", "treening", "trenn", "trepikoda", "trepp", "triibuline", "triikima", "triikimislaud", "triikraud", "triip", "trikk", "trikoo", "troll", "trumm", "truu", "tsirkus", "tualett", "tualettpaber", "tualettpott", "tuba", "tubli", "tublisti", "tudeng", "tugev", "tugevasti", "tugevdama", "tugevnema", "tugevus", "tugi", "tuginema", "tugitool", "tuhat", "tuhatoos", "tuhk", "tuisk", "tuju", "tulek", "tulekahju", "tulema", "tulemus", "tulenema", "tulev", "tulevane", "tulevik", "tuli", "tuline", "tulistama", "tulp", "tulu", "tulumaks", "tume", "tund", "tundlik", "tundma", "tundmatu", "tundmine", "tunduma", "tunduvalt", "tungima", "tunne", "tunnel", "tunnetama", "tunniplaan", "tunnistaja", "tunnistama", "tunnistus", "tunnus", "tunnustama", "tunnustus", "tuntud", "tupp", "turg", "turist", "turniir", "turvaline", "turvalisus", "turvamees", "tuttav", "tutvuma", "tutvus", "tutvustama", "tutvustamine", "tuul", "tuuline", "tuvastama", "tuvi", "uba", "udu", "udune", "uhke", "uhkus", "uisk", "uisutama", "ujula", "ujuma", "ujumine", "ujumisriided", "uks", "uksekell", "ulatama", "ulatuma", "ulatus", "umbes", "ummik", "uni", "unine", "unistama", "unistus", "unustama", "uppuma", "uriin", "usaldama", "usaldus", "usk", "usklik", "uskuma", "uskumatu", "uss", "uudis", "uudishimulik", "uuendus", "uuesti", "uurija", "uurima", "uurimine", "uurimus", "uuring", "uus", "uusaasta", "vaade", "vaal", "vaarikas", "vaas", "vaataja", "vaatama", "vaatamata", "vaatlema", "vaba", "vabaabielu", "vabadus", "vabalt", "vabandama", "vabandus", "vabandust", "vabanema", "vabariik", "vabastama", "vabatahtlik", "vabatahtlikult", "vabrik", "vaene", "vaenlane", "vaesus", "vaev", "vaevalt", "vagun", "vahe", "vaheaeg", "vahekord", "vahel", "vaheldus", "vahele", "vaheline", "vahelt", "vahemaa", "vahend", "vahendusel", "vahepeal", "vaher", "vahetama", "vahetamine", "vahetu", "vahetult", "vahetuma", "vahetund", "vahetus", "vaht", "vahva", "vaid", "vaidlema", "vaidlus", "vaikima", "vaikne", "vaikselt", "vaikus", "vaim", "vaimne", "vaimselt", "vaip", "vait", "vaja", "vajadus", "vajalik", "vajalikkus", "vajama", "vajuma", "vajutama", "valama", "vald", "valdama", "valdavalt", "valdkond", "valdus", "vale", "valesti", "valetama", "valge", "valgus", "valgusfoor", "valgustama", "vali", "valija", "valik", "valima", "valimine", "valimiskampaania", "valitseja", "valitsema", "valitsemine", "valitsus", "vallaline", "vallandama", "vallutama", "valmima", "valmimine", "valmis", "valmistama", "valmistamine", "valmistuma", "valu", "valus", "valutama", "valuuta", "valvama", "valve", "valvur", "vana", "vanaema", "vanaisa", "vanalinn", "vanasti", "vanem", "vang", "vangi", "vangis", "vangist", "vangla", "vanker", "vann", "vannituba", "vanur", "vanus", "vapp", "vapper", "vara", "varahommik", "varajane", "varane", "varas", "varastama", "varblane", "varem", "varemed", "vares", "vargus", "vari", "variant", "varjama", "varras", "varrukas", "vars", "varsti", "varu", "varuosa", "varustama", "varustus", "varvas", "vasak", "vasakul", "vasakule", "vasakult", "vastama", "vastand", "vastane", "vastas", "vastastikune", "vastav", "vastik", "vastu", "vastuolu", "vastupidav", "vastupidi", "vastupidine", "vastus", "vastutama", "vastutav", "vastutus", "vatt", "vedama", "vedel", "vedelik", "vedu", "veebruar", "veekogu", "veel", "veenduma", "veendumus", "veenma", "veerand", "veetma", "veevalaja", "veider", "veidi", "vein", "veiseliha", "vend", "vene", "venekeelne", "venelane", "venima", "veoauto", "veok", "veri", "verine", "verivorst", "versioon", "vesi", "vestlema", "vestlus", "video", "viga", "vigastama", "vigastus", "viha", "vihane", "vihaselt", "vihastama", "vihik", "vihjama", "vihje", "vihkama", "vihm", "vihmane", "vihmavari", "viibima", "viiendik", "viies", "viik", "viil", "viima", "viimane", "viimati", "viin", "viinamari", "viiner", "viirus", "viis", "viisa", "viisakalt", "viisakas", "viisakus", "viissada", "viisteist", "viitama", "viitenumber", "viitsima", "viiul", "viivis", "vikerkaar", "vilets", "vili", "vill", "villane", "virisema", "virsik", "visiit", "viskama", "vist", "vistrik", "vitamiin", "volitus", "voodi", "voodipesu", "vool", "voolama", "voor", "vorm", "vormistama", "vorst", "vuntsid"]