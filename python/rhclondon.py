#!/usr/bin/python3

import json

# This function determines if a given rhc record refers to a person we can consider 'from London'.

london_general = ['london', 'middlesex', 'westminster']
london_boroughs = ['battersea', 'bermondsey', 'bethnal green', 'camberwell', 'chelsea', 'deptford', 'finsbury', 'fulham', 'greenwich', 'hackney', 'hammersmith', 'hampstead', 'islington', 'kensington', 'lambeth', 'lewisham', 'paddington', 'poplar', 'marylebone', 'pancras', 'shoreditch', 'southwark', 'stepney', 'newington', 'wandsworth', 'westminster', 'woolwich']
#london_courts = ['c c c', 'worship st. pol. ct', 'c.c.c.', 'p.c. chapman, 378e', 'cent. crim. ct.', 'cent, crim. ct.', 'guildhall', 'mid. sess.', 'brentford pol. ct.', 'middlesex sess.', 'p.c. notley, 47sr', 'middlesex', 'p.s. nicholls, c.i.d -b', 'middx. sess.', 'brentford', 'midx sess.', 'edgware', 'n l.s.', 'marlboro’ st. pol. ct.', 'n.l s.', 'thames pol. ct.', 'n.l.s.', "marlboro' st. pol. ct.", 'n. london sess.', 'p.c. gough, c.i.d.-co', 'n. l. sess.', 'worship-st. pol. ct.', 'n. lon. sess.', 'marlborough st. pol. ct.', 'n. london sees.', 'p.c. english, 138-g', 'n. london sess', 'marlboro’ - st. police court', 'n.l.8.', 's.l.s.', 's.l.s', 'lambeth pol. ct.', 's l.s.', 'p.c. manners, 182m', 's. l. s.', 's. w. pol. ct.', 's. lon. sess.', 'southwark pol. ct.', 's. london sess.', 'lambeth', 's.l.s.', 'lambeth pol. ct.', 'south london sess.', 'perge petty sess.']

london_courts = [
'brentford', 
'brentford pol. ct.', 
'c c c', 
'c.c.c', 
'c.c.c,', 
'c.c.c.', 
'ccc', 
'cent, crim. ct.', 
'cent. crim. ct.', 
'edgware', 
'guildhall', 
'lambeth', 
'lambeth pol. ct.', 
"marlboro' st. pol. ct.", 
'marlborough st. pol. ct.', 
'marlboro’ - st. police court', 
'marlboro’ st. pol. ct.', 
'mid. sess.', 
'middlesex', 
'middlesex sess.', 
'middx.  sess.', 
'middx. sess', 
'middx. sess,', 
'middx. sess.', 
'midx sess.', 
'midx.  sess.', 
'midx. sess,', 
'midx. sess.', 
'n l.s.', 
'n. l. sess.', 
'n. lon. sess.', 
'n. london sees.', 
'n. london sess', 
'n. london sess.', 
'n.l s.', 
'n.l.8.', 
'n.l.s', 
'n.l.s,', 
'n.l.s.', 
'n.ls.', 
's l.s.', 
's. l. s.', 
's. lon. sess.', 
's. london sess.', 
's. w. pol. ct.', 
's.l.s', 
's.l.s.', 
's.ls.', 
'sl.s.', 
'south london sess.', 
'southwark pol. ct.', 
'thames pol. ct.', 
'worship st. pol. ct', 
'worship-st. pol. ct.'
]

def matcharray(s, arr):

    for ai in arr:

        if ai in s: return True

    return False

def rhclondon(jj, j):

    if jj['life_id'].startswith('obp'): return True # Anyone in RHC who is linked to OBP can be automatically assumed to be 'from London'.

    date = j['dm'].get('date')
                
    if (date):

        desc_year = date['ld']['year']

        if desc_year >= 1881 and desc_year <= 1895:

            if 'placeLastOffence' in j['sm'] and matcharray(j['sm']['placeLastOffence'].lower(), london_general + london_boroughs): return True
            if 'destination' in j['sm'] and matcharray(j['sm']['destination'].lower(), london_general + london_boroughs + ['r.s.a.d.p.']): return True

        elif desc_year >= 1896 and desc_year <= 1901:

            if 'addressOccupation' in j['sm'] and matcharray(j['sm']['addressOccupation'].lower(), london_general + london_boroughs): return True
            if 'tried' in j['sm'] and matcharray(j['sm']['tried'].lower(), london_general + london_courts): return True

    return False
