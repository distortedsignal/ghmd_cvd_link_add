from flask import abort, Flask, make_response, render_template, request

from .replace import replace_cve_text_with_link

app = Flask('CVE Text Replacer Server')

def process_form_post():
    abort(make_response(501))
    # This isn't technically correct. We need to wrap this guy in HTML to make the form response valid.
    doc = request.form.get('doc')
    if doc:
        return replace_cve_text_with_link(doc)
    else:
        abort(make_response(('Critical field not found:\n\nform must have field "doc".', 400)))

def process_text_post():
    return replace_cve_text_with_link(str(request.data))

def process_post():
    content_type = request.headers.get('Content-Type')
    if 'form-data' in content_type:
        return process_form_post()
    elif 'text/plain' in content_type:
        return process_text_post()
    else:
        abort(make_response(('Inappropriate Content-Type:\n\nContent-Type header must be one of the following:\nmultipart/form-data\napplication/text', 400)))


@app.route('/', methods=['GET', 'POST'])
def root_method():
    if request.method == 'GET':
        # Eventually we'll have a form here, but for now, it's fine.
        return render_template('base.html')
    if request.method == 'POST':
        return process_post()
