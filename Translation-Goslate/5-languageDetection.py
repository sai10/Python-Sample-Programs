import goslate

gs  = goslate.Goslate()

langID1 = gs.detect('Hello')
langID2 = gs.detect('hallo welt')

print 'language id 1 - '+langID1
print '\nlanguage id 2 - '+langID2

print '\nlanguage 1 is:'+gs.get_languages()[langID1]
print '\nlanguage 2 is:'+gs.get_languages()[langID2]
