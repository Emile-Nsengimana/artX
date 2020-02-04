from cerberus import Validator
from graphql import GraphQLError


class Validate:
    def art_info(**kwargs):
        schema = {
            'no': {'type': 'string', 'minlength': 3, 'maxlength': 30},
            'label': {'type': 'string', 'minlength': 3, 'maxlength': 30},
            'image': {'type': 'string', 'minlength': 15},
            'details': {'type': 'string', 'minlength': 3, 'maxlength': 200},
            'price': {'type': 'float', 'minlength': 3, 'maxlength': 30},
            'owner': {'type': 'string', 'minlength': 3, 'maxlength': 30},
            'category': {'type': 'string', 'allowed': ['painting', 'drawing', 'photography', 'digital graphics']},
            'status': {'type': 'string', 'allowed': ['available', 'sold']}
        }
        v = Validator()
        is_valid = v.validate(kwargs, schema)
        if v.errors:
            # errors = v.errors
            # for error in v.errors:
            #     errors[error] = errors[error][0]

            #     if error == 'email':
            #         errors['email'] = 'please provide valid email'

            #     if error == 'password':
            #         errors['password'] = 'provide atleast 8 character long with a number, special character, capital and small case letter'
            raise GraphQLError(v.errors)

        return is_valid
