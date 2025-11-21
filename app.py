# from flask import Flask, render_template, request, redirect, url_for, session, send_file
# import os
# import sqlite3
# from werkzeug.utils import secure_filename
# from datetime import datetime
# import csv
#
# app = Flask(__name__)
# app.secret_key = 'supersecretkey'
# UPLOAD_FOLDER = 'uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# ALLOWED_PDF = {'pdf'}
# ALLOWED_IMG = {'jpg', 'jpeg'}
#
# # Ensure upload folder exists
# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
#
# def init_db():
#     with sqlite3.connect('database.db') as conn:
#         conn.execute('''CREATE TABLE IF NOT EXISTS students (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             course TEXT,
#             roll_no TEXT,
#             score TEXT,
#             name TEXT,
#             father TEXT,
#             mother TEXT,
#             dob TEXT,
#             mobile TEXT,
#             email TEXT,
#             address TEXT,
#             previous_appearance TEXT,
#             previous_roll TEXT,
#             religion TEXT,
#             school_10 TEXT,
#             school_11 TEXT,
#             school_12 TEXT,
#             bank_name TEXT,
#             account_name TEXT,
#             ifsc TEXT,
#             branch TEXT,
#             account_no TEXT,
#             created_at TEXT
#         )''')
# init_db()
#
# def allowed_file(filename, allowed_set):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_set
#
# @app.route('/')
# def index():
#     return render_template('form_step1.html')
#
# # Step 1 -> Step 2
# @app.route('/form/step2', methods=['POST'])
# def form_step2():
#     session['course'] = request.form['course']
#     session['roll_no'] = request.form['roll_no']
#     session['score'] = request.form['score']
#     return render_template('form_step2.html')
#
# # Step 2 -> Step 3
# @app.route('/form/step3', methods=['POST'])
# def form_step3():
#     for field in ['name', 'father', 'mother', 'dob', 'mobile', 'email', 'address', 'previous', 'prev_roll', 'religion']:
#         session[field] = request.form[field]
#     return render_template('form_step3.html')
#
# # Step 3 -> Step 4
# @app.route('/form/step4', methods=['POST'])
# def form_step4():
#     for field in ['school_10', 'school_11', 'school_12']:
#         session[field] = request.form[field]
#     return render_template('form_step4.html')
#
# # Final Submit
# @app.route('/submit', methods=['POST'])
# def submit():
#     for field in ['account_name', 'bank_name', 'ifsc', 'branch', 'account_no']:
#         session[field] = request.form[field]
#
#     roll_no = session.get('roll_no')
#     folder = os.path.join(app.config['UPLOAD_FOLDER'], f"NEET{roll_no}")
#     os.makedirs(folder, exist_ok=True)
#
#     # Save files
#     files = {
#         'marks_10': ('marks_10', 'pdf'),
#         'marks_12': ('marks_12', 'pdf'),
#         'scorecard': ('scorecard', 'pdf'),
#         'aadhar': ('aadhar', 'pdf'),
#         'photo': ('photo', 'img'),
#         'signature': ('signature', 'img'),
#         'thumb': ('thumb', 'img'),
#     }
#
#     for field, (key, ftype) in files.items():
#         file = request.files.get(key)
#         if file and allowed_file(file.filename, ALLOWED_PDF if ftype == 'pdf' else ALLOWED_IMG):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(folder, filename))
#         else:
#             return f"Invalid or missing file: {field}", 400
#
#     # Insert into DB
#     with sqlite3.connect('database.db') as conn:
#         conn.execute('''INSERT INTO students (
#             course, roll_no, score, name, father, mother, dob, mobile, email,
#             address, previous_appearance, previous_roll, religion,
#             school_10, school_11, school_12,
#             bank_name, account_name, ifsc, branch, account_no, created_at
#         ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
#             (
#                 session['course'], session['roll_no'], session['score'], session['name'],
#                 session['father'], session['mother'], session['dob'], session['mobile'], session['email'],
#                 session['address'], session['previous'], session['prev_roll'], session['religion'],
#                 session['school_10'], session['school_11'], session['school_12'],
#                 session['bank_name'], session['account_name'], session['ifsc'], session['branch'],
#                 session['account_no'], datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#             )
#         )
#
#     session.clear()
#     return render_template('success.html')
#
# # Admin login
# @app.route('/admin', methods=['GET', 'POST'])
# def admin():
#     if request.method == 'POST':
#         if request.form['username'] == 'admin' and request.form['password'] == 'gyanguru123':
#             session['admin'] = True
#             return redirect(url_for('dashboard'))
#         else:
#             return "Invalid credentials", 403
#     return render_template('admin_login.html')
#
# @app.route('/dashboard')
# def dashboard():
#     if not session.get('admin'):
#         return redirect(url_for('admin'))
#     with sqlite3.connect('database.db') as conn:
#         students = conn.execute('SELECT * FROM students').fetchall()
#     return render_template('admin_dashboard.html', students=students)
#
# @app.route('/download_csv')
# def download_csv():
#     if not session.get('admin'):
#         return redirect(url_for('admin'))
#     with sqlite3.connect('database.db') as conn:
#         students = conn.execute('SELECT * FROM students').fetchall()
#     filepath = 'submissions.csv'
#     with open(filepath, 'w', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         headers = [description[0] for description in conn.execute('PRAGMA table_info(students)')]
#         writer.writerow(headers)
#         writer.writerows(students)
#     return send_file(filepath, as_attachment=True)
#
# @app.route('/logout')
# def logout():
#     session.clear()
#     return redirect(url_for('admin'))
#
# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, render_template, request, redirect, url_for, session, send_file
# import os
# import sqlite3
# from werkzeug.utils import secure_filename
# from datetime import datetime
# import csv
# from fpdf import FPDF
#
# app = Flask(__name__)
# app.secret_key = 'supersecretkey'
# UPLOAD_FOLDER = 'uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# ALLOWED_PDF = {'pdf'}
# ALLOWED_IMG = {'jpg', 'jpeg'}
#
# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
#
#
# def init_db():
#     with sqlite3.connect('database.db') as conn:
#         conn.execute('''CREATE TABLE IF NOT EXISTS students (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             course TEXT,
#             roll_no TEXT,
#             score TEXT,
#             name TEXT,
#             father TEXT,
#             mother TEXT,
#             dob TEXT,
#             mobile TEXT,
#             email TEXT,
#             address TEXT,
#             previous_appearance TEXT,
#             previous_roll TEXT,
#             religion TEXT,
#             school_10 TEXT,
#             school_11 TEXT,
#             school_12 TEXT,
#             bank_name TEXT,
#             account_name TEXT,
#             ifsc TEXT,
#             branch TEXT,
#             account_no TEXT,
#             created_at TEXT
#         )''')
#
#
# init_db()
#
#
# def allowed_file(filename, allowed_set):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_set
#
#
# def create_admission_pdf(data, folder):
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", size=14)
#     pdf.cell(200, 10, "Gyan Guru Pvt Ltd - Admission Record", ln=True, align="C")
#     pdf.set_font("Arial", size=11)
#
#     # Add main fields
#     for key, value in data.items():
#         if key in ['photo', 'signature', 'thumb']:  # images handled below
#             continue
#         pdf.cell(0, 10, f"{key.replace('_', ' ').title()}: {value}", ln=True)
#
#     pdf.ln(5)
#     # Embed images for photo, signature, thumb
#     for img_field in ['photo', 'signature', 'thumb']:
#         img_path = os.path.join(folder, data.get(img_field, ""))
#         if os.path.exists(img_path) and data.get(img_field):
#             pdf.cell(0, 10, f"{img_field.title()}:", ln=True)
#             pdf.image(img_path, w=25, h=25)
#             pdf.ln(2)
#
#     pdf.ln(8)
#     pdf.cell(0, 10, "Other Uploaded Documents:", ln=True)
#     for file in os.listdir(folder):
#         if file not in [data.get('photo'), data.get('signature'), data.get('thumb'), 'admission_record.pdf']:
#             pdf.cell(0, 10, f"- {file}", ln=True)
#
#     pdf.output(os.path.join(folder, "admission_record.pdf"))
#
#
# @app.route('/')
# def index():
#     return render_template('form_step1.html')
#
#
# @app.route('/form/step2', methods=['POST'])
# def form_step2():
#     session['course'] = request.form['course']
#     session['roll_no'] = request.form['roll_no']
#     session['score'] = request.form['score']
#     return render_template('form_step2.html')
#
#
# @app.route('/form/step3', methods=['POST'])
# def form_step3():
#     for field in ['name', 'father', 'mother', 'dob', 'mobile', 'email', 'address', 'previous', 'prev_roll', 'religion']:
#         session[field] = request.form[field]
#     return render_template('form_step3.html')
#
#
# @app.route('/form/step4', methods=['POST'])
# def form_step4():
#     for field in ['school_10', 'school_11', 'school_12']:
#         session[field] = request.form[field]
#     return render_template('form_step4.html')
#
#
# @app.route('/submit', methods=['POST'])
# def submit():
#     for field in ['account_name', 'bank_name', 'ifsc', 'branch', 'account_no']:
#         session[field] = request.form[field]
#
#     roll_no = session.get('roll_no')
#     folder = os.path.join(app.config['UPLOAD_FOLDER'], f"NEET{roll_no}")
#     os.makedirs(folder, exist_ok=True)
#
#     # Save files
#     files = {
#         'marks_10': ('marks_10', 'pdf'),
#         'marks_12': ('marks_12', 'pdf'),
#         'scorecard': ('scorecard', 'pdf'),
#         'aadhar': ('aadhar', 'pdf'),
#         'photo': ('photo', 'img'),
#         'signature': ('signature', 'img'),
#         'thumb': ('thumb', 'img'),
#     }
#
#     saved_file_names = {'photo': "", 'signature': "", 'thumb': ""}
#
#     for field, (key, ftype) in files.items():
#         file = request.files.get(key)
#         if file and allowed_file(file.filename, ALLOWED_PDF if ftype == 'pdf' else ALLOWED_IMG):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(folder, filename))
#             if field in ['photo', 'signature', 'thumb']:
#                 saved_file_names[field] = filename
#         else:
#             return f"Invalid or missing file: {field}", 400
#
#     # Insert into DB
#     with sqlite3.connect('database.db') as conn:
#         conn.execute('''INSERT INTO students (
#             course, roll_no, score, name, father, mother, dob, mobile, email,
#             address, previous_appearance, previous_roll, religion,
#             school_10, school_11, school_12,
#             bank_name, account_name, ifsc, branch, account_no, created_at
#         ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
#                      (
#                          session['course'], session['roll_no'], session['score'], session['name'],
#                          session['father'], session['mother'], session['dob'], session['mobile'], session['email'],
#                          session['address'], session['previous'], session['prev_roll'], session['religion'],
#                          session['school_10'], session['school_11'], session['school_12'],
#                          session['bank_name'], session['account_name'], session['ifsc'], session['branch'],
#                          session['account_no'], datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#                      )
#                      )
#     # Prepare data for PDF
#     data = {
#         'course': session['course'],
#         'roll_no': session['roll_no'],
#         'score': session['score'],
#         'name': session['name'],
#         'father': session['father'],
#         'mother': session['mother'],
#         'dob': session['dob'],
#         'mobile': session['mobile'],
#         'email': session['email'],
#         'address': session['address'],
#         'previous_appearance': session['previous'],
#         'previous_roll': session['prev_roll'],
#         'religion': session['religion'],
#         'school_10': session['school_10'],
#         'school_11': session['school_11'],
#         'school_12': session['school_12'],
#         'bank_name': session['bank_name'],
#         'account_name': session['account_name'],
#         'ifsc': session['ifsc'],
#         'branch': session['branch'],
#         'account_no': session['account_no'],
#         'photo': saved_file_names['photo'],
#         'signature': saved_file_names['signature'],
#         'thumb': saved_file_names['thumb'],
#     }
#     create_admission_pdf(data, folder)
#
#     session.clear()
#     return render_template('success.html')
#
#
# @app.route('/admin', methods=['GET', 'POST'])
# def admin():
#     if request.method == 'POST':
#         if request.form['username'] == 'admin' and request.form['password'] == 'gyanguru123':
#             session['admin'] = True
#             return redirect(url_for('dashboard'))
#         else:
#             return "Invalid credentials", 403
#     return render_template('admin_login.html')
#
#
# @app.route('/dashboard')
# def dashboard():
#     if not session.get('admin'):
#         return redirect(url_for('admin'))
#     with sqlite3.connect('database.db') as conn:
#         students = conn.execute('SELECT * FROM students').fetchall()
#     return render_template('admin_dashboard.html', students=students)
#
#
# @app.route('/download_csv')
# def download_csv():
#     if not session.get('admin'):
#         return redirect(url_for('admin'))
#     with sqlite3.connect('database.db') as conn:
#         students = conn.execute('SELECT * FROM students').fetchall()
#     filepath = 'submissions.csv'
#     with open(filepath, 'w', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         headers = [description[0] for description in conn.execute('PRAGMA table_info(students)')]
#         writer.writerow(headers)
#         writer.writerows(students)
#     return send_file(filepath, as_attachment=True)
#
#
# @app.route('/logout')
# def logout():
#     session.clear()
#     return redirect(url_for('admin'))
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, request, redirect, url_for, session, send_file
# import os
# import sqlite3
# from werkzeug.utils import secure_filename
# from datetime import datetime
# import csv
# from fpdf import FPDF
#
# app = Flask(__name__)
# app.secret_key = 'supersecretkey'
#
# UPLOAD_FOLDER = 'uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# ALLOWED_PDF = {'pdf'}
# ALLOWED_IMG = {'jpg', 'jpeg'}
#
# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
#
#
# def init_db():
#     with sqlite3.connect('database.db') as conn:
#         conn.execute('''CREATE TABLE IF NOT EXISTS students (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             course TEXT,
#             roll_no TEXT,
#             score TEXT,
#             name TEXT,
#             father TEXT,
#             mother TEXT,
#             dob TEXT,
#             mobile TEXT,
#             email TEXT,
#             address TEXT,
#             previous_appearance TEXT,
#             previous_roll TEXT,
#             religion TEXT,
#             school_10 TEXT,
#             school_11 TEXT,
#             school_12 TEXT,
#             bank_name TEXT,
#             account_name TEXT,
#             ifsc TEXT,
#             branch TEXT,
#             account_no TEXT,
#             created_at TEXT
#         )''')
#
#
# init_db()
#
#
# def allowed_file(filename, allowed_set):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_set
#
#
# # def create_admission_pdf(data, folder):
# #     logo_path = os.path.join(os.getcwd(), "gyanguru_logo.png")  # Add your logo in project folder if you have one
# #
# #     pdf = FPDF()
# #     pdf.add_page()
# #     pdf.set_auto_page_break(auto=True, margin=15)
# #
# #     # Logo and Title
# #     if os.path.exists(logo_path):
# #         pdf.image(logo_path, x=10, y=8, w=25)
# #     pdf.set_font("Arial", "B", 18)
# #     pdf.cell(0, 15, "Gyan Guru Pvt Ltd - Admission Record", ln=True, align="C")
# #
# #     pdf.set_font("Arial", "", 12)
# #     pdf.set_text_color(40, 40, 45)
# #     pdf.cell(0, 6, "Admission Details", ln=True, align="L")
# #     pdf.set_draw_color(70, 130, 180)
# #     pdf.set_line_width(0.8)
# #     pdf.line(10, pdf.get_y(), 200, pdf.get_y())
# #     pdf.ln(6)
# #
# #     # Two-column layout for essential fields
# #     col1_fields = ['name', 'roll_no', 'dob', 'mobile', 'father', 'mother', 'email', 'religion']
# #     col2_fields = ['course', 'score', 'address', 'previous_appearance', 'previous_roll', 'bank_name', 'account_name',
# #                    'branch']
# #
# #     for field1, field2 in zip(col1_fields, col2_fields):
# #         pdf.set_font("Arial", "B", 11)
# #         pdf.cell(40, 7, f"{field1.replace('_', ' ').title()}:")
# #         pdf.set_font("Arial", "", 11)
# #         pdf.cell(50, 7, f"{data.get(field1, '')}", border=0)
# #         pdf.set_font("Arial", "B", 11)
# #         pdf.cell(35, 7, f"{field2.replace('_', ' ').title()}:")
# #         pdf.set_font("Arial", "", 11)
# #         pdf.cell(0, 7, f"{data.get(field2, '')}", border=0, ln=True)
# #
# #     pdf.ln(4)
# #     pdf.set_font("Arial", "B", 12)
# #     pdf.cell(0, 8, "Marks Table", ln=True)
# #     pdf.set_font("Arial", "", 11)
# #     pdf.set_fill_color(230, 240, 255)
# #     pdf.cell(50, 8, "Class", 1, 0, "C", True)
# #     pdf.cell(50, 8, "Obtained Marks", 1, 1, "C", True)
# #     marks_fields = {'school_10': '10th Class', 'school_11': '11th Class', 'school_12': '12th Class'}
# #     for k, v in marks_fields.items():
# #         pdf.cell(50, 7, v, 1, 0)
# #         pdf.cell(50, 7, data.get(k, ''), 1, 1)
# #     pdf.ln(4)
# #
# #     pdf.set_font("Arial", "B", 12)
# #     pdf.cell(0, 10, "Uploaded Images", ln=True)
# #     for img_field in ['photo', 'signature', 'thumb']:
# #         img_path = os.path.join(folder, data.get(img_field, ""))
# #         if os.path.exists(img_path) and data.get(img_field):
# #             pdf.set_font("Arial", "B", 11)
# #             pdf.cell(0, 8, f"{img_field.replace('_', ' ').title()}:", ln=True)
# #             pdf.image(img_path, w=38, h=38)
# #             pdf.ln(6)
# #
# #     pdf.ln(6)
# #     pdf.set_font("Arial", "B", 12)
# #     pdf.cell(0, 10, "Other Uploaded Documents:", ln=True)
# #     pdf.set_font("Arial", "", 11)
# #     for file in os.listdir(folder):
# #         if file not in [data.get('photo'), data.get('signature'), data.get('thumb'), 'admission_record.pdf']:
# #             pdf.cell(0, 8, f"- {file}", ln=True)
# #
# #     # Footer
# #     pdf.set_y(-30)
# #     pdf.set_font("Arial", "B", 11)
# #     pdf.set_text_color(70, 70, 70)
# #     pdf.cell(0, 10, "Gyan Guru Pvt Ltd | www.gyanguru.com | +91-XXXXXXXXXX", ln=True, align="C")
# #
# #     pdf.output(os.path.join(folder, "admission_record.pdf"))
#
# # def create_admission_pdf(data, folder):
# #     logo_path = os.path.join(os.getcwd(), "gyanguru_logo.png")  # Place logo here
# #
# #     pdf = FPDF()
# #     pdf.add_page()
# #     pdf.set_auto_page_break(auto=True, margin=15)
# #
# #     # Logo (right-aligned)
# #     if os.path.exists(logo_path):
# #         pdf.image(logo_path, x=170, y=8, w=25)  # move to top-right
# #
# #     # Title (centered, not overlapped)
# #     pdf.set_xy(10, 10)
# #     pdf.set_font("Arial", "B", 18)
# #     pdf.cell(0, 15, "Gyan Guru Pvt Ltd - Admission Record", ln=True, align="C")
# #
# #     # Move down below title/logo
# #     pdf.set_y(30)
# #     pdf.set_font("Arial", "", 12)
# #     pdf.set_text_color(40, 40, 45)
# #     pdf.cell(0, 8, "Admission Details", ln=True, align="L")
# #     pdf.set_draw_color(70, 130, 180)
# #     pdf.set_line_width(0.8)
# #     pdf.line(10, pdf.get_y(), 200, pdf.get_y())
# #     pdf.ln(8)
# #
# #     # Two-column layout for essential fields
# #     col1_fields = ['name', 'roll_no', 'dob', 'mobile', 'father', 'mother', 'email', 'religion']
# #     col2_fields = ['course', 'score', 'address', 'previous_appearance', 'previous_roll', 'bank_name', 'account_name',
# #                    'branch']
# #
# #     for field1, field2 in zip(col1_fields, col2_fields):
# #         pdf.set_font("Arial", "B", 11)
# #         pdf.cell(40, 7, f"{field1.replace('_', ' ').title()}:", border=0)
# #         pdf.set_font("Arial", "", 11)
# #         pdf.cell(50, 7, f"{data.get(field1, '')}", border=0)
# #         pdf.set_font("Arial", "B", 11)
# #         pdf.cell(35, 7, f"{field2.replace('_', ' ').title()}:", border=0)
# #         pdf.set_font("Arial", "", 11)
# #         pdf.cell(0, 7, f"{data.get(field2, '')}", border=0, ln=True)
# #
# #     pdf.ln(4)
# #     pdf.set_font("Arial", "B", 12)
# #     pdf.cell(0, 8, "Marks Table", ln=True)
# #     pdf.set_font("Arial", "", 11)
# #     pdf.set_fill_color(230, 240, 255)
# #     pdf.cell(50, 8, "Class", 1, 0, "C", True)
# #     pdf.cell(50, 8, "Obtained Marks", 1, 1, "C", True)
# #     marks_fields = {'school_10': '10th Class', 'school_11': '11th Class', 'school_12': '12th Class'}
# #     for k, v in marks_fields.items():
# #         pdf.cell(50, 7, v, 1, 0)
# #         pdf.cell(50, 7, data.get(k, ''), 1, 1)
# #     pdf.ln(4)
# #
# #     pdf.set_font("Arial", "B", 12)
# #     pdf.cell(0, 10, "Uploaded Images", ln=True)
# #     for img_field in ['photo', 'signature', 'thumb']:
# #         img_path = os.path.join(folder, data.get(img_field, ""))
# #         if os.path.exists(img_path) and data.get(img_field):
# #             pdf.set_font("Arial", "B", 11)
# #             pdf.cell(0, 8, f"{img_field.replace('_', ' ').title()}:", ln=True)
# #             pdf.image(img_path, w=38, h=38)
# #             pdf.ln(6)
# #
# #     pdf.ln(6)
# #     pdf.set_font("Arial", "B", 12)
# #     pdf.cell(0, 10, "Other Uploaded Documents:", ln=True)
# #     pdf.set_font("Arial", "", 11)
# #     for file in os.listdir(folder):
# #         if file not in [data.get('photo'), data.get('signature'), data.get('thumb'), 'admission_record.pdf']:
# #             pdf.cell(0, 8, f"- {file}", ln=True)
# #
# #     # Footer
# #     pdf.set_y(-30)
# #     pdf.set_font("Arial", "B", 11)
# #     pdf.set_text_color(70, 70, 70)
# #     pdf.cell(0, 10, "Gyan Guru Pvt Ltd | www.gyanguru.com | +91-XXXXXXXXXX", ln=True, align="C")
# #
# #     pdf.output(os.path.join(folder, "admission_record.pdf"))
#
#
# def create_admission_pdf(data, folder):
#     logo_path = os.path.join(os.getcwd(), "gyanguru_logo.png")
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_auto_page_break(auto=True, margin=15)
#
#     # Logo (right-aligned)
#     if os.path.exists(logo_path):
#         pdf.image(logo_path, x=170, y=8, w=25)
#     pdf.set_xy(10, 10)
#     pdf.set_font("Arial", "B", 18)
#     pdf.cell(0, 15, "Gyan Guru Pvt Ltd - Admission Record", ln=True, align="C")
#     pdf.set_y(30)
#     pdf.set_font("Arial", "B", 14)
#     pdf.set_text_color(40, 40, 45)
#     pdf.cell(0, 8, "Admission Details", ln=True)
#     pdf.set_draw_color(70, 130, 180)
#     pdf.set_line_width(0.8)
#     pdf.line(10, pdf.get_y(), 200, pdf.get_y())
#     pdf.ln(6)
#
#     pdf.set_font("Arial", "", 12)
#     field_list = [
#         ('Name', data['name']),
#         ('Course', data['course']),
#         ('Roll No', data['roll_no']),
#         ('Score', data['score']),
#         ('Date of Birth', data['dob']),
#         ('Gender', data.get('gender', '')),
#         ('Mobile', data['mobile']),
#         ('Father', data['father']),
#         ('Mother', data['mother']),
#         ('Email', data['email']),
#         ('Address', data['address']),
#         ('Religion', data['religion']),
#         ('Previous Appearance', data.get('previous_appearance', '')),
#         ('Previous Roll', data.get('previous_roll', '')),
#         ('Bank Name', data['bank_name']),
#         ('Account Name', data['account_name']),
#         ('Branch', data['branch']),
#         ('IFSC', data['ifsc']),
#         ('Account Number', data['account_no'])
#     ]
#     for label, value in field_list:
#         pdf.set_font("Arial", "B", 12)
#         pdf.cell(55, 8, f"{label}:", border=0)
#         pdf.set_font("Arial", "", 12)
#         pdf.cell(0, 8, str(value), border=0, ln=True)
#
#     pdf.ln(8)
#     pdf.set_font("Arial", "B", 14)
#     pdf.cell(0, 8, "Schools Attended", ln=True)
#     pdf.set_font("Arial", "", 12)
#     school_fields = {
#         '10th School Name & Address': data['school_10'],
#         '11th School Name & Address': data['school_11'],
#         '12th School Name & Address': data['school_12']
#     }
#     for label, value in school_fields.items():
#         pdf.set_font("Arial", "B", 12)
#         pdf.cell(70, 8, f"{label}:", border=0)
#         pdf.set_font("Arial", "", 12)
#         pdf.multi_cell(0, 8, str(value))
#
#     pdf.ln(8)
#     pdf.set_font("Arial", "B", 14)
#     pdf.cell(0, 10, "Uploaded Images", ln=True)
#     for img_field in ['photo', 'signature', 'thumb']:
#         img_path = os.path.join(folder, data.get(img_field, ""))
#         if os.path.exists(img_path) and data.get(img_field):
#             pdf.set_font("Arial", "B", 12)
#             pdf.cell(0, 8, f"{img_field.replace('_',' ').title()}:", ln=True)
#             pdf.image(img_path, w=38, h=38)
#             pdf.ln(6)
#
#     pdf.ln(6)
#     pdf.set_font("Arial", "B", 14)
#     pdf.cell(0, 10, "Other Uploaded Documents:", ln=True)
#     pdf.set_font("Arial", "", 12)
#     for file in os.listdir(folder):
#         if file not in [data.get('photo'), data.get('signature'), data.get('thumb'), 'admission_record.pdf']:
#             pdf.cell(0, 8, f"- {file}", ln=True)
#
#     pdf.set_y(-25)
#     pdf.set_font("Arial", "B", 11)
#     pdf.set_text_color(70,70,70)
#     pdf.cell(0, 10, "Gyan Guru Pvt Ltd | www.gyanguru.com | +91-7795924370", ln=True, align="C")
#
#     pdf.output(os.path.join(folder, "admission_record.pdf"))
#
#
#
# @app.route('/')
# def index():
#     return render_template('form_step1.html')
#
#
# @app.route('/form/step2', methods=['POST'])
# def form_step2():
#     session['course'] = request.form['course']
#     session['roll_no'] = request.form['roll_no']
#     session['score'] = request.form['score']
#     return render_template('form_step2.html')
#
#
# @app.route('/form/step3', methods=['POST'])
# def form_step3():
#     for field in ['name', 'father', 'mother', 'dob', 'mobile', 'email', 'address', 'previous', 'prev_roll', 'religion']:
#         session[field] = request.form[field]
#     return render_template('form_step3.html')
#
#
# @app.route('/form/step4', methods=['POST'])
# def form_step4():
#     for field in ['school_10', 'school_11', 'school_12']:
#         session[field] = request.form[field]
#     return render_template('form_step4.html')
#
#
# @app.route('/submit', methods=['POST'])
# def submit():
#     for field in ['account_name', 'bank_name', 'ifsc', 'branch', 'account_no']:
#         session[field] = request.form[field]
#
#     roll_no = session.get('roll_no')
#     folder = os.path.join(app.config['UPLOAD_FOLDER'], f"NEET{roll_no}")
#     os.makedirs(folder, exist_ok=True)
#
#     # Save files
#     files = {
#         'marks_10': ('marks_10', 'pdf'),
#         'marks_12': ('marks_12', 'pdf'),
#         'scorecard': ('scorecard', 'pdf'),
#         'aadhar': ('aadhar', 'pdf'),
#         'photo': ('photo', 'img'),
#         'signature': ('signature', 'img'),
#         'thumb': ('thumb', 'img'),
#     }
#
#     saved_file_names = {'photo': "", 'signature': "", 'thumb': ""}
#
#     for field, (key, ftype) in files.items():
#         file = request.files.get(key)
#         if file and allowed_file(file.filename, ALLOWED_PDF if ftype == 'pdf' else ALLOWED_IMG):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(folder, filename))
#             if field in ['photo', 'signature', 'thumb']:
#                 saved_file_names[field] = filename
#         else:
#             return f"Invalid or missing file: {field}", 400
#
#     # Insert into DB
#     with sqlite3.connect('database.db') as conn:
#         conn.execute('''INSERT INTO students (
#             course, roll_no, score, name, father, mother, dob, mobile, email,
#             address, previous_appearance, previous_roll, religion,
#             school_10, school_11, school_12,
#             bank_name, account_name, ifsc, branch, account_no, created_at
#         ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
#                      (
#                          session['course'], session['roll_no'], session['score'], session['name'],
#                          session['father'], session['mother'], session['dob'], session['mobile'], session['email'],
#                          session['address'], session['previous'], session['prev_roll'], session['religion'],
#                          session['school_10'], session['school_11'], session['school_12'],
#                          session['bank_name'], session['account_name'], session['ifsc'], session['branch'],
#                          session['account_no'], datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#                      )
#                      )
#     # Prepare data for PDF
#     data = {
#         'course': session['course'],
#         'roll_no': session['roll_no'],
#         'score': session['score'],
#         'name': session['name'],
#         'father': session['father'],
#         'mother': session['mother'],
#         'dob': session['dob'],
#         'mobile': session['mobile'],
#         'email': session['email'],
#         'address': session['address'],
#         'previous_appearance': session['previous'],
#         'previous_roll': session['prev_roll'],
#         'religion': session['religion'],
#         'school_10': session['school_10'],
#         'school_11': session['school_11'],
#         'school_12': session['school_12'],
#         'bank_name': session['bank_name'],
#         'account_name': session['account_name'],
#         'ifsc': session['ifsc'],
#         'branch': session['branch'],
#         'account_no': session['account_no'],
#         'photo': saved_file_names['photo'],
#         'signature': saved_file_names['signature'],
#         'thumb': saved_file_names['thumb'],
#     }
#     create_admission_pdf(data, folder)
#
#     session.clear()
#     return render_template('success.html')
#
#
# @app.route('/admin', methods=['GET', 'POST'])
# def admin():
#     if request.method == 'POST':
#         if request.form['username'] == 'admin' and request.form['password'] == 'gyanguru123':
#             session['admin'] = True
#             return redirect(url_for('dashboard'))
#         else:
#             return "Invalid credentials", 403
#     return render_template('admin_login.html')
#
#
# @app.route('/dashboard')
# def dashboard():
#     if not session.get('admin'):
#         return redirect(url_for('admin'))
#     with sqlite3.connect('database.db') as conn:
#         students = conn.execute('SELECT * FROM students').fetchall()
#     return render_template('admin_dashboard.html', students=students)
#
#
# @app.route('/download_csv')
# def download_csv():
#     if not session.get('admin'):
#         return redirect(url_for('admin'))
#     with sqlite3.connect('database.db') as conn:
#         students = conn.execute('SELECT * FROM students').fetchall()
#     filepath = 'submissions.csv'
#     with open(filepath, 'w', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         headers = [description[0] for description in conn.execute('PRAGMA table_info(students)')]
#         writer.writerow(headers)
#         writer.writerows(students)
#     return send_file(filepath, as_attachment=True)
#
#
# @app.route('/logout')
# def logout():
#     session.clear()
#     return redirect(url_for('admin'))
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, request, redirect, url_for, session, send_file
# import os
# import sqlite3
# from werkzeug.utils import secure_filename
# from datetime import datetime
# import csv
# from fpdf import FPDF
#
# app = Flask(__name__)
# app.secret_key = 'supersecretkey'
# UPLOAD_FOLDER = 'uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# ALLOWED_PDF = {'pdf'}
# ALLOWED_IMG = {'jpg', 'jpeg'}
# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
#
# def init_db():
#     with sqlite3.connect('database.db') as conn:
#         conn.execute('''CREATE TABLE IF NOT EXISTS students (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             course TEXT,
#             roll_no TEXT,
#             score TEXT,
#             name TEXT,
#             father TEXT,
#             mother TEXT,
#             dob TEXT,
#             mobile TEXT,
#             email TEXT,
#             address TEXT,
#             previous_appearance TEXT,
#             previous_roll TEXT,
#             religion TEXT,
#             school_10 TEXT,
#             school_11 TEXT,
#             school_12 TEXT,
#             bank_name TEXT,
#             account_name TEXT,
#             ifsc TEXT,
#             branch TEXT,
#             account_no TEXT,
#             created_at TEXT
#         )''')
# init_db()
#
# def allowed_file(filename, allowed_set):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_set
#
# def create_admission_pdf(data, folder):
#     logo_path = os.path.join(os.getcwd(), "gyanguru_logo.png")
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_auto_page_break(auto=True, margin=15)
#     if os.path.exists(logo_path):
#         pdf.image(logo_path, x=170, y=8, w=25)
#     pdf.set_xy(10, 10)
#     pdf.set_font("Arial", "B", 18)
#     pdf.cell(0, 15, "Gyan Guru Pvt Ltd - Admission Record", ln=True, align="C")
#     pdf.set_y(30)
#     pdf.set_font("Arial", "B", 14)
#     pdf.set_text_color(40, 40, 45)
#     pdf.cell(0, 8, "Admission Details", ln=True)
#     pdf.set_draw_color(70, 130, 180)
#     pdf.set_line_width(0.8)
#     pdf.line(10, pdf.get_y(), 200, pdf.get_y())
#     pdf.ln(6)
#
#     pdf.set_font("Arial", "", 12)
#     field_list = [
#         ('Name', data['name']),
#         ('Course', data['course']),
#         ('Roll No', data['roll_no']),
#         ('Score', data['score']),
#         ('Date of Birth', data['dob']),
#         ('Gender', data.get('gender', '')),
#         ('Mobile', data['mobile']),
#         ('Father', data['father']),
#         ('Mother', data['mother']),
#         ('Email', data['email']),
#         ('Address', data['address']),
#         ('Religion', data['religion']),
#         ('Previous Appearance', data.get('previous_appearance', '')),
#         ('Previous Roll', data.get('previous_roll', '')),
#         ('Bank Name', data['bank_name']),
#         ('Account Name', data['account_name']),
#         ('Branch', data['branch']),
#         ('IFSC', data['ifsc']),
#         ('Account Number', data['account_no'])
#     ]
#     for label, value in field_list:
#         pdf.set_font("Arial", "B", 12)
#         pdf.cell(55, 8, f"{label}:", border=0)
#         pdf.set_font("Arial", "", 12)
#         pdf.cell(0, 8, str(value), border=0, ln=True)
#
#     pdf.ln(8)
#     pdf.set_font("Arial", "B", 14)
#     pdf.cell(0, 8, "Schools Attended", ln=True)
#     pdf.set_font("Arial", "", 12)
#     school_fields = {
#         '10th School Name & Address': data['school_10'],
#         '11th School Name & Address': data['school_11'],
#         '12th School Name & Address': data['school_12']
#     }
#     for label, value in school_fields.items():
#         pdf.set_font("Arial", "B", 12)
#         pdf.cell(70, 8, f"{label}:", border=0)
#         pdf.set_font("Arial", "", 12)
#         pdf.multi_cell(0, 8, str(value))
#
#     pdf.ln(8)
#     pdf.set_font("Arial", "B", 14)
#     pdf.cell(0, 10, "Uploaded Images", ln=True)
#     for img_field in ['photo', 'signature', 'thumb']:
#         img_path = os.path.join(folder, data.get(img_field, ""))
#         if os.path.exists(img_path) and data.get(img_field):
#             pdf.set_font("Arial", "B", 12)
#             pdf.cell(0, 8, f"{img_field.replace('_',' ').title()}:", ln=True)
#             pdf.image(img_path, w=38, h=38)
#             pdf.ln(6)
#
#     pdf.ln(6)
#     pdf.set_font("Arial", "B", 14)
#     pdf.cell(0, 10, "Other Uploaded Documents:", ln=True)
#     pdf.set_font("Arial", "", 12)
#     for file in os.listdir(folder):
#         if file not in [data.get('photo'), data.get('signature'), data.get('thumb'), 'admission_record.pdf']:
#             pdf.cell(0, 8, f"- {file}", ln=True)
#     pdf.set_y(-25)
#     pdf.set_font("Arial", "B", 11)
#     pdf.set_text_color(70,70,70)
#     pdf.cell(0, 10, "Gyan Guru Pvt Ltd | www.gyanguru.com | +91-XXXXXXXXXX", ln=True, align="C")
#     pdf.output(os.path.join(folder, "admission_record.pdf"))
#
# @app.route('/', methods=['GET', 'POST'])
# @app.route('/form/step1', methods=['GET', 'POST'])
# def form_step1():
#     return_step4 = request.args.get('return') == 'step4'
#     if request.method == 'POST':
#         session['course'] = request.form.get('course')
#         session['roll_no'] = request.form.get('roll_no')
#         session['score'] = request.form.get('score')
#         if return_step4:
#             return redirect(url_for('form_step4'))
#         else:
#             return redirect(url_for('form_step2'))
#     context = {k: session.get(k, '') for k in ['course', 'roll_no', 'score']}
#     return render_template('form_step1.html', **context)
#
# @app.route('/form/step2', methods=['GET', 'POST'])
# def form_step2():
#     return_step4 = request.args.get('return') == 'step4'
#     if request.method == 'POST':
#         for key in ['name', 'father', 'mother', 'dob', 'mobile', 'email', 'address', 'previous', 'prev_roll', 'religion']:
#             session[key] = request.form.get(key)
#         if return_step4:
#             return redirect(url_for('form_step4'))
#         else:
#             return redirect(url_for('form_step3'))
#     context = {key: session.get(key, '') for key in ['name', 'father', 'mother', 'dob', 'mobile', 'email', 'address', 'previous', 'prev_roll', 'religion']}
#     return render_template('form_step2.html', **context)
#
# @app.route('/form/step3', methods=['GET', 'POST'])
# def form_step3():
#     return_step4 = request.args.get('return') == 'step4'
#     if request.method == 'POST':
#         for key in ['school_10', 'school_11', 'school_12']:
#             session[key] = request.form.get(key)
#         return redirect(url_for('form_step4')) if return_step4 else redirect(url_for('form_step4'))
#     context = {key: session.get(key, '') for key in ['school_10', 'school_11', 'school_12']}
#     return render_template('form_step3.html', **context)
#
# @app.route('/form/step4', methods=['GET', 'POST'])
# def form_step4():
#     if request.method == 'POST':
#         # Accept bank fields and stay on step4 for preview/submit
#         for key in ['account_name', 'bank_name', 'ifsc', 'branch', 'account_no']:
#             session[key] = request.form.get(key)
#         return redirect(url_for('form_step4'))
#     context = {key: session.get(key, '') for key in
#              ['course', 'roll_no', 'score', 'name', 'father', 'mother', 'dob', 'mobile', 'email', 'address',
#               'previous', 'prev_roll', 'religion', 'school_10', 'school_11', 'school_12',
#               'account_name', 'bank_name', 'ifsc', 'branch', 'account_no']}
#     return render_template('form_step4.html', **context)
#
# @app.route('/submit', methods=['POST'])
# def submit():
#     for field in ['account_name', 'bank_name', 'ifsc', 'branch', 'account_no']:
#         session[field] = request.form.get(field)
#     roll_no = session.get('roll_no')
#     folder = os.path.join(app.config['UPLOAD_FOLDER'], f"NEET{roll_no}")
#     os.makedirs(folder, exist_ok=True)
#
#     files = {
#         'marks_10': ('marks_10', 'pdf'),
#         'marks_12': ('marks_12', 'pdf'),
#         'scorecard': ('scorecard', 'pdf'),
#         'aadhar': ('aadhar', 'pdf'),
#         'photo': ('photo', 'img'),
#         'signature': ('signature', 'img'),
#         'thumb': ('thumb', 'img'),
#     }
#     saved_file_names = {'photo': "", 'signature': "", 'thumb': ""}
#     for field, (key, ftype) in files.items():
#         file = request.files.get(key)
#         if file and allowed_file(file.filename, ALLOWED_PDF if ftype == 'pdf' else ALLOWED_IMG):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(folder, filename))
#             if field in ['photo', 'signature', 'thumb']:
#                 saved_file_names[field] = filename
#         else:
#             return f"Invalid or missing file: {field}", 400
#
#     with sqlite3.connect('database.db') as conn:
#         conn.execute('''INSERT INTO students (
#             course, roll_no, score, name, father, mother, dob, mobile, email,
#             address, previous_appearance, previous_roll, religion,
#             school_10, school_11, school_12,
#             bank_name, account_name, ifsc, branch, account_no, created_at
#         ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
#                      (
#                          session['course'], session['roll_no'], session['score'], session['name'],
#                          session['father'], session['mother'], session['dob'], session['mobile'], session['email'],
#                          session['address'], session['previous'], session['prev_roll'], session['religion'],
#                          session['school_10'], session['school_11'], session['school_12'],
#                          session['bank_name'], session['account_name'], session['ifsc'], session['branch'],
#                          session['account_no'], datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#                      )
#                      )
#     data = {
#         'course': session['course'],
#         'roll_no': session['roll_no'],
#         'score': session['score'],
#         'name': session['name'],
#         'father': session['father'],
#         'mother': session['mother'],
#         'dob': session['dob'],
#         'mobile': session['mobile'],
#         'email': session['email'],
#         'address': session['address'],
#         'previous_appearance': session['previous'],
#         'previous_roll': session['prev_roll'],
#         'religion': session['religion'],
#         'school_10': session['school_10'],
#         'school_11': session['school_11'],
#         'school_12': session['school_12'],
#         'bank_name': session['bank_name'],
#         'account_name': session['account_name'],
#         'ifsc': session['ifsc'],
#         'branch': session['branch'],
#         'account_no': session['account_no'],
#         'photo': saved_file_names['photo'],
#         'signature': saved_file_names['signature'],
#         'thumb': saved_file_names['thumb'],
#     }
#     create_admission_pdf(data, folder)
#     session.clear()
#     return render_template('success.html')
#
# # Admin, dashboard, CSV and logout routes unchanged
#
# @app.route('/admin', methods=['GET', 'POST'])
# def admin():
#     if request.method == 'POST':
#         if request.form['username'] == 'admin' and request.form['password'] == 'gyanguru123':
#             session['admin'] = True
#             return redirect(url_for('dashboard'))
#         else:
#             return "Invalid credentials", 403
#     return render_template('admin_login.html')
#
# @app.route('/dashboard')
# def dashboard():
#     if not session.get('admin'):
#         return redirect(url_for('admin'))
#     with sqlite3.connect('database.db') as conn:
#         students = conn.execute('SELECT * FROM students').fetchall()
#     return render_template('admin_dashboard.html', students=students)
#
# @app.route('/download_csv')
# def download_csv():
#     if not session.get('admin'):
#         return redirect(url_for('admin'))
#     with sqlite3.connect('database.db') as conn:
#         students = conn.execute('SELECT * FROM students').fetchall()
#     filepath = 'submissions.csv'
#     with open(filepath, 'w', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         headers = [description[0] for description in conn.execute('PRAGMA table_info(students)')]
#         writer.writerow(headers)
#         writer.writerows(students)
#     return send_file(filepath, as_attachment=True)
#
# @app.route('/logout')
# def logout():
#     session.clear()
#     return redirect(url_for('admin'))
#
# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, request, redirect, url_for, session, send_file
# import os
# import sqlite3
# from werkzeug.utils import secure_filename
# from datetime import datetime
# import csv
# from fpdf import FPDF
#
# app = Flask(__name__)
# app.secret_key = 'supersecretkey'
# UPLOAD_FOLDER = 'uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# ALLOWED_PDF = {'pdf'}
# ALLOWED_IMG = {'jpg', 'jpeg'}
# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
#
# def init_db():
#     with sqlite3.connect('database.db') as conn:
#         conn.execute('''CREATE TABLE IF NOT EXISTS students (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             course TEXT,
#             roll_no TEXT,
#             score TEXT,
#             name TEXT,
#             father TEXT,
#             mother TEXT,
#             dob TEXT,
#             mobile TEXT,
#             email TEXT,
#             address TEXT,
#             previous_appearance TEXT,
#             previous_roll TEXT,
#             religion TEXT,
#             school_10 TEXT,
#             school_11 TEXT,
#             school_12 TEXT,
#             bank_name TEXT,
#             account_name TEXT,
#             ifsc TEXT,
#             branch TEXT,
#             account_no TEXT,
#             created_at TEXT
#         )''')
# init_db()
#
# def allowed_file(filename, allowed_set):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_set
#
# def create_admission_pdf(data, folder):
#     logo_path = os.path.join(os.getcwd(), "gyanguru_logo.png")
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_auto_page_break(auto=True, margin=15)
#     if os.path.exists(logo_path):
#         pdf.image(logo_path, x=170, y=8, w=25)
#     pdf.set_xy(10, 10)
#     pdf.set_font("Arial", "B", 18)
#     pdf.cell(0, 15, "Gyan Guru Pvt Ltd - Admission Record", ln=True, align="C")
#     pdf.set_y(30)
#     pdf.set_font("Arial", "B", 14)
#     pdf.set_text_color(40, 40, 45)
#     pdf.cell(0, 8, "Admission Details", ln=True)
#     pdf.set_draw_color(70, 130, 180)
#     pdf.set_line_width(0.8)
#     pdf.line(10, pdf.get_y(), 200, pdf.get_y())
#     pdf.ln(6)
#
#     pdf.set_font("Arial", "", 12)
#     field_list = [
#         ('Name', data['name']),
#         ('Course', data['course']),
#         ('Roll No', data['roll_no']),
#         ('Score', data['score']),
#         ('Date of Birth', data['dob']),
#         ('Gender', data.get('gender', '')),
#         ('Mobile', data['mobile']),
#         ('Father', data['father']),
#         ('Mother', data['mother']),
#         ('Email', data['email']),
#         ('Address', data['address']),
#         ('Religion', data['religion']),
#         ('Previous Appearance', data.get('previous_appearance', '')),
#         ('Previous Roll', data.get('previous_roll', '')),
#         ('Bank Name', data['bank_name']),
#         ('Account Name', data['account_name']),
#         ('Branch', data['branch']),
#         ('IFSC', data['ifsc']),
#         ('Account Number', data['account_no'])
#     ]
#     for label, value in field_list:
#         pdf.set_font("Arial", "B", 12)
#         pdf.cell(55, 8, f"{label}:", border=0)
#         pdf.set_font("Arial", "", 12)
#         pdf.cell(0, 8, str(value), border=0, ln=True)
#
#     pdf.ln(8)
#     pdf.set_font("Arial", "B", 14)
#     pdf.cell(0, 8, "Schools Attended", ln=True)
#     pdf.set_font("Arial", "", 12)
#     school_fields = {
#         '10th School Name & Address': data['school_10'],
#         '11th School Name & Address': data['school_11'],
#         '12th School Name & Address': data['school_12']
#     }
#     for label, value in school_fields.items():
#         pdf.set_font("Arial", "B", 12)
#         pdf.cell(70, 8, f"{label}:", border=0)
#         pdf.set_font("Arial", "", 12)
#         pdf.multi_cell(0, 8, str(value))
#
#     pdf.ln(8)
#     pdf.set_font("Arial", "B", 14)
#     pdf.cell(0, 10, "Uploaded Images", ln=True)
#     for img_field in ['photo', 'signature', 'thumb']:
#         img_path = os.path.join(folder, data.get(img_field, ""))
#         if os.path.exists(img_path) and data.get(img_field):
#             pdf.set_font("Arial", "B", 12)
#             pdf.cell(0, 8, f"{img_field.replace('_',' ').title()}:", ln=True)
#             pdf.image(img_path, w=38, h=38)
#             pdf.ln(6)
#
#     pdf.ln(6)
#     pdf.set_font("Arial", "B", 14)
#     pdf.cell(0, 10, "Other Uploaded Documents:", ln=True)
#     pdf.set_font("Arial", "", 12)
#     for file in os.listdir(folder):
#         if file not in [data.get('photo'), data.get('signature'), data.get('thumb'), 'admission_record.pdf']:
#             pdf.cell(0, 8, f"- {file}", ln=True)
#     pdf.set_y(-25)
#     pdf.set_font("Arial", "B", 11)
#     pdf.set_text_color(70,70,70)
#     pdf.cell(0, 10, "Gyan Guru Pvt Ltd | www.gyanguru.com | +91-XXXXXXXXXX", ln=True, align="C")
#     pdf.output(os.path.join(folder, "admission_record.pdf"))
#
# @app.route('/', methods=['GET', 'POST'])
# @app.route('/form/step1', methods=['GET', 'POST'])
# def form_step1():
#     return_step4 = request.args.get('return') == 'step4'
#     if request.method == 'POST':
#         session['course'] = request.form.get('course')
#         session['roll_no'] = request.form.get('roll_no')
#         session['score'] = request.form.get('score')
#         if return_step4:
#             return redirect(url_for('form_step4'))
#         else:
#             return redirect(url_for('form_step2'))
#     context = {k: session.get(k, '') for k in ['course', 'roll_no', 'score']}
#     return render_template('form_step1.html', **context)
#
# @app.route('/form/step2', methods=['GET', 'POST'])
# def form_step2():
#     return_step4 = request.args.get('return') == 'step4'
#     if request.method == 'POST':
#         for key in ['name', 'father', 'mother', 'dob', 'mobile', 'email', 'address', 'previous', 'prev_roll', 'religion']:
#             session[key] = request.form.get(key)
#         if return_step4:
#             return redirect(url_for('form_step4'))
#         else:
#             return redirect(url_for('form_step3'))
#     context = {key: session.get(key, '') for key in ['name', 'father', 'mother', 'dob', 'mobile', 'email', 'address', 'previous', 'prev_roll', 'religion']}
#     return render_template('form_step2.html', **context)
#
# @app.route('/form/step3', methods=['GET', 'POST'])
# def form_step3():
#     return_step4 = request.args.get('return') == 'step4'
#     if request.method == 'POST':
#         for key in ['school_10', 'school_11', 'school_12']:
#             session[key] = request.form.get(key)
#         return redirect(url_for('form_step4')) if return_step4 else redirect(url_for('form_step4'))
#     context = {key: session.get(key, '') for key in ['school_10', 'school_11', 'school_12']}
#     return render_template('form_step3.html', **context)
#
# @app.route('/form/step4', methods=['GET', 'POST'])
# def form_step4():
#     show_preview = False
#     if request.method == 'POST':
#         # Save all bank/account fields always!
#         for key in ['account_name', 'bank_name', 'ifsc', 'branch', 'account_no']:
#             session[key] = request.form.get(key)
#         action = request.form.get("action", "")
#         if action == "preview":
#             show_preview = True
#         # Do not submit here, only preview or stay on page
#     context = {key: session.get(key, '') for key in
#         ['course', 'roll_no', 'score', 'name', 'father', 'mother', 'dob', 'mobile', 'email', 'address',
#         'previous', 'prev_roll', 'religion', 'school_10', 'school_11', 'school_12',
#         'account_name', 'bank_name', 'ifsc', 'branch', 'account_no']}
#     context["show_preview"] = show_preview
#     return render_template('form_step4.html', **context)
#
# @app.route('/submit', methods=['POST'])
# def submit():
#     for field in ['account_name', 'bank_name', 'ifsc', 'branch', 'account_no']:
#         session[field] = request.form.get(field)
#     roll_no = session.get('roll_no')
#     folder = os.path.join(app.config['UPLOAD_FOLDER'], f"NEET{roll_no}")
#     os.makedirs(folder, exist_ok=True)
#     files = {
#         'marks_10': ('marks_10', 'pdf'),
#         'marks_12': ('marks_12', 'pdf'),
#         'scorecard': ('scorecard', 'pdf'),
#         'aadhar': ('aadhar', 'pdf'),
#         'photo': ('photo', 'img'),
#         'signature': ('signature', 'img'),
#         'thumb': ('thumb', 'img'),
#     }
#     saved_file_names = {'photo': "", 'signature': "", 'thumb': ""}
#     for field, (key, ftype) in files.items():
#         file = request.files.get(key)
#         if file and allowed_file(file.filename, ALLOWED_PDF if ftype == 'pdf' else ALLOWED_IMG):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(folder, filename))
#             if field in ['photo', 'signature', 'thumb']:
#                 saved_file_names[field] = filename
#         else:
#             return f"Invalid or missing file: {field}", 400
#     with sqlite3.connect('database.db') as conn:
#         conn.execute('''INSERT INTO students (
#             course, roll_no, score, name, father, mother, dob, mobile, email,
#             address, previous_appearance, previous_roll, religion,
#             school_10, school_11, school_12,
#             bank_name, account_name, ifsc, branch, account_no, created_at
#         ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
#                      (
#                          session['course'], session['roll_no'], session['score'], session['name'],
#                          session['father'], session['mother'], session['dob'], session['mobile'], session['email'],
#                          session['address'], session['previous'], session['prev_roll'], session['religion'],
#                          session['school_10'], session['school_11'], session['school_12'],
#                          session['bank_name'], session['account_name'], session['ifsc'], session['branch'],
#                          session['account_no'], datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#                      )
#                      )
#     data = {
#         'course': session['course'],
#         'roll_no': session['roll_no'],
#         'score': session['score'],
#         'name': session['name'],
#         'father': session['father'],
#         'mother': session['mother'],
#         'dob': session['dob'],
#         'mobile': session['mobile'],
#         'email': session['email'],
#         'address': session['address'],
#         'previous_appearance': session['previous'],
#         'previous_roll': session['prev_roll'],
#         'religion': session['religion'],
#         'school_10': session['school_10'],
#         'school_11': session['school_11'],
#         'school_12': session['school_12'],
#         'bank_name': session['bank_name'],
#         'account_name': session['account_name'],
#         'ifsc': session['ifsc'],
#         'branch': session['branch'],
#         'account_no': session['account_no'],
#         'photo': saved_file_names['photo'],
#         'signature': saved_file_names['signature'],
#         'thumb': saved_file_names['thumb'],
#     }
#     create_admission_pdf(data, folder)
#     session.clear()
#     return render_template('success.html')
#
# @app.route('/admin', methods=['GET', 'POST'])
# def admin():
#     if request.method == 'POST':
#         if request.form['username'] == 'admin' and request.form['password'] == 'gyanguru123':
#             session['admin'] = True
#             return redirect(url_for('dashboard'))
#         else:
#             return "Invalid credentials", 403
#     return render_template('admin_login.html')
#
# @app.route('/dashboard')
# def dashboard():
#     if not session.get('admin'):
#         return redirect(url_for('admin'))
#     with sqlite3.connect('database.db') as conn:
#         students = conn.execute('SELECT * FROM students').fetchall()
#     return render_template('admin_dashboard.html', students=students)
#
# # @app.route('/download_csv')
# # def download_csv():
# #     if not session.get('admin'):
# #         return redirect(url_for('admin'))
# #     with sqlite3.connect('database.db') as conn:
# #         students = conn.execute('SELECT * FROM students').fetchall()
# #     filepath = 'submissions.csv'
# #     with open(filepath, 'w', newline='') as csvfile:
# #         writer = csv.writer(csvfile)
# #         headers = [description[0] for description in conn.execute('PRAGMA table_info(students)')]
# #         writer.writerow(headers)
# #         writer.writerows(students)
# #     return send_file(filepath, as_attachment=True)
#
# @app.route('/download_csv')
# def download_csv():
#     if not session.get('admin'):
#         return redirect(url_for('admin'))
#     with sqlite3.connect('database.db') as conn:
#         students = conn.execute('SELECT * FROM students').fetchall()
#         # List of column names, in same order as your table definition
#         fieldnames = [
#             "id", "course", "roll_no", "score", "name", "father", "mother", "dob", "mobile", "email", "address",
#             "previous_appearance", "previous_roll", "religion",
#             "school_10", "school_11", "school_12",
#             "bank_name", "account_name", "ifsc", "branch", "account_no", "created_at"
#         ]
#     filepath = 'submissions.csv'
#     with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(fieldnames)      # <<< writes the header row
#         writer.writerows(students)       # writes all student rows
#     return send_file(filepath, as_attachment=True)
#
#
# @app.route('/logout')
# def logout():
#     session.clear()
#     return redirect(url_for('admin'))
#
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, session, send_file, jsonify
import os
import sqlite3
from werkzeug.utils import secure_filename
from datetime import datetime
import csv
from fpdf import FPDF
import uuid
import shutil

