import pytest
import time

from naughty_words.filters import NaughtyWords
from naughty_words.filters import CommonSubstitutions


def test_default_filter_no_match():
    nw_filter = CommonSubstitutions(['buttcheeks', 'genital', 'auto erotic', 'sexpot', 'mutha fukah', 'blonde on blonde action', 'penisbanger', 'givehead', 'paki', 'piece of shit', 'pervert', "nigger's", 'lubejob', 'ahole', 'fuckhead', 'nut case', 'nut sack', 'goatcx', 'prick', 'pusse', 'backdoorman', 'dicks', 'niggling', 'pissoff', 'poorwhitetrash', 'snownigger', 'copulate', 'juggs', 'niggur', 'polack', 'tonguethruster', 'dago', 'sodomise', 'nookie', 'farting', 'mothafuckaz', 'blumpkin', 'fuckedup', 'shrimping', 'fucks', 'peedo', 'slanteye', 'huge fat', 'arsepirate', 'niggor', 'poonany', 'skanky', 'bungabunga', 'penis', 'panties', 'jihad', 'picaninny', 'hatred', 'goddamnmuthafucker', 'shitfull', 'dammit', 'blackout', 'necro', 'double penetration', 'cuntlicking', 'goatse', 'hobo', 'shag', 'asswipe', 'footjob', 'fuckingcunt', 'thirdleg', 'puke', 'footfucker', 'fucktard', 'penile', 'spreadeagle', 'funfuck', 'wanking', 'bdsm', 'sexymoma', 'god damn', 'missionary position', 'footfuck', 'manhater', 'cok', 'livesex', 'cumshot', 'darkie', 'osama bin laden', 'jiggerboo', 'shitface', 'sand nigger', 'semen', 'shitfucker', 'shithole', 'nig nog', 'lezzer', 'sextoy', 'bumfuck', 'cockjockey', 'dego', 'fuuck', 'scissoring', 'smackthemonkey', 'blue waffle', 'vjayjay', 'wetspot', 'hater', 'hoar', 'fuckstick', 'dickwod', 'footlicker', 'satan', 'santorum', 'one guy one jar', 'bitchin', 'shitspitter', 'prince albert piercing', 'kooch', 'lmfao', 'analsex', 'cntz', 'dragqueen', 'minge', 'undressing', 'shited', 'stupidfucker', 'dipstick', 'giant cock', 'rimming', 'humping', 'cunthole', 'fagbag', 'penis-breath', 'mother fuker', 'baby juice', 'cumslut', 'jerkoff', 'cuntslut', 'fuckinright', 'handjob', 'mother-fucker', 'phukking', 'shitbreath', 'cock-sucker', 'shiteater', 'pornflick', 'doggiestyle', 'assmuncher', 'seaman staines', 'pedobear', 'unfuckable', 'brown showers', 'ass monkey', 'kuntz', 'douchewaffle', 'polesmoker', 'wog', 'shitstain', 'basterdz', 'crap', 'usama bin laden', 'whoreface', 'jizz', 'ladyboy', 'cyberslimer', 'nigre', 'coprophilia', 'sexy', 'butthole', 'dickmonger', 'lameass', 'gonzagas', 'dickbrain', 'assfuck', 'beatyourmeat', 'queaf', 'screwyou', 'commie', 'dumass', 'spread legs', 'cockburger', 'shitter', 'vajayjay', 'doochbag', 'spaghettinigger', 'whitetrash', 'guido', 'masturbating', 'futanari', 'arsekiss', 'deggo', 'shemale', 'gook', 'bbw', 'yaoi', 'goddamn', 'sextogo', 'turnon', 'beaver cleaver', 'slimeball', 'lactate', 'fuckyou', 'arsekisser', 'fuks', 'fuckboy', 'gayz', 'stiffy', 'marijuana', 'cockfight', 'fastfuck', 'cockhead', 'fingerfuckers', 'cockknob', 'flamer', 'pimper', 'queerbait', 'douchbag', 'barelylegal', 'qweers', 'nutcase', 'arselicker', 'barely legal', 'feltch', 'slut', 'kyke', 'fudge packer', 'asslover', 'sissy', 'mothafucka', 'extremist', 'butt', 'doggy style', 'puto', 'douch', 'zipper head', 'bimbos', 'lezz', 'whoor', 'molester', 'nastybitch', 'badfuck', 'kumbubble', 's&m', 'cockmuncher', 'chav', 'bumblefuck', 'kinky', 'asshat', 'fuck buttons', 'camgirl', 'retard', 'ejaculate', 'mofo', 'spacca', 'phuck', 'fistfucking', 'rimjob', 'clogwog', 'hillbillies', 'dicktickler', 'whitey', 'torture', 'fingerfucked', 'peenus', 'tongue in a', 'nigra', 'masterbate', 'analannie', 'bugger', 'faigs', 'thicko', 'breastlover', 'fagging', 'rearend', 'brunette action', 'beaners', 'muffindiver', 'nastyho', 'suicide girls', 'beastality', 'jagoff', 'biteme', 'cooter', 'kinkster', 'arsebandit', 'va-j-j', 'titlover', 'assfucker', 'clitoris', 'arsefucker', 'shitlist', 'female squirting', 'skullfuck', 'mafia', 'jizm', 'sperm', 'fagz', 'damn', 'gyppie', 'sexfarm', 'lickme', 'dickweasel', 'strip club', 'cawk', 'cuntlick', 'barface', 'jerk-off', 'puuker', 'clamdigger', 'snowback', 'bollocks', 'bitchass', 'cockshit', 'bastard', 'felching', 'arsejockey', 'asslicker', 'boob', 'abuser', 'shitdick', 'domination', 'lezzie', 'heeb', 'niggards', 'dickwad', 'faget', 'breastjob', 'play girl', 'cumfest', 'phonesex', 'terror', 'vagina', 'mutha fucker', 'panty', 'bukkake', 'bastardo', 'cunnie', 'shiter', 'skanks', 'whore', 'dickless', 'cocktease', 'dominatrix', 'whitenigger', 'bigbutt', 'hoe', 'dipshit', 'male squirting', 'masterbates', 'niiger', 'splittail', 'kumming', 'penises', 'assholz', 'mother fukker', 'shibari', 'stripper', 'titjob', 'beaver lips', 'butchdike', 'cherrypopper', 'gang bang', 'fuckfriend', 'mattressprincess', 'shite', 'dingleberries', 'vulva', 'dumshit', 'playbunny', 'fucknutt', 'crotchrot', 'bestial', 'pussyeater', 'sandnigger', 'asses', 'sexkitten', 'cockface', 'sixsixsix', 'pikey', 'limpdick', 'sluts', 'valjina', 'pimpjuic', 'brotherfucker', 'bulldyke', 'dog style', 'orgasm', 'phuking', 'bullcrap', 'rag head', 'bassterds', 'sexhound', 'hard on', 'molestor', 'Fukken', 'spunk', 'asscracker', 'fuckers', 'femdom', 'punanny', 'assbag', 'cunillingus', 'meatrack', 'hardon', 'fetish', 'shat', 'buttmunch', 'loverocket', 'hells', 'turd', 'datnigga', 'tunneloflove', 'cumming', 'puuke', 'yellowman', 'lesbayn', 'how to murder', 'whop', 'interracial', 'Fukah', 'kummer', 'popimp', 'bitchslap', 'gayfuck', 'arsefuck', 'crack-whore', 'fuckpig', 'tosser', 'sucks', 'masturbate', 'arsemunch', 'muff', 'mufflikcer', 'perv', 'timbernigger', 'dolcett', 'tittie', 'whorehouse', 'shagger', 'orgies', 'asslick', 'tonguetramp', 'gangbanger', 'hotdamn', 'pussee', 'butchdyke', 'pussie', 'arsewhore', 'urethra play', 'scumbag', 'niggerhole', 'qweir', 'sexy-slim', 'phukked', 'black cock', 'felch', 'motha fukker', 'hijacking', 'lesbo', 'defecate', 'assgoblin', 'jigaboo', 'shhit', 'yiffy', 'buttbang', 'hitlerism', 'big breasts', 'shaved beaver', 'pussypounder', 'paedo', 'hore', 'babeland', 'cleveland steamer', 'sadism', 'chode', 'hoes', 'boffing', 'skankey', 'nookey', 'tight white', 'munging', 'cacker', 'phuked', 'Fukin', 'bunghole', 'fuker', 'Fukker', 'eunuch', 'bastardz', 'splooge', 'kiddy fiddler', 'sexed', 'asshore', 'slavedriver', 'fuckbrain', 'orifice', 'barenaked', 'ass', 'chinc', 'shyte', 'niggled', 'play boy', 'jerk off', 'scrotum', 'homobangers', 'shit', 'molest', 'suckme', 'autoerotic', 'cunnilingus', 'cuntz', 'anal', 'shitz', 'spaghettibender', 'dumb ass', 'dilldos', 'fuck', 'shiz', 'chickslick', 'eatpussy', 'slutwear', 'shitbag', 'how to kill', 'kunilingus', 'gotohell', 'playgirl', 'jiggabo', 'mother fukah', 'swinger', 'kraut', 'premature', 'dickbeaters', 'scag', 'cumtart', 'coochie', 'executioner', 'arsemuncher', 'whigger', 'freakfuck', 'clitface', 'shitfaced', 'niggles', 'mothafucked', 'twink', 'motherfuckings', 'swastika', 'topless', 'jap', 'Fukk', 'bulldike', 'jubblies', 'snowballing', 'azzhole', 'eatballs', 'vibrator', 'tribadism', 'clitfuck', 'flyd', 'virginbreaker', 'nlgger', 'fuckbutter', 'shitcanned', 'polak', 'dumbbitch', 'Fudge Packer', 'escort', 'horney', 'douche-fag', 'transvestite', 'strappado', 'spook', 'puntang', 'fecal', 'terrorist', 'thirdeye', 'piss', 'dominatricks', 'cracker', 'blow job', 'masstrbate', 'gaytard', 'phuk', 'make me come', 'dilldo', 'buttplug', 'asspacker', 'cocksucked', 'tarbaby', 'taste my', 'girl on', 'niggle', 'rosy palm', 'sonofbitch', 'easyslut', 'scrote', 'bollick', 'fucka', 'shortfuck', 'farted', 'bitchtits', 'skankfuck', "niggardliness's", 'gonorrehea', 'pooping', 'stupidfuck', 'horniest', 'lemon party', 'cunntt', 'pric', 'shaggin', 'motherfuck', 'fuckface', 'lady boy', 'peckerhead', 'sleezeball', 'cocksuck', 'paky', 'knobbing', 'cockwaffle', 'jizim', 'asskisser', 'gay', 'spermhearder', 'twat', 'busty', 'jelly donut', 'nsfw images', 'cockmongruel', 'spigotty', 'towelhead', 'sex', 'fuckoff', 'jailbait', 'cocklover', 'clit', 'squaw', 'neonazi', 'fannyfucker', 'negro', 'raped', 'style doggy', 'sodomite', 'whorebag', 'spastic', 'whiskeydick', 'fuckit', 'dickface', 'fuckme', 'nipplering', 'penuus', 'zipperhea', 'faig', 'g-spot', 'playboy', 'piccaninny', 'assholes', 'dickhole', 'tittyfuck', 'motherlovebone', 'skankywhore', 'tard', 'renob', 'fags', 'manpaste', 'foursome', 'vajina', 'homo', 'honky', 'bollock', 'kunnilingus', 'buttstain', 'quim', 'shitola', 'porch monkey', 'pussylicker', 'big knockers', '2 girls 1 cup', 'wanker', 'fucktards', 'moron', 'ecchi', 'fuckina', 'faggotcock', 'boner', 'kondum', 'leather restraint', 'banging', 'niggers', 'hentai', 'bangbros', 'fubar', 'pu55y', 'phuker', 'ball licker', 'alaskan pipeline', 'masochist', 'mooncricket', 'wuzzie', 'kootch', 'assklown', 'herpes', 'lezbe', 'fondle', 'asskiss', 'kums', 'queef', 'tosspot', 'fagot', 'murder', 'buttfuck', 'doggie style', 'beatoff', 'pimpjuice', 'shitass', 'hottotrot', 'dripdick', 'buttface', 'niggaz', 'cuntface', 'tub girl', 'violet wand', 'fuckinnuts', 'arsehat', 'fistfucker', 'cybersex', 'dendrophilia', 'dvda', 'nastywhore', 'ass-hat', 'buttwipe', 'snatchpatch', 'cuntass', 'asspuppies', 'mothafucker', 'nazi', 'palesimian', 'orgasim', 'cockblock', 'peckerwood', 'mggor', 'pornography', 'skanck', 'penus', 'arseranger', 'luckycameltoe', 'insest', 'holestuffer', 'sandm', 'shyt', 'balllicker', 'bohunk', 'donkey punch', 'mastrabator', 'hand job', 'piky', 'ball kicking', 'lucifer', 'bollox', 'krap', 'wank', 'nastyslut', 'nastt', 'shithapens', 'skankwhore', 'jiggaboo', 'thundercunt', 'spermacide', 'blonde action', 'spooge', 'choad', 'dickbag', 'slopey', 'ass-pirate', 'felatio', 'spermherder', 'titty', 'dickforbrains', 'mastabater', 'biatch', 'dixiedyke', 'sexslave', 'ball gag', 'bountybar', 'fuckbag', 'syphilis', 'tonguethrust', 'crackwhore', 'greaseball', 'pissing', 'assblaster', 'cumbubble', 'lezbefriends', 'nympho', 'gaybob', 'ponyplay', 'juggalo', '2g1c', 'negroid', 'cocksmith', 'purinaprincess', 'Fukkah', 'gyppo', 'gokkun', 'pakie', 'coochy', 'motha fukkah', 'mutha fuker', 'unclefucker', 'fingering', 'molestation', 'sexo', 'nigglings', 'bicurious', 'cuntfuck', 'honkey', 'slutz', 'cocksmoke', 'russkie', 'fuckersucker', 'panooch', 'honger', 'welcher', 'motherfucked', 'axwound', 'guro', 'cockmaster', 'jiss', 'shitbagger', 'bootycall', 'tits', 'whiskydick', 'assshit', 'double dong', 'ball licking', 'assnigger', 'shota', 'pi55', 'faggots', 'suckmytit', 'pollock', 'slutting', 'prostitute', 'twats', 'hitler', 'porn', 'twatlips', 'moneyshot', 'arse', 'motha fucker', 'pussyfucker', 'fucktart', 'poopchute', 'blowjob', 'orifiss', 'dirty sanchez', 'gaydo', 'dicklick', 'dickjuice', 'flydye', 'pleasure chest', 'phone sex', 'cunteyed', 'flid', 'assman', 'incest', 'fuckbutt', 'arses', 'hosejob', 'tea bagging', 'dirty pillows', 'tied up', 'goregasm', 'gaysex', 'cocksucer', 'anus', 'dominatrics', 'fagfucker', 'hymen', 'ballsack', 'packie', 'snatch', 'violate', 'shitoutofluck', 'dumbshit', 'big tits', 'hard core', 'assbagger', 'son-of-a-bitch', 'niigr', 'bung hole', 'beat-off', 'coitus', 'cocky', 'libido', 'pooperscooper', 'girls gone wild', 'bigass', 'rectum', 'skeet', 'cawks', 'fucker', 'cockknoker', 'nymphomania', 'low life', 'fuckhole', 'ass-jabber', 'motherfucking', 'jail bait', 'flydie', 'camwhore', 'stupid', 'stabber', 'kinbaku', 'dommes', 'buttpirate', 'slimebucket', 'bastinado', 'arsebagger', 'trailertrash', 'asswad', 'niggaracci', 'japcrap', 'dick-sneeze', 'dumbass', 'pubes', 'jackass', 'horseshit', 'sextoys', 'seymour butts', 'intercourse', 'date rape', 'kissass', 'jesuschrist', 'gayboy', 'fagtard', 'pole smoker', 'cuntlicker', 'gays', 'pubiclice', 'prickhead', 'fuckmehard', 'condom', 'asscowboy', 'jism', 'camslut', 'clamdiver', 'cocksucking', 'penas', 'gaywad', 'thai bride', 'mothafuck', 'assmonkey', 'masokist', 'bitcher', 'orgasum', 'chocolate rosebuds', 'saeema butt', 'fucking', 'douchebag', 'pornking', 'muffdiver', 'alabama hotpocket', 'assbite', 'sexing', 'cockmongler', 'crotchmonkey', 'pissed off', 'spic', 'pussylips', 'gaymuthafuckinwhore', 'sonofabitch', 'menage a trois', 'nigger', 'shitfuck', 'prik', 'paedophile', 'titfucker', 'poontang', 'russki', 'pusy', 'god-damned', 'enema', 'mcfagget', 'crotchjockey', 'sexhouse', 'suckdick', 'husky', 'bitch', 'fatass', 'cnts', 'towel head', 'damnation', 'williewanker', 'meatbeater', 'trannie', 'shitblimp', 'headfuck', 'kike', 'niggarding', 'gaylord', 'assclown', 'fudgepacker', 'dickmilk', 'asscock', 'tit', 'schlong', 'cocksman', 'racist', 'lovemuscle', 'goo girl', 'nigr', 'niggerhead', 'testicle', 'strapon', 'queers', 'lolita', 'iblowu', 'suckoff', 'twatwaffle', 'girl on top', 'panti', 'dry hump', 'poonani', 'cocksniffer', 'fuckher', 'slideitin', 'assassination', 'nigaboo', 'ball sucking', 'asswhore', 'daterape', 'birdlock', 'dickfuck', 'chesticle', 'bastards', 'clusterfuck', 'one cup two girls', 'shithouse', 'gyppy', 'bullet vibe', 'circlejerk', 'bazooms', 'tramp', 'wrinkled starfish', 'tranny', 'japs', 'barfface', 'screwing', 'tainted love', 'nonce', 'pube', 'alabama hot pocket', 'lesbian', 'phuq', 'faggit', 'carpetmuncher', 'sodom', 'butt-bang', 'wankjob', 'assjockey', 'hardcore', 'teat', 'tampon', 'two girls one cup', 'negroes', 'plumper', 'apeshit', 'sadist', 'cuntsucker', 'facefucker', 'x-rated', 'massterbait', 'redneck', 'nlggor', 'queer', 'polac', 'felcher', 'peeenusss', 'octopussy', 'carpet muncher', 'dragqween', 'cameljockey', 'kunt', 'qweerz', 'foot fetish', 'fatfucker', 'cocklicker', 'piss pig', 'spankthemonkey', 'cumqueen', 'fistfuck', 'butt-fuck', 'cocknugget', 'cum', 'phuc', 'protestant', 'twobitwhore', 'hotpussy', 'goodpoop', 'xxx', 'coondog', 'internet wife', 'trisexual', 'beastiality', 'douche', 'pissin', 'urinate', 'vag', 'wife beater', 'nudger', 'mound of venus', 'fugly', 'lezbo', 'shitbrains', 'perversion', 'deep throat', 'loadedgun', 'dickfucker', 'titfuck', 'cockmonkey', 'dick', 'orgasim', 'pisshead', 'arseblaster', 'group sex', 'gatorbait', 'pimpsimp', 'areola', 'darky', 'footaction', 'dookie', 'titfuckin', 'poop chute', 'jisim', 'shittiest', 'godammit', 'lovegun', 'slutty', 'peinus', 'spik', 'assface', 'omorashi', 'fagit', 'golden shower', 'fucked', 'queerhole', 'fuckable', 'shiznit', 'Fukkin', 'goddamit', 'knobz', 'camel toe', 'booby', 'hookers', 'nofuckingway', 'shitty', 'spac', 'fark', 'muff diver', 'big black', 'fisting', 'chink', 'dixiedike', 'vibrater', 'shitcunt', 'hijacker', 'bareback', 'buggery', 'jijjiboo', 'baldy', 'strap on', 'pedophile', 'freakyfucker', 'arsemonkey', 'arseholes', 'butthead', 'gayass', 'motherfuckin', 'nipple', 'swallower', 'pthc', 'jizm', 'teste', 'bitchez', 'skumbag', 'paedofile', 'hijack', 'goddammit', 'erotic', 'fuk', 'assranger', 'arseman', 'cumdumpster', 'pussies', 'raping', 'drag queen', 'lipshits', 'milf', 'oriface', 'clunge', 'mr hands', 'asshead', 'nude', 'cockblocker', 'abortionist', 'facist', 'crackpipe', 'fuckfest', 'dike', 'butchbabes', 'lardass', 'nutfucker', 'violation', 'sucker', "niggard's", 'titbitnipply', 'gypo', 'punta', 'butt-fucker', 'exhibitionist', 'fuckwad', 'jerkass', 'breastman', 'foreskin', 'rearentry', 'robber', 'gangbang', 'nigur', 'cockqueen', 'xx', 'ejaculated', 'orgy', 'nudity', 'gypp', 'titlicker', 'jackoff', 'tubgirl', 'dickweed', 'idiot', 'smut', 'asshopper', 'suckmydick', 'skankee', 'flasher', 'niggarded', 'poon', 'eat my ass', 'white power', 'lesbain', 'stripclub', 'trouser snake', 'jizjuice', 'arselick', 'assjacker', 'rusty trombone', 'niggah', 'cunilingus', 'snot', 'mothafuckings', 'arsecowboy', 'jungle bunny', 'retarded', 'nimphomania', 'waysted', 'penispuffer', 'suckass', 'spank', 'mgger', 'arselover', 'throating', 'fuckmonkey', 'bestiality', 'thick as', 'tantra', 'sodomize', 'buttman', 'fellatio', 'malicious', 'slantyeye', 'wuss', 'cunt', 'cockrider', 'fuckass', 'vorarephilia', 'homoerotic', 'fatfuck', 'master bates', 'scum', 'punany', 'sodomy', 'bigbastard', 'nittit', 'cocks', 'ruski', 'lezzo', 'feces', 'nigga', 'motherfucker', 'muffdiving', 'nawashi', 'dicklicker', 'lipshitz', 'gringo', 'muffdive', 'cockass', 'zigabo', 'kunts', 'slopy', 'bondage', 'fucck', 'ball gravy', 'fuckingbitch', 'hot chick', 'assbandit', 'urophilia', 'gooch', 'feltching', 'packi', 'peeenus', 'bitchy', 'excrement', 'peehole', 'shithappens', 'assassinate', 'pros', 'lapdance', 'mastabate', 'horny', 'fingerfucking', 'bampot', 'cockfucker', 'threesome', 'phukker', 'arsehore', 'whacker', 'leather straight jacket', 'ejaculating', 'homodumbshit', 'lovemaking', 'pisses', 'erotism', 'flipping the bird', 'pisspig', 'dicksucker', 'bukake', 'pussylicking', 'arsepacker', 'hindoo', 'shity', 'murderer', 'porno', 'abbo', 'damnit', 'pecker', 'fuckbuddy', 'arsehole', 'shyty', 'lowlife', 'faggot', 'beastial', 'fuckwitt', 'cameltoe', 'booty call', 'zoophilia', 'dickslap', 'farty', 'testicles', 'spermbag', 'thicklips', 'fuckin', 'cockcowboy', 'porchmonkey', 'lovepistol', 'shaved pussy', 'dildos', 'skankbitch', 'brothel', 'spitter', 'sexwhore', 'crappy', 'goddamned', 'sleezebag', 'vietcong', 'vomit', 'dp action', 'jack off', 'buttfucker', 'yellow showers', 'cocksmoker', 'vagiina', 'skankybitch', 'baby batter', 'kumbullbe', 'sultry women', 'ball sack', 'butt plug', 'pornprincess', 'intheass', 'devilworshipper', 'pussy', 'bitching', 'trots', 'cumguzzler', 'glazeddonut', 'jizzum', 'skum', 'upthebutt', 'shitting', 'flatulence', 'hot carl', 'lovejuice', 'poof', 'rosy palm and her 5 sisters', 'hitlerist', 'assbanger', 'labia', 'raging boner', 'mothafuckin', 'shits', 'dumbfuck', 'butt-pirate', 'packy', 'skinflute', 'spazza', 'genitals', 'pickaninny', 'clover clamps', 'suck', 'bazongas', 'mother fukkah', 'gay sex', 'shytty', 'muncher', 'pisser', 'deepthroat', 'blow your load', 'inthebuff', 'eatme', 'arsepuppies', 'buttfuckers', 'sadom', 'dicksucking', 'skank', 'buttfucka', 'buggered', 'jizzim', 'queerz', 'shitforbrains', 'asssucker', 'cumjockey', 'pissflaps', 'coons', 'mutha fukker', 'cornhole', 'urine', 'cuntfucker', 'dickhead', 'krappy', 'coprolagnia', 'pearlnecklace', 'tushy', 'assmunch', 'gaygirl', 'suckmyass', 'bum', 'assshole', 'goddamnes', 'junglebunny', 'asshole', 'poostabber', 'vaginal', 'goldenshower', 'cock-head', 'fuckup', 'niggard', 'faeces', 'lovegoo', 'lovebone', 'bullshit', 'dildo', 'nambla', 'spig', 'hoor', 'jackshit', 'alligatorbait', 'voyeur', 'motha fuker', 'nignog', 'reverse cowgirl', 'twinkie', 'stroking', 'xrated', 'ontherag', 'slutt', 'rapist', 'cumquat', 'lesbin', 'asspirate', 'smeg', 'pocketpool', 'shagging', 'basterds', 'pussylover', 'fart', 'whorefucker', 'gayfuckist', 'phungky', 'cocknob', 'wet dream', 'scank', 'cuntlicker', 'hoore', 'butt-fuckers', 'fatso', 'sixtynine', 'slopehead', 'fuckknob', 'fingerfuck', 'shitcan', 'raghead', 'shitted', 'dyke', 'fuckwhore', 'smelly', 'cocknose', 'wrapping men', 'bitches', 'fistfucked', 'figging', 'penisfucker', 'pu55i', 'boobies', 'slapper', 'venus mound', 'anilingus', 'play bunny', 'fuckfreak', 'rape', 'fornicate', 'rentafuck', 'pissed', 'ejaculation', 'spick', 'getiton', 'boobs', 'masterbaiter', 'fucknut', 'muthafucker', 'nutsack', 'wetback', 'slutbag', 'frotting', 'splooge moose', 'grostulation', 'cockbite', 'fuckwit', 'fag', 'freefuck', 'cocksucker', 'niglet', 'Fuken', 'slutwhore', 'shiting', 'cock', 'orafis', 'hooker', 'wop', 'mothafucking', 'mother fucker', 'byatch', 'shitfit', 'feltcher', 'acrotomophilia', 'fingerbang', 'tuckahoe', 'cumm', 'niggardly', 'pegging', 'recktum', 'coon', 'sixtyniner', 'arsewipe', 'vullva', 'dingleberry', 'gangbanged', 'upskirt', 'uptheass', 'deapthroat', 'goddamnit', 'shithead', 'cunts', 'honkers', 'cuntrag', 'nipples', 'doggystyle', 'uterus', 'titties', 'buttmuncher', 'masstrbait', 'grope', 'creampie', 'fingerfucker', 'scat', 'pindick', 'mutha fukkah', 'niggardliness', 'fister', 'beaner']
, 'There are no ducking words here.')
    assert nw_filter.has_profanity() is False