from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

from flask_cors import CORS, cross_origin

app = Flask(__name__)
api = Api(app)
cors = CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teachers_db.db'
db = SQLAlchemy(app)

class Teachers(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	full_name = db.Column(db.String(100), nullable=False)
	content_subject = db.Column(db.String(100), nullable=False)
	eligibility = db.Column(db.String(100), nullable=False)
	clg_street_name = db.Column(db.String(100), nullable=False)
	clg_state = db.Column(db.String(20), nullable=False)
	clg_city = db.Column(db.String(15), nullable=False)
	clg_contry = db.Column(db.String(10), nullable=False)
	clg_zip_code = db.Column(db.String(10), nullable=False)
	clg_code = db.Column(db.String(15), nullable=False)
	emp_street_name = db.Column(db.String(100), nullable=False)
	emp_state = db.Column(db.String(20), nullable=False)
	emp_city = db.Column(db.String(15), nullable=False)
	emp_contry = db.Column(db.String(15), nullable=False)
	emp_zip_code = db.Column(db.String(10), nullable=False)
	emp_contact = db.Column(db.String(10), nullable=False)
	emp_alt_contact = db.Column(db.String(10), nullable=False)
	issue_date = db.Column(db.String(15), nullable=False)
	joining_date = db.Column(db.String(10), nullable=False)
	fee = db.Column(db.String(10), nullable=False)
	transact_date = db.Column(db.String(10), nullable=False)
	reciept_num = db.Column(db.String(10), nullable=False)
	blood_grp = db.Column(db.String(10), nullable=False)

	def __repr__(self):
		return f"Teacher(full_name={full_name},content_subject={content_subject},eligibility={eligibility},clg_street_name={clg_street_name},clg_state={clg_state},clg_city={clg_city},clg_contry={clg_contry},clg_zip_code={clg_zip_code},clg_code={clg_code},emp_street_name={emp_street_name},emp_state={emp_state},emp_city={emp_city},emp_contry={emp_contry},emp_zip_code={emp_zip_code},emp_contact={emp_contact},emp_alt_contact={emp_alt_contact},issue_date={issue_date},joining_date={joining_date},fee={fee},transact_date={transact_date},reciept_num={reciept_num},blood_grp={blood_grp})"

class Admins(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	full_name = db.Column(db.String(100), nullable=False)
	email_id = db.Column(db.String(20), nullable=False)
	password = db.Column(db.String(150), nullable=False)

	def __repr__(self):
		return "AdminLog(full_name={name},email_id={email_id},password={password})"


with app.app_context(): # run this on first time only to create all the tables coded before this line.
    db.create_all() # db.fetch and other things have to check !! to check the tables

teacher_post_args = reqparse.RequestParser()
teacher_post_args.add_argument("full_name", type=str, help="Name is required", required=True)
teacher_post_args.add_argument("content_subject", type=str, help="Content/Subject is required", required=True)
teacher_post_args.add_argument("eligibility", type=str, help="Eligibility is required", required=True)
teacher_post_args.add_argument("clg_street_name", type=str, help="College street name is required", required=True)
teacher_post_args.add_argument("clg_state", type=str, help="College state is required", required=True)
teacher_post_args.add_argument("clg_city", type=str, help="College city is required", required=True)
teacher_post_args.add_argument("clg_contry", type=str, help="College contry is required", required=True)
teacher_post_args.add_argument("clg_zip_code", type=str, help="College ZIP code is required", required=True)
teacher_post_args.add_argument("clg_code", type=str, help="College code is required", required=True)
teacher_post_args.add_argument("emp_street_name", type=str, help="Employee street name is required", required=True)
teacher_post_args.add_argument("emp_state", type=str, help="Employee state is required", required=True)
teacher_post_args.add_argument("emp_city", type=str, help="Employee city is required", required=True)
teacher_post_args.add_argument("emp_contry", type=str, help="Employee contry is required", required=True)
teacher_post_args.add_argument("emp_zip_code", type=str, help="Employee ZIP code is required", required=True)
teacher_post_args.add_argument("emp_contact", type=str, help="Employee contact number is required", required=True)
teacher_post_args.add_argument("emp_alt_contact", type=str, help="Employee alternate contact number is required", required=True)
teacher_post_args.add_argument("issue_date", type=str, help="Issue date is required", required=True)
teacher_post_args.add_argument("joining_date", type=str, help="Joining date is required", required=True)
teacher_post_args.add_argument("fee", type=str, help="Fee details are required", required=True)
teacher_post_args.add_argument("transact_date", type=str, help="Transaction date is required", required=True)
teacher_post_args.add_argument("reciept_num", type=str, help="Reciept number is required", required=True)
teacher_post_args.add_argument("blood_grp", type=str, help="Blood group is required", required=True)

teacher_put_args = reqparse.RequestParser()
teacher_put_args.add_argument("full_name", type=str, help="Name is required")
teacher_put_args.add_argument("content_subject", type=str, help="Content/Subject is required")
teacher_put_args.add_argument("eligibility", type=str, help="Eligibility is required")
teacher_put_args.add_argument("clg_street_name", type=str, help="College street name is required")
teacher_put_args.add_argument("clg_state", type=str, help="College state is required")
teacher_put_args.add_argument("clg_city", type=str, help="College city is required")
teacher_put_args.add_argument("clg_contry", type=str, help="College contry is required")
teacher_put_args.add_argument("clg_zip_code", type=str, help="College ZIP code is required")
teacher_put_args.add_argument("clg_code", type=str, help="College code is required")
teacher_put_args.add_argument("emp_street_name", type=str, help="Employee street name is required")
teacher_put_args.add_argument("emp_state", type=str, help="Employee state is required")
teacher_put_args.add_argument("emp_city", type=str, help="Employee city is required")
teacher_put_args.add_argument("emp_contry", type=str, help="Employee contry is required")
teacher_put_args.add_argument("emp_zip_code", type=str, help="Employee ZIP code is required")
teacher_put_args.add_argument("emp_alt_contact", type=str, help="Employee alternate contact number is required")
teacher_put_args.add_argument("issue_date", type=str, help="Issue date is required")
teacher_put_args.add_argument("joining_date", type=str, help="Joining date is required")
teacher_put_args.add_argument("fee", type=str, help="Fee details are required")
teacher_put_args.add_argument("transact_date", type=str, help="Transaction date is required")
teacher_put_args.add_argument("reciept_num", type=str, help="Reciept number is required")
teacher_put_args.add_argument("blood_grp", type=str, help="Blood group is required")

admin_post_args = reqparse.RequestParser()
admin_post_args.add_argument("email_id", type=str, help="Email Id is required", required=True)
admin_post_args.add_argument("password", type=str, help="Password is required", required=True)

admin_put_args = reqparse.RequestParser()
admin_put_args.add_argument("full_name", type=str, help="Name is required", required=True)
admin_put_args.add_argument("email_id", type=str, help="Email Id is required", required=True)
admin_put_args.add_argument("password", type=str, help="Password is required", required=True)

resource_fields = {
	'full_name': fields.String,
	'content_subject': fields.String,
	'eligibility': fields.String,
	'clg_street_name': fields.String,
	'clg_state': fields.String,
	'clg_city': fields.String,
	'clg_contry': fields.String,
	'clg_zip_code': fields.String,
	'clg_code': fields.String,
	'emp_street_name': fields.String,
	'emp_state': fields.String,
	'emp_city': fields.String,
	'emp_contry': fields.String,
	'emp_zip_code': fields.String,
	'emp_contact': fields.String,
	'emp_alt_contact': fields.String,
	'issue_date': fields.String,
	'joining_date': fields.String,
	'fee': fields.String,
	'transact_date': fields.String,
	'reciept_num': fields.String,
	'blood_grp': fields.String
}

log_in_fields = {
	'full_name': fields.String,
	'email_id': fields.String,
	'password': fields.String
}

class Teacher(Resource):
	@marshal_with(resource_fields)
	def get(self, emp_contact):
		result = Teachers.query.filter_by(emp_contact=emp_contact).first()
		if not result:
			abort(404, message="Could not find the MEMBER")

		return result

	@marshal_with(resource_fields)
	def post(self, emp_contact):
		args = teacher_post_args.parse_args()
		result = Teachers.query.filter_by(emp_contact=emp_contact).first()
		if result:
			abort(409, message="Employee is already registered.")

		teacher = Teachers(full_name=args['full_name'],content_subject=args['content_subject'],eligibility=args['eligibility'],clg_street_name=args['clg_street_name'],clg_state=args['clg_state'],clg_city=args['clg_city'],clg_contry=args['clg_contry'],clg_zip_code=args['clg_zip_code'],clg_code=args['clg_code'],emp_street_name=args['emp_street_name'],emp_state=args['emp_state'],emp_city=args['emp_city'],emp_contry=args['emp_contry'],emp_zip_code=args['emp_zip_code'],emp_contact=emp_contact,emp_alt_contact=args['emp_alt_contact'],issue_date=args['issue_date'],joining_date=args['joining_date'],fee=args['fee'],transact_date=args['transact_date'],reciept_num=args['reciept_num'],blood_grp=args['blood_grp'])
		db.session.add(teacher)
		db.session.commit()
		return teacher, 201

class Admin(Resource):

	@marshal_with(resource_fields)
	def get(self,emp_contact):
		if emp_contact:
			result = Teachers.query.filter_by(emp_contact=emp_contact).first()
		else:
			result = Teachers.query.all()

		if not result:
			abort(404, message="can't fetch the Datails.")
		
		return result
	
	@marshal_with(resource_fields)
	def put(self,emp_contact):
		args = teacher_put_args.parse_args()
		result = Teachers.query.filter_by(emp_contact=emp_contact).first()
		if not result:
			abort(404, message="Member doesn't exist, cannot update")
		
		if args['full_name']:
			result.full_name = args['full_name']
		if args['content_subject']:
			result.content_subject = args['content_subject']
		if args['clg_street_name']:
			result.clg_street_name = args['clg_street_name']
		if args['clg_state']:
			result.clg_state = args['clg_state']
		if args['clg_city']:
			result.clg_city = args['clg_city']
		if args['clg_contry']:
			result.clg_contry = args['clg_contry']
		if args['clg_zip_code']:
			result.clg_zip_code = args['clg_zip_code']
		if args['clg_code']:
			result.clg_code = args['clg_code']
		if args['emp_street_name']:
			result.emp_street_name = args['emp_street_name']
		if args['emp_state']:
			result.emp_state = args['emp_state']
		if args['emp_city']:
			result.emp_city = args['emp_city']
		if args['emp_contry']:
			result.emp_contry = args['emp_contry']
		if args['emp_zip_code']:
			result.emp_zip_code = args['emp_zip_code']
		if args['emp_contact']:
			result.emp_contact = args['emp_contact']
		if args['emp_alt_contact']:
			result.emp_alt_contact = args['emp_alt_contact']
		if args['issue_date']:
			result.issue_date = args['issue_date']
		if args['joining_date']:
			result.joining_date = args['joining_date']
		if args['fee']:
			result.fee = args['fee']
		if args['transact_date']:
			result.transact_date = args['transact_date']
		if args['reciept_num']:
			result.reciept_num = args['reciept_num']
		if args['blood_grp']:
			result.blood_grp = args['blood_grp']
		
		db.session.commit()
		
		return result

	def delete(self,emp_contact):
		result = Teachers.query.filter_by(emp_contact=emp_contact).first()
		if not result:
			abort(404, message="Member doesn't exist, cannot delete")
		db.session.delete(result)
		db.session.commit()
		
		return '', 204
	
class Admin_log(Resource):
	@cross_origin(origin='*',headers=['Content-Type','Authorization'])
	@marshal_with(log_in_fields)
	def post(self):
		print("here")
		print(admin_post_args.parse_args())
		args = admin_post_args.parse_args()
		result = Admins.query.filter_by(email_id=args['email_id'],password=args['password']).first()
		if not result:
			abort(400, message="Account not found")
		return result, 200
	
	
	@marshal_with(log_in_fields)
	def put(self):
		args = admin_put_args.parse_args()
		result = Admins.query.filter_by(email_id=args['email_id']).first()
		if result:
			# return result
			abort(409, message="Account is already registered")
		
		admin = Admins(full_name=args['full_name'],email_id=args['email_id'],password=args['password'])
		db.session.add(admin)
		db.session.commit()
		print("Registered user ")
		return admin, 201
	
	@marshal_with(log_in_fields)
	def get(self):
		result = Admins.query.all()
		return result, 200



api.add_resource(Teacher, "/register/success/<int:emp_contact>")  
api.add_resource(Admin, "/admin/dashboard/<int:emp_contact>")  
api.add_resource(Admin_log, "/login") 	

if __name__ == "__main__":
	app.run(debug=True)