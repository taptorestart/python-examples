"""
https://github.com/scrapinghub/dateparser
"""
import dateparser

# Dateparser supports timezone
date = dateparser.parse("2022-01-01KST")
print(date)

date = dateparser.parse("2022-12-01UTC")
print(date)

"""
# Result
2022-01-01 00:00:00+09:00
2022-12-01 00:00:00+00:00
"""
