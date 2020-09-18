import re

class Regex:
    """ Helper class for Regex """

    def get_matches(self, str, regex):
        matches = re.finditer(regex, str, re.MULTILINE)

        m = {}

        for matchNum, match in enumerate(matches, start=1):
            m[matchNum] = []

            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1

                m[matchNum].append(match.group(groupNum).strip())

        return m
