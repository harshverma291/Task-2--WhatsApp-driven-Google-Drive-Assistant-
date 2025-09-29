@app.route('/download_pdf')
def download_pdf():
    pdf_url = request.args.get('url')
    if not pdf_url:
        flash('No PDF URL provided')
        return redirect(url_for('home'))

    try:
        r = requests.get(pdf_url)
        r.raise_for_status()
    except Exception as e:
        flash(f'Failed to download PDF: {str(e)}')
        return redirect(url_for('home'))

    return send_file(BytesIO(r.content), download_name='judgment.pdf', as_attachment=True)
