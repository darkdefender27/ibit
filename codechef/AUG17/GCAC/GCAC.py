#!/usr/bin/env python
import sys
from sets import Set


def solution_arr(cand_min_sal, comp_info, qual):
    candidates_placed, total_salary_sum, companies_not_recruited_anyone = 0, 0, 0
    recruited_companies = Set([])

    n, m = len(cand_min_sal), len(comp_info)
    for i in xrange(n):
        max_offer, company_placed_in = -1, -1
        for ii in xrange(m):
            # Jobs are still available at the company 'm'
            if qual[i][ii] == '1' and comp_info[ii][1] > 0:
                if comp_info[ii][0] > max_offer:
                    max_offer = comp_info[ii][0]
                    company_placed_in = ii

        if company_placed_in != -1:
            # Check if the max_salary being offered meets the expectations.
            if comp_info[company_placed_in][0] >= cand_min_sal[i]:
                # Reduce no. of available jobs by 1.
                recruited_companies.add(company_placed_in)
                comp_info[company_placed_in][1] -= 1
                candidates_placed += 1
                total_salary_sum += max_offer

    # Compute the no. of companies that did not recruit any candidate.
    for iii in xrange(m):
        if iii not in recruited_companies:
            companies_not_recruited_anyone += 1

    print candidates_placed, total_salary_sum, companies_not_recruited_anyone


def read_from_file():
    sys.stdin = open('gcac.in', 'r')
    T = int(sys.stdin.readline().strip())
    for _ in xrange(T):
        # N candidates & M companies
        n, m = map(int, sys.stdin.readline().strip().split(' '))
        # i-th candidate's minimum salary expectation
        candidates_min_salary = map(int, sys.stdin.readline().strip().split(' '))
        # 0 - Offered Salary :: 1 - Max Job Offers
        companies_info = [map(int, sys.stdin.readline().strip().split(' ')) for i in xrange(m)]
        # i-th candidate has qualified for a job in the j-th company
        qual = [map(None, sys.stdin.readline().strip()) for ii in xrange(n)]

        solution_arr(candidates_min_salary, companies_info, qual)


def read_from_console():
    T = int(raw_input().strip())
    for _ in xrange(T):
        # N candidates & M companies
        n, m = map(int, raw_input().strip().split(' '))
        # i-th candidate's minimum salary expectation
        candidates_min_salary = map(int, raw_input().strip().split(' '))
        # 0 - Offered Salary :: 1 - Max Job Offers
        companies_info = [map(int, raw_input().strip().split(' ')) for i in xrange(m)]
        # i-th candidate has qualified for a job in the j-th company
        qual = [map(None, raw_input().strip()) for ii in xrange(n)]

        solution_arr(candidates_min_salary, companies_info, qual)


def main():
    read_from_console()
    # read_from_file()


if __name__ == '__main__':
    main()
