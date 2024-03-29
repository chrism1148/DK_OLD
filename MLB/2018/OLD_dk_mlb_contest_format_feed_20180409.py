import csv
import re
import unicodedata


contest_date = 20180409
contest_name = 'fielders_choice'
contest_entry_fee = 50
contest_id = 55231523


def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

regex = re.compile(".*?\((0-9)\)")

ifile  = ('dk_mlb_%s_%d.csv' % (contest_name, contest_date))
ofile  = open('dk_mlb_%s_%d_formatted.csv' % (contest_name, contest_date), 'w') 
writer = csv.writer(ofile)


with open(ifile, 'r') as csvfile:
	reader = csv.reader(csvfile)
	# next(reader)

	for row in reader:
		rank              = row[0]
		entry_id          = row[1]
		entry_name        = re.sub(r'\s\(.*?\)', '', row[2])
		lineup_points     = row[4]
		player            = remove_accents(row[7])
		player_position   = row[8]
		player_percentage = row[9].replace('%', '')
		player_points     = row[10]
		lineup            = remove_accents(row[5])

		pitcher_2         = re.findall(r'\sP\s[A\-.-z]{1,}\s[A\-\'-z]{1,}', lineup)
		pitcher_2         = ', '.join(pitcher_2)
		pitcher_2         = pitcher_2.replace(' P ', '')
		
		pitcher_1         = re.findall(r'^P\s[A\-.-z]{1,}\s[A\-\'-z]{1,}', lineup)
		pitcher_1         = ', '.join(pitcher_1)
		pitcher_1         = pitcher_1.replace('P ', '')
		
		catcher           = re.findall(r'\sC\s[A\-.-z]{1,}\s[A\-\'-z]{1,}', lineup)
		catcher           = ', '.join(catcher)
		catcher           = catcher.replace(' C ','')

		first_base        = re.findall(r'\s1B\s[A\-.-z]{1,}\s[A\-\'-z]{1,}', lineup)
		first_base        = ', '.join(first_base)
		first_base        = first_base.replace(' 1B ','')

		second_base       = re.findall(r'\s2B\s[A\-.-z]{1,}\s[A\-\'-z]{1,}', lineup)
		second_base       = ', '.join(second_base)
		second_base       = second_base.replace(' 2B ','')

		third_base        = re.findall(r'\s3B\s[A\-.-z]{1,}\s[A\-\'-z]{1,}', lineup)
		third_base        = ', '.join(third_base)
		third_base        = third_base.replace(' 3B ','')

		short_stop        = re.findall(r'\sSS\s[A\-.-z]{1,}\s[A\-\'-z]{1,}', lineup)
		short_stop        = ', '.join(short_stop)
		short_stop        = short_stop.replace(' SS ','')

		outfield          = re.findall(r'\sOF\s[A\-.-z]{1,}\s[A\-\'-z]{1,}', lineup)
		outfield          = ', '.join(outfield)
		outfield          = outfield.replace(' OF ','')
		outfield          = outfield.replace(', ',',')
	
		output = (rank, entry_id, entry_name, lineup_points, player, player_position, player_percentage, player_points, pitcher_1, pitcher_2, catcher, first_base, second_base, third_base, short_stop, outfield)
		writer.writerows([output])
