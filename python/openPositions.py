# The goal of this question is to print out which portfolios have open positions.

# A portfolio is represented by a name, and a collection of positions. Each position has a name, a start date, and an end date.

# A position is considered to be open on a given date if its starting date is before or on the given date and its end date is either not specified or on a later date than the given date.

# Input:
# Your program should read lines of text from standard input (this is already part of the initial template). The first line will specify a date (in YYYY-MM-DD format). The rest of the lines will specify portfolios in the following format:

# PortfolioName|PositionName:startDate:endDate,PositionName:startDate:endDate

# If any dates are missing or in the wrong format, they can be considered null.

# For example, this will be a valid input:

# 2020-01-01
# XXKCN|BRTHFKS01:2019-01-04:2019-05-03,CHDKWYNK:2020-01-04:2022-12-24
# XXKSN|BRTHFKS04:2019-11-04:,PSNKWYNK:2020-06-01:2022-12-24 
# XXPSN|BRTHFKS02:2023-01-04:2019-05-03,SHDNWYNK:2024-01-01:2022-12-24,SHDNWPSH:2027-01-01:2030-12-24
# Output:
# If a portfolio contains at least an open position, print the portfolio name on a single line to standard output.

# The portfolio names should be printed on separate lines in the order in which they first appear in the input

# For example, this will be a valid output (there should be no extra new lines or spaces either before or after the portfolio list):

# XXKCE
# XXKSP
# XXKSQ
# If there are no open positions output "NONE", for example

# NONE
# Test 1:
# Input:
# 2020-01-01
# Portfolio1|CUSIP1:2019-01-01:2022-02-01
# Portfolio2|CUSIP2:2019-01-01:2022-02-01
# Expected Output:
# Portfolio1
# Portfolio2

# Test 2:
# Input:
# 2020-01-01
# Portfolio1|CUSIP1:2019-01-01:2022-02-01
# Portfolio2|CUSIP2:2019-01-01:2022-02-01
# Portfolio3|CUSIP3:2020-01-01:2022-02-01
# Portfolio4|CUSIP3:2020-01-01:2019-01-01
# Expected Output:
# Portfolio1
# Portfolio2
# Portfolio3

# Test 3:
# Input:
# 2020-01-01
# Portfolio1|CUSIP1:2021-01-01:2022-02-01
# Portfolio2|CUSIP2:2021-01-01:2022-02-01
# Portfolio3|CUSIP3:2021-01-01:2022-02-01
# Portfolio4|CUSIP3:2021-01-01:2022-01-01
# Expected Output:
# NONE

# import sys
# from typing import List, Set, Optional
# from datetime import datetime

# DATE_FORMAT = '%Y-%m-%d'
# Empty = 'NONE'


# def get_portfolios_with_open_positions(date_str: str, portfolio_strings: List[str]) -> List[str]:
#     """
#     Return a list of all portfolios with open positions on the given date.
#     """
#     date = datetime.strptime(date_str, DATE_FORMAT)
#     portfolios = set()
#     for portfolio_str in portfolio_strings:
#         portfolio_name, positions = portfolio_str.split('|')
#         positions = positions.split(',')
#         for position in positions:
#             position_name, start_date_str, end_date_str = position.split(':')
#             start_date = datetime.strptime(start_date_str, DATE_FORMAT)
#             if end_date_str:
#                 end_date = datetime.strptime(end_date_str, DATE_FORMAT)
#             else:
#                 end_date = None
#             if start_date <= date and (not end_date or date < end_date):
#                 portfolios.add(portfolio_name)

#     if not portfolios:
#         return ('NONE').split(',') 
#     return sorted(list(portfolios))

def hey():
    return 'NONE'

if __name__ == '__main__':
    print(hey())