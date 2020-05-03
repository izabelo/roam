# bibtex.py
import sys
import time

# --------------------------------------------------------
# Get the directory and filename as input parameters
# --------------------------------------------------------
inputfiledir = sys.argv[1]
inputfiledir+='/'
inputfilename = r''
inputfilename+=inputfiledir
inputfilename+=sys.argv[2]
inputfilename+='.bib'

# --------------------------------------------------------
# Initialise all the variables
# --------------------------------------------------------
vAbstract = ''
vAddress = ''
vAnnote = ''
vArchivePrefix = ''
vArxivId = ''
vAsin = ''
vAuthor = ''
vBibTex = ''
vBooktitle = ''
vChapter = ''
vCiteKey = ''
vDocType = ''
vDoi = ''
vEdition = ''
vEditor = ''
vEprint = ''
vFile = ''
vInstitution = ''
vIsbn = ''
vIssn = ''
vIssue = ''
vJournal = ''
vKeywords = ''
vMendeleyTags = ''
vOrganization = ''
vPages = ''
vPmid = ''
vPublisher = ''
vSchool = ''
vTitle = ''
vTitleHeading = ''
vType = ''
vUrl = ''
vVolume = ''
vYear = 'n.d.'

# --------------------------------------------------------
# Open the input file
# --------------------------------------------------------
f = open(inputfilename, 'r')

# --------------------------------------------------------
# Read through the file
# --------------------------------------------------------
while True:
    line=f.readline() # check for EOF
    if not line: break

    if line[0:5] == '@book':
        vDocType = 'book'
        vCiteKey = line[6:line.find(',')]
    elif line[0:8] == '@article':
        vDocType = 'article'
        vCiteKey = line[9:line.find(',')]
    elif line[0:10] == '@phdthesis':
        vDocType = 'thesis'
        vCiteKey = line[11:line.find(',')]
    elif line[0:11] == '@techreport':
        vDocType = 'report'
        vCiteKey = line[12:line.find(',')]
    elif line[0:12] == '@unpublished':
        vDocType = 'unpublished'
        vCiteKey = line[13:line.find(',')]
    elif line[0:13] == '@incollection':
        vDocType = 'book'
        vCiteKey = line[14:line.find(',')]
    elif line[0:14] == '@inproceedings':
        vDocType = 'conference'
        vCiteKey = line[15:line.find(',')]
    elif line[0:3] == 'doi':
        vDoi = line[3+4:line.find('}')]
    elif line[0:3] == 'url':
        vUrl = line[3+4:line.find('}')]
    elif line[0:4] == 'file':
        vFile = line[4+4:line.find('}')]
    elif line[0:4] == 'isbn':
        vIsbn = line[4+4:line.find('}')]
    elif line[0:4] == 'issn':
        vIssn = line[4+4:line.find('}')]
    elif line[0:4] == 'pmid':
        vIssn = line[4+4:line.find('}')]
    elif line[0:4] == 'type':
        vType = line[4+4:line.find('}')]
    elif line[0:4] == 'year':
        vYear = line[4+4:line.find('}')]
    elif line[0:5] == 'pages':
        vPages = line[5+4:line.find('}')]
    elif line[0:5] == 'title':
        vTitle = line[5+5:line.find('}')]
    elif line[0:6] == 'eprint':
        vEprint = line[6+4:line.find('}')]
    elif line[0:6] == 'author':
        vAuthor = line[6+4:line.find('}')]
    elif line[0:6] == 'volume':
        vVolume = line[6+4:line.find('}')]
    elif line[0:6] == 'editor':
        vEditor = line[6+4:line.find('}')]
    elif line[0:6] == 'school':
        vSchool = line[6+4:line.find('}')]
    elif line[0:6] == 'number':
        vIssue = line[6+4:line.find('}')]
    elif line[0:6] == 'annote':
        vAnnote = line[6+4:line.find('}')]
        # Amazon Kindle ASIN is in notes field
        if line[0:15] == 'annote = {ASIN:':
            vAsin = line[15:25]
    elif line[0:7] == 'chapter':
        vChapter = line[7+4:line.find('}')]
    elif line[0:7] == 'arxivId':
        vArxivId = line[7+4:line.find('}')]
    elif line[0:7] == 'journal':
        vJournal = line[7+4:line.find('}')]
    elif line[0:7] == 'address':
        vAddress = line[7+4:line.find('}')]
    elif line[0:7] == 'edition':
        vEdition = line[7+4:line.find('}')]
    elif line[0:8] == 'abstract':
        vAbstract = line[8+4:line.find('}')]
    elif line[0:8] == 'keywords':
        vKeywords = line[8+4:line.find('}')]
    elif line[0:9] == 'booktitle':
        vBooktitle = line[9+4:line.find('}')]
    elif line[0:9] == 'publisher':
        vPublisher = line[9+4:line.find('}')]
    elif line[0:11] == 'institution':
        vInstitution = line[11+4:line.find('}')]
    elif line[0:12] == 'organization':
        vOrganization = line[12+4:line.find('}')]
    elif line[0:13] == 'mendeley-tags':
        vMendeleyTags = line[13+4:line.find('}')]
    elif line[0:13] == 'archivePrefix':
        vBibTex+=line
        vArchivePrefix = line[13+4:line.find('}')]
#    else:
#        print ('###',line)

# Close the input file
f.close()

#=========================================================
# Use extracted fields to produce page elements
#=========================================================
# --------------------------------------------------------
# Authors
# --------------------------------------------------------
vDokuTemplate = '- authors:: '+vAuthor
print (vDokuTemplate)

# --------------------------------------------------------
# Year
# --------------------------------------------------------
vDokuTemplate = '- year:: [['+vYear+']]'
print (vDokuTemplate)

# --------------------------------------------------------
# Title
# --------------------------------------------------------
vDokuTemplate = '- title:: '+vTitle.strip().lower()
print (vDokuTemplate)

# --------------------------------------------------------
# Journal Article
# --------------------------------------------------------
if vDocType == '- article':
    vDokuTemplate = 'journal:: __'+vJournal+'__'
    if not vVolume == '':
        vDokuTemplate+=', '+vVolume
    if not vIssue == '':
        vDokuTemplate+='('+vIssue+')'
    print (vDokuTemplate)

# --------------------------------------------------------
# Pages
# --------------------------------------------------------
vDokuTemplate = '- **Pages**: '+vPages.replace('--','-')
print (vDokuTemplate)

# --------------------------------------------------------
# Show abstract (if there is one)
# --------------------------------------------------------
if len(vAbstract) > 0:
    vDokuTemplate = '- abstract:: '+vAbstract
    print (vDokuTemplate)

# --------------------------------------------------------
# Keywords
# --------------------------------------------------------
if len(vKeywords) > 0:
    vDokuTemplate = '- keywords:: '
    print (vDokuTemplate)
    vKeywordList = vKeywords.split(',')
    for vKeyword in vKeywordList:
        vDokuTemplate = '    - [['+vKeyword.strip().lower()+']]'
        print (vDokuTemplate)

# Add a heading at the end
vDokuTemplate = '- ## Notes:'
print (vDokuTemplate)
vDokuTemplate = '- '
print (vDokuTemplate)
