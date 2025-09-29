@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        case_type = request.form.get('case_type')
        case_number = request.form.get('case_number')
        year = request.form.get('year')

        if not (case_type and case_number and year):
            flash('Please fill all fields')
            return redirect(url_for('home'))

        try:
            details, pdf_url = fetch_case_details(case_type, case_number, year)
        except Exception as e:
            flash(f'Error fetching case details: {str(e)}')
            return redirect(url_for('home'))

        session = Session()
        case_query = CaseQuery(case_type=case_type, case_number=case_number, year=year, raw_response=details['raw_html'])
        session.add(case_query)
        session.commit()

        return render_template('details.html', details=details, pdf_url=pdf_url)

    return render_template('form.html')
