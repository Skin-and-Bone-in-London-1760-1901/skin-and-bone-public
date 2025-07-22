#!/usr/bin/python3

# This file was originally from tattoos and was used to obtain neat column values from the Larch json for the globaldesc tsv file

import os

def prettydate(d):
    if 'ld' in d:
      return format(d['ld']['year'], '04') + "-" + format(d['ld']['month'], '02') + "-" + format(d['ld']['day'], '02')
    else:
      return '0001-01-01'

def prettyperiod(p):
    ret = ''
    if 'life' in p:
      if p['life'] == True:
        return 'life'
    if 'p' in p:
      if 'years' in p['p']:
        if p['p']['years'] > 1:
          ret = ret + str(p['p']['years']) + ' years '
        elif p['p']['years'] > 0:
          ret = ret + str(p['p']['years']) + ' year '
    if 'months' in p['p']:
        if p['p']['months'] > 1:
          ret = ret + str(p['p']['months']) + ' months '
        elif p['p']['months'] > 0:
          ret = ret + str(p['p']['months']) + ' month '
    if 'days' in p['p']:
        if p['p']['days'] > 1:
          ret = ret + str(p['p']['days']) + ' days '
        elif p['p']['days'] > 0:
          ret = ret + str(p['p']['days']) + ' day '
    return ret

def prettybool(b):
    if b:
      return 'yes'
    elif b == '':
      return 'no'
    else:
      return 'no'

# k - key
# s - string
# i - integer
# f - float
# p - pivot

def klifeid(k):
  return j['create']['_id']

def sgiven(k):
  if 'can_given' in k['global']['sm']:
    return k['global']['sm']['can_given']
  else:
    return ''

def ssurname(k):
  if 'can_surname' in k['global']['sm']:
    return k['global']['sm']['can_surname']
  else:
    return ''

def sreligion(k):
  if 'religion' in k:
    return k['religion']
  else:
    return ''

def sreligioncat(k):
  if 'religion_category' in k['global']['ssm']:
    return ' '.join(k['global']['ssm']['religion_category'])
  else:
    return ''




def sgender(k):
  if 'gender' in k['global']['ssm']:
    return ' '.join(k['global']['ssm']['gender'])
  else:
    return ''

def splaceofbirth(k):
  if 'place_of_birth' in k['global']['ssm']:
    return ' '.join(k['global']['ssm']['place_of_birth'])
  else:
    return ''

def soccupation(k):
  if 'occupation' in k['global']['ssm']:
    return ' '.join(k['global']['ssm']['occupation'])
  else:
    return ''

def soccupationtop(k):
  if 'occupation_top' in k['global']['ssm']:
    return ' '.join(k['global']['ssm']['occupation_top'])
  else:
    return ''


def scomplexion(k):
  if 'complexion' in k['global']['ssm']:
    return ' '.join(k['global']['ssm']['complexion'])
  else:
    return ''

def seyes(k):
  if 'eyes' in k['global']['ssm']:
    return ' '.join(k['global']['ssm']['eyes'])
  else:
    return ''

def shair(k):
  if 'hair' in k['global']['ssm']:
    return ' '.join(k['global']['ssm']['hair'])
  else:
    return ''

def iborn(k):
  if 'born' in k['global']['im']:
    return k['global']['im']['born']
  else:
    return '0'

def itrials(k):
  if 'trials' in k['global']['im']:
    return k['global']['im']['trials']
  else:
    return '0'

def sconsidered(k):
  return k['global']['sm']['considered_for_pardon']

def sinhulks(k):
  return k['global']['sm']['in_hulks']

def spenalservitude(k):
  return k['global']['sm']['penalservitude']

def sinsane(k):
  return k['global']['sm']['insane']

