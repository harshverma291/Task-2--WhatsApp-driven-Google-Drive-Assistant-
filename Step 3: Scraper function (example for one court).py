def fetch_case_details(case_type, case_number, year):
    """
    Fetch case details from a sample eCourts portal.
    This example uses a dummy URL and parsing logic.
    You need to replace URLs and parsing based on actual court portals.
    """

    url = f"https://example-ecourts.gov.in/caseinfo?caseType={case_type}&caseNo={case_number}&year={year}"

    response = requests.get(url)
    if response.status_code != 200:
        raise Exception('Failed to fetch data from court portal')

    soup = BeautifulSoup(response.text, 'html.parser')

    parties = soup.find('div', {'id': 'parties'}).text.strip() if soup.find('div', {'id': 'parties'}) else 'N/A'

    filing_date = soup.find('span', {'id': 'filingDate'}).text.strip() if soup.find('span', {'id': 'filingDate'}) else 'N/A'

    next_hearing = soup.find('span', {'id': 'nextHearingDate'}).text.strip() if soup.find('span', {'id': 'nextHearingDate'}) else 'N/A'

    status = soup.find('span', {'id': 'caseStatus'}).text.strip() if soup.find('span', {'id': 'caseStatus'}) else 'N/A'

    pdf_link_tag = soup.find('a', {'id': 'judgmentPdf'})
    pdf_url = pdf_link_tag['href'] if pdf_link_tag else None

    details = {
        'parties': parties,
        'filing_date': filing_date,
        'next_hearing': next_hearing,
        'status': status,
        'raw_html': response.text
    }

    return details, pdf_url
