"""Declared folds. Each entry joins a spelling in one source to the title as seated in
Draft 15. Normalization (norm.match_key) cannot derive any of them; a replication that
does not apply them will not reproduce the counts."""

# Variant spelling -> title as seated in Draft 15 (or as printed in a residue).
SEATED = {
    # FM.6 and the name table
    "Black Orpheus": "Manha De Carnaval",
    "A Day in the Life of a Fool": "Manha De Carnaval",
    "The Theme From Black Orpheus": "Manha De Carnaval",
    "Morning of the Carnival": "Manha De Carnaval",
    "Chega de Saudade": "No More Blues",
    "No Blues": "Pfrancing",
    "No Me Esqueca": "Recordame",
    "Georgia": "Georgia on My Mind",
    "Our Love Is Here to Stay": "Love Is Here to Stay",
    "Lady Be Good": "Oh, Lady Be Good!",
    "Freddie the Freeloader": "Freddie Freeloader",
    "Blue Trane": "Blue Train",
    "Do Nothing Till You Hear From Me": "Do Nothin' Till You Hear from Me",
    "Do Nothing Til You Hear From Me": "Do Nothin' Till You Hear from Me",
    "Budo": "Hallucinations",
    "Corner Pocket": "Until I Met You",
    "Dippermouth Blues": "Sugar Foot Stomp",
    "Duke's Place": "C Jam Blues",
    "Dr. Jekyll": "Dr. Jackle",
    "Back Home Again in Indiana": "Indiana",
    "In a Mellow Tone": "In a Mellotone",
    "Quiet Nights": "Corcovado",
    "Quiet Nights of Quiet Stars": "Corcovado",
    "Unit 7": "Unit Seven",
    "UMMG": "Upper Manhattan Medical Group",
    "Wee": "Allen's Alley",
    "Take 5": "Take Five",
    "Samba De Orpheus": "Samba De Orfeu",
    "Samba de Orfeo": "Samba De Orfeu",
    "Solid": "Solid (Shaw)",
    "Nancy": "Nancy (with the Laughing Face)",
    "On a Clear Day": "On a Clear Day (You Can See Forever)",
    "They Can't Take That Away": "They Can't Take That Away from Me",
    "Can't Take That Away From Me": "They Can't Take That Away from Me",
    "Yes and No": "Yes Or No",
    "Milestones": "Milestones (modal)",
    "Milestones (New)": "Milestones (modal)",
    "Goodbye Porkpie Hat": "Goodbye Pork Pie Hat",
    "Daydream": "Day Dream",
    "What a Difference a Day": "What a Difference a Day Made",
    "What a Difference a Day Makes": "What a Difference a Day Made",
    "(The) More I See You": "The More I See You",
    "You Stepped Out a Dream": "You Stepped Out of a Dream",
    # Levine's chapter, folds used in the vocal band worksheet (seven mechanical, two judgment)
    "Bewitched, Bothered, And Bewildered": "Bewitched",
    "Do Nothing 'Til You Hear From Me": "Do Nothin' Till You Hear from Me",
    "Don't Worry About Me": "Don't Worry 'Bout Me",
    "Every Time We Say Goodbye": "Ev'ry Time We Say Goodbye",
    "Folks Who Live On The Hill": "The Folks Who Live on the Hill",
    "The Meaning Of The Blues": "Meaning of the Blues",
    "That Old Devil Moon": "Old Devil Moon",
    "In My Solitude": "Solitude",                                  # judgment
    "I've Grown Accustomed To Your Face": "I've Grown Accustomed to Her Face",   # judgment
    # Miller's log (FM.6)
    "My Secret Love": "Secret Love",
    "Can't Help Lovin That Man": "Can't Help Lovin' Dat Man",
    # Forms a source prints that norm.match_key cannot reach. Each is the spelling in the
    # file named, joined to the title as seated or as printed in a residue. Sources are
    # cited as printed (Index 3.1.d); the fold is declared here rather than by correcting
    # the source row.
    "Until I Met You (Corner Pocket)": "Until I Met You",      # ranked 1,000 #522
    "Ba-lue Bolivar Ba-lues-are": "Bolivar Blues",             # Levine ch. 21
    "No Blues (Pfrancing)": "Pfrancing",                       # Watkins categorical
    "Jodie Grind, The": "The Jody Grind",                      # Watkins categorical
    "Well You Needen't": "Well You Needn't",                   # Miller 201 #191
    "Weaver Of Dreams": "(You're A) Weaver Of Dreams",         # Miller's log; App. B #2
    "Flintstones, The": "(Meet) The Flintstones",              # Watkins categorical; App. B #1
    # Levine chapter 21, as printed there. Twenty-six spellings the chapter carries that
    # match_key cannot reach: subtitles the chapter drops, a Portuguese title, one
    # misspelling, and one reading stated at App. A. Without them a replicator building
    # the Levine-only residue from the book returns 444 rather than the 420 at App. A.
    "52nd St. Theme": "52nd Street Theme",
    "All God's Chillun": "All God's Chillun Got Rhythm",
    "Amor Em Paz": "Once I Loved",                             # same title, twice in the chapter
    "Bess You Is My Woman": "Bess, You Is My Woman Now",
    "Canteloupe Island": "Cantaloupe Island",
    "Chicago": "Chicago (That Toddlin' Town)",
    "Everything I Love": "Ev'rything I Love",
    "Green Dolphin Street": "On Green Dolphin Street",
    "I'll Get By": "I'll Get By (As Long As I Have You)",
    "I'm An Old Cowhand": "I'm an Old Cowhand (From the Rio Grande)",
    "I'm Confessin'": "I'm Confessin' That I Love You",
    "It's A Lazy Afternoon": "Lazy Afternoon",
    "It's Too Late Now": "Too Late Now",
    "I've Got Rhythm": "I Got Rhythm",
    "Liza": "Liza (All the Clouds'll Roll Away)",
    "Moon Song": "Moon Song (That Wasn't Meant for Me)",
    "Organ Grinder": "Organ Grinder's Swing",
    "A Portrait Of Jenny": "Portrait of Jennie",
    "Shaw": "Shaw Nuff",                                       # files between Shall We Dance and She
    "So In Love": "So in Love (Am I)",
    "Stairway To The Stars": "Stairway to the Stars (Park Avenue Fantasy)",
    "They Say That Falling In Love Is Wonderful": "They Say It's Wonderful",
    "When The Saints Go Marchin' In": "When the Saints Go Marching In",
    "Who Cares?": "Who Cares? (So Long As You Care for Me)",
    "You're Driving Me Crazy": "You're Driving Me Crazy (What Did I Do?)",
    # Gioia, as printed there. Three subtitles the guide carries and the Index does not.
    "It Don't Mean a Thing (If It Ain't Got That Swing)": "It Don't Mean a Thing",
    "These Foolish Things (Remind Me of You)": "These Foolish Things",
    "St. James Infirmary Blues": "St. James Infirmary",
}

# Folds that are valid for one source and wrong for the others, keyed by the source they
# belong to. "Lonely Woman" is the case: Levine's chapter carries Silver's title, Gioia and
# Watkins carry Coleman's, and TABLE R.4 puts Coleman's outside the pool. A flat table
# cannot hold both readings, so a join applies BY_SOURCE for the file it is reading and
# SEATED everywhere.
BY_SOURCE = {
    "levine_chapter_21": {
        "Lonely Woman": "Lonely Woman (Silver)",   # judgment; App. A prints the reading
    },
}

# Joins that a fuzzy matcher will make and that are refused.
REFUSED = {
    ("I Love You", "P.S. I Love You"),
    ("Prancing", "Pfrancing"),
    ("Milestones (Old)", "Milestones (modal)"),
    ("Sugar", "Sugar (That Sugar Baby O' Mine)"),
    ("Lonely Woman", "Lonely Woman (Silver)"),
    ("The Theme", "52nd Street Theme"),
}
