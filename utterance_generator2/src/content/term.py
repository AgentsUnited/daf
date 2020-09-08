import re

def get_term_specifications(terms):
    '''
    Gets the prolog-style specification of given terms as (<term>, <parameter_count>, <parameters>)
    '''
    speficifications = []

    for a in terms:
        a = str(a)
        matches = re.findall(re.compile(r"([^\( \)\n\r]+)(\([^\(\)]+\))?"), a)
        if matches:
            term = matches[0][0]
            if len(matches[0]) > 1:
                parameters = [p.strip() for p in matches[0][1][1:-1].split(",")]
                parameter_count = len(matches[0][1].split(","))
            else:
                parameters = []
                parameter_count = 0

            speficifications.append((term.strip(), parameter_count, parameters))

    return speficifications

def get_term_specification(term):
    spec = get_term_specifications([term])

    if spec:
        return spec[0]
    else:
        return ("",0,[])
