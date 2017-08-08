#!/usr/bin/env python
import heapq as hq
import sys
from sets import Set

class Company(object):

    def __init__(self, company_id, salary_offered, max_jobs):
        self.company_id = company_id
        self.salary_offered = salary_offered
        self.available_jobs = max_jobs
        self.recruited = False

    def __cmp__(self, other):
        return -cmp(self.salary_offered, other.salary_offered)

    def are_jobs_available(self):
        return True if self.available_jobs > 0 else False

    def offer_job(self):
        self.available_jobs -= 1
        if not self.recruited:
            self.recruited = True


class Candidate(object):

    def __init__(self, candidate_id, min_expectation):
        self.candidate_id = candidate_id
        self.min_expectation = min_expectation
        self.qualified_companies = []

    def add_qualified_company(self, company):
        hq.heappush(self.qualified_companies, company)

    def get_max_job_offer(self, companies):
        found = False
        while(found == False and len(self.qualified_companies) > 0):
            qual_comp = hq.heappop(self.qualified_companies)
            if companies[qual_comp.company_id].are_jobs_available():
                found = True

        if found and qual_comp.salary_offered >= self.min_expectation:
            return qual_comp
        else:
            return -1


def solution(candidates, companies):
    candidates_placed = 0
    total_salary_sum = 0
    companies_not_recruited_anyone = 0

    for candidate in candidates:
        job_offer = candidate.get_max_job_offer(companies)
        if job_offer != -1:
            company = companies[job_offer.company_id]
            company.offer_job()
            total_salary_sum += job_offer.offered_salary
            candidates_placed += 1

    for company in companies:
        if not company.recruited:
            companies_not_recruited_anyone += 1

    print candidates_placed, total_salary_sum, companies_not_recruited_anyone


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
        companies_info = [[map(int, raw_input().strip().split(' '))] for i in xrange(m)]
        # i-th candidate has qualified for a job in the j-th company
        qual = [[map(None, raw_input().strip())] for i in xrange(n)]

        solution_arr(candidates_min_salary, companies_info, qual)


def main():
    # read_from_console()
    read_from_file()


if __name__ == '__main__':
    main()