app = Flask(__name__)
app.secret_key = 'supersecretkey'
UPLOAD_FOLDER = 'uploads'
TEMP_UPLOAD_FOLDER = 'temp_uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['TEMP_UPLOAD_FOLDER'] = TEMP_UPLOAD_FOLDER

ALLOWED_PDF = {'pdf'}
ALLOWED_IMG = {'jpg', 'jpeg'}
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['TEMP_UPLOAD_FOLDER'], exist_ok=True)

def init_db():
    with sqlite3.connect('database.db') as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course TEXT,
            roll_no TEXT,
            score TEXT,
            name TEXT,
            father TEXT,
            mother TEXT,
            dob TEXT,
            mobile TEXT,
            email TEXT,
            address TEXT,
            previous_appearance TEXT,
            previous_roll TEXT,
            religion TEXT,
            school_10 TEXT,
            school_11 TEXT,
            school_12 TEXT,
            bank_name TEXT,
            account_name TEXT,
            ifsc TEXT,
            branch TEXT,
            account_no TEXT,
            created_at TEXT
        )''')
init_db()

def allowed_file(filename, allowed_set):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_set

def get_temp_dir():
    roll_no = session.get('roll_no', session.get('session_id'))
    if not roll_no:
        # create unique session id for anonymous temp uploads
        s_id = str(uuid.uuid4())
        session['session_id'] = s_id
        roll_no = s_id
    temp_dir = os.path.join(app.config['TEMP_UPLOAD_FOLDER'], f"NEET{roll_no}")
    os.makedirs(temp_dir, exist_ok=True)
    return temp_dir

@app.route('/upload_temp_file', methods=['POST'])
def upload_temp_file():
    # Handles single file AJAX upload per field
    key = request.form['field']
    file = request.files.get('file')
    if not file or not key:
        return jsonify({"error": "Missing upload"}), 400
    ext = file.filename.rsplit('.', 1)[-1].lower()
    if key in ['marks_10', 'marks_12', 'scorecard', 'aadhar']:
        if ext not in ALLOWED_PDF:
            return jsonify({"error": "Wrong file type"}), 400
    else:
        if ext not in ALLOWED_IMG:
            return jsonify({"error": "Wrong file type"}), 400
    temp_dir = get_temp_dir()
    filename = secure_filename(f"{key}_{uuid.uuid4().hex}.{ext}")
    file.save(os.path.join(temp_dir, filename))
    # track in session
    temp_files = session.get('temp_files', {})
    temp_files[key] = filename
    session['temp_files'] = temp_files
    session.modified = True
    return jsonify({"filename": filename})

def create_admission_pdf(data, folder):
    logo_path = os.path.join(os.getcwd(), "gyanguru_logo.png")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    if os.path.exists(logo_path):
        pdf.image(logo_path, x=170, y=8, w=25)
    pdf.set_xy(10, 10)
    pdf.set_font("Arial", "B", 18)
    pdf.cell(0, 15, "Gyan Guru Pvt Ltd - Admission Record", ln=True, align="C")
    pdf.set_y(30)
    pdf.set_font("Arial", "B", 14)
    pdf.set_text_color(40, 40, 45)
    pdf.cell(0, 8, "Admission Details", ln=True)
    pdf.set_draw_color(70, 130, 180)
    pdf.set_line_width(0.8)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(6)

    pdf.set_font("Arial", "", 12)
    field_list = [
        ('Name', data['name']),
        ('Course', data['course']),
        ('Roll No', data['roll_no']),
        ('Score', data['score']),
        ('Date of Birth', data['dob']),
        ('Gender', data.get('gender', '')),
        ('Mobile', data['mobile']),
        ('Father', data['father']),
        ('Mother', data['mother']),
        ('Email', data['email']),
        ('Address', data['address']),
        ('Religion', data['religion']),
        ('Previous Appearance', data.get('previous_appearance', '')),
        ('Previous Roll', data.get('previous_roll', '')),
        ('Bank Name', data['bank_name']),
        ('Account Name', data['account_name']),
        ('Branch', data['branch']),
        ('IFSC', data['ifsc']),
        ('Account Number', data['account_no'])
    ]
    for label, value in field_list:
        pdf.set_font("Arial", "B", 12)
        pdf.cell(55, 8, f"{label}:", border=0)
        pdf.set_font("Arial", "", 12)
        pdf.cell(0, 8, str(value), border=0, ln=True)

    pdf.ln(8)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 8, "Schools Attended", ln=True)
    pdf.set_font("Arial", "", 12)
    school_fields = {
        '10th School Name & Address': data['school_10'],
        '11th School Name & Address': data['school_11'],
        '12th School Name & Address': data['school_12']
    }
    for label, value in school_fields.items():
        pdf.set_font("Arial", "B", 12)
        pdf.cell(70, 8, f"{label}:", border=0)
        pdf.set_font("Arial", "", 12)
        pdf.multi_cell(0, 8, str(value))

    pdf.ln(8)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Uploaded Images", ln=True)
    for img_field in ['photo', 'signature', 'thumb']:
        img_path = os.path.join(folder, data.get(img_field, ""))
        if os.path.exists(img_path) and data.get(img_field):
            pdf.set_font("Arial", "B", 12)
            pdf.cell(0, 8, f"{img_field.replace('_',' ').title()}:", ln=True)
            pdf.image(img_path, w=38, h=38)
            pdf.ln(6)

    pdf.ln(6)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Other Uploaded Documents:", ln=True)
    pdf.set_font("Arial", "", 12)
    for file in os.listdir(folder):
        if file not in [data.get('photo'), data.get('signature'), data.get('thumb'), 'admission_record.pdf']:
            pdf.cell(0, 8, f"- {file}", ln=True)
    pdf.set_y(-25)
    pdf.set_font("Arial", "B", 11)
    pdf.set_text_color(70,70,70)
    pdf.cell(0, 10, "Gyan Guru Pvt Ltd | www.gyanguru.com | +91-XXXXXXXXXX", ln=True, align="C")
    pdf.output(os.path.join(folder, "admission_record.pdf"))

@app.route('/', methods=['GET', 'POST'])
@app.route('/form/step1', methods=['GET', 'POST'])
def form_step1():
    return_step4 = request.args.get('return') == 'step4'
    if request.method == 'POST':
        session['course'] = request.form.get('course')
        session['roll_no'] = request.form.get('roll_no')
        session['score'] = request.form.get('score')
        if return_step4:
            return redirect(url_for('form_step4'))
        else:
            return redirect(url_for('form_step2'))
    context = {k: session.get(k, '') for k in ['course', 'roll_no', 'score']}
    return render_template('form_step1.html', **context)

@app.route('/form/step2', methods=['GET', 'POST'])
def form_step2():
    return_step4 = request.args.get('return') == 'step4'
    if request.method == 'POST':
        for key in ['name', 'father', 'mother', 'dob', 'mobile', 'email', 'address', 'previous', 'prev_roll', 'religion']:
            session[key] = request.form.get(key)
        if return_step4:
            return redirect(url_for('form_step4'))
        else:
            return redirect(url_for('form_step3'))
    context = {key: session.get(key, '') for key in ['name', 'father', 'mother', 'dob', 'mobile', 'email', 'address', 'previous', 'prev_roll', 'religion']}
    return render_template('form_step2.html', **context)

@app.route('/form/step3', methods=['GET', 'POST'])
def form_step3():
    return_step4 = request.args.get('return') == 'step4'
    if request.method == 'POST':
        for key in ['school_10', 'school_11', 'school_12']:
            session[key] = request.form.get(key)
        return redirect(url_for('form_step4')) if return_step4 else redirect(url_for('form_step4'))
    context = {key: session.get(key, '') for key in ['school_10', 'school_11', 'school_12']}
    return render_template('form_step3.html', **context)

@app.route('/form/step4', methods=['GET', 'POST'])
def form_step4():
    show_preview = False
    if 'temp_files' not in session:
        session['temp_files'] = {}
    if request.method == 'POST':
        # Save all bank/account fields always!
        for key in ['account_name', 'bank_name', 'ifsc', 'branch', 'account_no']:
            session[key] = request.form.get(key)
        action = request.form.get("action", "")
        if action == "preview":
            show_preview = True
    # File fields: send in context if temp_files exists for the user
    context = {key: session.get(key, '') for key in
        ['course', 'roll_no', 'score', 'name', 'father', 'mother', 'dob', 'mobile', 'email', 'address',
        'previous', 'prev_roll', 'religion', 'school_10', 'school_11', 'school_12',
        'account_name', 'bank_name', 'ifsc', 'branch', 'account_no']}
    context["show_preview"] = show_preview
    context["temp_files"] = session.get('temp_files', {})
    return render_template('form_step4.html', **context)

@app.route('/submit', methods=['POST'])
def submit():
    for field in ['account_name', 'bank_name', 'ifsc', 'branch', 'account_no']:
        session[field] = request.form.get(field)
    roll_no = session.get('roll_no')
    folder = os.path.join(app.config['UPLOAD_FOLDER'], f"NEET{roll_no}")
    os.makedirs(folder, exist_ok=True)
    temp_files = session.get('temp_files', {})
    temp_dir = get_temp_dir()

    # List of files (draft names) to pick up from temp to permanent
    files = {
        'marks_10': ('marks_10', 'pdf'),
        'marks_12': ('marks_12', 'pdf'),
        'scorecard': ('scorecard', 'pdf'),
        'aadhar': ('aadhar', 'pdf'),
        'photo': ('photo', 'img'),
        'signature': ('signature', 'img'),
        'thumb': ('thumb', 'img'),
    }
    saved_file_names = {'photo': "", 'signature': "", 'thumb': ""}

    for field, (key, ftype) in files.items():
        if field not in temp_files:
            return f"Missing file upload: {field}", 400
        temp_path = os.path.join(temp_dir, temp_files[field])
        if not os.path.exists(temp_path):
            return f"File not found: {temp_files[field]}", 400
        ext = temp_files[field].rsplit('.', 1)[-1]
        final_name = secure_filename(f"{field}.{ext}")
        shutil.copy(temp_path, os.path.join(folder, final_name))
        if field in ['photo', 'signature', 'thumb']:
            saved_file_names[field] = final_name

    with sqlite3.connect('database.db') as conn:
        conn.execute('''INSERT INTO students (
            course, roll_no, score, name, father, mother, dob, mobile, email,
            address, previous_appearance, previous_roll, religion,
            school_10, school_11, school_12,
            bank_name, account_name, ifsc, branch, account_no, created_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                     (
                         session['course'], session['roll_no'], session['score'], session['name'],
                         session['father'], session['mother'], session['dob'], session['mobile'], session['email'],
                         session['address'], session['previous'], session['prev_roll'], session['religion'],
                         session['school_10'], session['school_11'], session['school_12'],
                         session['bank_name'], session['account_name'], session['ifsc'], session['branch'],
                         session['account_no'], datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                     )
                     )
    data = {
        'course': session['course'],
        'roll_no': session['roll_no'],
        'score': session['score'],
        'name': session['name'],
        'father': session['father'],
        'mother': session['mother'],
        'dob': session['dob'],
        'mobile': session['mobile'],
        'email': session['email'],
        'address': session['address'],
        'previous_appearance': session['previous'],
        'previous_roll': session['prev_roll'],
        'religion': session['religion'],
        'school_10': session['school_10'],
        'school_11': session['school_11'],
        'school_12': session['school_12'],
        'bank_name': session['bank_name'],
        'account_name': session['account_name'],
        'ifsc': session['ifsc'],
        'branch': session['branch'],
        'account_no': session['account_no'],
        'photo': saved_file_names['photo'],
        'signature': saved_file_names['signature'],
        'thumb': saved_file_names['thumb'],
    }
    create_admission_pdf(data, folder)
    # Optionally: remove temp uploads directory
    shutil.rmtree(temp_dir, ignore_errors=True)
    session.pop('temp_files', None)
    session.pop('session_id', None)
    session.clear()
    return render_template('success.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'gyanguru123':
            session['admin'] = True
            return redirect(url_for('dashboard'))
        else:
            return "Invalid credentials", 403
    return render_template('admin_login.html')

@app.route('/dashboard')
def dashboard():
    if not session.get('admin'):
        return redirect(url_for('admin'))
    with sqlite3.connect('database.db') as conn:
        students = conn.execute('SELECT * FROM students').fetchall()
    return render_template('admin_dashboard.html', students=students)

@app.route('/download_csv')
def download_csv():
    if not session.get('admin'):
        return redirect(url_for('admin'))
    with sqlite3.connect('database.db') as conn:
        students = conn.execute('SELECT * FROM students').fetchall()
        fieldnames = [
            "id", "course", "roll_no", "score", "name", "father", "mother", "dob", "mobile", "email", "address",
            "previous_appearance", "previous_roll", "religion",
            "school_10", "school_11", "school_12",
            "bank_name", "account_name", "ifsc", "branch", "account_no", "created_at"
        ]
    filepath = 'submissions.csv'
    with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)
        writer.writerows(students)
    return send_file(filepath, as_attachment=True)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)