#def itotal(row, j, k):{"total_records", "im", "archive_size"},
#def itotalob(row, j, k):{"total_records_old_bailey", "im", "obp"},
#def dfirstoffencedate(row, j, k):{"first_offence_date", "dm", "earliest_trial"},
#def ifirstoffenceage(row, j, k):{"first_offence_age", "im", "earliest_trial_age"},
#def sfirstoffencetype(row, j, k):{"first_offence_type", "ssm", "earliest_trial_offence_category"},
#def sfirstoffencesentence(row, j, k):{"first_offence_sentence", "ssm", "earliest_trial_sentence_category"},
#def sfirstoffencepunishment(row, j, k):{"first_offence_punishment", "sm", "earliest_trial_so_type"},
#def slastoffencedate(row, j, k):{"last_offence_date", "dm", "latest_trial"},
#def ilastoffenceage(row, j, k):{"last_offence_age", "im", "latest_trial_age"},
#def slastoffencetype(row, j, k):{"last_offence_type", "ssm", "latest_trial_offence_category"},
#def slastoffencesentence(row, j, k):{"last_offence_sentence", "ssm", "latest_trial_sentence_category"},
#def slastoffencepunishment(row, j, k):{"last_offence_punishment", "sm", "latest_trial_so_type"},
#def stransported(row, j, k):{"transported", "sm", "transported"},
#def dtransporteddate(row, j, k):{"transported_date", "dm", "transported"},
#def stransportedcolony(row, j, k):{"transported_colony", "ssm", "colony"},
#def sticketofleave(row, j, k):{"ticket_of_leave", "sm", "ticket_of_leave"},
#def dticketofleavedate(row, j, k):{"ticket_of_leave_date", "dm", "ticket_of_leave"},
#def spenalservitude(row, j, k):{"penal_servitude", "sm", "penalservitude"},
#def dpenalservitudedate(row, j, k):{"penal_servitude_date", "dm", "penalservitude_started"},
#def dpenalservitudereleaseddate(row, j, k):{"penal_servitude_released_date", "dm", "penalservitude_released"},
#def sgrantedprisonlicense(row, j, k):{"granted_prison_license", "sm", "granted_prison_license"},
#def dgrantedprisonlicensedate(row, j, k):{"granted_prison_license_date", "dm", "granted_prison_license"},
#def sexecuted(row, j, k):{"executed", "sm", "executed"},
#def dexecuteddate(row, j, k):{"executed_date", "dm", "executed"},
#def inumberofchildren(row, j, k):{"number_of_children", "im", "number_of_children"},
#def ifirstchildbornage(row, j, k):{"first_child_born_age", "im", "first_child_born_age"},
#def dfirstbordchilddate(row, j, k):{"first_child_born_date", "dm", "first_child_born_date"},
#def imarriedage(row, j, k):{"married_age", "im", "married_age"},
#def dmarrieddate(row, j, k):{"married_date", "dm", "married_date"},
#def ddieddate(row, j, k):{"died_date", "dm", "died"},

def smarried(k):
  if 'married' in k['global']['sm']:
    return k['global']['sm']['married']
  else:
    return ''

# DON'T FORGET JOIN!! return ' '.join(k['global']['ssm']['earliest_trial_offence_category']))

def itrials(k):
  if 'trials' in k['global']['im']:
    return k['global']['im']['trials']
  else:
    return '0';

def iearliest_trial_year(k):
  if 'earliest_trial' in k['global']['dm']:
    return k['global']['dm']['earliest_trial']['ld']['year']
  else:
    return '0'

def ilatest_trial_year(k):
  if 'latest_trial' in k['global']['dm']:
    return k['global']['dm']['latest_trial']['ld']['year']
  else:
    return '0'

def searliest_trial_offence_category(k):
  if 'earliest_trial_offence_category' in k['global']['ssm']:
    return ' '.join(k['global']['ssm']['earliest_trial_offence_category'])
  else:
    return ''

def searliest_trial_sentence_category(k):
  if 'earliest_trial_sentence_category' in k['global']['ssm']:
    return ' '.join(k['global']['ssm']['earliest_trial_sentence_category'])
  else:
    return ''

def slatest_trial_offence_category(k):
  if 'latest_trial_offence_category' in k['global']['ssm']:
    return ' '.join(k['global']['ssm']['latest_trial_offence_category'])
  else:
    return ''

def slatest_trial_sentencecategory(k):
  if 'latest_trial_sentence_category' in k['global']['ssm']:
    return ' '.join(k['global']['ssm']['latest_trial_sentence_category'])
  else:
    return ''

def sship(k):
  if 'ship' in k['global']['ssm']:
    return ' '.join(k['global']['ssm']['ship'])
  else:
    return ''

def fheight(k):
  if 'height' in k:
    return k['height']
  else:
    return '0.0'

def trialconforms(row):
    year = int(row[29][0:4])
    if (year < 1763 or year > 1879): return False # out of desired date range
    if (row[18] == ''): return False # obpid must not be ''
    if ('not_guilty' in row[32] and (row[33] == ''  or row[33] == 'no_punishment')): return False # if verdict contains 'not_guilty' and sentence is empty we must reject
    return True


