from cerberus import Validator
from graphql import GraphQLError


class Validate:
    def user_info(**kwargs):
        schema = {
            'city': {'type': 'string', 'minlength': 3, 'maxlength': 30},
            'country': {'type': 'string', 'minlength': 3, 'maxlength': 30},
            'dob': {'type': 'date'},
            'email': {'type': 'string', 'maxlength': 45,
                      'regex':
                      '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'},
            'first_name': {'type': 'string', 'minlength': 3, 'maxlength': 30},
            'last_name': {'type': 'string', 'minlength': 3, 'maxlength': 30},
            'password': {'type': 'string', 'minlength': 6, 'maxlength': 30,
                         'regex': '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$'},
            'phone_no': {'type': 'string'},
            'post_code': {'type': 'string', 'minlength': 3, 'maxlength': 15},
            'role': {'type': 'string',
                     'allowed': ['artist', 'Customer', 'system user'],
                     'forbidden': ['admin']},
            'status': {'type': 'string', 'allowed': ['active', 'deactivated']},
            'street_no': {'type': 'string', 'minlength': 3, 'maxlength': 10},
            'user_id': {'type': 'string', 'minlength': 10, 'maxlength': 16},
            'username': {'type': 'string', 'minlength': 3, 'maxlength': 30}
        }
        v = Validator()
        is_valid = v.validate(kwargs, schema)
        if v.errors:
            errors = v.errors
            for error in v.errors:
                errors[error] = errors[error][0]

                if error == 'email':
                    errors['email'] = 'please provide valid email'

                if error == 'password':
                    errors['password'] = 'provide atleast 8 character long with a number, special character, capital and small case letter'

            raise GraphQLError(errors)

        return is_valid
