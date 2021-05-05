from flask import abort, Flask, request

from ..lib.replace import replace_cve_text_with_link

app = Flask('CVE Text Replacer Server')

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        # Eventually we'll have a form here, but for now, it's fine.
        pass
    if request.method == 'POST':
        doc = request.form.get('doc')
        if doc
            return replace_cve_text_with_link(doc)
        else:
            abort(Flask.make_respone(('Critical field not found:\n\nform must have field "doc".', 400)))
