### PROCESS SUMMARY ###

# for each alphabet section, loops through each line collecting:
## counts for each author (including multiple authors in a line)

# when detects 'alphasectend':
## writes author counts to a text file
## moves on to the next alphabet section

## NOTES ON TEXT ##

# lines 1-7348 (slice [0:7347]) are intro text (line 7348 is 'alphasectend' string for intro)

# dictionary content begins on line 7349 (slice [7348:])

#improved cleanline function                                 #from Johnson4_v1_split_alphasectend-retain-punct
import string

def clean_line(line_str):
    cleanline = line_str.lower()
    cleanline = cleanline.replace("°", "o")
    cleanline = cleanline.replace("º", "o")
    cleanline = cleanline.replace("×", "x")
    cleanline = cleanline.replace("à", "a")
    cleanline = cleanline.replace("á", 'a')
    cleanline = cleanline.replace('â', 'a')
    cleanline = cleanline.replace('ä', 'a')
    cleanline = cleanline.replace('ă', 'a')
    cleanline = cleanline.replace('ã', 'a')
    cleanline = cleanline.replace('å', 'a')
    cleanline = cleanline.replace('ā', 'a')
    cleanline = cleanline.replace('ą', 'a')
    cleanline = cleanline.replace('ć', 'c')
    cleanline = cleanline.replace('č', 'c')
    cleanline = cleanline.replace('ç', 'c')
    cleanline = cleanline.replace('è', 'e')
    cleanline = cleanline.replace('é', 'e')
    cleanline = cleanline.replace('ë', 'e')
    cleanline = cleanline.replace('ē', 'e')
    cleanline = cleanline.replace('ę', 'e')
    cleanline = cleanline.replace('ê', 'e')
    cleanline = cleanline.replace('ğ', 'g')
    cleanline = cleanline.replace('í', 'i')
    cleanline = cleanline.replace('ì', 'i')
    cleanline = cleanline.replace('ń', 'n')
    cleanline = cleanline.replace('ñ', 'n')
    cleanline = cleanline.replace('ň', 'n')
    cleanline = cleanline.replace('ó', 'o')
    cleanline = cleanline.replace('ö', 'o')
    cleanline = cleanline.replace('ð', 'o')
    cleanline = cleanline.replace('ø', 'o')
    cleanline = cleanline.replace('ò', 'o')
    cleanline = cleanline.replace('ř', 'r')
    cleanline = cleanline.replace('š', 's')
    cleanline = cleanline.replace("ſ", "s")
    cleanline = cleanline.replace('ś', 's')
    cleanline = cleanline.replace('ş', 's')
    cleanline = cleanline.replace('ţ', 't')
    cleanline = cleanline.replace('ü', 'u')
    cleanline = cleanline.replace('ú', 'u')
    cleanline = cleanline.replace('ū', 'u')
    cleanline = cleanline.replace('ź', 'z')
    cleanline = cleanline.replace('ż', 'z')
    cleanline = cleanline.replace('ž', 'z')
    return cleanline

# open Johnson_reprint volume                                 #from Johnson4_v1_split_alphasectend-retain-punct
infile = open('uc1.31175025730543.txt','r', encoding='utf-8')
text = str(infile.read())
infile.close()

# split into lines                                 #from Johnson4_v1_split_alphasectend-retain-punct
lines_list = text.split('\n')
print("success: split into lines")

# clean lines and add cleaned lines to a list        #from Johnson4_v1_split_alphasectend-retain-punct
cleaned_lines_list = []
for line in lines_list:
    cleaned_line = clean_line(line)
    cleaned_lines_list.append(cleaned_line)

# final product: cleaned_lines_list

# lines_list = ['this line has a shakespeare citation.', 'this line has a shakespeare citation and a milton citation.', 'alphasectend', 'this line has no citations.', 'this line has a shakespeare citation and a shaks. citation.', 'this line has a milton citation, a locke citation, a dryden citation, and a milton citation', 'alphasectend']

# # dictionary of two-item lists (for writing to a CSV):
# # key = alphabet section     #value = empty list for author-string list pairs (list of two-item lists)
# alpha_dictionary = {"A":[], "B":[]}

# import csv

