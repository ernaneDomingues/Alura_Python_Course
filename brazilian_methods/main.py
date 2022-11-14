#Validation CPF and CNPJ documents
# from cpf_cnpj_validation import Document
#
# cpf = '87500886535'
#
# print(Document.create_document(cpf))
#
# cnpj = '76614752000104'
#
# print(Document.create_document(cnpj))

#Cell phone number validation
# from mobile_number_validation import MobileValidation
#
# cellphone_number = '11993760424'
#
# mobile = MobileValidation(cellphone_number)
# print(mobile)

#Enrollment date record
# from date_zone_br import DateRegistration
#
# cadastro = DateRegistration()
# print(cadastro)

from cep import ZipCodeSearch

# cep = '87043702'
# cep = '04832140'
cep = '87910000'

zip_code = ZipCodeSearch(cep)
address = zip_code.zip_code_search()
print(address)
