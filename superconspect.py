import os
import re
import sys

from urllib.parse import quote

if len(sys.argv) <= 1:
    print('Enter source folder name as command argument')
    exit(1)


folder = sys.argv[1]

if all(map(lambda x: x.endswith('.md') or '.' not in x, os.listdir(folder))):
    supername = folder + "_superconspect.md"
    BLACKLIST = [supername]

    contents = {}

    text = ''

    for i in os.listdir(folder):
        if not i.endswith('.md') or any([j in i for j in BLACKLIST]):
            continue

        file_text = open(os.path.join(folder, i), 'r', encoding='utf8').read()
        if re.match(r'\s*#ignore', file_text):
            print(f'File {i} ignored')
            continue

        for header_match in re.finditer('(^|\n)((#+) +(.+))\n', file_text, re.U):
            header_level = len(header_match.group(3))
            header_name = header_match.group(4).strip()

            header_link = quote(header_name.lower().replace(' ', '-'), safe='', encoding='utf8')

            temp = header_link
            counter = 1
            while temp in contents:
                temp = header_link + f'-{counter}'
                counter += 1

            contents[temp] = (header_name, header_level)

            file_text = file_text.replace(
                header_match.group(2),
                header_match.group(3) + f' <a name="{header_link}"></a> ' + header_match.group(4), 1)

        text += file_text + '\n\n'

    table_of_contents = ''
    for link, (header, header_level) in contents.items():
        table_of_contents += '  ' * (header_level - 1) + '* ' + f'[{header}](#{link})\n'

    first_header = re.search('#+.+\n', text)
    first_header_text = None
    if first_header:
        first_header_text = first_header.group(0)
        text = text[len(first_header_text):]

    text = table_of_contents + '\n\n' + text
    if first_header:
        text = first_header_text + '\n\n' + text

    open(os.path.join(folder, supername), 'w', encoding='utf8').write(text)

    print('Markdown file is combined.')

else:
    supername = folder + "_superconspect.tex"
    BLACKLIST = ['cheatsheet', supername]

    subject = None
    teacher = None

    text = ''

    for i in os.listdir(folder):
        if i.endswith('.tex') and not any([j in i for j in BLACKLIST]):
            t = open(os.path.join(folder, i), 'r', encoding='utf8').read()
            if subject is None:
                subject = re.search(r'\\fancyhead\[LO,LE]\{(.*)}', t).group(1)
            if teacher is None:
                teacher = re.search(r'\\fancyhead\[RO,RE]\{(.*)}', t).group(1)
            t = re.search(r'\\begin\{document\}(.+?)\n*\\end\{document\}', t, re.S | re.M | re.I)

            text += f'    % begin {i}\n'

            text += t.group(1) + f'\n    % end {i}\n\n'


    text = re.sub(r'section\[.*]', 'section', text)
    text = (open('superconspect_template.tex', encoding='utf8').read().
            replace('$conspects$', text).
            replace('$subject$', subject).
            replace('$teacher$', teacher))
    open(os.path.join(folder, supername), 'w', encoding='utf8').write(text)

    os.system("python linter.py " + os.path.join(".", folder, supername))