# # dictionary of page numbers:
# pages = 0
# # key = alphabet section      #value = empty 'pages' variable
# page_counter = {"A": pages, "B": pages, "C": pages, "D": pages, "E": pages, "F": pages, "G": pages, "H": pages, "I": pages, "K": pages}

# define text outfile that will contain author citation counts
outfile_total_count = open("Johnson_reprint_counts.txt", 'w', encoding="UTF-8")

# define starting alpha_sect ("A")
alpha_sect = 65

# define regex pattern functions

import re

shak = re.compile('shak[^i]')
milton = re.compile('mil.')
locke = re.compile('loc.')
dryden = re.compile('dry[^i]')

# defining functions that add author-citation pairs to CSV

# def finding_shakespeare(x_line):
#     shak = re.compile('shak[^i]')
#     shakespeare_appears = shak.findall(x_line)
#     if shakespeare_appears:
#         alpha_dictionary[chr(alpha_sect)].append([line, "shakespeare"])
#
# def finding_milton(x_line):
#     milton = re.compile('mil.')
#     milton_appears = milton.findall(x_line)
#     if milton_appears:
#         alpha_dictionary[chr(alpha_sect)].append([line, "milton"])
#
# def finding_locke(x_line):
#     locke = re.compile('loc.')
#     locke_appears = locke.findall(x_line)
#     if locke_appears:
#         alpha_dictionary[chr(alpha_sect)].append([line, "locke"])
#
# def finding_dryden(x_line):
#     dryden = re.compile('dry[^i]')
#     dryden_appears = dryden.findall(x_line)
#     if dryden_appears:
#         alpha_dictionary[chr(alpha_sect)].append([line, "dryden"])

#define author count variables

shakespeares = 0
miltons = 0
lockes = 0
drydens = 0

for line in cleaned_lines_list[7348:]:
    if 'alphasectend' in line:
        # write dictionary contents to CSV                   ## CSV COUNT ##
#         with open("Letter_" + str(chr(alpha_sect)) + "_counts.csv", 'w', newline = '', encoding="UTF-8") as outfile_csv:
#             filewriter = csv.writer(outfile_csv, delimiter=',')
#             for pair in alpha_dictionary[chr(alpha_sect)]:
#                 citation_string = pair[0]
#                 label = pair[1]
#                 row = [label, citation_string]
#                 filewriter.writerow(row)

        # print count results to text file
        section_header = ("ALPHABET SECTION: " + str(chr(alpha_sect)))
#         page_counts_statement = ("Page count = " + str(page_counter[chr(alpha_sect)]))
        shak_counts_statement = ("Shakespeare citations = " + str(shakespeares))
        milton_counts_statement = ("Milton citations = " + str(miltons))
        locke_counts_statement = ("Locke citations = " + str(lockes))
        dryden_counts_statement = ("Dryden citations = " + str(drydens))
        section_border = ("- - - - - - - - - - - - -")

        print(section_header, file=outfile_total_count)
#         print(page_counts_statement, file=outfile_total_count)
        print(shak_counts_statement, file=outfile_total_count)
        print(milton_counts_statement, file=outfile_total_count)
        print(locke_counts_statement, file=outfile_total_count)
        print(dryden_counts_statement, file=outfile_total_count)
        print(section_border, file=outfile_total_count)

        # redefine alpha section
        if alpha_sect == 73 or alpha_sect == 85:
            alpha_sect = alpha_sect + 2
        else:
            alpha_sect = alpha_sect + 1

        # reset citation counts
        shakespeares = 0
        miltons = 0
        lockes = 0
        drydens = 0

#     # adding to page count
#     elif 'div class="page"' in line:
#         page_counter[chr(alpha_sect)] = page_counter[chr(alpha_sect)] + 1

    else:
        # counting occurrences of author citations
        shakespeares = len(shak.findall(line)) + shakespeares
        miltons = len(milton.findall(line)) + miltons
        lockes = len(locke.findall(line)) + lockes
        drydens = len(dryden.findall(line)) + drydens

        # adding author-citation pairs to dictionary for printing to CSV
#         finding_shakespeare(line)
#         finding_milton(line)
#         finding_locke(line)
#         finding_dryden(line)


# outfile_csv.close()
outfile_total_count.close()

print("Complete!")
