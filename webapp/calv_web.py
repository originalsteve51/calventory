from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

run_on_host = os.environ.get('RUN_ON_HOST') 
using_port = os.environ.get('USING_PORT')
debug_mode = os.environ.get('DEBUG_MODE')

current_working_directory = '/home/stephenharding/my_code/python/calventoryweb'

properties_path = f'{current_working_directory}/dropzone/calvaryproperty.csv'

def load_properties(file_path):
    return pd.read_csv(file_path)

properties = load_properties(properties_path)
    

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = f'{current_working_directory}/dropzone'

@app.route('/')
def index():
    properties = load_properties(properties_path)
    return render_template('index.html', properties=properties)


@app.route('/<int:property_id>')
def property_detail(property_id):
    properties = load_properties(properties_path)

    # Obtain the row for the specified property id
    property_item = properties[properties['Control ID'] == property_id].iloc[0]
    
    # Also get the column names for the details contained in the row
    col_names = properties.columns.tolist()

    return render_template('property_detail.html', 
                            item=property_item, 
                            col_names=col_names)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']

    print('------> ', file)
    
    if file.filename == '':
        return "No selected file", 400
    
    if file and file.filename.endswith('.csv'):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        print(f'File saved to {filepath}')
        return f'File saved to {filepath}', 200
    return "Only CSV files are allowed", 400

if __name__ == "__main__":

    debug_mode_bool = True if debug_mode == 'True' else False

    app.run(debug=debug_mode_bool, threaded=True, port=8082, host='0.0.0.0')