# source-normalized key -> RBI normalized key
ALIAS = {
 'blackorpheus':'manhadecarnaval',
 'inamellowtone':'inamellotone',
 'backhomeagaininindiana':'indiana',
 'take5':'takefive',
 'ourloveisheretostay':'loveisheretostay',
 'freddiethefreeloader':'freddiefreeloader',
 'wee':'allensalley',
 'unit7':'unitseven',
 'noblues':'pfrancing',
 'myfavouritethings':'myfavoritethings',
 'shadowofthesmile':'shadowofyoursmile',
 'georgia':'georgiaonmymind',
 'bluebolivarblues':'bolivarblues',
 'chegadesaudade':'nomoreblues',
 'canttakethatawayfromme':'theycanttakethatawayfromme',
 'eastofthesunandwestofthemoon':'eastofthesun',
 'donothingtillyouhearfromme':'donothintillyouhearfromme',
 'jumponatthewoodside':'jumpinatthewoodside',
 'whatadifferenceadaymakes':'whatadifferenceadaymade',
 'canthelplovinthatman':'canthelplovindatman',
 'wellyouneedent':'wellyouneednt',
 'senorblues':'senorblues',
 'waltzfordebbie':'waltzfordebby',
 'bluetrain':'bluetrane',
 'jodiegrind':'jodygrind',
 'mysecretlove':'secretlove',   # declared in the Invitation, Draft 10.3 p.149
 'sambadeorpheus':'sambadeorfeu',   # declared at the Appendix A head-note, Draft 10.3 p.65
}

# One name, two works. The opposite of a fold: these must NOT collapse together.
# The parenthetical on such a title is load-bearing and normalization would eat it,
# so a key built for joining has to fall back to the parenthetical-preserving form.
# code/verify.py asserts that no title outside this set collides in the pool.
HOMONYMS = {
 'milestones',       # the 1947 line and the 1958 modal piece, both Miles Davis
}
