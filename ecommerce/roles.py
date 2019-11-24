from rolepermissions.roles import AbstractUserRole


class Doctor(AbstractUserRole):
    available_permissions = {
        'create_medical_record': True,
        'edit_patient_file':True,
    }

class Nurse(AbstractUserRole):
    available_permissions = {
        'edit_patient_file': True,
    }

class SystemAdmin(AbstractUserRole):
    available_permissions = {
        'drop_tables': True,
    }

from rolepermissions.permissions import grant_permission, revoke_permission

# revoke_permission(user, 'create_medical_record')
# grant_permission(user, 'edit_patient_file')
#
# ve=has_permission(user, 'create_medical_record')
# print(ve)
# ver=has_permission(user, 'edit_patient_file')
# print(ver)




