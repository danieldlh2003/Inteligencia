import re
def check_re(i):
    """
        check Regex Match
    """
    if re.match('###### (.*)', i) is not None:
        i = '<h6>' + i[7:] + '</h6>'
    elif re.match('##### (.*)', i) is not None:
        i = '<h5>' + i[6:] + '</h5>'
    elif re.match('#### (.*)', i) is not None:
        i = '<h4>' + i[5:] + '</h4>'
    elif re.match('### (.*)', i) is not None:
        i = '<h3>' + i[4:] + '</h3>'
    elif re.match('## (.*)', i) is not None:
        i = '<h2>' + i[3:] + '</h2>'
    elif re.match('# (.*)', i) is not None:
        i = '<h1>' + i[2:] + '</h1>'
    return i
def curr_match_group(match, is_bold, is_italic):
    """
        check Regex match group
    """
    curr = match.group(1)
    match1 = re.match('(.*)__(.*)__(.*)', curr)
    if match1:
        is_bold = True
    match1 = re.match('(.*)_(.*)_(.*)', curr)
    if match1:
        is_italic = True
    if is_bold:
        curr = match1.group(1) + '<strong>' + \
               match1.group(2) + '</strong>' + match1.group(3)
    if is_italic:
        curr = match1.group(1) + '<em>' + match1.group(2) + \
               '</em>' + match1.group(3)
    return curr
def parse(markdown):
    """
        Parser Function
    """
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False
    for i in lines:
        i = check_re(i)
        match = re.match(r'\* (.*)', i)
        if match:
            if not in_list:
                in_list = True
                is_bold = False
                is_italic = False
                curr = match.group(1)
                match1 = re.match('(.*)__(.*)__(.*)', curr)
                if match1:
                    curr = match1.group(1) + '<strong>' + \
                           match1.group(2) + '</strong>' + match1.group(3)
                    is_bold = True
                match1 = re.match('(.*)_(.*)_(.*)', curr)
                if match1:
                    curr = match1.group(1) + '<em>' + match1.group(2) + \
                           '</em>' + match1.group(3)
                    is_italic = True
                i = '<ul><li>' + curr + '</li>'
            else:
                is_bold = False
                is_italic = False
                i = '<li>' + curr_match_group(match, is_bold, is_italic) + '</li>'
        else:
            if in_list:
                in_list_append = True
                in_list = False
        match = re.match('<h|<ul|<p|<li', i)
        if not match:
            i = '<p>' + i + '</p>'
        match = re.match('(.*)__(.*)__(.*)', i)
        if match:
            i = match.group(1) + '<strong>' + match.group(2) + '</strong>' + match.group(3)
        match = re.match('(.*)_(.*)_(.*)', i)
        if match:
            i = match.group(1) + '<em>' + match.group(2) + '</em>' + match.group(3)
        if in_list_append:
            i = '</ul>' + i
            in_list_append = False
        res += i
    if in_list:
        res += '</ul>'
    return res