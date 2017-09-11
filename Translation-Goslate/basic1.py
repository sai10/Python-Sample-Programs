import goslate

gs = goslate.Goslate()


hin = gs.translate('love','hi')

eng = gs.translate(hin,'eng')

print eng
